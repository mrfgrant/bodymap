"""Hazard profiles by career field. Each profile lists the job hazards and the body areas they reach.
Condition lists and rating codes are draft content for review against 38 CFR Part 4 and by a clinician."""

# ---------- hazard library ----------
H = {
 "pt":        ("Years of PT, ruck marches and field duty", "Every service member ran, rucked and trained in boots regardless of job. Basic training alone loads knees, feet and back."),
 "load":      ("Heavy loads on foot", "Weapon, body armor, pack and equipment carried for hours, often 60 to 100 lb or more."),
 "marching":  ("Forced marches and running", "Conditioning hikes under load, field exercises and years of running in boots."),
 "terrain":   ("Falls and rough terrain", "Night movement, dismounting vehicles and uneven ground while loaded."),
 "airborne":  ("Parachute jumps", "Hard landings under full combat load, repeated over a career."),
 "blast":     ("Weapons blast and noise", "Small arms, crew-served weapons, explosives and vehicle fire in training and in combat."),
 "combat":    ("Combat and deployment events", "Depends on where and when you served. For combat veterans, 38 U.S.C. 1154(b) eases proof of what happened."),
 "vibration": ("Whole-body vibration", "Hours in tracked or heavy vehicles, aircraft or around running machinery."),
 "jolts":     ("Vehicle jolts and hard riding", "Off-road travel, turret time, hatches and hard seats with no suspension to speak of."),
 "confined":  ("Cramped crew spaces", "Working bent and twisted inside a hull, cockpit, turret or engine room."),
 "climbing":  ("Climbing and working at height", "Ladders, towers, aircraft, masts and vehicle decks, often carrying tools."),
 "kneeling":  ("Kneeling, crawling and squatting", "Hours on concrete, flight lines, decks or under vehicles."),
 "lifting":   ("Heavy lifting", "Repeated lifting and carrying of equipment, parts, rounds, cases or people."),
 "repetitive":("Repetitive hand work", "Hours of the same gripping, turning, typing, cutting or tool use every day."),
 "standing":  ("Long shifts on your feet", "Ten to fourteen hour shifts standing on concrete, steel or tile."),
 "sitting":   ("Long hours seated", "Desk, console, cockpit or driver's seat for most of every shift."),
 "posture":   ("Bent or head-down work", "Working hunched over a table, patient, engine, screen or sink."),
 "jet":       ("Jet and rotor noise", "Flight line, hangar deck or cockpit noise at levels hearing protection only partly stops."),
 "machinery": ("Machinery and generator noise", "Engine rooms, generators, compressors and power tools, often around the clock."),
 "fumes":     ("Exhaust, smoke and fumes", "Engine exhaust, burning fuel, welding smoke or cooking smoke in closed spaces."),
 "solvents":  ("Fuels, solvents and chemicals on the skin", "Degreasers, hydraulic fluid, JP-8, paint and cleaning agents, often without gloves."),
 "heat":      ("Heat, flame and steam", "Hot equipment, open flame, engine spaces or MOPP gear in the heat."),
 "cold":      ("Cold and wet exposure", "Field problems and guard duty in the cold, wet boots for days."),
 "wet":       ("Wet work and sanitizers", "Hands in water, cleaning chemicals and bleach for hours."),
 "knives":    ("Blades and cutting tools", "Daily knife, slicer or cutting tool work at speed."),
 "floors":    ("Slips and falls", "Wet, greasy or oily floors and decks while carrying loads."),
 "trauma":    ("Exposure to injury and death", "Treating, guarding, recovering or documenting the badly hurt and the dead."),
 "shifts":    ("Shift work and broken sleep", "Rotating shifts, watches, alerts and 24-hour operations for years."),
 "headset":   ("Headset and radio noise", "Long shifts with audio at high volume in one or both ears."),
 "exposure":  ("Deployment exposures", "Burn pits, dust, oil smoke and other exposures tied to where you served, not the job."),
 "pressure":  ("Pressure changes", "Diving, altitude or unpressurized flight, with ear and sinus barotrauma."),
 "armor":     ("Body armor and duty belt", "Daily weight on the hips, lower back and shoulders for a full shift."),
 "handling":  ("Patient and casualty handling", "Lifting, turning and carrying people, often awkwardly and in a hurry."),
 "needles":   ("Needlesticks, blood and infection", "Daily contact with blood, body fluids and sick patients."),
 "lines":     ("Lines, mooring and cargo", "Hauling line, chain and cargo on a moving deck."),
 "asbestos":  ("Asbestos, lagging and shipboard dust", "Older ships and engine rooms, pipe lagging, grinding and painting in closed spaces."),
 "voice":     ("Shouting and voice strain", "Cadence, commands and instruction over noise for hours."),
 "handpiece": ("Dental handpiece and suction noise", "High-pitched tool noise close to the ear all day."),
 "range":     ("Range and qualification noise", "Annual weapons qualification and range duty, even in non-combat jobs."),
}

