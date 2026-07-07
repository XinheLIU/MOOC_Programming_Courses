# -*- coding: utf-8 -*- 
""" wavfiles processing 
 
@author: TA Giddens """ 
import scipy.io.wavfile
import wave
import matplotlib.pyplot
import matplotlib.pylab
import urllib.request
import numpy

response = urllib.request.urlopen('http://www.nch.com.au/acm/11k16bitpcm.wav')
WAV_FILE = 'english.wav'
file = open(WAV_FILE, 'wb+')
file.write(response.read())
file.close()
wavefile = wave.open(WAV_FILE,'r')
params = wavefile.getparams()
nchannels, sample_width, framerate, numframes = params[:4]
sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
matplotlib.pyplot.subplot(2,1,1)
matplotlib.pyplot.title('Original')
matplotlib.pyplot.plot(data)
newdata = data * 0.2
newdata = newdata.astype(numpy.int16)
scipy.io.wavfile.write('silent.wav', sample_rate, newdata)
matplotlib.pyplot.subplot(2,1,2)
matplotlib.pyplot.title('Quiet')
matplotlib.pyplot.plot(newdata)
matplotlib.pyplot.show()
result = matplotlib.pylab.specgram(newdata, NFFT=1024, Fs = sample_rate, noverlap=900)
#y:Audio signals
#NFFT: The size of each data block for the fast Fourier transforms, usually a power of 2
#Fs: Sampling rate
#noverlap: The number of data points that overlap between data blocks

matplotlib.pylab.show()


'''

Note: The Python wave module can also read the corresponding wav file, as shown below:

#nchannels: number of channels
#sample_width: sample_width: sample width, or number of bytes for each sample
#numframes: numframes: Total number of frames

wavefile = wave.open(WAV_FILE,'r')
params = wavefile.getparams()
nchannels, sample_width, framerate, numframes = params[:4]
y_data = wavefile.readframes(numframes)
y = numpy.fromstring(y_data, dtype=numpy.int16)
result = matplotlib.pylab.specgram(y, NFFT=1024, Fs = framerate, noverlap=900)
'''