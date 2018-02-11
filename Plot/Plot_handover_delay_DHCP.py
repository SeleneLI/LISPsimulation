# -*- coding: utf-8 -*-
__author__ = 'yueli'

import matplotlib.pyplot as plt
from config.config import *
import numpy as np
import math
from collections import Counter
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True
mpl.rcParams.update({'figure.autolayout': True})
plt.rcParams["font.family"] = "Times New Roman"

# xTR_TRACE_PATH = 'LISP_mobility_xTR.csv'
#
# with open(xTR_TRACE_PATH) as f_handler:
#     next(f_handler)
#     print f_handler
#     for line in f_handler:
#         print line
#         lines = line.split(';')
#         print lines[0], lines[-1]

# # For LISP_mobility_xTR:
# DHCP_delay_list = [0.0,0.1,0.3,0.5,1.0,1.5,2.0]
# last_UDP_list = [26.359045,26.366230,26.366230,26.366230,26.366971,26.175051,25.360947]
# first_DHCP_list = [26.365173,26.372359,26.372359,26.372359,26.373177,26.181248,25.367112]
# last_DHCP_list = [26.368360,26.475511,26.675511,26.875511,27.376330,27.684320,27.370184]
# first_UDP_list = [26.423986,26.534058,26.734058,26.934058,27.434650,27.744139,27.434094]

# # For LISP_mobility_LISPMN:
# DHCP_delay_list = [0.0,0.1,0.3,0.5,1.0,1.5,2.0]
# last_UDP_list = [26.161697,26.161697,26.161697,26.161697,26.161697,25.570286,26.173139]
# first_DHCP_list = [26.167970,26.167970,26.167970,26.167970,26.167970,25.576503,26.179383]
# last_DHCP_list = [26.174323,26.273184,26.473184,26.673184,27.173184,27.081196,28.184066]
# first_LISP_list = [26.183366,26.279019,26.479019,26.679019,27.179019,27.086842,28.189892]
# last_LISP_list = [26.214562,26.308269,26.508269,26.708269,27.208268,27.116058,28.219223]
# first_UDP_list = [26.244728,26.334728,26.534728,26.734728,27.234728,27.144228,28.244727]


# For LISP_mobility_double_encap:
DHCP_delay_list = [0.0,0.1,0.3,0.5,1.0,1.5,2.0]
last_UDP_list = [25.058018,25.058018,25.058018,25.058018,25.064548,25.755451,24.950013]
first_DHCP_list = [25.061533,25.061533,25.061533,25.061533,25.068019,25.756989,24.951551]
last_DHCP_list = [25.068067,25.166964,25.366964,25.566964,26.073422,27.262419,26.957044]
first_LISP_list = [25.073758,25.172709,25.372709,25.572709,26.079149,27.268254,26.964195]
last_LISP_list = [25.326211,25.425189,25.625189,25.825189,26.334627,27.523260,27.216583]
first_UDP_list = [25.364897,25.464897,25.664897,25.864897,26.364897,27.564897,27.244897]

# Minus elements in two lists and put the results in a new list
delay_list = [x - y for x, y in zip(first_UDP_list, last_UDP_list)]

plt.plot(DHCP_delay_list, delay_list, linewidth = 3)
plt.scatter(DHCP_delay_list, delay_list, s = 100)
plt.xlabel(r"\textrm{DHCP association delay (s)}", font)
plt.ylabel(r"\textrm{Handover delay (s)}", font)
plt.xticks(fontsize=40, fontname="Times New Roman")
plt.yticks(fontsize=40, fontname="Times New Roman")
plt.xlim(0,2)
# plt.ylim(0,2.25)
plt.savefig('LISP_mobility_double_encap_DHCP.eps', dpi=300, transparent=True)
plt.show()
plt.close()
