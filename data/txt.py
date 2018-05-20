import re
from data import dbg_data_txt
from builtins import int


############################################
#
#    read from txt-file
#
############################################
def getDimSrv(f):
    line = f.readline().rstrip('\n')
    reg = re.compile("[ ;]")
#    res = reg.split(line)[1:-1]
    res = reg.split(line)
    if res[-1] is '':
        res = res [1:-1]
    else:
        res = res[1:]
    if dbg_data_txt:
        print("data.txt.getDimSrv: line: '%s', res: %s" % (line, res))
    return res


def get_diap(f):
    s = getDimSrv(f)
    l = len(s)
    # http://www.i-programmer.info/programming/python/3942-arrays-in-python.html?start=1
    r = [[0 for j in range(l)] for i in range(2)]
    # if dbg_data_txt:
    #     print("data.txt.get_diap: r: %s" % r)
    #     for i in range(2):
    #         for j in range(l):
    #             print("data.txt.get_diap: r[%d, %d]: %d" % (i,j,r[i][j]))

    for i in range(l):
        q = s[i]
        lower_bound = int(q.split(',')[0])
        upper_bound = int(q.split(',')[1])
        if dbg_data_txt:
            print("data.txt.get_diap: part(%d): '%s', lower_bound: %d, upper_bound: %d" % (
            i, q, lower_bound, upper_bound))
        r[0][i] = lower_bound;
        r[1][i] = upper_bound;
    if dbg_data_txt: print("data.txt.get_diap: r: %s" % r)
    return r


def read_string(f):
    line1 = f.readline().rstrip('\n')
    line2 = f.readline().rstrip('\n')
    if dbg_data_txt:
        print("data.txt.read_string: comment: '%s', string: '%s'" % (line1, line2))
    return line2


def read_integer(f):
    line1 = f.readline().rstrip('\n')
    line2 = f.readline().rstrip('\n')
    rez = int(line2)
    if dbg_data_txt:
        print("data.txt.read_integer: comment: '%s', rez: %d" % (line1, rez))
    return rez  # !!!


def read_float(f):
    line1 = f.readline().rstrip('\n')
    line2 = f.readline().rstrip('\n')
    rez = float(line2.replace(',', '.'))
    if dbg_data_txt:
        print("data.txt.read_float: comment: '%s', rez: %f" % (line1, rez))
    return rez


def read_boolean(f):
    line1 = f.readline().rstrip('\n')
    line2 = f.readline().rstrip('\n')
    rez = line2 == 'Истина'
    if dbg_data_txt:
        print("data.txt.read_boolean: comment: '%s', value: '%s', rez: %r" % (line1, line2, rez))
    return rez
