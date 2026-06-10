import glob

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
            --color-brand-green: var(--color-success);
            --color-brand-purple: var(--color-secondary);
            --color-brand-purple-dark: var(--color-primary);
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
    
    start_tag = '<script src="https://cdn.tailwindcss.com"></script>'
    if start_tag in content:
        # Check if there is a preceding comment
        start_idx = content.find(start_tag)
        preceding_comment_idx = content.rfind("<!-- Tailwind", 0, start_idx)
        if preceding_comment_idx != -1 and start_idx - preceding_comment_idx < 100:
            start_idx = preceding_comment_idx
            
        script_tag_start = content.find("tailwind.config", start_idx)
        if script_tag_start != -1:
            end_idx = content.find("</script>", script_tag_start) + len("</script>")
            
            new_content = content[:start_idx] + new_config + content[end_idx:]
            
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated config in {file}")
