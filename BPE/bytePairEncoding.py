from importlib.metadata import version
import tiktoken
print("Tiktoken version", version("tiktoken"))
tokenizer = tiktoken.get_encoding("gpt2")

text = (
    "Hello, do you like tea <|endoftext|> In the sunlit terraces"
    "of someuknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)

strings = tokenizer.decode(integers)
print(strings)
