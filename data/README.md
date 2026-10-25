# MOS lookup data

- `mos.json`: every job code across Army (enlisted, officer, warrant), Navy, Marine Corps, Air Force and Coast Guard, plus ~200 older Army codes mapped to their successors. Each row carries the VA Duty MOS Noise Exposure Listing rating (H/M/L), its source (`va`, `successor` for legacy codes, `estimated` for a few codes the listing does not carry), a hazard profile id and search words.
- `profiles.json`: 31 hazard profiles by career field. Each lists job hazards and the body areas they reach, with condition names and typical rating codes.
- `src/`: the source tables and the build script. Edit there, then run `python3 data/src/build.py` and `python3 build_site.py`.

Noise ratings were transcribed from republished copies of VA's listing (vaclaimsinsider.com and veteranbenefitdesk.com). Hazard profiles, condition lists, rating codes and the legacy code map are draft content written for this build. They need review against 38 CFR Part 4 and by a clinician before a veteran relies on them.
