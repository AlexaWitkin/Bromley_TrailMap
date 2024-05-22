# Bromley_TrailMap
New interface for Bromley's trail map, utilizing Feratel's hardware.

----------------------------------------------------------------------
**Notes:**

Cord in Port 21 (dell room)

DELL
- turn black box router off, then on
- Go to applications -> Firefox 
- Feratel media technologies AG CPS.net -BROM-Bromley SkiResort - Mozilla Firefox
- BROML, feratel, cps!linux

MAC
- ip: 192.168.2.38
- Admin login 
- BROML, bromley, bromley 
- Go into tools -> 
- Go into sources -> jquery -> external/jquery
- Buttons around lines 7650 in jquery-ui.js 
- Date/time around lines 7900
- Color animations around lines 13975
- Look through 

*Research how to use port forwarding to make specific ip address public 

----------------------------------------------------------------------

TRAILMAP PANNEL (115V -be careful-)
- uses an RS442 on board's X9 for communication to network/router(?)
- RS442 poinout:
  1. TXA
  2. TXB
  3. RXA
  4. RXB
  5. GND 
- RS442 Computer____to____R2442 Device
  - __ TXA+ _______ to ______ RXA+
  - __ TDB- _______ to ______ RXB-
  - __ RXA+ _______ to ______ TXA+
  - __ RXB- _______ to ______ TXB-
  - __ GND  _______ to ______ GND
(may need to swap +/- values, feratel is diff from US board)


- uses an RS442 on board's X8 for communication
- LEDI RS232 pinout:
  1. RA
  2. RB
  3. RX
  4. TX
  5. GND
 




--------------------------------------------------------------------------
Questions for James:
- How are things localized on the network?
  - ip addresses
- How do you access specific paths on specific routers?
  - Can that all be done through ip address?
  - ip addresses and serial input
- If I make a funcitoning website, can we give select people access to the network from anywhere?
  - yes, talk to firewall man (peter)
- When I used HC-05's for bluetooth I get its address and then I use rfcomm bind to bind the primary and secondary (main/sub)
  - How does that work on a larger scale such as with routers and networks?
    - serial input
    - leearn more about the feratel box downstairs
      - pretty sure it's the thing actually communicating with the sign
  
