import random
from collections import Counter


class SlotRand(object):
    def rand(self, seq, multiple=100):
        key_list = seq if isinstance(seq, list) else [i for i, j in seq]
        if sum(key_list) != 1:
            raise ValueError("The sum of percentage did't equal `1`")
        if isinstance(seq, list):
            list_of_candidates_list = [
                [i] * int(seq[i] * multiple) for i in range(len(seq))]
        elif isinstance(seq, tuple):
            list_of_candidates_list = [[j] * int(i * multiple) for i, j in seq]
        else:
            raise ValueError("Please input list or dict as the seq param!")

        list_of_candidates = sum(list_of_candidates_list, [])
        ret = random.choice(list_of_candidates)
        return ret



if __name__ == '__main__':
    lst1 = []
    lst2 = []
    r1 = [0.3, 0.1, 0.6]
    r2 = ((0.3, "A"), (0.4, "B"), (0.3, "C"))
    sr = SlotRand()
    for i in range(1000):
        d1 = sr.rand(r1)
        lst1.append(d1)
        d2 = sr.rand(r2)
        lst2.append(d2)

    print("r1:", r1)
    print(Counter(lst1))
    print("r2:", r2)
    print(Counter(lst2))
