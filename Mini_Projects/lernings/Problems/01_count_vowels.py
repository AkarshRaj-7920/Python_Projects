# Vowels COunting program

us_type = str(input("Word: ").lower())
# tier = "Akrsheshouiushimen"

gin2_ = us_type.count("e")
gin1_ = us_type.count("a")
gin3_ = us_type.count("i")
gin4_ = us_type.count("o")
gin5_ = us_type.count("u")

gin_ = [gin1_, gin2_, gin3_, gin4_, gin5_]
a = sum(gin_)

print (a)