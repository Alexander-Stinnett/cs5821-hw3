from transformers import GPTNeoXForCausalLM, AutoTokenizer

param_choice = "1.4b-deduped"
model_choice = "EleutherAI/pythia-" + param_choice
cache_dir_choice = "./pythia-" + param_choice + "/step3000"


model = GPTNeoXForCausalLM.from_pretrained(
    model_choice,
    revision="step3000",
    cache_dir=cache_dir_choice,
)
tokenizer = AutoTokenizer.from_pretrained(
    model_choice,
    revision="step3000",
    cache_dir=cache_dir_choice,
)

inputs = tokenizer("The top ten things to do in New York are: 1. ", return_tensors="pt")
tokens = model.generate(**inputs)
print(tokenizer.decode(tokens[0]))