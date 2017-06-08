'''

while True:
	reply = raw_input('Enter text:')
	if reply == 'stop': break
	print(reply.upper())
'''
'''
f=open('install.sh','w')
f.write('#hello\n')
f.writelines(['pwd\n','ls -a -l'])
f.close()
'''

a=raw_input('a:')
b=raw_input('b:')
c=cmp(a,b)
if c < 0:
	print("a is small than b")
elif c==0:
	print("a is equal to b")
elif c>=0:
	print("a is bigger than b")

print("compare over!!!")
