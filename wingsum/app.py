#!/usr/bin/env python3

# wingsum: Parses flightlog and sums up the flight time/count per wing
# Copyright (C) 2018  Øyvind 'Mr.Elendig' Heggstad

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import requests
import lxml.html
import click
import tabulate

FL_URL = "http://no.flightlog.org/fl.html"
TABLE_FORMATS = ["plain",
        "simple",
        "grid",
        "fancy_grid",
        "pipe",
        "orgtbl",
        "jira",
        "presto",
        "psql",
        "rst",
        "mediawiki",
        "moinmoin",
        "youtrack",
        "html",
        "latex",
        "latex_raw",
        "latex_booktabs",
        "textile"
        ]

def hm_to_i(s):
    """'01:30' -> 90"""
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def i_to_hm(i):
    """90 -> '1:30'"""
    return "{:0=2}:{:0=2}".format(i // 60, i % 60)


def convf(f):
    """'/ 9' -> 9"""
    if f:
        return int(f[0].strip("/ "))
    return 1


@click.command()
@click.version_option()
@click.option("--style", "-s", default="simple", type=click.Choice(TABLE_FORMATS),
        help="The table style to use")
@click.argument("uid")
def main(uid, style):
    """ Parses flightlog and sums up the flight time/count per wing

    UID: flightlog user ID"""

    req = requests.get(FL_URL, params={"a": 28, "user_id": uid})

    if not req.ok:
        print(req.status, file=sys.stderr)
        sys.exit(1)

    doc = lxml.html.fromstring(req.content)

    wings = {}
    for tr in doc.xpath("/html/body/div/div/table/tr[text()]"):
        name, time, *flights = tr.xpath("td[position() = 3 or position() = 4]/text()")
        wings[name] = [a + b for a, b in zip(wings.get(name, [0, 0]), [hm_to_i(time), convf(flights)])]

    table = [[wing, i_to_hm(wings[wing][0]), wings[wing][1]] for wing in wings]

    if not table:
        print("No flights found for UID {}".format(uid), file=sys.stderr)
        sys.exit(2)

    print(tabulate.tabulate(table, ["Wings", "Time", "Flights"], tablefmt=style))


if __name__ == "__main__":
    main()
