####################################
# Version : python 3.6.9 64bits    #
####################################

####################################
# pip3 install sympy               #
####################################

####################################
# run this commande in the shell   #
# python3 simulation.py > log.txt  #
####################################

# import this library 

import random
import simpy
import yaml
# simulation function
import utils



# main of the simulation
if __name__ == "__main__":

    #load the config file
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
    
    # define simulation's values
    RANDOM_SEED = cfg['config']['RANDOM_SEED']
    NUM_AREA = cfg['config']['NUM_AREA']
    TIMEMEET = cfg['config']['TIMEMEET']
    NUM_PERSON = cfg['config']['NUM_PERSON']
    NUM_CYCLE_OUTPUT = cfg['config']['NUM_CYCLE_OUTPUT']
    NUM_TIPS = cfg['config']['NUM_TIPS']
    SIM_TIME = cfg['config']['SIM_TIME']
    
    # This helps reproducing the results 
    random.seed(RANDOM_SEED)  

    # cycle 
    for c in range(NUM_CYCLE_OUTPUT):

        # Create an environment and start the setup process
        env = simpy.Environment()

        # Setup and start the simulation 
        env.process(utils.setup(env, NUM_AREA, TIMEMEET,NUM_PERSON,NUM_TIPS))

        # Execute!
        env.run(until=SIM_TIME)
        print("====================== end cycle {} ======================".format(c))


    