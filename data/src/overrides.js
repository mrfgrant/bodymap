const IMG = {front:"__FRONT__", back:"__BACK__"};
const STRENGTH = {3:"Strong fit with job duties",2:"Plausible fit",1:"Weak from MOS alone",0:"Presumptive by dates and places"};

/* Body areas are shared by every MOS and every presumptive program.
   spots: [x, y, rx, ry?] in the illustration's pixel grid (1116 x 1999). side: label margin. */
const AREAS = [
  {id:"head",label:"Head",title:"Head",v:{front:{side:"L",spots:[[558,142,36,20]]}}},
  {id:"ears",label:"Ears",title:"Ears",v:{front:{side:"R",spots:[[480,250,16],[638,250,16]]}}},
  {id:"neck",label:"Neck",title:"Neck",v:{back:{side:"L",spots:[[558,352,30,22]]}}},
  {id:"shoulders",label:"Shoulders",title:"Shoulders",v:{front:{side:"R",spots:[[365,500,24],[750,500,24]]},back:{side:"R",spots:[[360,480,24],[755,480,24]]}}},
  {id:"airways",label:"Airways",title:"Lungs and airways",v:{front:{side:"L",spots:[[524,566,46,34]]}}},
  {id:"heart",label:"Heart",title:"Heart and circulation",v:{front:{side:"R",spots:[[640,590,24]]}}},
  {id:"upperback",label:"Upper back",title:"Upper and mid back",v:{back:{side:"L",spots:[[558,585,52,34]]}}},
  {id:"urinary",label:"Urinary",title:"Kidneys, bladder and reproductive organs",v:{back:{side:"L",spots:[[468,716,22],[648,716,22]]}}},
  {id:"gut",label:"Digestive",title:"Digestive system",v:{front:{side:"L",spots:[[558,762,44,26]]}}},
  {id:"lowback",label:"Low back",title:"Low back",v:{back:{side:"L",spots:[[558,822,72,36]]}}},
  {id:"abdomen",label:"Abdomen",title:"Abdominal wall",v:{front:{side:"L",spots:[[558,884,42,22]]}}},
  {id:"hips",label:"Hips",title:"Hips",v:{front:{side:"L",spots:[[436,952,24],[682,952,24]]},back:{side:"L",spots:[[428,962,24],[690,962,24]]}}},
  {id:"elbows",label:"Elbows",title:"Elbows",v:{front:{side:"R",spots:[[320,744,22],[796,744,22]]},back:{side:"R",spots:[[316,744,22],[800,744,22]]}}},
  {id:"skin",label:"Skin",title:"Forearm and hand skin",v:{front:{side:"R",spots:[[296,842,22],[820,842,22]]}}},
  {id:"wrists",label:"Hands",title:"Wrists and hands",v:{front:{side:"R",spots:[[246,1004,26],[866,1004,26]]},back:{side:"R",spots:[[250,994,26],[870,994,26]]}}},
  {id:"whole",label:"Whole body",title:"Whole body",v:{front:{side:"L",spots:[[258,1290,30]]},back:{side:"L",spots:[[258,1290,30]]}}},
  {id:"knees",label:"Knees",title:"Knees",v:{front:{side:"R",spots:[[462,1385,30],[655,1385,30]]},back:{side:"R",spots:[[465,1380,30],[650,1380,30]]}}},
  {id:"lowerlegs",label:"Lower legs",title:"Lower legs",v:{front:{side:"L",spots:[[455,1580,22],[660,1580,22]]},back:{side:"L",spots:[[455,1560,22],[660,1560,22]]}}},
  {id:"feet",label:"Feet",title:"Feet and ankles",v:{front:{side:"R",spots:[[440,1812,28],[675,1812,28]]},back:{side:"R",spots:[[440,1820,28],[670,1820,28]]}}}
];
const BACK_NOTE = "VA rates the upper, mid and low back together as one unit (the thoracolumbar spine). This area and the low back lead to one rating, not two.";

