string = "python_genius"

print(f"""
Origional:       {string}
First char:      {string[0]}
Last char:       {string[-1]}
Every but last:  {string[:-1]}
First slice:     {string[:6]}
Middle slice:    {string[5:8]}
Last slice:      {string[-6:]}
Every n'th:      {string[::2]}
Reverse:         {string[::-1]}
""")
