import numpy

def evaluate(observation, model, states=None):
    """
    TODO
    If you want the real evaluation (you don't know the states) do not set the states.
    Implements the forward algorithm for evaluation of an observation sequence given the HMM model.
    """
    N = model.N
    T = observation.shape[0]

    if states is None:
        alphas = numpy.zeros((T,N))
        
        """ Initialization """
        alphas[0, :] = model.pi * model.B[:, observation[0]]

        """ Forward Updates """
        for t in range(1, T):
            alphas[t, :] = numpy.dot(alphas[t-1, :], model.A) # matrix multiply
            alphas[t, :] = alphas[t, :] * model.B[:, observation[t]]

        """ Termination """
        return alphas[T-1, :].sum()

    else:
        #check number of states for compatibility
        result = 1
        for i in range(T):
            result *= model.B[states[i], observation[i]]
        return result