const MOS = {
  "94B":{
    name:"Food Service Specialist", branch:"Army", blurb:"Army cook, later recoded 92G", start:"knees",
    noise:"92G Food Service Specialist (formerly 94B) is rated Low.",
    hazards:{
      standing:{label:"Long shifts on your feet",desc:"Ten to fourteen hour shifts standing on concrete or tile, often starting before 0400."},
      lifting:{label:"Heavy lifting",desc:"Full stock pots, 50 lb sacks, ration cases and insulated food containers, lifted and carried many times a shift."},
      field:{label:"Field kitchen setup",desc:"Raising and breaking down the mobile kitchen, hauling burner units, water cans and equipment by hand."},
      repetitive:{label:"Repetitive hand work",desc:"Hours of chopping, stirring, scooping and working the serving line."},
      posture:{label:"Bent, head-down work",desc:"Hours bent over prep tables, deep sinks and low ovens with the head down."},
      heat:{label:"Heat, flame and steam",desc:"Grills, ovens, deep fryers and steam kettles at close range every shift."},
      knives:{label:"Knives and slicers",desc:"Daily blade work at speed, plus meat slicers and can openers."},
      floors:{label:"Wet, greasy floors",desc:"Slips and falls while carrying loads."},
      wet:{label:"Cleaning chemicals and wet work",desc:"Hands in hot water, degreasers and sanitizers for hours."},
      fumes:{label:"Cooking smoke and burner exhaust",desc:"Grill smoke indoors and fuel-fired burners in field kitchens."},
      noise:{label:"Noise",desc:"VA rates this MOS Low for noise. Any noise claim has to rest on something other than the job title.",stmt:"[Describe the noise you were around: ranges, generators, vehicles, and how often.]"}
    },
    regions:{
      ears:{s:1,hazards:["noise"],conds:[["Tinnitus","DC 6260"],["Hearing loss","DC 6100"]],
        note:"VA's own listing rates this MOS Low for noise, so the MOS will not carry this claim. Look for other exposure: weapons qualification, generators in the field, or assignment to an artillery, armor or aviation unit.",
        evidence:["Unit assignment history showing a loud unit","Statement describing range time and field generators","Current audiogram"]},
      neck:{s:2,hazards:["posture","lifting"],conds:[["Cervical strain","DC 5237"],["Degenerative arthritis of the cervical spine","DC 5242"],["Cervical radiculopathy, secondary to the neck","DC 8510"]],
        evidence:["Statement on hours of head-down prep work and loads carried","Treatment records, even years later","Current imaging and range of motion exam"]},
      shoulders:{s:2,hazards:["lifting","field"],conds:[["Shoulder strain or rotator cuff tendinopathy","DC 5201"],["Shoulder impingement","DC 5201, by analogy"]],
        evidence:["Statement on lifting pots and cases to and from high shelves","Buddy statement from the same kitchen","Current orthopedic exam or imaging"]},
      airways:{s:1,hazards:["fumes","wet"],conds:[["Asthma","DC 6602"],["Chronic rhinitis","DC 6522"]],
        note:"The job gives a possible exposure, but the link is weaker than for joints. Service dates and places may give a stronger presumptive path than the MOS does.",
        evidence:["Statement on ventilation and field burner use","Service dates and locations for presumptive screening","Pulmonary function test"]},
      upperback:{s:2,hazards:["posture","lifting","field"],conds:[["Thoracic strain","DC 5237"]],note:BACK_NOTE,
        evidence:["Statement on bending and lifting through a shift","Buddy statement from the same kitchen","Current exam covering the whole back"]},
      lowback:{s:3,hazards:["lifting","field","standing","floors","posture"],conds:[["Lumbosacral strain","DC 5237"],["Degenerative arthritis of the spine","DC 5242"],["Sciatica, secondary to the back","DC 8520"]],
        evidence:["Statement on what was lifted, how heavy and how often","Buddy statement describing a specific injury or fall","Current imaging and range of motion exam"]},
      abdomen:{s:2,hazards:["lifting","field"],conds:[["Hernia","DC 7338"]],
        evidence:["Statement tying onset to a lift","Surgical records, including civilian repair after service","Current exam"]},
      hips:{s:2,hazards:["standing","lifting","floors"],conds:[["Hip strain or limited motion","DC 5251 to 5253"],["Trochanteric bursitis","DC 5019"],["Degenerative arthritis of the hip","DC 5003"]],
        evidence:["Statement on standing hours, lifting and any falls","Buddy statement","Current imaging and range of motion exam"]},
      elbows:{s:2,hazards:["repetitive","lifting"],conds:[["Lateral epicondylitis (tennis elbow)","DC 5024, by analogy"]],
        evidence:["Statement on daily repetitive tasks","Treatment records, even years later","Current exam"]},
      skin:{s:3,hazards:["heat","knives","wet"],conds:[["Burn scars","DC 7801 to 7805"],["Laceration scars","DC 7804, 7805"],["Contact dermatitis or eczema","DC 7806"]],
        note:"Scars are their own evidence. A visible burn or cut scar plus a statement on how it happened is a clean claim even with no service records.",
        evidence:["Photos of scars with measurements","Statement on how each burn or cut happened","Dermatology exam"]},
      wrists:{s:3,hazards:["repetitive","knives"],conds:[["Carpal tunnel syndrome","DC 8515"],["Wrist tendinitis or De Quervain's","DC 5024"],["Finger injury residuals from cuts","DC 5216 to 5230"]],
        evidence:["Statement on hours of knife and ladle work","Nerve conduction study","Buddy statement on a specific hand injury"]},
      knees:{s:3,hazards:["standing","lifting","field","floors"],conds:[["Knee strain or patellofemoral pain","DC 5260, 5261"],["Knee instability","DC 5257"],["Degenerative arthritis of the knee","DC 5003"]],
        evidence:["Statement on standing hours and any falls","Buddy statement","Current imaging and exam"]},
      lowerlegs:{s:2,hazards:["standing"],conds:[["Varicose veins","DC 7120"]],
        evidence:["Statement on years of standing shifts","Photos","Vascular exam"]},
      feet:{s:3,hazards:["standing","floors"],conds:[["Plantar fasciitis","DC 5269"],["Flatfoot, acquired or aggravated","DC 5276"],["Ankle sprain residuals","DC 5271"]],
        evidence:["Statement on shift length, flooring and boots","Buddy statement from the same dining facility","Podiatry diagnosis"]}
    }
  },
  "0352":{
    name:"Anti-Tank Missileman", branch:"Marine Corps", blurb:"Marine Corps infantry, TOW and Javelin gunner", start:"ears",
    noise:"Marine Corps enlisted 03XX Infantry, which includes 0352, is rated Highly Probable.",
    hazards:{
      blast:{label:"Weapons blast and noise",desc:"Missile launches and backblast, machine guns and small arms, in training and in combat."},
      load:{label:"Heavy loads on foot",desc:"Missiles, launch units and tripods carried on top of a full combat load."},
      marching:{label:"Forced marches and running",desc:"Conditioning hikes under load, field exercises and years of running in boots."},
      crew:{label:"Lifting and mounting the system",desc:"Hoisting launchers, tripods and missiles on and off vehicles and into firing position."},
      mounted:{label:"Vehicle and turret time",desc:"Riding and manning a TOW vehicle: jolts, vibration and a helmet on the neck for hours."},
      terrain:{label:"Falls and rough terrain",desc:"Night movement, dismounting vehicles and uneven ground while loaded."},
      combat:{label:"Combat and deployment events",desc:"Depends on where and when the Marine served. For combat veterans, 38 U.S.C. 1154(b) eases proof of what happened.",stmt:"[Describe the specific combat or blast events, with dates and places as best you remember.]"},
      exposure:{label:"Deployment exposures",desc:"Burn pits, dust and other exposures tied to service location and dates, not to the MOS.",stmt:"[Describe what you were exposed to and where: burn pits, smoke, dust, fuel.]"}
    },
    regions:{
      ears:{s:3,hazards:["blast"],conds:[["Tinnitus","DC 6260"],["Hearing loss","DC 6100"]],
        note:"VA's noise listing rates Marine infantry Highly Probable, so hazardous noise exposure is conceded from the MOS. This is the strongest link on this map.",
        evidence:["DD-214 showing MOS 0352","Statement on when the ringing or hearing trouble began","Current audiogram"]},
      head:{s:2,hazards:["blast","combat"],conds:[["Traumatic brain injury residuals","DC 8045"],["Migraine or post-traumatic headaches","DC 8100"],["PTSD","DC 9411"]],
        note:"These turn on what happened, not on the job title. Describe the specific blasts or events. A combat MOS, deployment record or Combat Action Ribbon makes those events easier to establish.",
        evidence:["Deployment records and awards","Statement naming specific blast or combat events","Buddy statements from the same unit","Neurology or mental health evaluation"]},
      neck:{s:2,hazards:["mounted","load"],conds:[["Cervical strain","DC 5237"],["Degenerative arthritis of the cervical spine","DC 5242"],["Cervical radiculopathy, secondary to the neck","DC 8510"]],
        evidence:["Statement on helmet, pack and turret time","Treatment records, even years later","Current imaging and range of motion exam"]},
      shoulders:{s:3,hazards:["load","crew"],conds:[["Shoulder strain or rotator cuff tendinopathy","DC 5201"],["AC joint or collarbone injury","DC 5203"]],
        evidence:["Statement on carrying and shouldering the weapon system","Buddy statement from the same section","Current orthopedic exam or imaging"]},
      airways:{s:1,hazards:["exposure"],conds:[["Asthma","DC 6602"],["Chronic rhinitis","DC 6522"],["Chronic sinusitis","DC 6510 to 6514"]],
        note:"The MOS adds little here. Service dates and places decide it. Fill in When and where above to check the presumptive path.",
        evidence:["Service dates and locations for presumptive screening","Current diagnosis","Pulmonary function test"]},
      upperback:{s:2,hazards:["load","crew"],conds:[["Thoracic strain","DC 5237"]],note:BACK_NOTE,
        evidence:["Statement on pack weight and lifting the system","Buddy statement","Current exam covering the whole back"]},
      lowback:{s:3,hazards:["load","marching","crew","mounted","terrain"],conds:[["Lumbosacral strain","DC 5237"],["Intervertebral disc syndrome","DC 5243"],["Sciatica, secondary to the back","DC 8520"]],
        evidence:["Statement on loads carried, how far and how often","Buddy statement describing a specific injury or fall","Current imaging and range of motion exam"]},
      abdomen:{s:2,hazards:["crew","load"],conds:[["Hernia","DC 7338"]],
        evidence:["Statement tying onset to a lift","Surgical records, including civilian repair after service","Current exam"]},
      hips:{s:2,hazards:["load","marching"],conds:[["Hip strain or limited motion","DC 5251 to 5253"],["Trochanteric bursitis","DC 5019"],["Degenerative arthritis of the hip","DC 5003"]],
        evidence:["Statement on hikes under load","Buddy statement","Current imaging and range of motion exam"]},
      knees:{s:3,hazards:["load","marching","terrain"],conds:[["Knee strain or patellofemoral pain","DC 5260, 5261"],["Knee instability","DC 5257"],["Degenerative arthritis of the knee","DC 5003"]],
        evidence:["Statement on hikes, running and any falls","Buddy statement","Current imaging and exam"]},
      lowerlegs:{s:2,hazards:["marching","load"],conds:[["Shin splints","DC 5262"],["Stress fracture residuals","DC 5262"]],
        evidence:["Statement on when the shin pain began and how it was treated","Any sick call or light duty memory, backed by a buddy","Current exam or imaging"]},
      feet:{s:3,hazards:["marching","load","terrain"],conds:[["Plantar fasciitis","DC 5269"],["Flatfoot, acquired or aggravated","DC 5276"],["Ankle sprain residuals","DC 5271"]],
        evidence:["Statement on hikes, boots and ankle rolls","Buddy statement","Podiatry diagnosis"]}
    }
  }
};
const ALIAS = {"92G":"94B"};

