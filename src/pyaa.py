from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import matplotlib.pyplot as plt
import pandas as pd
import json
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.pyplot.switch_backend('Agg')

def zcr_sigenergy(INPUTPATH, OUTPATH):
    try:
        [Fs, x] = audioBasicIO.read_audio_file(INPUTPATH)

        try:
            CH = x.shape[1]
        except:
            CH = 1
        
        if CH == 1:
            F_0, f_names_0 = ShortTermFeatures.feature_extraction(x[:,], Fs, 0.050*Fs, 0.025*Fs)
            fig = plt.figure(figsize=(18, 8), dpi=200)
            ax1 = fig.add_subplot(111)
            ax1.plot(F_0[0,:], label=f_names_0[0])
            ax1.plot(F_0[1,:], label=f_names_0[1])
            ax1.legend()
            # Set common labels
            fig.text(0.5, 0.01, 'Frame no.', ha='center', va='center')
            fig.text(0.004, 0.5, 'Zero Crossing Rate / Signal Energy', ha='center', va='center', rotation='vertical')
            ax1.set_title('Channel 1')
            fig.tight_layout()
            plt.savefig(OUTPATH + 'zcr_energy.png')
            plt.close()
            return "Complete"

        if CH==2:
            F_0, f_names_0 = ShortTermFeatures.feature_extraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)
            F_1, f_names_1 = ShortTermFeatures.feature_extraction(x[:,1], Fs, 0.050*Fs, 0.025*Fs)
            fig = plt.figure(figsize=(18, 8), dpi=200)
            ax1 = fig.add_subplot(211)
            ax2 = fig.add_subplot(212)
            ax1.plot(F_0[0,:], label=f_names_0[0])
            ax1.plot(F_0[1,:], label=f_names_0[1])
            ax2.plot(F_1[0,:], label=f_names_1[0])
            ax2.plot(F_1[1,:], label=f_names_1[1])
            ax1.legend()
            ax2.legend()
            # Set common labels
            fig.text(0.5, 0.01, 'Frame no.', ha='center', va='center')
            fig.text(0.004, 0.5, 'Zero Crossing Rate / Signal Energy', ha='center', va='center', rotation='vertical')
            ax1.set_title('Channel 1')
            ax2.set_title('Channel 2')
            fig.tight_layout()
            plt.savefig(OUTPATH + 'zcr_energy.png')
            plt.close()
            return "Complete"
    except Exception as e:
        return "Error: " + str(e)

def feature_extraction(INPUTPATH, OUTPATH):
    try:
        [Fs, x] = audioBasicIO.read_audio_file(INPUTPATH)
        try:
            CH = x.shape[1]
        except:
            CH = 1
        
        if CH == 1:
            c1 = ShortTermFeatures.feature_extraction(x[:,], Fs, 0.050*Fs, 0.025*Fs)

            channel1 = {}
            for i in range(0, len(c1[1])):
                channel1[c1[1][i]] = c1[0][i]

            channel1 = pd.DataFrame(channel1)
            channel1.to_json(OUTPATH + "channel1_features.json")
            result = {
                'channel1': json.loads(channel1.to_json())
            }
        
        if CH == 2:
            c1 = ShortTermFeatures.feature_extraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)
            c2 = ShortTermFeatures.feature_extraction(x[:,1], Fs, 0.050*Fs, 0.025*Fs)

            channel1 = {}
            channel2 = {}
            for i in range(0, len(c1[1])):
                channel1[c1[1][i]] = c1[0][i]
            
            for i in range(0, len(c2[1])):
                channel2[c2[1][i]] = c2[0][i]

            channel1 = pd.DataFrame(channel1)
            channel1.to_json(OUTPATH + "channel1_features.json")

            channel2 = pd.DataFrame(channel2)
            channel2.to_json(OUTPATH + "channel2_features.json")
            result = {
                'channel1': json.loads(channel1.to_json()),
                'channel2': json.loads(channel2.to_json())
            }


        return json.dumps(result)

    except Exception as e:
        return "Error: " + str(e)