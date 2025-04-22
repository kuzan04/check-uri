import sys
import time
import re
import socket
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import groupby, product


def resolve(i):
    # time.sleep(1/100000000.0) # Nano-sec
    try:
        socket.inet_aton(i)
        try:
            return [socket.gethostbyaddr(i)[0], "block in the Proxy.", "LOG"]
        except socket.herror:
            return [f"unknow.({i})", "block in the Proxy.", "LOG"]
    except socket.error:
        return [i, "block in the Proxy.", "LOG"]

def matching(a, b):
    # Convert raw data.
    m = [i for i,j in product(a, b) if i in j[0] or j[0] in i]
    bp = [i for i,j in product(a, b) if i not in j[0] or j[0] not in i]
    nm = [j for i,j in product(a, b) if i not in j[0] or j[0] not in i]
    # Format Data.
    nm = [i for i,_ in groupby(sorted(nm))]
    nm = [i[0] for i in nm if int(i[1]) == 0 and int(i[2]) != 0]
    mres = sorted([[i, "found in the Proxy.", "TEXT"] for i in m])
    mres = [i for i,_ in groupby(mres)]
    bpres = sorted([[i, "on Bypass in the Proxy.", "TEXT"] for i in bp if i not in m])
    bpres = [i for i,_ in groupby(bpres)]

    return [mres, bpres, nm]

def process(a, b):
    try:
        # Thread or Process pool — use ThreadPoolExecutor for I/O-bound, ProcessPoolExecutor for CPU-bound
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures1 = [executor.submit(matching, a, b)]
            rs = []
            # tqdm + as_completed to show progress
            for ft in tqdm(as_completed(futures1), total=len(futures1), desc="Processing"):
                rs.append(ft.result())
            # Split value.
            nm = rs[0].pop()
            bp = rs[0].pop()
            m = rs[0].pop()
            # Concatenate list.
            res = m + bp
            print()
            futures = [executor.submit(resolve, i) for i in nm]
            # tqdm + as_completed to show progress
            for ft in tqdm(as_completed(futures), total=len(futures), desc="Processing"):
                res.append(ft.result())

        res = [i for i in res if i is not None]
        return [i for i,_ in groupby(sorted(res))]
    except Exception:
        sys.exit(0)
