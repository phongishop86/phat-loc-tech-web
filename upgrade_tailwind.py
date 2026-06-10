import glob
import re

old_config_regex = r'<!-- Tailwind CSS \(CDN\) -->\s*<script src="https://cdn\.tailwindcss\.com"></script>\s*<script>\s*tailwind\.config = \{.*?\n\s*\}\s*</script>'

new_config = """<!-- Tailwind CSS v4 (CDN) -->
    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
    <style type="text/tailwindcss">
        @theme {
            --font-sans: 'Inter', sans-serif;
            --font-serif: '"Playfair Display"', serif;
            
            --color-primary: #0F172A;
            --color-secondary: #2563EB;
            --color-accent: #06B6D4;
            --color-success: #10B981;
            
            /* Legacy mappings to ease transition */
            --color-brand-green: #10B981;
            --color-brand-purple: #2563EB;
            --color-brand-purple-dark: #0F172A;
            --color-brand-orange: #f97316;

            --animate-float1: float1 4s ease-in-out infinite;
            --animate-float2: float2 3.5s ease-in-out infinite;
            --animate-pulse-g: pulse-g 2s ease-in-out infinite;

            @keyframes float1 {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            @keyframes float2 {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-8px); }
            }
            @keyframes pulse-g {
                0%, 100% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.7; transform: scale(1.2); }
            }
        }
    </style>"""

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(old_config_regex, new_config, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated config in {file}")
    else:
        print(f"Regex not matched in {file}")
