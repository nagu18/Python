alean_0={'x_postion':0,'y_postion':25,'speed':'fast'}
if alean_0['speed'] == 'slow':
    alean_0['x_increment']=1
elif alean_0['speed'] == 'mediam':
    alean_0['x_increment']=2
elif alean_0['speed'] == 'fast':
    alean_0['x_increment']=3

alean_0['x_postion']=alean_0['x_postion']+alean_0['x_increment']
print(alean_0['x_postion'])