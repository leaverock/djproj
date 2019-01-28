import os, sys, time
import subprocess
from datetime import datetime
from shutil import copyfile
import os, time
from stat import *  # ST_SIZE etc

dbg_init = True
# dbg_init = False

dbg_body = True
# dbg_body = False

dbg_run = True
# dbg_run = False

dbg_done = True
# dbg_done = False
start_time = None
#timeout = 30

pkg = __package__
src_dir = r'C:\work\veip\djproj\veip\run\\'
log_file_name = pkg + '.out'
log_file = None

# work_dir = src_dir + datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f_')
# work_dir = work_dir + ('%d,' * 6 + '%.3f,' * 8 + '%.3f/') % (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15)
work_dir = src_dir


def go(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15):
    log_file = open(src_dir + log_file_name, "w")
    start_time = time.time()
    #os.chdir(os.getcwd() + '/' + pkg)

    fixed_files = ['veip9.exe', 'veip8.exe', 'veip7.exe', 'veip6.exe', 'veip4.exe', 'veip3.exe', 'veip2.exe', 'veip1.exe', 'veip0.exe' ]
    fixed_files = fixed_files + ['SPKH', 'SPKV', 'VSP', 'EKIP', 'SRVN', 'UST.OTL', 'sd', 'TPS', 'AB', 'vertiz', 'moments', 'PRODSILA']

    #a1 = int(sys.argv[1]); a2 = int(sys.argv[2]); a3 = int(sys.argv[3]); a4 = int(sys.argv[4]); a5 = int(sys.argv[5])
    #a6 = int(sys.argv[6]); a7 = float(sys.argv[7]); a8 = float(sys.argv[8]); a9 = float(sys.argv[9]); a10 = float(sys.argv[10])
    #a11 = float(sys.argv[11]); a12 = float(sys.argv[12]); a13 = float(sys.argv[13]); a14 = float(sys.argv[14]); a15 = float(sys.argv[15])

    #if not len(sys.argv) == 16:
    #    raise NameError(f"Длина аргументов: {len(sys.argv)}")


    # try:
    #     os.mkdir(work_dir)
    #     if dbg_init: print("Directory '%s' created " % work_dir, file= log_file)
    # except FileExistsError:
    #     print("Directory '%s' already exists" % work_dir, file= log_file)
    #     exit(1828)

    # for f in fixed_files:
    #     copyfile(src_dir + f, work_dir + f)

    with open(work_dir + 'input', 'w') as f:
        f.write(("%2d" * 6 + '\n') % (a1, a2, a3, a4, a5, a6))
        f.write(("%10.3f" * 6 + '\n') % (a7, a8, a9, a10, a11, a12))
        f.write(("%10.3f" * 3 + '\n') % (a13, a14, a15))

    if dbg_init:
        print('%s.init: current time: %s' % (pkg, datetime.now().strftime('%Y-%m-%d %H:%M:%S')), file= log_file)
        print('%s.init: work_dir: "%s"' % (pkg, work_dir), file= log_file)
        print('%s.init: fixed_files: "%s"\npython path:' % (pkg, fixed_files), file= log_file)
        print('%s.init: current folder: "%s"\npython path:' % (pkg, os.getcwd()), file= log_file)
        for p in sys.path: print(p, file=log_file)

    print("%s.body: veip2" % pkg, file=log_file)
    r = RunVEIP0();
    res = r.result()
    r = RunVEIP1();
    res = r.result() and res
    r = RunVEIP2();
    res = r.result() and res
    r = RunVEIP3();
    res = r.result() and res
    r = RunVEIP4();
    res = r.result() and res
    r = RunVEIP6();
    res = r.result() and res
    r = RunVEIP7();
    res = r.result() and res
    r = RunVEIP8();
    res = r.result() and res
    r = RunVEIP9();
    res = r.result() and res

    if dbg_body:
        print("%s.body: exit" % pkg, file=log_file)
    log_file.close()



def FileInfo (proc_name, file):
    try:
        st = os.stat(file)
    except IOError:
        if dbg_run:
            print ("%s: failed to get information about %s" % (proc_name, file), file=log_file)
        return False
    else:
        if dbg_run:
            print( "%s: file '%17s' - size: %6d, modified: %s" %
               (proc_name, file, st[ST_SIZE], time.asctime(time.localtime(st[ST_MTIME]))), file=log_file)
        return st[ST_SIZE] > 0


