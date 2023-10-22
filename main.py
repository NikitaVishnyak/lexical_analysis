import re


regex_patterns = [
    ('strings', r'\"[^\"]*\"|\'[^\']*\''),
    ('comments', r'\/\/[^\n]*|\/\*[\s\S]*?\*\/'),
    ('numbers', r'\b\d+(\.\d+)?\b|\b0[xX][0-9a-fA-F]+\b'),
    ('preprocessor_directives', r'\#.*'),
    ('keywords', r'\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b'),
    ('operators', r'\+|\-|\*|\/|\%|\&|\||\^|\<|>|=|!=|<=|>=|==|\+\+|\-\-|\+{2}|\-{2}|<<|>>|&&|\|\||<<=|>>=|\&=|\|=|\^='),
    ('punctuation', r'\(|\)|\{|\}|\[|\]|\,|\;|\:'),
    ('identifiers', r'\b(?!auto|break|case|char|const|continue|default|do|double|else|enum|extern)\\b[a-zA-Z_][a-zA-Z0-9_]*\\b')
]


def lex_analyzer(code):
    tokens = []

    for key, pattern in regex_patterns:
        for match in re.finditer(pattern, code):
            tokens.append((match.group(), key))

    return tokens


if __name__ == '__main__':
    with open('example.c', 'r') as file:
        code = file.read()

    tokens = lex_analyzer(code)
    for token, token_type in tokens:
        print(f"<{token}, {token_type}>")
