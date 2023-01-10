import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

class Bayes():

    def __init__(self):
        print('program start')

    def make_x_range(self):
        data = []
        for i in range(101):
            try:
                value = i / 100
                data.append(value)
            except:
                print('error')
                pass

        return data

    def make_data_p_t(self):
        data = []
        for i in range(101):
            try:
                value = 1 / 101
                data.append(value)
            except:
                print('error')
                pass

        return data


    def make_p_a_t(self, hantei):
        data = []
        for i in range(0,101,1):
            try:
                value = i / 100
                if hantei == 0:
                    value = 1 - value
                data.append(value)
            except:
                print('error')
                pass

        return data

    def make_p_t_a(self, p_t, p_a_t, mu):
        data = []
        sum = 0
        for i in range(101):
            try:
                value =  mu * p_t[i] * p_a_t[i]
                sum = sum + value
                data.append(value)
            except:
                print('error')
                pass

        #print("積分値 : ", sum)
        return data

    def answer_probability(self, data, value):
        print("\n",value, "回目の施行")
        print("max probability : ", max(data))
        print("finish rate : ", data.index(max(data)) / 100)


    def make_figure(self, x, first, second, third, forth, fifth):

        #全部の結果をグラフに出力

        #施行１回目のグラフ
        plt.figure()
        plt.plot(x,first)
        plt.suptitle("new algorithm probability for 1st execution")
        plt.xlabel("t")
        plt.ylabel("probability")
        plt.xticks([0.00, 0.5, 1])
        plt.yticks([0.00, 0.02, 0.04, 0.06, 0.08])
        plt.savefig("../figure/新アルゴリズム_施行1回目の確率分布.png")

        #施行２回目のグラフ
        plt.figure()
        plt.plot(x,second)
        plt.xlabel("t")
        plt.ylabel("probability")
        plt.xticks([0.00, 0.5, 1])
        plt.yticks([0.00, 0.02, 0.04, 0.06, 0.08])
        plt.savefig("../figure/新アルゴリズム_施行1回目の確率分布.png")
        plt.suptitle("new algorithm probability for 2st execution")
        plt.xlabel("t")
        plt.ylabel("probability")
        plt.xticks([0.00, 0.5, 1])
        plt.yticks([0.00, 0.02, 0.04, 0.06, 0.08])
        plt.savefig("../figure/新アルゴリズム_施行2回目の確率分布.png")

        #施行３回目のグラフ
        plt.figure()
        plt.plot(x,third)
        plt.suptitle("new algorithm probability for 3st execution")
        plt.xlabel("t")
        plt.ylabel("probability")
        plt.xticks([0.00, 0.5, 1])
        plt.yticks([0.00, 0.02, 0.04, 0.06, 0.08])
        plt.savefig("../figure/新アルゴリズム_施行3回目の確率分布.png")

        #施行４回目のグラフ
        plt.figure()
        plt.plot(x,forth)
        plt.suptitle("new algorithm probability for 4st execution")
        plt.xlabel("t")
        plt.ylabel("probability")
        plt.xticks([0.00, 0.5, 1])
        plt.yticks([0.00, 0.02, 0.04, 0.06, 0.08])
        plt.savefig("../figure/新アルゴリズム_施行4回目の確率分布.png")

        #施行５回目のグラフ
        plt.figure()
        plt.plot(x,fifth)
        plt.suptitle("new algorithm probability for 5st execution")
        plt.xlabel("t")
        plt.ylabel("probability")
        plt.xticks([0.00, 0.5, 1])
        plt.yticks([0.00, 0.02, 0.04, 0.06, 0.08])
        plt.savefig("../figure/新アルゴリズム_施行5回目の確率分布.png")

        #plt.show()


if __name__ == "__main__":
    kakuritu = Bayes()
    x = kakuritu.make_x_range()

    # 施行１回目の確率計算
    p_t = kakuritu.make_data_p_t()
    p_a_t1 = kakuritu.make_p_a_t(1)
    p_t_a1 = kakuritu.make_p_t_a(p_t, p_a_t1, 2)
    kakuritu.answer_probability(p_t_a1, 1)


    # 施行２回目の確率計算
    p_a_t2 = kakuritu.make_p_a_t(1)
    p_t_a2 = kakuritu.make_p_t_a(p_a_t2, p_t_a1, 1.49254)
    kakuritu.answer_probability(p_t_a2, 2)


    # 施行３回目の確率計算
    p_a_t3 = kakuritu.make_p_a_t(1)
    p_t_a3 = kakuritu.make_p_t_a(p_a_t3, p_t_a2, 1.32675)
    kakuritu.answer_probability(p_t_a3, 3)


    # 施行４回目の確率計算
    p_a_t4 = kakuritu.make_p_a_t(1)
    p_t_a4 = kakuritu.make_p_t_a(p_a_t4, p_t_a3, 1.243825)
    kakuritu.answer_probability(p_t_a4, 4)


    # 施行５回目の確率計算
    p_a_t5 = kakuritu.make_p_a_t(1)
    p_t_a5 = kakuritu.make_p_t_a(p_a_t5, p_t_a4, 1.19408)
    kakuritu.answer_probability(p_t_a5, 5)

    kakuritu.make_figure(x,p_t_a1, p_t_a2, p_t_a3, p_t_a4, p_t_a5)
