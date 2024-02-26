import datetime

import CoT

string = """<?xml version="2.0"?>
    <event
        version="2.0"
        type="a-h-G-E-V-A-T"
        access="Unclassified"
        uid="FBCB2.T-117"
        time="2002-10-05T18:00:23Z"
        start="2002-10-05T18:00:23Z"
        stale="2002-10-05T18:00:23Z"
        how="m-i">
    <point lat="26.4321" lon="-82.0554" hae="0" ce="32" le="221"/>
    </event>
"""

event = CoT.Event(**CoT.xml.parse(string))

print(event.xml())

assert event.uid == "FBCB2.T-117"
assert event.access == "Unclassified"
assert event.time == "2002-10-05T18:00:23.00Z"
assert event.start == "2002-10-05T18:00:23.00Z"
assert event.time == "2002-10-05T18:00:23.00Z"
assert event.type == "a-h-G-E-V-A-T"
