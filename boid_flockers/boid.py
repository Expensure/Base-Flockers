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
    ):
        """
        Create a new Boid flocker agent.

        Args:
            unique_id: Unique agent identifyer.
            pos: Starting position


        """
        super().__init__(unique_id, model)
        self.pos = np.array(pos)

    def step(self):
        """
        Get the Boid's neighbors
        """

        self.velocity = 1
        new_pos = self.pos
        self.model.space.move_agent(self, new_pos)
