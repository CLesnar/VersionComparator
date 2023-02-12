#!/usr/bin/python

import sys
import re

# Compares version strings and returns 
# 0 for equal version1 and version2, 
# -1 for version1 < version2
# 1 for version1 > version2
def version_compare( version1: str, version2: str ):
    # sanitize
    # RE: regexr.com/77vml
    regExpStr = "(^\d+(\.\d*){0,4}$)"
    v1re = re.match(regExpStr, version1, re.IGNORECASE)
    v2re = re.search(regExpStr, version2, re.IGNORECASE)

    # debug
    # print("v1, v2: ", v1re, v2re)

    if v1re is None:
        raise Exception("version1 param has invalid version string format: ", version1, "expected 1.2.3.4.5")
    if v2re is None:
        raise Exception("version2 param has invalid version string format: ", version2, "expected 1.2.3.4.5")

    # read inputs
    version1list, version2list = list(map(int, version1.split("."))), list(map(int, version2.split(".")))
    v1len, v2len = len(version1list), len(version2list)
    maxLength = max(v1len, v2len)
    # compare
    i = 0
    for i in range(0, maxLength):
        if i < v1len and i < v2len:
            if version1list[i] > version2list[i]:
                return 1
            elif version1list[i] < version2list[i]:
                return -1
        elif i < v1len and i >= v2len:
            if version1list[i] > 0:
                return 1
        elif i >= v1len and i < v2len:
            if version2list[i] > 0:
                return -1
    return 0

# compare versions
# versions are stored in <format>
# version format: string, 5 parts: M.m.p.b.c
# version numbers are always positive integers
# examples: "2", "1.5", "2.12.4.0.6" 

def testCompareVersion():
    testCases = [
        # map {version1: <str>, version2: <str>, expected_result: <int>}
    {"version1":"2","version2":"2.0", "expected_result":0},
    {"version1":"2","version2":"2.1", "expected_result":-1},
    {"version1":"2.2","version2":"2.1", "expected_result":1},
    {"version1":"2.2","version2":"2", "expected_result":1},
    {"version1":"2.2","version2":"2.0", "expected_result":1},
    {"version1":"2","version2":"2.0.0.0", "expected_result":0},
    {"version1":"2.0","version2":"2.0.0.0", "expected_result":0},
    {"version1":"2.0.0","version2":"2.0.0.0", "expected_result":0},
    {"version1":"2.0.0.0","version2":"2.0.0.0", "expected_result":0},
    {"version1":"2.0.0.0","version2":"2.0.0", "expected_result":0},
    {"version1":"2.0.0.0","version2":"2.0", "expected_result":0},
    {"version1":"2.0.0.0","version2":"2", "expected_result":0},
    {"version1":"285858585.555.0.0","version2":"285858585.555", "expected_result":0},
    {"version1":"3", "version2":"2", "expected_result":1},
    {"version1":"3.0", "version2":"2.0", "expected_result":1},
    {"version1":"3.0", "version2":"2.0.0.0", "expected_result":1},
    {"version1":"3.0", "version2":"4.0.0.0", "expected_result":-1},
    {"version1":"3.1.0", "version2":"4.0.0.0", "expected_result":-1},
    {"version1":"4.1.2.3.5", "version2":"4.1.2.3.6", "expected_result":-1},
    {"version1":"4.1.2.3.7", "version2":"4.1.2.3.6", "expected_result":1},
    ]

    failures = 0
    for tc in testCases:
        result = version_compare(tc["version1"], tc["version2"])
        if tc["expected_result"] != result:
            print("test failed:  tc: ", tc, ", Result: ", result)
            failures += 1
        else:
            print("test succeeded: tc: ", tc, ", Result: ", result)
    
    exceptionCases = [
        # map {version1: <str>, version2: <str>, expected_result: <int>}
    {"version1":"2","version2":"2.a"},
    {"version1":"A","version2":"2.1"},
    {"version1":"2.2.1.c","version2":"2.1"},
    {"version1":"2.2.1.c","version2":"aB"},
    {"version1":"2.2.1.c","version2":""},
    {"version1":"","version2":""},
    {"version1":"","version2":"1.2.3.4.5"},
    {"version1":"1.2.3","version2":""},
    {"version1":"1.2.3","version2":".1"},
    {"version1":".3","version2":"0.1"},
    {"version1":".3","version2":".b1"},
    ]

    for tc in exceptionCases:
        isRaised = False
        try:
            result = version_compare(tc["version1"], tc["version2"])
        except:
            isRaised = True

        if not isRaised:
            print("test failed:  tc: ", tc, ", Result: ", result, "No exception occurred")
            failures += 1
        else:
            print("test succeeded: tc: ", tc, ", Result: ", result)
    
    if failures == 0:
        print("All tests successful!")
    else:
        print("Failures: ", failures)

def main():
    print("hi")
    testCompareVersion()

main()