import numpy as np
from abc import ABC, abstractmethod
from person import Person



class Model():
    def __init__(self, fDiagram, pde, params, dt=0.01, verbose=True):
        
        self.room_l, self.room_w, self.a, self.b = params

        self.current_people = []
        self.all_people = []
        self.fd = fDiagram
        self.pde = pde
        self.t = 0.
        self.t_array = [self.t]
        self.dt = dt
        Person.id_counter = 0
        Person.dt = self.dt

        self.verb = verbose #To control if print information while simulate

    def generate_person(self):

        lambda_t = 2*self.room_l * self.a * (self.fd.p_max - self.pde.density([0,0], self.t)) * self.dt
        n = np.random.poisson(lambda_t)

        for _ in range(n):
            person = Person(self.t)
            self.current_people.append(person)
            self.all_people.append(person)
            if self.verb:
                print(f"{person} entered the room. | There are currently {len(self.current_people)} inside.")


    def who_left(self):
        # Check who left the room and remove from current_people

        # Include that initial condition if a person goes backward
        # in the begin, i.e. reflect or absorb.

        for person in self.current_people:

            # This is the reflection conditions at entrance
            # Improve this.
            # Change P_in and P_out for their respective formulas
            P_in = 0.5
            P_out = 0.9
            if person.position[0] < 0:
                if np.random.uniform(0, 1) < P_in:
                    person.position[0] = -1 * person.position[0]
                else:
                    self.current_people.remove(person)
                    if self.verb:
                        print(f"{person} left the room.| There are currently {len(self.current_people)} inside.")
            
            elif person.position[0] > self.room_l:
                if np.random.uniform(0, 1) < P_out:
                    person.position[0] = self.room_l - (person.position[0] - self.room_l)
                else:
                    self.current_people.remove(person)
                    if self.verb:
                        print(f"{person} left the room.| There are currently {len(self.current_people)} inside.")


    def people_step(self, t):
        for person in self.current_people:
            density = self.pde.density(person.position[:2], t) #Return the density given position
            drift = self.fd(density)
            person.step(drift, t)
        pass

    def model_step(self):

        self.generate_person()
        self.people_step(self.t)
        self.who_left()
        
        
        self.t += self.dt
        self.t_array.append(self.t)



        

