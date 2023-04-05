print ('a'.isidentifier())
print ('a b'.isidentifier())
print ('__'.isidentifier())
print ('3c'.isidentifier())

print('while' .isidentifier())
print('for' .isidentifier())


"""import keyword as k"""
print(k.kwlist)
print(len(keyword.kwlist))

print(k.iskeyword('while'))
print(k.iskeyword('for'))
print(k.iskeyword('if'))
print(k.iskeyword('print'))
print(k.iskeyword('true'))

a=10
b=5
a,b=b,a
print(a)
print(b)
