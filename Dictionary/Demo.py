data={0:10,1:20,2:30,3:40,4:50,5:60,6:70,7:80,8:90,9:100}
print(type(data))
print(data)
print(data[7])

data2={'uday':32,'sai':45,'kumar':67,'reddy':89}
print(data2['uday'])

keys={'uday','sai','kumar','reddy'}
values={32,45,67,89}
data3=dict(zip(keys,values))


print(data3.pop('uday'))
print(data3)
print(data3.popitem())
# list inside dictionary
data3={'js':'vscode','python':['vscode','pycharm'],'java':['eclipse','vscode', 'intelijIdea'],'c++':'codeblocks'}
print(data3['python'])
print(data3['java'][2])
