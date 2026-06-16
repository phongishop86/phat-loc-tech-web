import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

map_html = """
              <!-- Map Section -->
              <div class="mt-8 mb-12 bg-[#003380] rounded-2xl p-6 md:p-8">
                  <h4 class="text-white text-xl font-bold mb-4 font-montserrat">Bản đồ</h4>
                  <div class="w-full h-64 md:h-80 rounded-xl overflow-hidden shadow-lg border border-white/10">
                      <iframe src="https://maps.google.com/maps?q=V%C4%83n%20ph%C3%B2ng%20%E1%BA%A3o%20T%C3%A2n%20B%C3%ACnh%20-%20SeaOffice&t=&z=16&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                  </div>
              </div>
"""

# Insert before the copyright divider
target_str = '<div class="border-t border-slate-200 pt-8 text-center text-xs text-gray-600">'
new_content = content.replace(target_str, map_html + '\n              ' + target_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Map section added successfully.")
