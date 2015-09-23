#!/usr/bin/env python

# Copyright 2015 Bas van Meerten and Wouter Franssen

#This file is part of ssNake.
#
#ssNake is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#ssNake is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with ssNake. If not, see <http://www.gnu.org/licenses/>.

import math
import re

def safeEval(inp):
    env = vars(math).copy()
    env["locals"]   = None
    env["globals"]  = None
    env["__name__"] = None
    env["__file__"] = None
    env["__builtins__"] = None
    env["slice"] = slice
    inp =  re.sub('([0-9]+)[k,K]','\g<1>*1024',inp) #WF: allow 'K' input
    try:
        return eval(inp,env)
    except:
        print("Could not interpret input")
        return 0
