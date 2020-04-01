import math
from random import random
import numpy as np
import matplotlib.pyplot as plt


buf_size = 4

lyambda = np.arange(0.1, 1, 0.1)
mes_count = 10000


def get_tao(lyambda):
    return (-1 / lyambda) * math.log(random())


def gen_mes(lyambda):
    count = 0
    tao = 0
    sumTao = 0

    while sumTao < 1:
        tao = get_tao(lyambda)
        sumTao += tao
        if sumTao < 1:
            count += 1

    return count


def append_to_buf(buf, num_mes):
    while num_mes > 0 and len(buf) < buf_size:
        buf = np.append(buf, 0)
        num_mes -= 1
    return buf


def gen_matrix(L):
    states_num = buf_size + 1
    P = [[0] * states_num] * states_num
    P = np.asarray(P, dtype=float)
    for i in range(0, states_num - 1):
        P[0, i] = P[1, i] = get_prob(i, L)
    P[0, states_num - 1] = 1 - sum(P[0])
    P[1, states_num - 2] = 0

    for i in range(2, states_num - 1):
        deg = 0
        for j in range(i - 1, states_num - 2):
            P[i, j] = get_prob(deg, L)
            deg += 1

    for i in range(1, states_num - 1):
        P[i, states_num - 2] = 1 - sum(P[i])

    P[states_num - 1, states_num - 2] = 1

    for i in range(0, states_num):
        P[i, i] -= 1

    P = np.transpose(P)
    P[states_num - 1] = np.array([1] * states_num)
    #P[0] = np.array([1] * states_num)

    return P



def get_prob(i, L):
    return math.pow(L, i) * np.exp(-L) / math.factorial(i)


d = np.array([0] * len(lyambda))
average_N = [0] * len(lyambda)
d_theor = np.array([0] * len(lyambda), dtype=float)
average_N_theor = [0] * len(lyambda)


for i in range(0, len(lyambda)):
    sended = 0
    time = 0
    N = 0
    buf = np.array([])
    total_mes = 0
    empty = True

    while sended < mes_count:
        mes_per_window = gen_mes(lyambda[i])
        total_mes += mes_per_window
        buf = append_to_buf(buf, mes_per_window)


        if len(buf) > 0 and not empty:
            sended += 1
            d[i] += buf[0]
            buf = buf[1:]

        time += 1
        N += len(buf)
        buf = buf + 1
        if len(buf) > 0:
            empty = False
        else:
            empty = True

    average_N[i] = N / time

    P = gen_matrix(lyambda[i])
    vector = np.array([0] * (buf_size + 1))
    vector[buf_size] = 1
    #vector[0] = 1
    Pi = np.linalg.solve(P, vector)
    for j in range(0, len(Pi)):
        average_N_theor[i] += j * Pi[j]

    l_out = 1 - Pi[0] #sended / total_mes
    d_theor[i] = average_N_theor[i] / l_out


d = d / mes_count

print("d    : " + str(d.tolist()))
print("d (t): " + str(d_theor.tolist()))
print("N    : " + str(average_N))
print("N (t): " + str(average_N_theor))

figure = plt.figure()
plt.subplot(211)
plt.plot(lyambda, d, label="d")
plt.plot(lyambda, d_theor, label="d (t)")
plt.legend()
plt.subplot(212)
plt.plot(lyambda, average_N, label="N")
plt.plot(lyambda, average_N_theor, label="N (t)")
plt.legend()
plt.show()


plt.show()