/* ---------- Presumptive programs: conditions taken from VA.gov, grouped by body area ---------- */
const LOCS = [
  {id:"vietnam",short:"Vietnam",label:"Vietnam, its inland waterways, or within 12 nautical miles offshore"},
  {id:"thailand",short:"Thailand",label:"Thailand, at a US or Royal Thai military base"},
  {id:"dmz",short:"the Korean DMZ",label:"In or near the Korean DMZ"},
  {id:"aoother",short:"Laos, Cambodia, Guam, American Samoa or Johnston Atoll",label:"Laos, Cambodia (Mimot or Krek), Guam, American Samoa or Johnston Atoll"},
  {id:"gulf",short:"the Gulf region",label:"Iraq, Kuwait, Saudi Arabia, Bahrain, Qatar, UAE or Oman, or the Gulf region's waters"},
  {id:"somalia",short:"Somalia",label:"Somalia"},
  {id:"afghan",short:"Afghanistan, Egypt, Jordan or Syria",label:"Afghanistan, Egypt, Jordan or Syria"},
  {id:"post911",short:"Djibouti, Lebanon, Uzbekistan or Yemen",label:"Djibouti, Lebanon, Uzbekistan or Yemen"},
  {id:"isrtur",short:"Israel or Turkey",label:"Israel or Turkey"},
  {id:"lejeune",short:"Camp Lejeune or MCAS New River",label:"Camp Lejeune or MCAS New River, 30 days or more in total"}
];
const PROGS = {
  ao:{name:"Agent Orange",note:"Chloracne, early-onset peripheral neuropathy and porphyria cutanea tarda must be at least 10% disabling within 1 year of exposure.",
    conds:{
      whole:["Diabetes mellitus type 2","Hypothyroidism","Chronic B-cell leukemia","Hodgkin's disease","Multiple myeloma","Non-Hodgkin's lymphoma","MGUS (monoclonal gammopathy of undetermined significance)","AL amyloidosis","Some soft tissue sarcomas","Chloracne","Porphyria cutanea tarda"],
      heart:["Ischemic heart disease","High blood pressure (hypertension)"],
      head:["Parkinson's disease","Parkinsonism"],
      airways:["Respiratory cancers, including lung cancer"],
      urinary:["Bladder cancer","Prostate cancer"],
      feet:["Peripheral neuropathy, early onset"]}},
  burn:{name:"Burn pits and other toxins (PACT Act)",note:"",
    conds:{
      airways:["Asthma diagnosed after service","Chronic bronchitis","Chronic obstructive pulmonary disease (COPD)","Chronic rhinitis","Chronic sinusitis","Constrictive or obliterative bronchiolitis","Emphysema","Granulomatous disease","Interstitial lung disease","Pleuritis","Pulmonary fibrosis","Sarcoidosis","Respiratory cancer of any type"],
      head:["Brain cancer","Glioblastoma","Head cancer of any type","Neck cancer of any type"],
      gut:["Gastrointestinal cancer of any type","Pancreatic cancer"],
      urinary:["Kidney cancer","Reproductive cancer of any type"],
      whole:["Lymphoma of any type","Melanoma"]}},
  gulf:{name:"Gulf War illness",note:"The illness must have lasted at least 6 months.",
    conds:{
      whole:["Chronic fatigue syndrome","Fibromyalgia","Medically unexplained chronic multisymptom illness","Undiagnosed muscle and joint pain"],
      gut:["Functional gastrointestinal disorders"],
      head:["Undiagnosed chronic headaches"],
      heart:["Undiagnosed cardiovascular signs and symptoms"]}},
  lej:{name:"Camp Lejeune water",note:"",
    conds:{
      whole:["Adult leukemia","Aplastic anemia and other myelodysplastic syndromes","Multiple myeloma","Non-Hodgkin's lymphoma"],
      urinary:["Bladder cancer","Kidney cancer"],
      gut:["Liver cancer"],
      head:["Parkinson's disease"]}}
};

