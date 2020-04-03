####################################
# pip3 install matplotlib          #
# pip3 install numpy               #
####################################

#library used
import matplotlib.pyplot as plt
import numpy as np

FILE_NAME = "log.txt"


# main
if __name__ == "__main__":
    count=0
    listscore = list()
    # read the log file in order to analyse the resultat product by the simulator
    with open(FILE_NAME, "r") as f:
        for line in f.readlines():
            # line by line
            if ("is infected by person" in line):
                # a person is infected now
                count+=1
            elif("cycle" in line):
                # change cycle
                listscore.append(count)
                count=0
            else:
                pass
    
    # cumulative sum 
    listCumlative = np.cumsum(listscore, dtype=int)
    # print this list in the console
    print(listCumlative)
    # X abscissa 
    x=range(0,len(listscore))

    

    # plot infected/days
    plt.plot(x, listscore,'-b', label='infected')
    # plot infected cumulative/days
    plt.plot(x,listCumlative,'-r', label='infected cumulative')
    # set a title
    plt.suptitle('Virus propagation')
    # display plot
    plt.xlabel("days (d)")
    plt.ylabel("number of infected")
    plt.legend()
    plt.show()
            