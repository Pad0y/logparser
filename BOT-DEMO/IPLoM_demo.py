#!/usr/bin/env python

import sys

sys.path.append("../")
from logparser import IPLoM

input_dir = "../logs/BOT/"  # The input directory of log file
output_dir = "../results/IPLoM_result/"  # The output directory of parsing results
log_file = "BOT_2K.log"  # The input log file name
# log_file = "BOT_2K.log"  # The input log file name
# log_format = "<Date> <Time> <Pid> <Level> <Component>: <Content>"  # HDFS log format
log_format = "<SIP> <UREG> <USANAME> <[REQTIME]> <\"RM> <URI> <HTTPVER\"> <CODE> <RESPSIZE> <\"REF\"> <\"UA\"> <\"ATACK\"> <SOURCE>"  # HDFS log format
maxEventLen = 120  # The maximal toke number of log messages (default: 200)
step2Support = 0  # The minimal support for creating a new partition (default: 0)
CT = 0.35  # The cluster goodness threshold (default: 0.35)
lowerBound = 0.25  # The lower bound distance (default: 0.25)
upperBound = 0.9  # The upper bound distance (default: 0.9)
regex = []  # Regular expression list for optional preprocessing (default: [])

parser = IPLoM.LogParser(
    log_format=log_format,
    indir=input_dir,
    outdir=output_dir,
    maxEventLen=maxEventLen,
    step2Support=step2Support,
    CT=CT,
    lowerBound=lowerBound,
    upperBound=upperBound,
    rex=regex,
)
parser.parse(log_file)
