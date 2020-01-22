import pickle
def dump(file_, filename):
    with open(filename+'.pkl','wb') as f:
        pickle.dump(file_, f, pickle.HIGHEST_PROTOCOL)

pickle.dump(file_, open(filename+'.pkl','wb'), pickle.HIGHEST_PROTOCOL)

def load(filename):
    with open(filename,'rb') as f:
        return pickle.load(f)

loaded = pickle.load(open(filename.pkl','rb'))
