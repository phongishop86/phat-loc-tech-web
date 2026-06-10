import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the start marker
start_marker = '<!-- 3D Cube Right Side -->'

# Use regex to replace the whole block starting from start_marker down to the closing div of that block
# The block starts with <div class="relative hidden lg:flex items-center justify-center scale-95 z-20">
# We can just match the whole 3D cube block. Let's find it with regex.
# Since python re.sub with DOTALL is powerful, let's use it.

pattern = r'<!-- 3D Cube Right Side -->.*?<div class="cube-scene">.*?</div>\s*</div>\s*</div>'

map_html = """<!-- Google Maps Location Right Side -->
                <div class="relative hidden lg:flex items-center justify-center z-20">
                    <div class="w-full max-w-[480px] aspect-square rounded-2xl overflow-hidden shadow-2xl shadow-secondary/20 border-[6px] border-white/30 bg-white/10 backdrop-blur-sm transform transition-transform hover:scale-105 duration-500">
                        <iframe 
                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.066465365518!2d106.63665791480112!3d10.806222892301142!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752b1e3271221b%3A0x7d0231d6833130d!2zNDkxLzEgVHLGsOG7nW5nIENoaW5oLCBQaMaw4budbmcgMTQsIFTDom4gQsOsbmgsIEjhu5MgQ2jDrSBNaW5oLCBWaWV0bmFt!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s" 
                            width="100%" 
                            height="100%" 
                            style="border:0;" 
                            allowfullscreen="" 
                            loading="lazy" 
                            referrerpolicy="no-referrer-when-downgrade">
                        </iframe>
                    </div>
                </div>"""

new_content = re.sub(pattern, map_html, content, flags=re.DOTALL)

if new_content != content:
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced Rubik cube with Google Maps.")
else:
    print("Failed to replace using regex.")

