import os
import sys
import argparse
import yaml
import math


def parseLidarYaml(yamlFile):
    with open(yamlFile) as file:
        obj = yaml.safe_load(file)

        print(
            "double[] {0} = {1}".format(
                os.path.splitext(os.path.basename(yamlFile))[0], "{"
            )
        )
        cnt = 4
        for laser in obj["lasers"]:
            deg = math.degrees(laser["vert_correction"])
            print("{0},".format(deg), end="")
            cnt -= 1
            if cnt <= 0:
                print("")
                cnt = 4

        print("{0};".format("}"))


parser = argparse.ArgumentParser()
parser.add_argument("yml", nargs="+")

args = vars(parser.parse_args())

if len(args) < 1:
    parser.print_help()
    exit(0)

for f in args["yml"]:
    parseLidarYaml(f)
