# library used
import random
import simpy

# listperson in your simulation
global listperson
listperson = list() 


def number_infected():
    """
    calculate the number of infected in listperson
    """
    nb = 0
    for item in listperson:
        if item.status == "sick":
            nb+=1
    return nb

class Person(object):
    """
    status : "NOTsick" / "sick" 
    """
    def __init__(self,id,status="NOTsick"):
        """
        contructor
        """
        self.id = id
        self.status = status

    def infected(self,id,p):
        """
        you infect an other person or not
        with a probabily p
        """

        if self.status == "sick" and listperson[id].status != "sick" :
            if random.random() <= p :
                listperson[id].status="sick"
                print("the person {} is infected by person {} ".format( self.id, listperson[id].id ))
            else:
                print("you have a chance you are not infected")
        elif listperson[id].status == "sick" and self.status != "sick":
            if random.random() <= p :
                self.status = "sick"
                print("the person {} is infected by person {} ".format(listperson[id].id, self.id))
            else:
                print("you have a chance you are not infected")
        else:
            print("nothing")
            pass

class World(object):
    """
    this is your world (simulation)
    """
    def __init__(self, env, area_zone, meetime):
        self.env = env
        self.meet = simpy.Resource(env, area_zone)
        self.meetime = meetime
        

    def area(self, id,num_person,timemeet,p):
        """
        propagation's area
        in this area , one person can meet an other person
        """
        rand = random.randint(0,num_person)
        print("Person {} : Enter in the meeting zone {}".format(rand,self.env.now))
        listperson[id].infected(rand,p)
        yield self.env.timeout(timemeet)
        print("Person {} : Enter in the meeting zone {}".format(rand,self.env.now))


def meet(env, name, cw,id,num_person,timemeet,p):
    """
    create meet between person (in the area)
    """
    print("{} : wait in order to leave house at {}".format(name,env.now))
    with cw.meet.request() as request:
        yield request
        # meeting zone
        print("{} : Enter in the meeting zone {}".format(name,env.now))
        yield env.process(cw.area(id,num_person,timemeet,p))
        # exit the meeting
        print('%s exit the meeting zone %.2f.' % (name, env.now))


def setup(env, area_zone, meetime,num_person,num_tips,p):
    """
    init the simulation
    """
    # Create the World
    world = World(env, area_zone, meetime)

    # Create n person person in your world
    # patient zero ( infected )

    listperson.append(Person(0,"sick"))
    for i in range(1,num_person):
        listperson.append(Person(i))
    
    
    # for j in range(area_zone):
    #     rand = random.randint(0,num_person)
    #     env.process(meet(env, 'Person {} '.format(rand), world,rand))   
    # yield env.timeout(1)

    # start the meet between person
    for i in range(num_tips):
        rand = random.randint(0,num_person)
        env.process(meet(env, 'Person %d' % rand, world,rand,num_person,meetime,p))
    yield env.timeout(random.randint(500 - 2, 500 + 2))
    