from concurrent.future import ThreadPoolExecutor
import time

from SocketServer import ThreadingTCPServer,StreamRequestHandler

class MyStreamRequestHandler(StreamRequestHandler):

    def handle(self):

        whiel True:
            try :
                data=self.rfile.readline().strip()
                print ("receive from (%r): %r"% (self.client_address,data))
                self.wfile.write(data.upper())
            except:
                traceback.print_exc()
                break
# 进程有自己的地址空间，线程没有，它只是进程执行的一种路径一旦死掉，等于整个进程
# 死掉，所以不如线程健壮。
# 两种方式创建线程，一种通过继承Thread类，重写run方法，另一种是创建一个
# threading。Thread对象，在它的初始函数中将可调用对象作为参数传入
# threading模块中的join函数主要作用是阻塞进程直到线程执行完毕，通用的做法是启动
# 一批线程，最后join这些线程结束。原理就是一次检验线程池中的线程是否结束，没有结束就
# 阻塞直到线程结束，如果结束就跳转执行下一个线程。
if __name__=="__main__":
    host =""
    port = 9999
    addr = (host,port)
    server = ThreadingTCPServer(addr, MyStreamRequestHandler)
    server.serve_forever()