# ---------- condition blocks by area ----------
C = {
 "ears":      [["Tinnitus","DC 6260"],["Hearing loss","DC 6100"]],
 "head_combat":[["Traumatic brain injury residuals","DC 8045"],["Migraine or post-traumatic headaches","DC 8100"],["PTSD","DC 9411"]],
 "head_mh":   [["PTSD (non-combat stressor)","DC 9411"],["Depression or anxiety","DC 9434, 9400"],["Migraine headaches","DC 8100"]],
 "head_sleep":[["Chronic headaches","DC 8100"],["Insomnia or sleep disorder","Rated with mental health or DC 6847"]],
 "head_baro": [["Migraine headaches","DC 8100"],["Barotrauma residuals (ears, sinuses)","DC 6204, 6510"]],
 "neck":      [["Cervical strain","DC 5237"],["Degenerative arthritis of the cervical spine","DC 5242"],["Cervical radiculopathy, secondary to the neck","DC 8510"]],
 "shoulders": [["Shoulder strain or rotator cuff tendinopathy","DC 5201"],["Shoulder impingement","DC 5201, by analogy"],["AC joint or collarbone injury","DC 5203"]],
 "upperback": [["Thoracic strain","DC 5237"]],
 "lowback":   [["Lumbosacral strain","DC 5237"],["Degenerative arthritis of the spine","DC 5242"],["Intervertebral disc syndrome","DC 5243"],["Sciatica, secondary to the back","DC 8520"]],
 "abdomen":   [["Hernia","DC 7338"]],
 "hips":      [["Hip strain or limited motion","DC 5251 to 5253"],["Trochanteric bursitis","DC 5019"],["Degenerative arthritis of the hip","DC 5003"]],
 "elbows":    [["Lateral epicondylitis (tennis elbow)","DC 5024, by analogy"],["Elbow bursitis","DC 5019"]],
 "skin_burn": [["Burn scars","DC 7801 to 7805"],["Laceration scars","DC 7804, 7805"],["Contact dermatitis or eczema","DC 7806"]],
 "skin_chem": [["Contact dermatitis or eczema","DC 7806"],["Chloracne or chemical acne","DC 7829"],["Scars","DC 7804, 7805"]],
 "wrists":    [["Carpal tunnel syndrome","DC 8515"],["Wrist tendinitis or De Quervain's","DC 5024"],["Hand or finger injury residuals","DC 5216 to 5230"]],
 "knees":     [["Knee strain or patellofemoral pain","DC 5260, 5261"],["Knee instability","DC 5257"],["Degenerative arthritis of the knee","DC 5003"]],
 "lowerlegs": [["Shin splints","DC 5262"],["Stress fracture residuals","DC 5262"],["Varicose veins","DC 7120"]],
 "feet":      [["Plantar fasciitis","DC 5269"],["Flatfoot, acquired or aggravated","DC 5276"],["Ankle sprain residuals","DC 5271"]],
 "feet_cold": [["Plantar fasciitis","DC 5269"],["Flatfoot, acquired or aggravated","DC 5276"],["Ankle sprain residuals","DC 5271"],["Cold injury residuals","DC 7122"]],
 "airways":   [["Asthma","DC 6602"],["Chronic rhinitis","DC 6522"],["Chronic sinusitis","DC 6510 to 6514"],["Chronic bronchitis or COPD","DC 6600, 6604"]],
 "airways_asb":[["Asbestosis or pleural plaques","DC 6833"],["Chronic bronchitis or COPD","DC 6600, 6604"],["Asthma","DC 6602"]],
}
EV = {
 "ortho": ["Statement on what you did, how heavy, how often and when it started","Buddy statement from the same unit or shop","Current imaging and range of motion exam"],
 "ears":  ["DD-214 showing the job","Statement on when the ringing or hearing trouble began","Current audiogram"],
 "head":  ["Deployment records and awards","Statement naming specific events","Buddy statements from the same unit","Neurology or mental health evaluation"],
 "mh":    ["Statement describing the stressor events","Buddy statement or unit records","Mental health evaluation"],
 "skin":  ["Photos of scars or rash","Statement on how and when it happened","Dermatology exam"],
 "air":   ["Statement on the exposure and ventilation","Service dates and places for presumptive screening","Pulmonary function test"],
 "feet":  ["Statement on boots, hikes and standing hours","Buddy statement","Podiatry diagnosis"],
}

def R(s, hz, conds, ev="ortho", note=None):
    d = {"s": s, "hazards": hz, "conds": C[conds] if isinstance(conds, str) else conds, "evidence": EV[ev]}
    if note: d["note"] = note
    return d

BASE = {  # every profile gets at least this; profiles override per area
 "knees": R(2, ["pt"], "knees"),
 "feet":  R(2, ["pt"], "feet", "feet"),
 "lowback": R(2, ["pt"], "lowback"),
}

P = {}
def prof(pid, name, hazards, regions, start, blurb):
    reg = dict(BASE); reg.update(regions)
    hz = ["pt"] + [h for h in hazards if h != "pt"]
    P[pid] = {"name": name, "blurb": blurb, "hazards": hz, "start": start, "regions": reg}

prof("infantry", "Infantry and combat arms", ["load","marching","terrain","blast","combat","cold","airborne"], {
 "ears": R(3, ["blast"], "ears", "ears"),
 "head": R(2, ["blast","combat"], "head_combat", "head", "These turn on what happened, not the job title. Describe the specific blasts or events."),
 "neck": R(2, ["load","jolts"] if False else ["load"], "neck"),
 "shoulders": R(3, ["load"], "shoulders"),
 "upperback": R(2, ["load"], "upperback"),
 "lowback": R(3, ["load","marching","terrain","airborne"], "lowback"),
 "abdomen": R(2, ["load"], "abdomen"),
 "hips": R(2, ["load","marching"], "hips"),
 "knees": R(3, ["load","marching","terrain","airborne"], "knees"),
 "lowerlegs": R(2, ["marching","load"], "lowerlegs"),
 "feet": R(3, ["marching","load","cold","terrain"], "feet_cold", "feet"),
}, "knees", "rucks, ranges and rough ground")

prof("armor", "Armor, cavalry and tracked vehicles", ["vibration","jolts","confined","blast","combat","climbing","lifting"], {
 "ears": R(3, ["blast","vibration"], "ears", "ears"),
 "head": R(2, ["blast","combat","jolts"], "head_combat", "head", "Hatch strikes and hard jolts count. Describe specific events."),
 "neck": R(3, ["jolts","confined","vibration"], "neck"),
 "shoulders": R(2, ["lifting","climbing"], "shoulders"),
 "lowback": R(3, ["vibration","jolts","lifting","confined"], "lowback"),
 "hips": R(2, ["vibration","confined"], "hips"),
 "elbows": R(2, ["confined","lifting"], "elbows"),
 "wrists": R(2, ["lifting","confined"], "wrists"),
 "knees": R(3, ["climbing","confined","jolts"], "knees"),
 "feet": R(2, ["climbing","jolts"], "feet", "feet"),
}, "neck", "turret time, track vibration and hatches")

