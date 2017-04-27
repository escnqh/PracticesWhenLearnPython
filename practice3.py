stature=float(input('please enter your stature:'))
wight=int(input('please enter your wight:'))
r=wight/(stature*stature)
if r<18.5:
    print('过轻！')
elif r>=18.5 and r<25:
    print('正常！')
elif r>=25 and r<28:
    print('过重！')
elif r>=28 and r<32:
    print('肥胖！')
elif r>=32:
    print('严重肥胖！')