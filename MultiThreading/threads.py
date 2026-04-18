from threading import Thread


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello",i+1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi",i+1)


if __name__=="__main__":
    t1= Hello()
    t2=Hi()
    t1.start()
    t2.start()
