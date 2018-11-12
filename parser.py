import argparse

class Parser():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--mode", default="random", choices=["random", "trivium"],
                            help="What polynomial to perform the attack on ?\
                                  a random polynomial or trivium ?")

        parser.add_argument("--action", default="verify", choices=["verify", "attack"],
                            help="verify trivium maxterms or perform cube attack on trivium ?")

        parser.add_argument("--n_rounds", default=672, type=int,
                            help="number of initialisation rounds for trivium ?")

        parser.add_argument("--degree", default=5, type=int,
                            help="If mode is random, specify the degree of \
                                  the polynomial. Ignored in the case of trivium")

        parser.add_argument("--private_key", default="-1", help="private key of the scheme if random")

        parser.add_argument("--equation", default="v1x1 v2x2x2x2x4 v3v3x3x4 v4x1x5",#"v1x1 v2x2 x1x2 v1x1x3 v3x1", 
                            help= "enter the equation terms with spaces")

        parser.add_argument("--nx", default=1, 
                            help= "enter the omega x length for algo2")

        parser.add_argument("--nv", default=1, 
                            help= "enter the omega v length for algo2")

        self.parser = parser

        self.args = self.parser.parse_args()

def str2bool(self, text):
    if text == 'True':
        arg = True
    elif text == 'False':
        arg = False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    return arg

if __name__=="__main__":
    h = Parser()
    print(h.args.__dict__)
