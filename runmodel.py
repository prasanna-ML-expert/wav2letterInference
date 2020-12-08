import os
import signal
from subprocess import Popen, PIPE  

class runmodel():
  def run(model_path,w2l_bin,path_to_audio_file):
 
    
    w2l_process = Popen(['{} --input_files_base_path={}'.format(w2l_bin, model_path)],
                      stdin=PIPE, stdout=PIPE, stderr=PIPE,
                      shell=True)

    # write to the stdin of the process
    # make sure to flush and add \n to the string
    w2l_process.write(b"input={}\n".format(path_to_audio_file))
    w2l_process.stdin.flush()
    
    while True:
      # read from process stdout
      output = p.stdout.readline()
      if output == b'#finish transcribing\n':
        # finish transcribing an audio
        break
      else:
        print(output)
    return output
# finish the process
os.killpg(os.getpgid(w2l_process.pid), signal.SIGTERM)  