prof("artillery", "Artillery and air defense", ["blast","lifting","vibration","load","combat"], {
 "ears": R(3, ["blast"], "ears", "ears"),
 "head": R(2, ["blast","combat"], "head_combat", "head", "Concussive blast from the gun line is a recognized cause even without a single injury."),
 "neck": R(2, ["lifting","vibration"], "neck"),
 "shoulders": R(3, ["lifting"], "shoulders"),
 "lowback": R(3, ["lifting","vibration","load"], "lowback"),
 "abdomen": R(2, ["lifting"], "abdomen"),
 "hips": R(2, ["lifting","load"], "hips"),
 "elbows": R(2, ["lifting"], "elbows"),
 "wrists": R(2, ["lifting"], "wrists"),
 "knees": R(3, ["lifting","load","vibration"], "knees"),
 "feet": R(2, ["load","vibration"], "feet", "feet"),
}, "ears", "gun line blast and hundred-pound rounds")

prof("engineer", "Engineers and construction", ["lifting","vibration","machinery","kneeling","fumes","solvents","heat","climbing","blast"], {
 "ears": R(3, ["machinery","blast"], "ears", "ears"),
 "neck": R(2, ["posture","vibration"] if False else ["vibration","lifting"], "neck"),
 "shoulders": R(3, ["lifting","climbing"], "shoulders"),
 "airways": R(2, ["fumes"], "airways", "air"),
 "lowback": R(3, ["lifting","vibration","kneeling"], "lowback"),
 "abdomen": R(2, ["lifting"], "abdomen"),
 "hips": R(2, ["lifting","kneeling"], "hips"),
 "elbows": R(2, ["lifting","machinery"], "elbows"),
 "skin": R(2, ["solvents","heat"], "skin_burn", "skin"),
 "wrists": R(2, ["machinery","lifting"], "wrists"),
 "knees": R(3, ["kneeling","lifting","climbing"], "knees"),
 "feet": R(2, ["climbing","lifting"], "feet", "feet"),
}, "lowback", "heavy equipment, demolition and concrete")

prof("aviation_maint", "Aircraft maintenance and flight line", ["jet","fumes","solvents","kneeling","climbing","lifting","machinery"], {
 "ears": R(3, ["jet","machinery"], "ears", "ears"),
 "neck": R(2, ["posture","climbing"] if False else ["climbing","kneeling"], "neck"),
 "shoulders": R(3, ["lifting","climbing"], "shoulders"),
 "airways": R(2, ["fumes","solvents"], "airways", "air"),
 "lowback": R(3, ["lifting","kneeling","climbing"], "lowback"),
 "hips": R(2, ["kneeling","climbing"], "hips"),
 "elbows": R(2, ["machinery","lifting"], "elbows"),
 "skin": R(2, ["solvents"], "skin_chem", "skin"),
 "wrists": R(2, ["machinery","lifting"], "wrists"),
 "knees": R(3, ["kneeling","climbing"], "knees"),
 "feet": R(2, ["climbing","standing"], "feet", "feet"),
}, "ears", "jet noise, hydraulic fluid and hangar decks")

prof("aircrew", "Pilots and aircrew", ["jet","vibration","sitting","climbing","pressure","shifts"], {
 "ears": R(3, ["jet"], "ears", "ears"),
 "head": R(2, ["pressure","shifts"], "head_baro", "head"),
 "neck": R(3, ["vibration","sitting"], "neck", "ortho", "Helmet and night vision weight on the neck for hours is a recognized aircrew problem."),
 "shoulders": R(2, ["sitting","climbing"], "shoulders"),
 "lowback": R(3, ["vibration","sitting"], "lowback"),
 "hips": R(2, ["sitting","vibration"], "hips"),
 "knees": R(2, ["climbing","sitting"], "knees"),
 "feet": R(1, ["climbing"], "feet", "feet"),
}, "ears", "cockpit noise, vibration and helmet weight")

prof("mechanic", "Vehicle and equipment mechanics", ["lifting","kneeling","posture","machinery","solvents","fumes","vibration"], {
 "ears": R(3, ["machinery"], "ears", "ears"),
 "neck": R(2, ["posture","kneeling"], "neck"),
 "shoulders": R(3, ["lifting","posture"], "shoulders"),
 "airways": R(2, ["fumes"], "airways", "air"),
 "lowback": R(3, ["lifting","kneeling","posture"], "lowback"),
 "hips": R(2, ["kneeling"], "hips"),
 "elbows": R(2, ["machinery","lifting"], "elbows"),
 "skin": R(2, ["solvents"], "skin_chem", "skin"),
 "wrists": R(3, ["machinery","repetitive"], "wrists"),
 "knees": R(3, ["kneeling"], "knees"),
 "feet": R(2, ["standing"], "feet", "feet"),
}, "lowback", "under vehicles with tools, solvents and exhaust")

prof("driver", "Motor transport and drivers", ["vibration","jolts","sitting","lifting","machinery","lines"], {
 "ears": R(2, ["machinery"], "ears", "ears"),
 "neck": R(2, ["vibration","sitting"], "neck"),
 "shoulders": R(2, ["lifting","lines"], "shoulders"),
 "lowback": R(3, ["vibration","jolts","sitting","lifting"], "lowback"),
 "hips": R(2, ["sitting","vibration"], "hips"),
 "wrists": R(1, ["vibration"], "wrists"),
 "knees": R(2, ["climbing","jolts"] if False else ["jolts","lifting"], "knees"),
 "feet": R(1, ["pt"], "feet", "feet"),
}, "lowback", "hours in the cab on bad roads, then tie-downs")

prof("supply", "Supply, logistics and warehouse", ["lifting","repetitive","standing","machinery"], {
 "ears": R(1, ["machinery"], "ears", "ears"),
 "neck": R(1, ["lifting"], "neck"),
 "shoulders": R(2, ["lifting","repetitive"], "shoulders"),
 "lowback": R(3, ["lifting","standing"], "lowback"),
 "abdomen": R(2, ["lifting"], "abdomen"),
 "hips": R(1, ["standing"], "hips"),
 "elbows": R(1, ["lifting"], "elbows"),
 "wrists": R(2, ["repetitive","lifting"], "wrists"),
 "knees": R(2, ["lifting","standing"], "knees"),
 "feet": R(2, ["standing"], "feet", "feet"),
}, "lowback", "pallets, cases and concrete floors")

