#!/usr/bin/env python3

# wingsum: Parses flighlog and sums up the flight time/count per wing
# Copyright (C) 2012  Øyvind 'Mr.Elendig' Heggstad

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


from setuptools import setup, find_packages
setup(
    name = "wingsum",
    version = '0.1.1',
    description = "Parses flighlog and sums up the flight time/count per wing",
    url = "https://github.com/MrElendig/wingsum",
    author = "Øyvind \"Mr.Elendig\" Heggstad",
    author_email = "mrelendig@har-ikkje.net",
    license = "AGPLv3",
    packages = find_packages(),
    entry_points = """
        [console_scripts]
        wingsum=wingsum.app:main
    """,
    python_requires = ">=3",
    install_requires = ["requests", "lxml", "click", "setuptools", "tabulate"]
)
