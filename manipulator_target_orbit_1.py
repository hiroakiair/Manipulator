## マニピュレータの位置制御
## 目標軌道を決定するためのシミュレーション
## ロボット制御基礎論 吉川恒夫(p133~138)
guzai_0 = math.sqrt(3)/2
guzai_f = 1
t_f = 2.0
t = np.arange(0, t_f, 0.01)
grad = (guzai_f - guzai_0)/(t_f - 2*delta_t)

guzai_02 = guzai_0 + grad*delta_t
guzai_f1 = guzai_f - grad*delta_t

a_1[0] = guzai_0
a_1[1] = 0
a_1[2] = 0
a_1[3] = (20*guzai_02 - 20*guzai_0 - (8*grad + 12*0)*2*delta_t)/(2*pow(2*delta_t,3))
a_1[4] = (30*guzai_0 - 30*guzai_02 + (14*grad + 16*0)*2*delta_t)/(2*pow(2*delta_t,4))

a_2[0] = guzai_f1
a_2[1] = grad
a_2[2] = 0
a_2[3] = (20*guzai_f - 20*guzai_f1 - (8*0 + 12*grad)*2*delta_t)/(2*pow(t_f,3))
a_2[4] = (30*guzai_f1 - 30*guzai_f + (14*0 + 16*grad)*2*delta_t)/(2*pow(t_f,4))

x_1 = a_1[0] + a_1[1]*t_1 + a_1[2]*pow(t_1, 2) + a_1[3]*pow(t_1, 3) + a_1[4]*pow(t_1, 4) 
x_2 = grad*(t_2 - 2*delta_t) + guzai_02
x_3 = a_2[0] + a_2[1]*t_3 + a_2[2]*pow(t_3, 2) + a_2[3]*pow(t_3, 3) + a_2[4]*pow(t_3, 4) 

x = np.r_[x_1, x_2]
t = np.r_[t_1, t_2]
pyplot.plot(t, x)
pyplot.show()
