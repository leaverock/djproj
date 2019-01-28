from stat import *  # ST_SIZE etc
import os, time
import subprocess

# dbg = True
dbg = False
start_time = None
pkg = __package__
#src_dir = r'C:\work\veip\djproj\veip\run\\'
log_file_name = pkg + '.out'
work_dir = r'./veip/run/'
log_file = None

def init():
    global  log_file
    log_file = open(work_dir + log_file_name, "w")

def FileInfo (proc_name, file):
    try:
        st = os.stat(file)
    except IOError:
        if dbg:
            print("%s: failed to get information about %s" % (proc_name, file), file=log_file)
        return False
    else:
        if dbg:
            print("%s: file '%17s' - size: %6d, modified: %s" %
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

        if dbg:
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
    def __init__(self, work_dir, timeout):
        self.r = Run('veip0.exe', work_dir, timeout)

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

class RunVEIP1:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip1.exe', work_dir, timeout)

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

class RunVEIP2:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip2.exe', work_dir, timeout)

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

class RunVEIP3:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip3.exe', work_dir, timeout)

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

class RunVEIP4:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip4.exe', work_dir, timeout)

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

class RunVEIP6:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip6.exe', work_dir, timeout)

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

class RunVEIP7:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip7.exe', work_dir, timeout)

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

class RunVEIP8:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip8.exe', work_dir, timeout)

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

class RunVEIP9:
    def __init__(self, work_dir, timeout):
        self.r = Run('veip9.exe', work_dir, timeout)

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


