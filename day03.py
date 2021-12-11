#!/usr/bin/env python

import argparse
import logging
import sys


def find_common_bits(diagnosticList, invert):
    # Assume all entries in list are the same length
    count = [0] * len(list(diagnosticList[0]))
    commonBits = [0] * len(list(diagnosticList[0]))
    uncommonBits = [0] * len(list(diagnosticList[0]))

    for i in range(len(diagnosticList)):
        diagnostic = list(map(int, diagnosticList[i]))
        for j in range(len(diagnostic)):
            if diagnostic[j] == 1:
                count[j] = count[j] + 1

    for i in range(len(count)):
        if count[i] >= (len(diagnosticList) / 2):
            commonBits[i] = 1
        else:
            uncommonBits[i] = 1

    if invert:
        return uncommonBits

    return commonBits


def list_to_int(rateList):
    rateString = ""
    for c in rateList:
        rateString = rateString + str(c)
    rateInt = int(rateString, 2)

    return rateInt


def filter_by_bit_criteria(diagnosticList, rateList, index):
    outputList = []
    for i in range(len(diagnosticList)):
        diagnostic = list(map(int, diagnosticList[i]))
        if diagnostic[index] == rateList[index]:
            outputList.append(diagnosticList[i])

    return outputList


parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

with open(args.file, "r") as f:
    diagnostics = f.read().splitlines()

gamma_rate = find_common_bits(diagnostics, 0)
epsilon_rate = find_common_bits(diagnostics, 1)
logging.debug('gamma rate: %s' % gamma_rate)
logging.debug('epsilon rate: %s' % epsilon_rate)

gammaInt = list_to_int(gamma_rate)
epsilonInt = list_to_int(epsilon_rate)
power_consumption = gammaInt * epsilonInt
print("Power consumption (gamma * epsilon) = %i * %i = %i" % (gammaInt, epsilonInt, power_consumption))

oxygen_generator_rating = diagnostics
rateList = gamma_rate
for i in range(len(rateList)):
    if len(oxygen_generator_rating) < 2:
        logging.debug('oxygen_generator_rating calculation stopped at %i' % i)
        break
    oxygen_generator_rating = filter_by_bit_criteria(oxygen_generator_rating, rateList, i)
    rateList = find_common_bits(oxygen_generator_rating, 0)

co2_scrubber_rating = diagnostics
rateList = epsilon_rate
for i in range(len(rateList)):
    if len(co2_scrubber_rating) < 2:
        logging.debug('co2_scrubber_rating calculation stopped at %i' % i)
        break
    co2_scrubber_rating = filter_by_bit_criteria(co2_scrubber_rating, rateList, i)
    rateList = find_common_bits(co2_scrubber_rating, 1)

logging.debug('oxygen generator rating: %s' % oxygen_generator_rating)
logging.debug('co2_scrubber_rating rate: %s' % co2_scrubber_rating)

oxygen_generator_ratingInt = list_to_int(oxygen_generator_rating)
co2_scrubber_ratingInt = list_to_int(co2_scrubber_rating)
life_support_rating = oxygen_generator_ratingInt * co2_scrubber_ratingInt
print("Life support rating (oxygen generator rating * CO2 scrubber rating) = %i * %i = %i" % (oxygen_generator_ratingInt, co2_scrubber_ratingInt, life_support_rating))
