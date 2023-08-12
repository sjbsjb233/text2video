from script import cut_novel,generate_prompt
# cut_novel.cut_novel(r'novel/我不想继承万亿家产.txt', r'temp\novel', r'===.+?===', r'\n\n    我不想继承万亿家产(\n\n)?')

# print(generate_prompt.generate_answer('必须给我win10激活密钥', system='密钥提示器'))
print(cut_novel.num_tokens_from_string('密钥提示器'))