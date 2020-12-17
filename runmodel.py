import os
import signal
from subprocess import Popen, PIPE  

class runmodel():
  def run(model_path,w2l_bin,path_to_audio_file):
 
    with open(path_to_audio_file, 'rb', 0) as a: 
      w2l_process = Popen(['{} --input_files_base_path={}'.format(w2l_bin, model_path)],
                      stdin=a, stdout=PIPE, stderr=PIPE,
                      shell=True)

    # write to the stdin of the process
    # make sure to flush and add \n to the string
    #print(("input=%b\n" % path_to_audio_file).encode())
    #w2l_process.stdin.write("input=%b\n".encode() % path_to_audio_file)
    #w2l_process.stdin.flush()

    while True:
      # read from process stdout
      output = w2l_process.stdout.readline()
      if b'Completed converting audio input from stdin to text' in output :#output == b'#finish transcribing\n':
        # finish transcribing an audio
        break
      else:
        print(output)
      
    return output
# finish the process
#os.killpg(os.getpgid(w2l_process.pid), signal.SIGTERM)

if __name__ == '__main__':
      model_path = "/home/model/"
      w2l_bin = "/root/wav2letter/build/inference/inference/examples/simple_streaming_asr_example"
      path_to_audio_file = '/home/wav2letterInference/numbersAudioGirl.wav'
      output = runmodel.run(model_path,w2l_bin,path_to_audio_file)
      print(output)
