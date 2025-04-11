# Overview

Execution of a "Pesky Neighbor" attack against a team
This attack exploits a design flaw where instead of having a global timestamp counter for accepting frames after a certain timestamp, there is instead one per channel. This allows us to send out of order frames for one channel and then another, technically violating sequential timestamp requirements and earning a flag.

This is a version of the nonglobal_monotonic except it is with just channel 0.

# Running

Run the package script:

```
./package.sh team_name
```

Submit the resulting zip file to the pesky neighbor service.

# Teams Attacked

- CAT
