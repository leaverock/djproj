from . import dbg_done, pkg, log_file_name, work_dir, fixed_files, os, log_file, copyfile, src_dir, time, start_time
from .body import res

if dbg_done:
    print("%s.done: enter" % pkg, file=log_file )

print("%s.done: result of veip: %r, %.3f sec" % (pkg, res, time.time() - start_time), file=log_file)

# for f in fixed_files:
#     os.remove(work_dir + f)

if dbg_done:
    print("%s.done: exit" % pkg, file=log_file )
log_file.close()
#copyfile(src_dir + log_file_name, work_dir + log_file_name)

