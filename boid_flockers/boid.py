import numpy as np

from mesa import Agent


class Boid(Agent):
    """
    A Boid-style flocker agent.
    """

    def __init__(
            self,
            unique_id,
            model,
            pos,
            speed,
            velocity,
            vision,
            separation,
    ):
        """
        Create a new Boid flocker agent.

        Args:
            unique_id: Unique agent identifyer.
            pos: Starting position
            speed: Distance to move per step.
            heading: numpy vector for the Boid's direction of movement.
            vision: Radius to look around for nearby Boids.
            separation: Minimum distance to maintain from other Boids.

        """
        super().__init__(unique_id, model)
        self.pos = np.array(pos)
        self.speed = speed
        self.velocity = velocity
        self.vision = vision
        self.separation = separation

    def step(self):
        """
        Get the Boid's neighbors, compute the new vector, and move accordingly.
        """

        self.velocity = 1
        new_pos = self.pos + (1, 0)
        self.model.space.move_agent(self, new_pos)
