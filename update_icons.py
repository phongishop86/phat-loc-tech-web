import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Top Node (Máy tính)
old_top_node = '<div class="text-slate-500 font-bold mb-4 bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm z-10">Máy tính</div>'
new_top_node = """<div class="flex flex-col items-center gap-2 mb-6">
                                <div class="w-16 h-16 bg-white rounded-2xl shadow-lg border border-slate-200 flex items-center justify-center text-3xl text-blue-500 z-10 relative hover:scale-110 transition-transform">
                                    <i class="ph-duotone ph-desktop"></i>
                                </div>
                                <span class="font-bold text-slate-700 text-sm bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm z-10">Máy tính</span>
                            </div>"""
content = content.replace(old_top_node, new_top_node)

# Replace Bottom Node (Phần mềm số hóa)
old_bottom_node = '<div class="text-slate-500 font-bold mt-4 bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm z-10">Phần mềm số hóa</div>'
new_bottom_node = """<div class="flex flex-col items-center gap-2 mt-6">
                                <span class="font-bold text-slate-700 text-sm bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm z-10">Phần mềm số hóa</span>
                                <div class="w-16 h-16 bg-white rounded-2xl shadow-lg border border-slate-200 flex items-center justify-center text-3xl text-purple-500 z-10 relative hover:scale-110 transition-transform">
                                    <i class="ph-duotone ph-cloud-arrow-up"></i>
                                </div>
                            </div>"""
content = content.replace(old_bottom_node, new_bottom_node)

# Adjust Left/Right Nodes slightly to match the 16x16 size if we want consistency, 
# The left/right nodes are w-20 h-20. Let's make top/bottom also w-20 h-20 to be perfectly symmetrical.
# Wait, I set w-16 in the string above. Let me replace w-16 with w-20.
content = content.replace('w-16 h-16', 'w-20 h-20')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated central nodes with icons.')
