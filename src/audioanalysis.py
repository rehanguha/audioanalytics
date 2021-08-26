import parselmouth
import glob
import pandas as pd
import numpy as np
import scipy
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import os
from src.utils import extractFilename

def mysptotal(sound, sourcerun):

    path, filename = extractFilename(sound, withextension=True)
    path=path+"/"
    try:
        objects= parselmouth.praat.run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        #print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str(objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=np.array(z2)
        z4=np.array(z3)[np.newaxis]
        z5=z4.T

        db= binom.rvs(n=10,p=float(z2[14]),size=10000)
        a=np.array(db)
        b=np.mean(a)*100/10


        dataset=pd.DataFrame({"number_of_syllables":z5[0,:],
                              "number_of_pauses":z5[1,:],
                              "rate_of_speech":z5[2,:],
                              "articulation_rate":z5[3,:],
                              "speaking_duration":z5[4,:],
                              "original_duration":z5[5,:],
                              "pronunciation_posteriori_probability_score_percentage":b,
                              "balance":z5[6,:],
                              "f0_mean":z5[7,:],
                              "f0_std":z5[8,:],
                              "f0_median":z5[9,:],
                              "f0_min":z5[10,:],
                              "f0_max":z5[11,:],
                              "f0_quantile25":z5[12,:],
                              "f0_quan75":z5[13,:]})
        return dataset.to_json(orient='index')
    except Exception as e:
        return {"Try again the sound of the audio was not clear" + str(e)}