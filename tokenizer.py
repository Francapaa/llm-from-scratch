class SimpleTokenizerV2:
    def __init__(self, vocab):
       self.str_to_int = vocab
       self.int_to_str = { i:s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = r.split(r'([, . : ; ? _ ! " () \']|--|\s', text)