prof("food", "Food service", ["standing","lifting","repetitive","posture","heat","knives","floors","wet","fumes"], {
 "ears": R(1, ["range"], "ears", "ears", "The job alone will not carry a hearing claim. Look for other exposure: ranges, generators, a loud unit."),
 "neck": R(2, ["posture","lifting"], "neck"),
 "shoulders": R(2, ["lifting"], "shoulders"),
 "airways": R(1, ["fumes","wet"], "airways", "air"),
 "upperback": R(2, ["posture","lifting"], "upperback"),
 "lowback": R(3, ["lifting","standing","floors","posture"], "lowback"),
 "abdomen": R(2, ["lifting"], "abdomen"),
 "hips": R(2, ["standing","lifting","floors"], "hips"),
 "elbows": R(2, ["repetitive","lifting"], "elbows"),
 "skin": R(3, ["heat","knives","wet"], "skin_burn", "skin", "Scars are their own evidence. A visible burn or cut scar plus a statement on how it happened is a clean claim even with no service records."),
 "wrists": R(3, ["repetitive","knives"], "wrists"),
 "knees": R(3, ["standing","lifting","floors"], "knees"),
 "lowerlegs": R(2, ["standing"], [["Varicose veins","DC 7120"]]),
 "feet": R(3, ["standing","floors"], "feet", "feet"),
}, "knees", "twelve-hour shifts on concrete, hot lines and knives")

prof("medical", "Medical and dental", ["handling","standing","trauma","needles","posture","shifts","solvents"], {
 "ears": R(1, ["range"], "ears", "ears"),
 "head": R(2, ["trauma","shifts"], "head_mh", "mh", "Treating the badly hurt is a recognized stressor. Describe what you saw and when."),
 "neck": R(2, ["posture","handling"], "neck"),
 "shoulders": R(2, ["handling"], "shoulders"),
 "lowback": R(3, ["handling","standing"], "lowback"),
 "hips": R(1, ["standing"], "hips"),
 "skin": R(1, ["solvents","wet"], "skin_chem", "skin"),
 "wrists": R(2, ["repetitive","handling"], "wrists"),
 "knees": R(2, ["standing","handling"], "knees"),
 "feet": R(2, ["standing"], "feet", "feet"),
}, "lowback", "patient lifting, long shifts and what you saw")

prof("combat_medic", "Combat medics and corpsmen", ["load","marching","terrain","blast","combat","handling","trauma","needles","cold"], {
 "ears": R(3, ["blast"], "ears", "ears"),
 "head": R(3, ["blast","combat","trauma"], "head_combat", "head", "Both the blasts and what you treated count. Describe specific events."),
 "neck": R(2, ["load","handling"], "neck"),
 "shoulders": R(3, ["load","handling"], "shoulders"),
 "lowback": R(3, ["load","handling","marching","terrain"], "lowback"),
 "abdomen": R(2, ["load","handling"], "abdomen"),
 "hips": R(2, ["load","marching"], "hips"),
 "wrists": R(2, ["handling"], "wrists"),
 "knees": R(3, ["load","marching","terrain"], "knees"),
 "lowerlegs": R(2, ["marching"], "lowerlegs"),
 "feet": R(3, ["marching","load","cold"], "feet_cold", "feet"),
}, "head", "everything the infantry carried, plus the casualties")

prof("admin", "Administration, finance and legal", ["sitting","repetitive","posture","shifts"], {
 "ears": R(1, ["range"], "ears", "ears", "The job alone will not carry a hearing claim. Look for ranges, generators or a loud unit."),
 "head": R(1, ["shifts","posture"], "head_sleep", "mh"),
 "neck": R(2, ["sitting","posture"], "neck"),
 "shoulders": R(1, ["posture"], "shoulders"),
 "lowback": R(2, ["sitting"], "lowback"),
 "hips": R(1, ["sitting"], "hips"),
 "wrists": R(2, ["repetitive"], "wrists"),
}, "wrists", "desk, keyboard and the same PT as everyone else")

prof("signal", "Signal, communications and IT", ["lifting","climbing","machinery","sitting","repetitive","headset","cold"], {
 "ears": R(2, ["machinery","headset"], "ears", "ears", "Generators and headsets add to whatever the noise listing says for this job."),
 "neck": R(2, ["sitting","lifting"], "neck"),
 "shoulders": R(2, ["lifting","climbing"], "shoulders"),
 "lowback": R(3, ["lifting","sitting"], "lowback"),
 "hips": R(1, ["sitting"], "hips"),
 "elbows": R(1, ["lifting"], "elbows"),
 "wrists": R(2, ["repetitive","lifting"], "wrists"),
 "knees": R(2, ["climbing","lifting"], "knees"),
 "feet": R(2, ["climbing","cold"], "feet_cold", "feet"),
}, "lowback", "cable reels, antenna masts and generators")

prof("intel", "Intelligence and linguists", ["sitting","headset","shifts","repetitive"], {
 "ears": R(2, ["headset"], "ears", "ears", "Hours of headset audio is a noise exposure the listing may not credit. Describe it."),
 "head": R(2, ["shifts","trauma"], "head_sleep", "mh"),
 "neck": R(2, ["sitting","posture"], "neck"),
 "lowback": R(2, ["sitting"], "lowback"),
 "hips": R(1, ["sitting"], "hips"),
 "wrists": R(2, ["repetitive"], "wrists"),
}, "ears", "headsets, consoles and rotating shifts")

prof("police", "Military police and security forces", ["armor","standing","sitting","blast","trauma","terrain","shifts"], {
 "ears": R(3, ["blast"], "ears", "ears"),
 "head": R(2, ["trauma","shifts"], "head_mh", "mh", "Use-of-force events, accidents and what you responded to are stressors. Describe specific events."),
 "neck": R(2, ["armor","sitting"], "neck"),
 "shoulders": R(2, ["armor"], "shoulders"),
 "lowback": R(3, ["armor","sitting","standing"], "lowback"),
 "hips": R(3, ["armor","standing"], "hips", "ortho", "A loaded duty belt on the hips for a full shift, year after year."),
 "wrists": R(1, ["repetitive"], "wrists"),
 "knees": R(3, ["standing","terrain","armor"], "knees"),
 "feet": R(2, ["standing"], "feet", "feet"),
}, "hips", "duty belt, body armor and twelve-hour shifts")

