import multiprocessing

def f(ns):
    ns.x.append(10)
    ns.y.append(10)

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    ns = manager.Namespace()
    ns.x = [] #manager.list()
    ns.y = []

    print ('before', ns.x, ns.y)
    p = multiprocessing.Process(target=f, args=(ns,))
    p.start()
    p.join()
    print ('after', ns.x, ns.y)