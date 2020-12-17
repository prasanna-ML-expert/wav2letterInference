import cherrypy
import sys
import json
from runmodel import runmodel
#p = runmodel.runmodel()

class convertAudio(object):
  #p = runmodel.runmodel()
  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.json_in()
  def index(self):
      #data = cherrypy.request.json
      #df = pd.DataFrame(data)
      model_path = "/home/model/"
      w2l_bin = "/root/wav2letter/build/inference/inference/examples/simple_streaming_asr_example"
      path_to_audio_file = '/home/wav2letterInference/numbersAudioGirl.wav'
      output = runmodel.run(model_path,w2l_bin,path_to_audio_file)
      return output.replace('\n',' ') #.to_json() 
  index.exposed = True

  def process(self):
      #data = cherrypy.request.json
      #df = pd.DataFrame(data)
      model_path = "/content/wav2letter/build/recipes/utilities/convlm_serializer/SerializeConvLM"
      w2l_bin = "/content/flashlight/build/bin/asr/fl_asr_decode"
      path_to_audio_file = '/content/wav2letterInference/numbersAudioMale.wav'
      output = runmodel.run(model_path,w2l_bin,path_to_audio_file)
      return output#.to_json()
  process.exposed = True


if __name__ == '__main__':
    config = {'global':{'server.socket_host': '0.0.0.0','server.socket_port' : int(sys.argv[1])}}
    cherrypy.config.update(config)
    cherrypy.quickstart(convertAudio())
