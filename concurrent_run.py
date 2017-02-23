from multiprocessing import Pool
from multiprocessing import cpu_count

def concurrent_run(command, args_list):
    result_list = list()
    try:
        pool = Pool(cpu_count())
        result_list = pool.map(command, args_list)
    except Exception as e:
        print(e)
        print("args_list %s" % args_list)
        exit("concurrent_run error")
    finally:
        pool.close()
        pool.join()
    return result_list
