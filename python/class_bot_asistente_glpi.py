from class_basic_voice_bot import BasicVoiceBot

class AsistenteGlpi(BasicVoiceBot):
	def __init__(self,name_,file_tag):
		BasicVoiceBot.__init__(self, name_)

	def procesa_msg(self,aaa,bbb):
		self.log('procesa_post_msg')

asistenteBot = AsistenteGlpi("Asistente GLPI","GLPI")
#asistenteBot.vozTesting_DISPONIBLES()
asistenteBot.vozChange('MSTTS_V110_esMX_RaulMM')
asistenteBot.setUtilComando_SRC('commands/COMMAND_DEF_GLPI.json')
asistenteBot.load()
asistenteBot.batch("commands/BATCH_FLOW_GLPI.txt")
