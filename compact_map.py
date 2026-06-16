import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the previously added full-width Map Section
map_section_pattern = re.compile(r'<!-- Map Section -->.*?</div>\s*</div>\s*', re.DOTALL)
content = map_section_pattern.sub('', content)

# 2. Re-layout the Footer grid
# Change grid class
content = content.replace('<div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">', 
                          '<div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-12">')

# Col 1
content = content.replace('<div class="col-span-1 md:col-span-1">', '<div class="col-span-1 lg:col-span-4">')
# Col 2
content = content.replace('<div class="md:col-span-1">', '<div class="lg:col-span-3">')

# For Col 3 and Col 4, we need to wrap them and append the map.
# Find the start of Col 3 (Danh Mục Dịch Vụ)
col3_start_pattern = r'<div>\s*<h4[^>]*>Danh Mục Dịch Vụ</h4>'
# Wait, the h4 might have mojibake if read as cp1252, but we are reading as utf-8, so it's "Danh Mục Dịch Vụ".
col3_start_match = re.search(col3_start_pattern, content)

if col3_start_match:
    # We will replace the start of Col 3 to include the wrapper.
    # But we need to close the wrapper after Col 4.
    # Let's find the end of Col 4.
    # Col 4 ends before `</div>\s*<div class="border-t border-slate-200`
    
    # Let's extract the whole grid content safely by replacing markers.
    content = content.replace('<div>\n                      <h4 class="text-primary font-semibold mb-4 uppercase text-sm tracking-wider">Danh Mục Dịch Vụ</h4>',
                              '<div class="lg:col-span-5 flex flex-col gap-6">\n                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">\n                      <div>\n                      <h4 class="text-primary font-semibold mb-4 uppercase text-sm tracking-wider">Danh Mục Dịch Vụ</h4>')
    
    # Find the end of Col 4, which is right before:
    # </div>
    # <div class="border-t border-slate-200 pt-8 text-center text-xs text-gray-600">
    
    # We need to insert:
    # </div> <!-- close grid-cols-2 -->
    # <!-- Map -->
    # <div class="...">...</div>
    # </div> <!-- close col-span-5 -->
    
    map_html = """
                  </div> <!-- Close grid-cols-2 -->
                  
                  <!-- Compact Map -->
                  <div class="bg-[#1e3a8a] rounded-2xl p-4 shadow-lg border border-white/10 mt-2">
                      <h4 class="text-white text-sm font-bold mb-3 font-montserrat uppercase tracking-wider">Bản đồ</h4>
                      <div class="w-full h-40 rounded-xl overflow-hidden">
                          <iframe src="https://maps.google.com/maps?q=V%C4%83n%20ph%C3%B2ng%20%E1%BA%A3o%20T%C3%A2n%20B%C3%ACnh%20-%20SeaOffice&t=&z=16&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                      </div>
                  </div>
              </div> <!-- Close col-span-5 -->
"""
    # Replace the closing of the 4-column grid with our injected HTML + the closing
    # The grid ends exactly before the copyright section.
    # Let's use a targeted replace.
    # The end of Col 4 is `</ul>\n                  </div>\n              </div>\n              \n              <div class="border-t`
    
    target_end = '</ul>\n                  </div>\n              </div>\n              \n              <div class="border-t'
    new_end = '</ul>\n                  </div>' + map_html + '\n              </div>\n              \n              <div class="border-t'
    
    content = content.replace(target_end, new_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer layout updated to compact the map.")