prof("fire_eod", "Firefighters and explosive ordnance disposal", ["blast","heat","fumes","lifting","kneeling","load","trauma"], {
 "ears": R(3, ["blast","machinery"], "ears", "ears"),
 "head": R(2, ["blast","trauma"], "head_combat", "head"),
 "neck": R(2, ["load","lifting"], "neck"),
 "shoulders": R(3, ["lifting","load"], "shoulders"),
 "airways": R(3, ["fumes","heat"], "airways", "air", "Smoke and combustion products are a direct exposure. Keep any records of fire calls or training burns."),
 "lowback": R(3, ["lifting","load","kneeling"], "lowback"),
 "hips": R(2, ["load"], "hips"),
 "skin": R(2, ["heat","solvents"], "skin_burn", "skin"),
 "wrists": R(2, ["lifting"], "wrists"),
 "knees": R(3, ["kneeling","load"], "knees"),
 "feet": R(2, ["load","heat"], "feet", "feet"),
}, "airways", "smoke, blast and the weight of the gear")

prof("deck", "Shipboard deck and boat crews", ["lines","climbing","floors","machinery","heat","solvents","asbestos","cold"], {
 "ears": R(3, ["machinery"], "ears", "ears"),
 "neck": R(2, ["lines","climbing"], "neck"),
 "shoulders": R(3, ["lines","lifting"], "shoulders"),
 "airways": R(2, ["asbestos","solvents"], "airways_asb", "air", "Ship class and years matter. Pre-1990s ships had asbestos lagging; note which ships you served on."),
 "lowback": R(3, ["lines","climbing","floors"], "lowback"),
 "hips": R(2, ["climbing"], "hips"),
 "elbows": R(1, ["lines"], "elbows"),
 "skin": R(2, ["solvents","heat"], "skin_chem", "skin"),
 "wrists": R(2, ["lines","repetitive"], "wrists"),
 "knees": R(3, ["climbing","floors"], "knees"),
 "feet": R(2, ["climbing","cold"], "feet", "feet"),
}, "lowback", "ladders, lines and a moving deck")

prof("engineroom", "Shipboard engineering and machinery", ["machinery","heat","asbestos","solvents","climbing","confined","lifting"], {
 "ears": R(3, ["machinery"], "ears", "ears"),
 "neck": R(2, ["confined","climbing"], "neck"),
 "shoulders": R(2, ["lifting","confined"], "shoulders"),
 "airways": R(3, ["asbestos","fumes","heat"], "airways_asb", "air", "Engine rooms on older ships are the classic asbestos exposure. Name the ships and years."),
 "lowback": R(3, ["lifting","confined","climbing"], "lowback"),
 "hips": R(2, ["climbing","confined"], "hips"),
 "skin": R(2, ["solvents","heat"], "skin_chem", "skin"),
 "wrists": R(2, ["machinery","lifting"], "wrists"),
 "knees": R(3, ["climbing","confined"], "knees"),
 "feet": R(2, ["climbing","heat"], "feet", "feet"),
}, "ears", "engine rooms, steam and lagging")

prof("submarine", "Submarine crews", ["confined","machinery","shifts","climbing","pressure"], {
 "ears": R(2, ["machinery"], "ears", "ears"),
 "head": R(2, ["shifts","confined"], "head_sleep", "mh"),
 "neck": R(2, ["confined"], "neck"),
 "lowback": R(2, ["confined","climbing"], "lowback"),
 "knees": R(2, ["climbing","confined"], "knees"),
 "feet": R(1, ["climbing"], "feet", "feet"),
}, "head", "months submerged on an 18-hour day")

prof("ordnance", "Ammunition, munitions and weapons", ["lifting","blast","solvents","machinery","kneeling"], {
 "ears": R(3, ["blast","machinery"], "ears", "ears"),
 "head": R(1, ["blast"], "head_combat", "head"),
 "neck": R(2, ["lifting"], "neck"),
 "shoulders": R(3, ["lifting"], "shoulders"),
 "airways": R(1, ["solvents"], "airways", "air"),
 "lowback": R(3, ["lifting","kneeling"], "lowback"),
 "abdomen": R(2, ["lifting"], "abdomen"),
 "hips": R(2, ["lifting"], "hips"),
 "skin": R(2, ["solvents"], "skin_chem", "skin"),
 "wrists": R(2, ["lifting","repetitive"], "wrists"),
 "knees": R(2, ["lifting","kneeling"], "knees"),
 "feet": R(2, ["lifting"], "feet", "feet"),
}, "lowback", "heavy rounds, propellant and solvents")

prof("cbrn", "Chemical, biological and decontamination", ["solvents","heat","lifting","fumes"], {
 "ears": R(1, ["range"], "ears", "ears"),
 "head": R(1, ["heat"], "head_sleep", "mh"),
 "shoulders": R(2, ["lifting"], "shoulders"),
 "airways": R(3, ["solvents","fumes"], "airways", "air", "Decon agents, smoke pots and training chambers are direct exposures. Name them."),
 "lowback": R(2, ["lifting","heat"], "lowback"),
 "skin": R(3, ["solvents","heat"], "skin_chem", "skin"),
 "knees": R(2, ["lifting"], "knees"),
}, "skin", "decon chemicals and MOPP gear in the heat")

prof("band", "Bands and musicians", ["machinery","standing","repetitive","marching","posture"], {
 "ears": R(3, ["machinery"], "ears", "ears", "Instrument noise is the exposure. Brass and percussion sections run well above safe levels."),
 "neck": R(2, ["posture"], "neck"),
 "shoulders": R(2, ["posture","repetitive"], "shoulders"),
 "lowback": R(2, ["standing","marching"], "lowback"),
 "wrists": R(2, ["repetitive"], "wrists"),
 "knees": R(1, ["marching"], "knees"),
 "feet": R(2, ["marching","standing"], "feet", "feet"),
}, "ears", "rehearsal rooms and parade routes")

