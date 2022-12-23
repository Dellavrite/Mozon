

fields = [
    'name',
    'cost',
    'specifications',
    'description',
    'manufacturer',
    'picture',
    'category'
]

text = ""
for i in fields:
    text += f'model.{i} = data.cleaned_data["{i}"]\n'

print(text)