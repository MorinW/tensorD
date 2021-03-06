#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 PM7:22
# @Author  : Shiloh Leung
# @Site    :
# @File    : cp_ex.py
# @Software: PyCharm Community Edition

from tensorD.factorization.env import Environment
from tensorD.dataproc.provider import Provider
from tensorD.factorization.ncp import NCP_BCU
from tensorD.demo.DataGenerator import *
import sys


def ncp_run(N1, N2, N3, gR, dR, time):
    # ncp test
    X = synthetic_data_cp([N1, N2, N3], gR, 0)
    data_provider = Provider()
    data_provider.full_tensor = lambda: X
    env = Environment(data_provider, summary_path='/tmp/ncp_' + str(N1))
    ncp = NCP_BCU(env)
    args = NCP_BCU.NCP_Args(rank=dR, validation_internal=200)
    ncp.build_model(args)
    print('\n\nNCP with %dx%dx%d, gR=%d, dR=%d, time=%d' % (N1, N2, N3, gR, dR, time))
    hist = ncp.train(6000)
    scale = str(N1) + '_' + str(gR) + '_' + str(dR)
    out_path = '/root/tensorD_f/data_out_tmp/python_out/ncp_' + scale + '_' + str(time) + '.txt'
    with open(out_path, 'w') as out:
        for iter in hist:
            loss = iter[0]
            rel_res = iter[1]
            out.write('%.10f, %.10f\n' % (loss, rel_res))


if __name__ == '__main__':
    ncp_run(N1=int(sys.argv[1]),
            N2=int(sys.argv[2]),
            N3=int(sys.argv[3]),
            gR=int(sys.argv[4]),
            dR=int(sys.argv[5]),
            time=int(sys.argv[6]))
