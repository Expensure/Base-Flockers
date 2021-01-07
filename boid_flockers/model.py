"""
Flockers
=============================================================
A Mesa implementation of Craig Reynolds's Boids flocker model.
"""

import numpy as np

from mesa import Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation

from .boid import Boid


class BoidFlockers(Model):
    """
    Flocker model class. Handles agent creation and placement
    """

    def __init__(
        self,
        population=100,
        width=100,
        height=100,
    ):
        """
        Create a new Flockers model.

        Args:
            population: Number of Boids
            width, height: Size of the space.
                    keep from any other"""
        self.population = population
        self.schedule = RandomActivation(self)
        self.space = ContinuousSpace(width, height, True)
        self.make_agents()
        self.running = True

    def make_agents(self):
        """
        Create self.population agents, with random positions
        """
        for i in range(self.population):
            x = self.random.random() * self.space.x_max
            y = self.random.random() * self.space.y_max
            pos = np.array((x, y))
            boid = Boid(
                i,
                self,
                pos,
            )
            self.space.place_agent(boid, pos)
            self.schedule.add(boid)

    def step(self):
        self.schedule.step()
