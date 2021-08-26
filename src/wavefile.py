import librosa
import librosa.display
import matplotlib.pyplot as plt
from src.utils import extractFilename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def audio_waveplot(INPUTPATH, OUTPATH):
    x , sr = librosa.load(INPUTPATH)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    
    try:
        fig = plt.Figure(figsize=(14, 5), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        p = librosa.display.waveplot(x, sr=sr, ax=ax)
        fig.savefig(OUTPATH + "waveplot")

        del fig, canvas, ax, p

        fig = plt.Figure(figsize=(14, 5), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        p = librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz', ax=ax)

        fig.savefig(OUTPATH + "spec")

        del fig, canvas, ax, p

        return "Complete"
    except Exception as e:
        return "Error: " + str(e)