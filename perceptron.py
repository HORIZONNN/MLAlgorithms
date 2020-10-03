import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    datas = np.array([[1,2],[3,1],[4,5],[3,4]])
    labels = np.array([-1, -1, 1, 1])
    w = np.random.random(2)
    b = np.random.random()
    gamma = 0.1

    
    fig = plt.figure()

    while(True):
        done = True
        for i in range(len(labels)):
            value = np.sum(w*datas[i]) + b
            value *= labels[i]
            if value < 0:
                w += gamma*labels[i]*datas[i]
                b += gamma*labels[i]
                done = False


        x = np.linspace(0, 5, num=10)
        y = (-b - w[0]*x) / w[1]
        plt.cla()
        plt.plot(x, y)
        data_x, data_y = zip(*datas)
        plt.scatter(data_x, data_y)
        plt.pause(1)

        if done:
            break



        

        


