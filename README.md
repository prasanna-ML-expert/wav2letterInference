**wav2letter Inference API:** 

wav2letter.ipynb is google colab notebook file.

Run this colab file in google colab, which will fetch all dependencies, compile and run the inference. The output of the inference is served over python web API.

While installing Arrayfire, you need to accept the licence by inputting Y in the output cell. 

Upload wav file to wav2letterInference folder and change the name to numbersAudioMale.wav(or change filename/line 16 in convertAudio.py) for Inference

**Run the container**
1)sudo docker run --rm -itd --ipc=host --name w2l wav2letter/wav2letter:inference-latest
2)sudo docker exec -it w2l bash

**Running inference inside the container using python code**,
1)download model from AWS with below command into folder model
for f in acoustic_model.bin tds_streaming.arch decoder_options.json feature_extractor.bin language_model.bin lexicon.txt tokens.txt ; do wget http://dl.fbaipublicfiles.com/wav2letter/inference/examples/model/${f} ; done

2)and run(python runmodel.py) . 
Change path for binary, model folder and wav file path accordingly in the runmodel file


contact jkreddy@colorssoftware.com

Output looks like below
b'Started features model file loading ... \n'
b'Completed features model file loading elapsed time=2407 microseconds\n'
b'\n'
b'Started acoustic model file loading ... \n'
b'Completed acoustic model file loading elapsed time=4732 milliseconds\n'
b'\n'
b'Started tokens file loading ... \n'
b'Completed tokens file loading elapsed time=1341 microseconds\n'
b'\n'
b'Tokens loaded - 9998 tokens\n'
b'Started decoder options file loading ... \n'
b'Completed decoder options file loading elapsed time=91 microseconds\n'
b'\n'
b'Started create decoder ... \n'
b'Completed create decoder elapsed time=1653 milliseconds\n'
b'\n'
b'Started converting audio input from stdin to text... ... \n'
b'#start (msec), end(msec), transcription\n'
b'0,1000,\n'
b'1000,2000,\n'
b'2000,3000,one \n'
b'3000,4000,two three \n'
b'4000,5000,four \n'
b'5000,6000,five six \n'
b'6000,7000,seven eight \n'
b'7000,8000,nine \n'
b'8000,9000,ten eleven \n'
b'9000,10000,twelve thirty \n'
b'10000,10334,forty fifty \n'
b'Completed converting audio input from stdin to text... elapsed time=2626 milliseconds\n'

