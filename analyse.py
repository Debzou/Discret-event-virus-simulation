####################################
# pip3 install matplotlib          #
# pip3 install numpy               #
####################################

#library used
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

FILE_NAME = "log.txt"

def predict(xOUT):
    """
    create a linear function
    """
    # print("{}X + {}".format(slope,intercept))
    return slope * xOUT + intercept
    

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
            
    ### deeper analysis

    # remove outlier (value < q1 and value > q3)
    q1 = np.quantile(listCumlative,0.25)
    q3 = np.quantile(listCumlative,0.75)
    listCumlativeOUT = list(filter(lambda x: x > q1 and x < q3,listCumlative))
    
    # find index connected with list X
    index1 = list(listCumlative).index(listCumlativeOUT[0])
    index2 = list(listCumlative).index(listCumlativeOUT[-1])+1
    xOUT = list(range(index1,index2))
    
    # slope analysis
    # linear regression
    # first find coef    
    slope, intercept, r_value, p_value, std_err = stats.linregress(xOUT,listCumlativeOUT)
    fitLine = predict(range(index1,index2))
    
    # display    
    plt.suptitle('Linear regression between quantile 1 et quantile 3') 
    plt.xlabel("days (d)")
    plt.ylabel("number of infected")
    plt.plot(xOUT,fitLine,label="{}X + {}".format(slope,intercept))
    plt.plot(xOUT,listCumlativeOUT,label='infected cumulative')
    plt.legend()
    plt.show()
    