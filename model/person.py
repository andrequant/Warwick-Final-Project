import numpy as np



class Person():
    ### As people are homogenous wrt to the parameters, they are set
    ### as class attributes, so they all have the same. That is just
    ### the \Sigma matrix, tough
    Sigma = np.diag([0,0])
    dt = 0.01
    id_counter = 0

    def __init__(self, t):

        # Unique id for each person
        self.id = Person.id_counter
        Person.id_counter += 1


        self.position = np.array([0., 0., t]) # [entrance/exit, walls, time in the whole system]
        self.trajectory = [self.position.copy()]
        self.dw = np.random.standard_normal([10000,2])*np.sqrt(Person.dt)
        self.i = 0 # time for this single person (0 is when it is created)
    
    def __repr__(self):
        return f"Person({self.id})"


    def step(self, drift, t):
        # Check all dimensions
        dx = np.dot(drift, [1,0]) * Person.dt + np.dot(np.sqrt(2 * Person.Sigma), self.dw[self.i])
        self.position[0] += dx[0]
        self.position[1] += dx[1]
        self.position[2] = t
        self.trajectory.append(self.position.copy())
        self.i += 1

    def position_at_t(self,t):
        indice = np.where(np.array(self.trajectory)[:, 2] == t)[0]

        if len(indice) > 0:
            return np.array(self.trajectory)[indice][:2]
        else:
            return None


