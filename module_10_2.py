from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self,name,power):
        Thread.__init__(self)
        self.name=name
        self.power=power

    def run(self):
        print(f'{self.name}, на нас напали')
        i=0
        vrag=int(100)
        while vrag != 0:
            i+=1
            sleep(1)
            vrag = vrag - self.power
            print(f'{self.name} сражается {i} день(дня)..., осталось {vrag} воинов')
        print(f'{self.name} одержал победу спустя {i} дней (дня)!')
        return

first_knight=Knight('Sir Lancelot',10)
second_knight=Knight('Sir Galahad',20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')