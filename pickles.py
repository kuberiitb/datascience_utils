import pickle
def dump(file_, filename='out.pkl'):
    with open(filename,'wb') as f:
        pickle.dump(file_, f, pickle.DEFAULT_PROTOCOL)

pickle.dump(file_, open(filename,'wb'), pickle.DEFAULT_PROTOCOL)

def load(filename):
    with open(filename,'rb') as f:
        return pickle.load(f)

loaded = pickle.load(open(filename+'.pkl','rb'))
