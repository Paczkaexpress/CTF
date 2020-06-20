import sys
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt

if __name__ == "__main__":
    refBaseFile = "data/ref.wav"
    satFiles = ["data/sat_1.wav","data/sat_2.wav","data/sat_3.wav","data/sat_4.wav","data/sat_5.wav","data/sat_6.wav","data/sat_7.wav","data/sat_8.wav"] 
    refBaseWaveF, refBaseWaveData = wavfile.read(refBaseFile)

    satWaveF = [None] * 8
    satWaveData = [None] * 8
    for i in range(len(satFiles)):
        satWaveF[i], satWaveData[i] = wavfile.read(satFiles[i])
        print("Freq {} for sateline number {}".format(satWaveF[i],i))
    #print(refBaseWaveData)
    #print(len(refBaseWaveData))


    T = 1.0         # Sample Period
    fs = 5000000       # sample rate, Hz
    cutoff = 50000      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
    nyq = 0.5 * fs  # Nyquist Frequencyorder = 2       # sin wave can be approx represented as quadratic
    n = int(T * fs) # total number of samples

    normalCutoff = cutoff / nyq

    # get the filter coefs
    b, a = butter(2, normalCutoff, btype = 'low', analog=False)
    refBaseFilt = filtfilt(b,a,refBaseWaveData)

    satDataFilt = [None] * 8
    for i in range(len(satWaveData)):
        satDataFilt[i] = filtfilt(b,a,satWaveData[i])


    plt.hold(True)
    plt.plot(refBaseWaveData)
    for i in range(len(satWaveData)):
        plt.plot(satDataFilt[i])
    #plt.plot(satWaveData[0])
    #plt.plot(satWaveData[1])
    #plt.plot(satWaveData[2])
    #plt.plot(satWaveData[3])
    #plt.plot(satWaveData[4])
    #plt.plot(satWaveData[5])
    #plt.plot(satWaveData[6])
    #plt.plot(satWaveData[7])

    plt.show()
