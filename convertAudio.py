import cherrypy
import pandas as pd
import runmodel
p = runmodel.runmodel()

class convertAudio(object):
  p = runmodel.runmodel()
  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.json_in()
  def index(self):
      #data = cherrypy.request.json
      #df = pd.DataFrame(data)
      model_path = "/content/wav2letter/build/recipes/utilities/convlm_serializer/SerializeConvLM"
      w2l_bin = "/content/flashlight/build/bin/asr/fl_asr_decode"
      path_to_audio_file = '/content/wav2letterInference/numbersAudioMale.wav'
      output = p.run(model_path,w2l_bin,path_to_audio_file)
      return output#.to_json()
  index.exposed = True

  def process(self):
      #data = cherrypy.request.json
      #df = pd.DataFrame(data)
      model_path = "/content/wav2letter/build/recipes/utilities/convlm_serializer/SerializeConvLM"
      w2l_bin = "/content/flashlight/build/bin/asr/fl_asr_decode"
      path_to_audio_file = '/content/wav2letterInference/numbersAudioMale.wav'
      output = p.run(model_path,w2l_bin,path_to_audio_file)
      return output#.to_json()
  process.exposed =index True


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0','server.socket_port' : int(sys.argv[1])}
    cherrypy.config.update(config)
    cherrypy.quickstart(convertAudio())