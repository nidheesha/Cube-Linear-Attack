import logging
logging.basicConfig(level=logging.INFO)
import cube_attack
from trivium import Trivium
from blackboxpoly import BlackBoxPoly
from blackboxpoly import sum_mod2


class TriviumCubeAttack(cube_attack.CubeAttack):
    def __init__(self, n_rounds, action="verify"):
        super(cube_attack.CubeAttack,self).__init__()
        self.degree = 80
        print("#going into trivim func from TriviumCubeAttack")
        self.bbpoly = Trivium(n_rounds)
        print("#back from trivim func from TriviumCubeAttack")
        self.action = action
        print(self.degree," ", str(self.bbpoly)," ")
        return

