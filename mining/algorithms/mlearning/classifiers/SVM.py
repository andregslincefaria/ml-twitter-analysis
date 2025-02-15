from sklearn.linear_model import SGDClassifier

from settings import *
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from mining.algorithms.mlearning.classifiers.Classifier import Classifier

class SVM(Classifier):
    def __init__(self, fname=SVM_FNAME, n_neighbours = SVM_NEIGHBOURS_COUNT):
        self.n_neighbours = n_neighbours
        super(SVM, self).__init__(name=SVM_NAME,initials=SVM_INITIALS)
        if fname!=None:
            super(SVM,self).load(fname)
        else:
            self.create()

    def create(self):
        #self.clf = OneVsRestClassifier(SVC(random_state=SVM_SVC_RANDOM_STATE, kernel=SVM_SVC_KERNEL))
        self.clf = SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42,max_iter=5, tol=None)