prof("airops", "Air traffic and airfield operations", ["jet","headset","shifts","sitting"], {
 "ears": R(3, ["jet","headset"], "ears", "ears"),
 "head": R(2, ["shifts","headset"], "head_sleep", "mh"),
 "neck": R(2, ["sitting"], "neck"),
 "lowback": R(2, ["sitting"], "lowback"),
 "wrists": R(1, ["repetitive"], "wrists"),
}, "ears", "the tower, the flight line and rotating shifts")

prof("fuels", "Fuels, petroleum and water", ["solvents","fumes","lifting","machinery","heat"], {
 "ears": R(2, ["machinery","jet"], "ears", "ears"),
 "head": R(1, ["fumes"], "head_sleep", "mh"),
 "neck": R(1, ["lifting"], "neck"),
 "shoulders": R(2, ["lifting"], "shoulders"),
 "airways": R(3, ["fumes","solvents"], "airways", "air", "Fuel vapor exposure is daily and direct. Note the fuels handled: JP-4, JP-8, diesel, MOGAS."),
 "lowback": R(3, ["lifting"], "lowback"),
 "skin": R(3, ["solvents"], "skin_chem", "skin"),
 "knees": R(2, ["lifting"], "knees"),
 "feet": R(1, ["standing"], "feet", "feet"),
}, "skin", "hoses, vapor and fuel on the skin")

prof("trainer", "Drill instructors and trainers", ["standing","marching","voice","blast","shifts"], {
 "ears": R(3, ["blast"], "ears", "ears"),
 "head": R(1, ["shifts","voice"], "head_sleep", "mh"),
 "neck": R(1, ["standing"], "neck"),
 "lowback": R(2, ["marching","standing"], "lowback"),
 "knees": R(2, ["marching"], "knees"),
 "feet": R(3, ["marching","standing"], "feet", "feet"),
}, "feet", "every march, every range, every cycle")

prof("dental", "Dental", ["posture","repetitive","handpiece","needles"], {
 "ears": R(2, ["handpiece"], "ears", "ears"),
 "neck": R(3, ["posture"], "neck", "ortho", "Bent over patients for a career is the classic dental neck injury."),
 "shoulders": R(2, ["posture"], "shoulders"),
 "lowback": R(2, ["posture"], "lowback"),
 "skin": R(1, ["solvents","wet"], "skin_chem", "skin"),
 "wrists": R(2, ["repetitive"], "wrists"),
}, "neck", "bent over a chair with a handpiece")

prof("diver", "Divers", ["pressure","cold","lifting","machinery"], {
 "ears": R(3, ["pressure","machinery"], "ears", "ears"),
 "head": R(2, ["pressure"], "head_baro", "head"),
 "shoulders": R(2, ["lifting"], "shoulders"),
 "airways": R(2, ["pressure"], [["Pulmonary barotrauma residuals","DC 6817, by analogy"],["Asthma","DC 6602"]], "air"),
 "lowback": R(2, ["lifting"], "lowback"),
 "knees": R(2, ["lifting","cold"], "knees"),
 "feet": R(2, ["cold"], "feet_cold", "feet"),
}, "ears", "pressure, cold water and heavy rigs")

prof("rigger", "Parachute riggers and airdrop", ["lifting","repetitive","airborne","posture"], {
 "ears": R(1, ["jet"], "ears", "ears"),
 "neck": R(2, ["posture"], "neck"),
 "shoulders": R(2, ["lifting"], "shoulders"),
 "lowback": R(3, ["lifting","airborne"], "lowback"),
 "wrists": R(3, ["repetitive"], "wrists"),
 "knees": R(2, ["airborne","lifting"], "knees"),
 "feet": R(2, ["airborne"], "feet", "feet"),
}, "wrists", "sewing machines, canopies and jumps")

prof("services", "Laundry, mortuary and field services", ["lifting","solvents","heat","wet","trauma"], {
 "ears": R(1, ["machinery"], "ears", "ears"),
 "head": R(2, ["trauma"], "head_mh", "mh", "Mortuary affairs is a recognized stressor. Describe the work."),
 "shoulders": R(2, ["lifting"], "shoulders"),
 "airways": R(2, ["solvents","heat"], "airways", "air"),
 "lowback": R(3, ["lifting"], "lowback"),
 "skin": R(2, ["solvents","wet","heat"], "skin_chem", "skin"),
 "wrists": R(2, ["repetitive","wet"], "wrists"),
 "knees": R(2, ["lifting","standing"], "knees"),
 "feet": R(2, ["standing"], "feet", "feet"),
}, "lowback", "chemicals, heat and heavy wet loads")

prof("generic", "General service", ["standing","lifting"], {
 "ears": R(1, ["range"], "ears", "ears"),
 "shoulders": R(1, ["lifting"], "shoulders"),
 "neck": R(1, ["pt"], "neck"),
 "hips": R(1, ["pt"], "hips"),
}, "knees", "training, ranges and field duty like everyone")

