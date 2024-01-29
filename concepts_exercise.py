from jupyprint import jupyprint
import numpy as np

def concepts_exercise(keys=True):
    defs_dict = {
    "**Statistics**:": """ the science of modelling data which involves uncertainty
    - e.g. data from complex systems, typically resulting in imperfect,
    probabilistic relationships.""",

    "**Data Science**:": """statistics + computing e.g. dealing with entire data science pipelines 
    (obtaining, cleaning, organizing, and analysing data). We could - if we're in a mood for very
    simple definitions - view "statistics" just as relating to the theory of the 'analysing data' part
    of the definition of data science.""",

    "**Observational unit**:": """any thing for which we can record scores on different variables. E.g.
    (people, cars, streets, geographical areas, institutions)""",

    "**Population**:": """the complete (possibly infinite) set of observational units in which we are
    interested for some research question.""",

    "**Variable**:": """a characteristic which varies between observational units.""",

    "**Statistical Model**:": """probabilistic model which describes the relationship between variables. We
    can think of our variables as a collection of vectors, and the model is a mathematical statement
    which involves the vectors, and describes the relationship between them. Typically, we describe
    the relationship between a set of predictor variables and an outcome variable.""",

    "**Statistical Significance**:": """
    'Statistical significance helps quantify
    whether a result is likely due to chance or to some factor of interest,
    [...] When a finding is significant, it simply means you can feel confident
    that it is real, not that you just got lucky (or unlucky) in choosing the sample.'
    [Quote is from here.](https://hbr.org/2016/02/a-refresher-on-statistical-significance)""",

    "**Machine Learning**:": """[IBM](https://www.ibm.com/topics/machine-learning)
    define this as follows : 'Machine learning is a branch of artificial intelligence
     (AI) and computer science which focuses
    on the use of data and algorithms to imitate the way that humans learn,
    gradually improving its accuracy. A broader definition might be '[machine learning involves]
    prediction by using general-purpose learning algorithms to find patterns in often rich and unwieldy
data (Bzdok, Altman, & Krzywinski, 2018)'""",

    "**Artificial Intelligence**:": """training machines to engage in intelligent behaviour (with more or less
    similarity to human intelligence)."""   
}
    if keys == True:
        for key in np.random.permutation(list(defs_dict.keys())):
            jupyprint(key)
    elif keys == False:
        for key in np.random.permutation(list(defs_dict.keys())):
            jupyprint(f"{key}  {defs_dict[key]}")