class Run (object):
    def __init__(self, subj, where, to):
        self.subj = subj
        self.where = where
        self.start_time = time.time()
        self.tio = to

    def result (self):
        r = None
        try:
            r = subprocess.run([self.subj], cwd=self.where, shell=True, check=False, timeout=self.tio,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        except subprocess.TimeoutExpired:
            print("%s.run: subprocess.TimeoutExpired: '%s' timed out after %d seconds" %
                  (pkg, self.subj, self.tio), file=log_file)
            log_file.close()
            exit(7893)
            #return False

        if dbg_run:
            print("%s.run: args: %s, returncode: %d, %.3f sec" %
                  (pkg, r.args, r.returncode, time.time() - self.start_time), file=log_file)
            if r.stdout: print("%s.run: stdout:\n'%s'" % (pkg, r.stdout.decode('cp1251')), file=log_file)
            if r.stderr: print("%s.run: stderr:\n'%s'" % (pkg, r.stderr.decode('cp1251')), file=log_file)
        if not r.returncode == 0:
            print("%s.run: stderr:\n'%s'" % (pkg, r.stderr.decode('cp1251')), file=log_file)
            log_file.close()
            exit(7888)
        return not r.stderr
class RunVEIP0:
    def __init__(self):
        self.r = Run('veip0.exe', work_dir, 0.2)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP0', work_dir + 'middle')
        r = r and FileInfo('RunVEIP0', work_dir + 'eko.inp')
        r = r and FileInfo('RunVEIP0', work_dir + 'input')
        r = r and FileInfo('RunVEIP0', work_dir + 'tps')
        r = r and FileInfo('RunVEIP0', work_dir + 'vsp')
        r = r and FileInfo('RunVEIP0', work_dir + 'spkh')
        r = r and FileInfo('RunVEIP0', work_dir + 'spkv')
        return r

class RunVEIP1 (Run):
    def __init__(self):
        self.r = Run('veip1.exe', work_dir, 0.15)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP1', work_dir + 'middle')
        r = r and FileInfo('RunVEIP1', work_dir + 'eko.1')
        r = r and FileInfo('RunVEIP1', work_dir + 'fort8')
        r = r and FileInfo('RunVEIP1', work_dir + 'output.st1')
        r = r and FileInfo('RunVEIP1', work_dir + 'put.ekp')
        FileInfo('RunVEIP1', work_dir + 'input')
        FileInfo('RunVEIP1', work_dir + 'ekip')
        FileInfo('RunVEIP1', work_dir + 'middle')
        return r

class RunVEIP2 (Run):
    def __init__(self):
        self.r = Run('veip2.exe', work_dir, 20.0)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP2', work_dir + 'teta')
        r = r and FileInfo('RunVEIP2', work_dir + 'rail')
        r = r and FileInfo('RunVEIP2', work_dir + 'output.st2')
        r = r and FileInfo('RunVEIP2', work_dir + 'teraz')
        FileInfo('RunVEIP2', work_dir + 'middle')
        FileInfo('RunVEIP2', work_dir + 'AB')
        FileInfo('RunVEIP2', work_dir + 'PRODSILA')
        FileInfo('RunVEIP2', work_dir + 'MOMENTS')
        return r

class RunVEIP3 (Run):
    def __init__(self):
        self.r = Run('veip3.exe', work_dir, 0.15)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP3', work_dir + 'ust')
        r = r and FileInfo('RunVEIP3', work_dir + 'rail')
        r = r and FileInfo('RunVEIP3', work_dir + 'output.st3')
#        r = r or FileInfo('RunVEIP3', work_dir + 'ust.otl')
#        r = FileInfo('RunVEIP3', work_dir + 'ust.otl') or r
        FileInfo('RunVEIP3', work_dir + 'ust.otl')
        FileInfo('RunVEIP3', work_dir + 'teta')
        FileInfo('RunVEIP3', work_dir + 'ab')
        return r

class RunVEIP4 (Run):
    def __init__(self):
        self.r = Run('veip4.exe', work_dir, 0.15)

    def result (self):
        r = self.r.result()
        FileInfo('RunVEIP4', work_dir + 'eko.6')
        FileInfo('RunVEIP4', work_dir + 'rail')
        FileInfo('RunVEIP4', work_dir + 'fort33')
        FileInfo('RunVEIP4', work_dir + 'teta')
        FileInfo('RunVEIP4', work_dir + 'ust')
        FileInfo('RunVEIP4', work_dir + 'IUOMEGA')
        FileInfo('RunVEIP4', work_dir + 'output.st4')
        FileInfo('RunVEIP4', work_dir + 'ownmod')
        FileInfo('RunVEIP4', work_dir + 'output.st6')
        FileInfo('RunVEIP4', work_dir + 'AB')
        FileInfo('RunVEIP4', work_dir + 'AMFT')
        FileInfo('RunVEIP4', work_dir + 'SKOSK')
        FileInfo('RunVEIP4', work_dir + 'eko.inp')
        FileInfo('RunVEIP4', work_dir + 'iznos')
        FileInfo('RunVEIP4', work_dir + 'puty')
        FileInfo('RunVEIP4', work_dir + 'putv')
        return r

class RunVEIP6(Run):
    def __init__(self):
        self.r = Run('veip6.exe', work_dir, 0.15)

    def result(self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP6', work_dir + 'output.st6')
        r = r and FileInfo('RunVEIP6', work_dir + 'puty')
        r = r and FileInfo('RunVEIP6', work_dir + 'putv')
        r = r and FileInfo('RunVEIP6', work_dir + 'eko.6')
        r = r and FileInfo('RunVEIP6', work_dir + 'iznos')
        FileInfo('RunVEIP6', work_dir + 'fort13')
        FileInfo('RunVEIP6', work_dir + 'ust')
        FileInfo('RunVEIP6', work_dir + 'rail')
        FileInfo('RunVEIP6', work_dir + 'teta')
        FileInfo('RunVEIP6', work_dir + 'BOKOVAYA')
        FileInfo('RunVEIP6', work_dir + 'eko.inp')
        FileInfo('RunVEIP6', work_dir + 'iznos')
        FileInfo('RunVEIP6', work_dir + 'puty')
        FileInfo('RunVEIP6', work_dir + 'putv')
        FileInfo('RunVEIP6', work_dir + 'ab')
        return r

class RunVEIP7 (Run):
    def __init__(self):
        self.r = Run('veip7.exe', work_dir, 0.15)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP7', work_dir + 'output.st7')
        r = r and FileInfo('RunVEIP7', work_dir + 'eko.7')
        r = r and FileInfo('RunVEIP7', work_dir + 'fort17')
        r = r and FileInfo('RunVEIP7', work_dir + 'otl')
        FileInfo('RunVEIP7', work_dir + 'puty')
        FileInfo('RunVEIP7', work_dir + 'putv')
        FileInfo('RunVEIP7', work_dir + 'middle')
        return r

class RunVEIP8 (Run):
    def __init__(self):
        self.r = Run('veip8.exe', work_dir, 0.15)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP8', work_dir + 'output.st8')
        r = r and FileInfo('RunVEIP8', work_dir + 'eko.8')
        FileInfo('RunVEIP8', work_dir + 'fort13')
        FileInfo('RunVEIP8', work_dir + 'middle')
        FileInfo('RunVEIP8', work_dir + 'ust')
        FileInfo('RunVEIP8', work_dir + 'rail')
        FileInfo('RunVEIP8', work_dir + 'put.ekp')
        FileInfo('RunVEIP8', work_dir + 'eko.inp')
        FileInfo('RunVEIP8', work_dir + 'output.st2')
        FileInfo('RunVEIP8', work_dir + 'iznos')
        FileInfo('RunVEIP8', work_dir + 'sd')
        return r

class RunVEIP9 (Run):
    def __init__(self):
        self.r = Run('veip9.exe', work_dir, 0.15)

    def result (self):
        r = self.r.result()
        r = r and FileInfo('RunVEIP9', work_dir + 'vivod')
        r = r and FileInfo('RunVEIP9', work_dir + 'middle')
        r = r and FileInfo('RunVEIP9', work_dir + 'eko.inp')
        r = r and FileInfo('RunVEIP9', work_dir + 'output.st1')
        r = r and FileInfo('RunVEIP9', work_dir + 'output.st2')
        r = r and FileInfo('RunVEIP9', work_dir + 'output.st3')
        r = r and FileInfo('RunVEIP9', work_dir + 'output.st6')
        r = r and FileInfo('RunVEIP9', work_dir + 'output.st7')
        return r


