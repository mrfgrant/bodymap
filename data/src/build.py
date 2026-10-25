"""Builds data/mos.json and data/profiles.json from the source tables. Run: python3 data/src/build.py"""
import csv, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from profiles import P, H, profile_for

OUT = os.path.join(HERE, "..")
NOISE_NAME = {"H": "Highly Probable", "M": "Moderate", "L": "Low"}

# plain-word keywords by profile, so "cook" or "truck driver" finds the right jobs
KW = {
 "infantry": "grunt rifleman ground pounder ranger airborne paratrooper sniper machine gunner squad",
 "armor": "tanker tank crew bradley track scout cav",
 "artillery": "cannon howitzer gun bunny redleg mortar rockets patriot stinger air defense",
 "engineer": "sapper builder carpenter plumber electrician heavy equipment dozer bridge seabee",
 "aviation_maint": "crew chief helicopter mechanic jet mechanic avionics hangar flight line plane captain",
 "aircrew": "pilot aviator door gunner flight crew navigator",
 "mechanic": "mechanic motor pool wrench turner grease monkey welder machinist generator",
 "driver": "truck driver trucker convoy transport",
 "supply": "supply clerk warehouse forklift logistics storekeeper parts",
 "food": "cook chef kitchen dfac mess hall galley food service baker",
 "medical": "medic nurse doctor hospital clinic lab tech x-ray pharmacy therapist",
 "combat_medic": "combat medic corpsman doc line medic field medic",
 "admin": "clerk office personnel finance pay legal paralegal chaplain assistant recruiter typist secretary",
 "signal": "commo radio operator wire dawg network it computer satellite switchboard",
 "intel": "intel analyst linguist interpreter interrogator sigint imagery",
 "police": "mp military police security forces cop sp gate guard k9 corrections",
 "fire_eod": "firefighter fireman crash rescue eod bomb disposal damage control",
 "deck": "deck seaman boatswain bosun sailor ship small boat coxswain",
 "engineroom": "engine room snipe boiler machinist mate engineman hull tech shipfitter",
 "submarine": "submarine sub bubblehead sonar",
 "ordnance": "ammo ammunition gunners mate armorer munitions weapons loader",
 "cbrn": "chemical nbc cbrn decon",
 "band": "band musician bugler drummer",
 "airops": "air traffic control tower airfield ops",
 "fuels": "fuel pol petroleum gas jp8 refueler water purification",
 "trainer": "drill sergeant drill instructor mti instructor training",
 "dental": "dental dentist hygienist",
 "diver": "diver scuba salvage",
 "rigger": "rigger parachute packer airdrop",
 "services": "laundry mortuary graves registration shower",
 "generic": "",
}

def load(fn):
    with open(os.path.join(HERE, fn), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

rows = []
for fn in ["noise_army_enlisted.csv", "noise_army_other.csv", "noise_navy_usmc_cg.csv", "noise_airforce.csv"]:
    rows += load(fn)

# a few codes the VA listing does not carry; ratings estimated from the nearest listed job
ESTIMATED = {"Navy|Enlisted|SN", "Navy|Enlisted|FN", "Navy|Enlisted|AN", "Navy|Enlisted|CTN", "Navy|Enlisted|CMC",
             "Navy|Officer|1110","Navy|Officer|1120","Navy|Officer|1130","Navy|Officer|1140","Navy|Officer|1310","Navy|Officer|1320",
             "Navy|Officer|1510","Navy|Officer|1520","Navy|Officer|1800","Navy|Officer|1810","Navy|Officer|1820","Navy|Officer|1830",
             "Navy|Officer|2100","Navy|Officer|2200","Navy|Officer|2300","Navy|Officer|2500","Navy|Officer|2900","Navy|Officer|3100",
             "Navy|Officer|4100","Navy|Officer|5100","Navy|Officer|6490","Navy|Officer|7200"}

out, index = [], {}
for r in rows:
    key = f'{r["branch"]}|{r["component"]}|{r["code"]}'
    pid, how = profile_for(r["branch"], r["component"], r["code"], r["title"])
    e = {"k": key, "code": r["code"], "branch": r["branch"], "comp": r["component"], "title": r["title"].strip(),
         "noise": r["noise"], "noiseSrc": "estimated" if key in ESTIMATED else "va", "profile": pid}
    out.append(e); index[key] = e

# legacy codes: inherit profile and noise from the successor
leg = load("legacy_army.csv"); missing = []
for r in leg:
    succ = index.get(f'Army|Enlisted|{r["successor"]}')
    if not succ: missing.append(r["successor"]); continue
    key = f'Army|Enlisted|{r["code"]}|legacy'
    e = {"k": key, "code": r["code"], "branch": "Army", "comp": "Enlisted", "title": r["title"].strip(),
         "noise": succ["noise"], "noiseSrc": "successor", "profile": succ["profile"], "legacy": True,
         "successor": succ["code"], "successorTitle": succ["title"]}
    if r.get("note"): e["note"] = r["note"]
    out.append(e)

# search words
for e in out:
    words = set(re.findall(r"[a-z0-9]+", (e["title"] + " " + KW.get(e["profile"], "")).lower()))
    e["kw"] = " ".join(sorted(words))

def hz_all(p):
    keys = list(p["hazards"]) + ["range"]
    for r in p["regions"].values():
        for h in r["hazards"]:
            if h not in keys: keys.append(h)
    return {h: {"label": H[h][0], "desc": H[h][1]} for h in keys}
profiles = {pid: {"name": p["name"], "blurb": p["blurb"], "start": p["start"],
                  "hazards": hz_all(p), "regions": p["regions"]} for pid, p in P.items()}

os.makedirs(OUT, exist_ok=True)
json.dump({"generated": "see README", "count": len(out), "noiseNames": NOISE_NAME, "jobs": out},
          open(os.path.join(OUT, "mos.json"), "w"), separators=(",", ":"), ensure_ascii=False)
json.dump(profiles, open(os.path.join(OUT, "profiles.json"), "w"), separators=(",", ":"), ensure_ascii=False)

from collections import Counter
c = Counter(e["profile"] for e in out); hw = Counter(profile_for(e["branch"], e["comp"], e["code"], e["title"])[1] for e in out if not e.get("legacy"))
print(len(out), "jobs;", sum(1 for e in out if e.get("legacy")), "legacy;", "missing successors:", missing)
print("by profile:", dict(c)); print("mapped by:", dict(hw))
print("generic:", [e["code"] + " " + e["title"] for e in out if e["profile"] == "generic"][:40])
