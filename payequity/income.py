#!/usr/bin/python

# Calculates income disparity between men and women in the US based on total
# dollars earned by each gender.

import csv
import os

def getIncomeTable(path):
  income_map = {}
  with open(path, 'r') as csvfile:
    income_file = csv.reader(csvfile)
    for line in income_file:
      income_map[line[0]] = (int(line[1].replace(',','')), int(line[2].replace(',', '')))
  return income_map


def computeTotalIncome(income_map):
  total = 0
  for i in income_map:
    total += income_map[i][0] * income_map[i][1]
  return total


def run(dir):
  f_map = getIncomeTable(os.path.join(dir, 'female_income.csv'))
  m_map = getIncomeTable(os.path.join(dir, 'male_income.csv'))

  f_total = computeTotalIncome(f_map)
  m_total = computeTotalIncome(m_map)

  print "Female income fraction = %f" % (float(f_total) / (f_total + m_total))
