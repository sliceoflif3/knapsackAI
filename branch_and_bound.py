from queue import Queue
from datetime import datetime
startTime = datetime.now()


class Node:
    def __init__(self) -> None:
        self.lv = int(0)
        self.val = float(0)
        self.bnd = float(0)
        self.wei = float(0)


class Item:
    def __init__(self, i: int, v: float, w: float, c: int) -> None:
        self.idx = i
        self.val = v
        self.wei = w
        self.cls = c


limit = float()
m = int()
items = []
classes = set()


q = Queue()
res_items = []


def cal_bnd(node: Node):
    if node.wei >= limit:
        return 0

    bnd = int(node.val)
    total_wei = int(node.wei)

    i = node.lv + 1
    while i < len(items) and total_wei + items[i].wei <= limit:
        total_wei += items[i].wei
        bnd += items[i].val
        i += 1

    if i < len(items):
        bnd += (limit - total_wei) * items[i].val / items[i].wei

    return bnd


def solve():
    u = Node()
    u.lv = -1
    q.put(u)

    max_val = float(0)

    while not q.empty():
        u = q.get()

        v = Node()
        if u.lv == -1:
            v.lv = 0

        if u.lv == len(items) - 1:
            continue

        v.lv = u.lv + 1
        v.wei = u.wei + items[v.lv].wei
        v.val = u.val + items[v.lv].val

        if v.wei <= limit and v.val > max_val:
            max_val = v.val
            res_items.append(items[v.lv])

        v.bnd = cal_bnd(v)
        if v.bnd > max_val:
            q.put(v)

        v = Node()
        v.lv = u.lv + 1
        v.wei = u.wei
        v.val = u.val
        v.bnd = cal_bnd(v)

        if v.bnd > max_val:
            q.put(v)

    return max_val


def check():
    res_cls_ls = set([i.cls for i in res_items])
    if len(res_cls_ls) != m:
        cls = list(classes - set(res_cls_ls))[0]
        for i in items:
            if i.cls == cls:
                return i

    return -1


def swap_to_begin(i: int):
    items[0], items[i] = items[i], items[0]
    return items


if __name__ == "__main__":
    for i in range(2,4):
        inp = f"smallInput/INPUT_{i}.txt"
        out = f"smallOutput2/OUTPUT_{i}.txt"

        with open(inp) as fi:
            limit = int(fi.readline())
            m = int(fi.readline())

            wei_ls = fi.readline().split(", ")
            val_ls = fi.readline().split(", ")
            cls_ls = fi.readline().split(", ")

            for i in range(len(wei_ls)):
                cls = int(cls_ls[i])
                items.append(Item(i, float(val_ls[i]), float(wei_ls[i]), cls))
                classes.add(cls)

        items = sorted(items, key=lambda i: i.val / i.wei, reverse=True)

        res_wei = solve()
        chk = check()
        while chk >= 0:
            items = swap_to_begin(chk)
            res_wei = solve()
            chk = check()

        res = [0] * len(items)
        for i in res_items:
            res[i.idx] = 1

        with open(out, "w") as fo:
            fo.write(str(int(res_wei)) + "\n")
            fo.write(", ".join(map(str, res)))

print(datetime.now() - startTime)