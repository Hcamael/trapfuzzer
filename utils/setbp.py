import os
import shutil
import getopt
import sys
from struct import pack, unpack

target = sys.argv[1]
bb_file = sys.argv[2]
print("Modifying %s based of BB-s in %s" % (target, bb_file))
shutil.copyfile(target, target + "_original")
f = open(bb_file, "rb")
fa = open(target, "r+b")

rva_size = unpack("<I", f.read(4))[0]
fname_sz = unpack("<I", f.read(4))[0]
fname = f.read(fname_sz)

print(f"fname: {fname}")

while True:
    data = f.read(12)
    if len(data) < 12:
        break

    voff, foff, instr_sz = unpack("<III", data)
    instr = f.read(instr_sz)
    fa.seek(foff)
    fa.write(b"\xcc" * instr_sz)

f.close()
fa.close()
print("DONE")