class InputPluginInterface:
    def init(self):
        pass

    def gather_input(self):
        raise NotImplementedError


class LLMPluginInterface:
    def init(self):
        pass

    def predict(self, message, history):
        raise NotImplementedError


class TranslationPluginInterface:
    def init(self):
        pass

    def translate(self, text):
        raise NotImplementedError

    # Use the two letter language codes from here: https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
    def get_input_language_code(self):
        raise NotImplementedError

    def get_output_language_code(self):
        raise NotImplementedError


class TTSPluginInterface:
    def init(self):
        pass

    def synthesize(self, text):
        raise NotImplementedError
