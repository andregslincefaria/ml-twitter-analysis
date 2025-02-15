from settings import *
from mining.algorithms.mlearning.classifiers.Classifier import Classifier
from sklearn.linear_model import LogisticRegression

class LR(Classifier):
    def __init__(self, fname=LR_FNAME):
        super(LR, self).__init__(name=LR_NAME,initials=LR_INITIALS)
        if fname!=None:
            super(LR,self).load(fname)
        else:
            self.create()

    def create(self):
        self.clf = LogisticRegression(random_state=0, multi_class='ovr')