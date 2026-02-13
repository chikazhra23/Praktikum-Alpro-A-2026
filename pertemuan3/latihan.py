class Minuman:
  def __init__(self, warna,merk,rasa):
    self.warna = warna
    self.merk = merk
    self.rasa = rasa

    
    def tambah(self):
        print("Sprite")

    def kurang(self):
        print("Cola")

p1 = Minuman("putih","milk","manis")
p2 = Minuman("coklat","luwak","pahit")
p3 = Minuman("merah","cola","asam")


p1.rasa =("hambar")
print(p1.rasa)

print(p1.warna)
print(p1.merk)
print(p1.rasa)



