import re

path = r'd:\KARIJERA\KLIJENTI\VITA FIZIOTERAPIJA\Vita\index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

def replacer(match):
    full_text = match.group(2)
    # Split by <br>
    parts = re.split(r'<br\s*/?>', full_text, flags=re.IGNORECASE)
    
    # We want odd parts to have class 'service-line-down' (coming from top)
    # and even parts to have class 'service-line-up' (coming from bottom)
    new_html = '\n'
    for i, part in enumerate(parts):
        cls = 'service-line-down' if (i % 2 == 0) else 'service-line-up'
        new_html += f'            <span class="{cls}">{part}</span>\n'
    new_html += '          '
    return match.group(1) + new_html + match.group(3)

old_pattern = r'(<h2 class="service-title">)(.*?)(</h2>)'
c_new = re.sub(old_pattern, replacer, c, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c_new)

print('SUCCESS')