/* ---------- Secondary conditions: what commonly follows from a primary ---------- */
const SEC = [
  [/knee|patellofemoral/i,[["Opposite knee condition","DC 5260","Favoring the injured knee overloads the other one."],["Hip strain","DC 5252","A changed gait shifts load to the hip."],["Low back strain","DC 5237","Limping changes how the spine is loaded."]]],
  [/lumbosacral|arthritis of the spine|disc syndrome|thoracic strain/i,[["Sciatica or radiculopathy in the legs","DC 8520","Nerve roots in the low back can be pinched or irritated."],["Hip strain","DC 5252","A stiff or painful back changes how the hips move."]]],
  [/plantar|flatfoot/i,[["Knee strain","DC 5260","Foot mechanics change how the knee tracks."],["Low back strain","DC 5237","A changed gait travels up to the spine."]]],
  [/ankle/i,[["Knee strain","DC 5260","An unstable ankle changes the load on the knee."],["Plantar fasciitis","DC 5269","Guarding the ankle strains the foot."]]],
  [/^hip|trochanteric|of the hip/i,[["Low back strain","DC 5237","Hip pain changes posture and gait."],["Knee strain","DC 5260","A guarded hip shifts load to the knee."]]],
  [/cervical strain|cervical spine/i,[["Cervical radiculopathy in the arms","DC 8510","Nerve roots in the neck can be pinched or irritated."],["Headaches arising from the neck","DC 8100","Neck problems are a recognized cause of chronic headaches."]]],
  [/shoulder|AC joint/i,[["Neck strain","DC 5237","Guarding a shoulder strains the neck muscles."]]],
  [/tinnitus/i,[["Migraine or tension headaches","DC 8100","Constant ringing is a frequently claimed trigger."],["Anxiety or depression","DC 9400, 9434","Chronic tinnitus is linked to mood symptoms."],["Insomnia","Rated with mental health conditions","Ringing often disrupts sleep."]]],
  [/hearing loss/i,[["Tinnitus","DC 6260","Hearing loss and tinnitus commonly occur together."]]],
  [/traumatic brain/i,[["Post-traumatic headaches","DC 8100","Headaches are among the most common lasting effects."],["Depression","DC 9434","Listed as secondary to TBI in 38 CFR 3.310(d) under set conditions."],["Parkinsonism, seizures or dementia","38 CFR 3.310(d)","Presumed secondary to moderate or severe TBI under set conditions."]]],
  [/PTSD/,[["Sleep apnea","DC 6847","Commonly claimed. Needs a sleep study and a medical opinion."],["Acid reflux (GERD)","DC 7206","Often tied to the condition or its medication."],["Migraine headaches","DC 8100","Frequently occur together."],["High blood pressure","DC 7101","Chronic stress is a claimed contributor. Needs a medical opinion."],["Erectile dysfunction","DC 7522","Can follow from the condition or its medication."]]],
  [/migraine|headache/i,[["Depression","DC 9434","Chronic headaches are linked to mood symptoms."]]],
  [/asthma|rhinitis|sinusitis|bronchitis|COPD|emphysema/i,[["Sleep apnea","DC 6847","Airway disease is a commonly claimed contributor. Needs a sleep study."],["Acid reflux (GERD)","DC 7206","Often occurs alongside chronic airway disease."]]],
  [/diabetes/i,[["Peripheral neuropathy in the feet or hands","DC 8520, 8515","Nerve damage is a common complication."],["Diabetic eye disease (retinopathy)","DC 6006","A common complication."],["Kidney disease","DC 7541","A common complication."],["Erectile dysfunction","DC 7522","A common complication."],["High blood pressure","DC 7101","When tied to diabetic kidney disease."]]],
  [/high blood pressure|hypertension/i,[["Hypertensive heart disease","DC 7007","Long-term high blood pressure strains the heart."],["Kidney disease","Rated on kidney function","High blood pressure can damage the kidneys over time."]]],
  [/ischemic heart/i,[["Depression","DC 9434","Heart disease is linked to mood symptoms."]]],
  [/hernia/i,[["Painful surgical scar","DC 7804","Repair scars can stay tender."],["Groin nerve pain after repair","DC 8530","A known complication of hernia surgery."]]],
  [/prostate cancer/i,[["Erectile dysfunction","DC 7522","A common result of treatment."],["Urinary leakage or frequency","Rated as voiding dysfunction","A common result of treatment."]]],
  [/parkinson/i,[["Tremor, balance, speech and swallowing problems","Each rated separately","Each effect of the disease can be rated on its own."],["Depression","DC 9434","Common with the disease."]]],
  [/fibromyalgia|chronic fatigue/i,[["Depression","DC 9434","Common with long-term pain and fatigue."]]]
];
const ORTHO = /strain|arthritis|fasciitis|flatfoot|sprain|tendin|bursitis|epicondylitis|disc syndrome|shin splints|stress fracture|carpal|impingement|AC joint|patellofemoral|limited motion|instability/i;
const ORTHO_SEC = [["Depression or anxiety from chronic pain","DC 9434, 9400","Long-term pain is a recognized cause of mood symptoms."],["Stomach problems from long-term pain medication","DC 7206","Years of anti-inflammatory use can damage the stomach lining."]];
function secFor(name){
  const out = [], seen = new Set([name.toLowerCase()]);
  const add = l => l.forEach(x => { const k = x[0].toLowerCase(); if(!seen.has(k)){ seen.add(k); out.push(x); } });
  SEC.forEach(([re,l]) => { if(re.test(name)) add(l); });
  if(ORTHO.test(name)) add(ORTHO_SEC);
  return out;
}