# ---------- mapping rules: (branch, component or None, regex on code, profile) checked in order; title regex fallback ----------
import re
RULES = [
 # Army enlisted by CMF (order matters: specific before broad)
 ("Army","Enlisted",r"^(68W|18D)",    "combat_medic"),
 ("Army","Enlisted",r"^(11|18)",      "infantry"),
 ("Army","Enlisted",r"^19",           "armor"),
 ("Army","Enlisted",r"^(13|14|16|17)","artillery"),
 ("Army","Enlisted",r"^12D",          "diver"),
 ("Army","Enlisted",r"^(12M|21M|89D|55D)", "fire_eod"),
 ("Army","Enlisted",r"^(12|21|51|62|81)", "engineer"),
 ("Army","Enlisted",r"^(15P|15Q|93)", "airops"),
 ("Army","Enlisted",r"^(15|94[KLR])", "aviation_maint"),
 ("Army","Enlisted",r"^(31B|31D|31E|95)", "police"),
 ("Army","Enlisted",r"^(42R|42S|02)", "band"),
 ("Army","Enlisted",r"^68E",         "dental"),
 ("Army","Enlisted",r"^68",          "medical"),
 ("Army","Enlisted",r"^74D",         "cbrn"),
 ("Army","Enlisted",r"^(25|31|74|36K|05|29|39B)", "signal"),
 ("Army","Enlisted",r"^(27D|36B|42|43F|71|73|75|79|46|56M|00Z|00R|00E|83|84|25M|25Q)", "admin"),
 ("Army","Enlisted",r"^(35|96|97|98|33W|37F|38)", "intel"),
 ("Army","Enlisted",r"^(74D|54)",     "cbrn"),
 ("Army","Enlisted",r"^(88M|64C)",    "driver"),
 ("Army","Enlisted",r"^(88K|88L|61B|61C|88P|88T|88U)", "deck"),
 ("Army","Enlisted",r"^(88|57H)",     "supply"),
 ("Army","Enlisted",r"^(89|55)",      "ordnance"),
 ("Army","Enlisted",r"^(94B|92G)",     "food"),
 ("Army","Enlisted",r"^(91|63|52|44|45)", "mechanic"),
 ("Army","Enlisted",r"^(92F|92L|92W|77)", "fuels"),
 ("Army","Enlisted",r"^(92R|43E)",    "rigger"),
 ("Army","Enlisted",r"^(92S|92M|57E|43M)", "services"),
 ("Army","Enlisted",r"^(92|76)",      "supply"),
 ("Army","Enlisted",r"^(94|27|35|39|24|23|21G)", "signal"),
 # Army officer / warrant
 ("Army",None,r"^(11A|18A|02)",       "infantry"),
 ("Army",None,r"^19",                 "armor"),
 ("Army",None,r"^(13A|14A|131A|140)", "artillery"),
 ("Army",None,r"^(12|21|120A|210A|125D|215D)", "engineer"),
 ("Army",None,r"^(15[2-5]|155|153|154|152|15A|15B|15C|67J)", "aircrew"),
 ("Army",None,r"^(151A|150)",         "aviation_maint"),
 ("Army",None,r"^(25|24|53|250|251|254|255|290|29A|30A|57A)", "signal"),
 ("Army",None,r"^(31|311A)",          "police"),
 ("Army",None,r"^(34|35|350|351|352|353|37|38|48)", "intel"),
 ("Army",None,r"^(42C|420C)",         "band"),
 ("Army",None,r"^(63|64|65|66|67|70|71|72|73|60|61|62|640A|670A)", "medical"),
 ("Army",None,r"^(74|740A)",          "cbrn"),
 ("Army",None,r"^(88|882A)",          "driver"),
 ("Army",None,r"^(880A|881A)",        "deck"),
 ("Army",None,r"^(89|890A)",          "ordnance"),
 ("Army",None,r"^(91|913A|914A|915|919A|948)", "mechanic"),
 ("Army",None,r"^(922A)",             "food"),
 ("Army",None,r"^(921A|92D)",         "rigger"),
 ("Army",None,r"^(923A|92F)",         "fuels"),
 ("Army",None,r"^(90|92|920)",        "supply"),
 ("Army",None,r"^(180A)",             "infantry"),
 ("Army",None,r"^(40|47|49|51|52|56|59|01A|27|36|42|46|270A|420A|001A|003A|004A|002A)", "admin"),
 # Navy
 ("Navy",None,r"^(SO|SB)$",           "infantry"),
 ("Navy",None,r"^(EOD)$",             "fire_eod"),
 ("Navy",None,r"^(ND)$",              "diver"),
 ("Navy",None,r"^(AB|ABE|ABF|ABH|AD|AE|AM|AME|AS|AT|AZ|PR)$", "aviation_maint"),
 ("Navy",None,r"^(ABF)$",             "fuels"),
 ("Navy",None,r"^(AW|AWF|AWO|AWR|AWS|AWV|1310|1320|AN)$", "aircrew"),
 ("Navy",None,r"^(AC)$",              "airops"),
 ("Navy",None,r"^(AO|GM|MN|FC|FT)$",  "ordnance"),
 ("Navy",None,r"^(BU|EO|SW|CE|UT|CM|EA|5100)$", "engineer"),
 ("Navy",None,r"^(BM|SN|QM|OS|1110)$","deck"),
 ("Navy",None,r"^(CS)$",              "food"),
 ("Navy",None,r"^(CTI|CTM|CTR|CTT|CTN|IS|1810|1830|AG)$", "intel"),
 ("Navy",None,r"^(ET|IT|IC|1820)$",   "signal"),
 ("Navy",None,r"^(HM)$",              "combat_medic"),
 ("Navy",None,r"^(2100|2300|2900)$",  "medical"),
 ("Navy",None,r"^(2200)$",            "dental"),
 ("Navy",None,r"^(LN|LS|NC|PS|RP|YN|SH|CMC|2500|3100|4100|AZ)$", "admin"),
 ("Navy",None,r"^(MA|6490)$",         "police"),
 ("Navy",None,r"^(MC)$",              "admin"),
 ("Navy",None,r"^(MU)$",              "band"),
 ("Navy",None,r"^(DC)$",              "fire_eod"),
 ("Navy",None,r"^(EM|EN|GS|GSE|GSM|HT|MM|MR|FN|7200|1510|1520)$", "engineroom"),
 ("Navy",None,r"^(STS|MT|1120)$",     "submarine"),
 ("Navy",None,r"^(STG|1130|1140)$",   "deck"),
 # Marines by occupational field
 ("Marine Corps",None,r"^09",         "trainer"),
 ("Marine Corps",None,r"^03",         "infantry"),
 ("Marine Corps",None,r"^18",         "armor"),
 ("Marine Corps",None,r"^08",         "artillery"),
 ("Marine Corps",None,r"^(13|11)",    "engineer"),
 ("Marine Corps",None,r"^(60|61|62|63|64|66|70)", "aviation_maint"),
 ("Marine Corps",None,r"^65",         "ordnance"),
 ("Marine Corps",None,r"^(73|75)",    "aircrew"),
 ("Marine Corps",None,r"^72",         "airops"),
 ("Marine Corps",None,r"^(21|23)",    "ordnance"),
 ("Marine Corps",None,r"^(06|28|59)", "signal"),
 ("Marine Corps",None,r"^(02|26|27|68)", "intel"),
 ("Marine Corps",None,r"^33",         "food"),
 ("Marine Corps",None,r"^35",         "driver"),
 ("Marine Corps",None,r"^(04|30|31)", "supply"),
 ("Marine Corps",None,r"^57",         "cbrn"),
 ("Marine Corps",None,r"^58",         "police"),
 ("Marine Corps",None,r"^55",         "band"),
 ("Marine Corps",None,r"^(01|05|34|41|43|44|46|48|80|99)", "admin"),
 # Air Force
 ("Air Force",None,r"^(1A|11|12|92T|8A000)", "aircrew"),
 ("Air Force",None,r"^(1C2|1T2|13D)", "infantry"),
 ("Air Force",None,r"^(1C|13|1S|1T|8S100)", "airops"),
 ("Air Force",None,r"^(1N|14|1W|15|16|8D000)", "intel"),
 ("Air Force",None,r"^(2A|2P|2R|21B|21M|H21B)", "aviation_maint"),
 ("Air Force",None,r"^(2W|2M|8S000|94N0)", "ordnance"),
 ("Air Force",None,r"^(2E|3C|33)",    "signal"),
 ("Air Force",None,r"^2F",            "fuels"),
 ("Air Force",None,r"^(2T1)",         "driver"),
 ("Air Force",None,r"^(2T3)",         "mechanic"),
 ("Air Force",None,r"^(2S|2T|2G|20|21)", "supply"),
 ("Air Force",None,r"^(3E7|3E8)",     "fire_eod"),
 ("Air Force",None,r"^(3E|32)",       "engineer"),
 ("Air Force",None,r"^(3P|31|7S|71|8J000)", "police"),
 ("Air Force",None,r"^(3N1|3N2|35B|8G000|85G0)", "band"),
 ("Air Force",None,r"^(4Y|47)",       "dental"),
 ("Air Force",None,r"^(4F|4M)",       "aircrew"),
 ("Air Force",None,r"^(4|40|41|42|43|44|45|46|48)", "medical"),
 ("Air Force",None,r"^(8B)",          "trainer"),
 ("Air Force",None,r"^(3A|3S|3M|3N|3V|3H|30|34|35|36|38|5|6|8|9|10|90|91|97|93|96|95|81|82|83|84|86|87|88)", "admin"),
 # Coast Guard
 ("Coast Guard",None,r"^(AET|AMT)$",  "aviation_maint"),
 ("Coast Guard",None,r"^(AST)$",      "aircrew"),
 ("Coast Guard",None,r"^(BM|QM|OS|RD|MST)$", "deck"),
 ("Coast Guard",None,r"^(DC)$",       "fire_eod"),
 ("Coast Guard",None,r"^(MK|EM)$",    "engineroom"),
 ("Coast Guard",None,r"^(ET|IT)$",    "signal"),
 ("Coast Guard",None,r"^(FS)$",       "food"),
 ("Coast Guard",None,r"^(GM|FT)$",    "ordnance"),
 ("Coast Guard",None,r"^(HS)$",       "medical"),
 ("Coast Guard",None,r"^(IS|IV)$",    "intel"),
 ("Coast Guard",None,r"^(PS)$",       "police"),
 ("Coast Guard",None,r"^(MU)$",       "band"),
 ("Coast Guard",None,r"^(SK|YN|PA)$", "admin"),
]
TITLE_RULES = [
 (r"infantry|rifle|scout|special forces|ranger|recon", "infantry"),
 (r"armor|tank|cavalry", "armor"),
 (r"artillery|cannon|mortar|missile crew|air defense", "artillery"),
 (r"aircraft|avionic|helicopter|aerospace|flight line", "aviation_maint"),
 (r"pilot|aviator|aircrew|navigator|loadmaster|flight engineer", "aircrew"),
 (r"mechanic|repairer|maintainer|maintenance", "mechanic"),
 (r"engineer|construction|carpent|plumb|electrician|equipment operator", "engineer"),
 (r"cook|food|culinary|dining", "food"),
 (r"medic|corpsman|nurse|physician|surgeon|health|medical|pharmac|laborator|radiolog|therap", "medical"),
 (r"dental|dentist", "dental"),
 (r"police|security|corrections|master-at-arms|investigat", "police"),
 (r"supply|logistic|storekeeper|cargo|warehouse|transportation management", "supply"),
 (r"driver|motor transport|vehicle operat", "driver"),
 (r"signal|communication|radio|network|information technology|computer|cable", "signal"),
 (r"intelligence|linguist|cryptolog|interrogat|analyst", "intel"),
 (r"band|music", "band"),
 (r"fire|explosive ordnance|eod", "fire_eod"),
 (r"ammunition|ordnance|munition|gunner|weapons", "ordnance"),
 (r"chemical|cbrn|nbc", "cbrn"),
 (r"fuel|petroleum|water treatment", "fuels"),
 (r"parachute|rigger|airdrop", "rigger"),
 (r"laundry|mortuary|shower", "services"),
 (r"boatswain|deck|seaman|quartermaster|watercraft", "deck"),
 (r"machinist|engineman|hull|damage control|gas turbine|boiler|engine room", "engineroom"),
 (r"submarine|sonar", "submarine"),
 (r"air traffic|airfield|air operations|command post", "airops"),
 (r"diver", "diver"),
 (r"drill|instructor|training", "trainer"),
 (r"admin|personnel|finance|legal|paralegal|chaplain|recruit|human resources|clerk|yeoman|public affairs|journalist|postal|services", "admin"),
]
def profile_for(branch, comp, code, title):
    for b, c, rx, pid in RULES:
        if b == branch and (c is None or c == comp) and re.match(rx, code): return pid, "code"
    t = title.lower()
    for rx, pid in TITLE_RULES:
        if re.search(rx, t): return pid, "title"
    return "generic", "fallback"
