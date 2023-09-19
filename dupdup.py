import gdb
inf = gdb.selected_inferior()

print("st addr: ",end='')
st_addr = input()
if st_addr.startswith("0x"):
    st_addr = int(st_addr,16)
else:
    st_addr = int(st_addr)
print("end addr: ",end='')
end_addr = input()
if end_addr.startswith("0x"):
    end_addr = int(end_addr,16)
else:
    end_addr = int(end_addr)
assert (end_addr - st_addr > 0)
sz = end_addr - st_addr

print("except? [y/n]: ",end='')
if 'y' in input():
    print("qword, dword, word, byte: ",end='')
    unit = 8
    a = input()
    if 'qword' in a:
        unit = 8
    elif 'dword' in a:
        unit = 4 
    elif 'word' in a:
        unit = 2
    elif 'byte' in a:
        unit = 1
    print("arr: ",end='')
    arr = eval(input())
    assert sz % unit == 0
    assert type(arr) == type([])
    pay = b''
    addr = st_addr
    while (addr < end_addr):
        if addr in arr:
            tmp = inf.read_memory(addr,unit)
        else:
            tmp = b'\x41'*unit
        pay += tmp
        addr += unit
    assert len(pay) == sz
    inf.write_memory(st_addr,pay, sz)
else:
    inf.write_memory(st_addr, b'\x41'*sz, sz)
print("Success")
        
    
