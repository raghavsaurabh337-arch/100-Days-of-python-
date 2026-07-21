s1={2,4,5,7,23,45}
s2={8,4,9,10,2,7}
print("union",s1.union(s2))
print("intersection",s1.intersection(s2))
print("symmetric",s1.symmetric_difference(s2))
print("isdisjoint",s1.isdisjoint(s2))
print("issuperset",s1.issuperset(s2))

s1.update(s2)
print(s1,s2)
