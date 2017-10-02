========================================================================
wingsum: Parses flightlog.org and sums up the flight time/count per wing
========================================================================
:Author: Øyvind 'Mr.Elendig' Heggstad

Description
===========
| A silly little tool I wrote just beacuse I was too lazy to sum
| up the number of flights and time per wing on flightlog.org

Dependencies
============
| python 3 (tested on 3.6, no guarantees for earlier versions)
| requests
| lxml
| click
| tableprint
| setuptools (for the setup.py)

Instalation
============
| pip install --user . / virtualenv / whatever
| if you run sudo pip ... you will be eaten by a grue.

Usage
=====
| Run `wingsum <UID>` where UID is the flighlog.org user ID.
| Example output:
| ◢■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■◣
|               Wing                Time    Flights  
|  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
|         Niviuk Koyot 3 28 Citrus   37:33        95 
|  Skywalk Mescal 4 L (skulevinge)   01:35        17 
| ◥■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■◤
