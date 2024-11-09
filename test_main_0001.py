def test_func():
    pass

def kmph_to_mps(kmph):
    return kmph * 1000 / (60 * 60)

def mps_to_kmph(mps):
    return mps / 1000 * (60 * 60)

print('hello warld!!')

v = 50
v2 = kmph_to_mps(v)
print(f'v2:{v2}') 
v1 = mps_to_kmph(v2)
print(f'v1:{v1}') 


