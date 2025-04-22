import sys
import time
import re
import socket
from tqdm import tqdm
from rapidfuzz import process as pro, fuzz
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import groupby


def resolve(i):
    time.sleep(1/100000000)
    try:
        socket.inet_aton(i)
        try:
            return socket.gethostbyaddr(i)[0]
        except socket.herror:
            return f"unknow.({i})"
    except socket.error:
        return i

def matching(a, b):
    time.sleep(1/10000)
    m, s, _ = pro.extractOne(b[0], a, scorer=fuzz.token_sort_ratio)
    if s > 80 and int(b[1]) != 0 and int(b[2]) == 0:
        return [b[0], "found and allow in the Proxy", "Text"]
    elif s > 80 and int(b[1]) == 0 and int(b[2]) != 0:
        return [b[0], "found and block in the Proxy" , "Text"]
    elif int(b[1]) == 0 and int(b[2]) != 0:
        return [resolve(b[0]), "block in the Proxy", "Log"]
    else:
        return None

def process(a, b):
    try:
        a = list(set(a))
        # regex to contains string.
        p = '|'.join([i[0] for i in b])
        bp = [i for i in a if i not in p]
        res = [[i, "on not found in the Proxy", "Text"] for i in bp]

        # Thread or Process pool — use ThreadPoolExecutor for I/O-bound, ProcessPoolExecutor for CPU-bound
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(matching, a, i) for i in b]
            # tqdm + as_completed to show progress
            for ft in tqdm(as_completed(futures), total=len(futures), desc="Processing"):
                res.append(ft.result())
                sys.stdout.flush()

        res = [i for i in res if i is not None]
        return [i for i,_ in groupby(sorted(res))]
    except Exception as e:
        print(e)
        sys.exit(0)
