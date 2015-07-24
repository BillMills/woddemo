from wodpy import wod

file = open("example.dat")
profile = wod.WodProfile(file)

print profile.latitude()
