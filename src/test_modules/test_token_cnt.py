import tiktoken

encoding = tiktoken.get_encoding("o200k_base")
test_str = "this is the test string"
# print(f"test str: {test_str} has {len(encoding.encode(test_str))} tokens")

print(len(encoding.encode(test_str)))