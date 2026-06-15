import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the 3 generic CSS lines
lines_to_remove = """<!-- Connecting Lines on PC -->
                        <div class="hidden lg:block absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[150%] h-0.5 bg-slate-200 z-0"></div>
                        <div class="hidden lg:block absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-0.5 bg-slate-200 z-0 rotate-45"></div>
                        <div class="hidden lg:block absolute top-3/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-0.5 bg-slate-200 z-0 -rotate-45"></div>"""

content = content.replace(lines_to_remove, '<!-- Connecting Lines on PC -->\n                        <svg id="eco-lines" class="hidden lg:block absolute inset-0 w-full h-full pointer-events-none z-0"></svg>')

# 2. Add id="eco-center" to the center logo container
center_logo_html = """<!-- Center Column (Logo) -->
                    <div class="flex flex-col items-center justify-center w-full lg:w-[30%] relative z-10 order-first lg:order-none mb-12 lg:mb-0">"""
center_logo_replaced = """<!-- Center Column (Logo) -->
                    <div id="eco-center" class="flex flex-col items-center justify-center w-full lg:w-[30%] relative z-10 order-first lg:order-none mb-12 lg:mb-0">"""
content = content.replace(center_logo_html, center_logo_replaced)

# 3. Add eco-node to Left and Right column nodes
# Left Column
content = content.replace('<!-- Left Column (3 Nodes) -->\n                    <div class="flex flex-col gap-6 w-full lg:w-[35%] relative z-20">', '<!-- Left Column (3 Nodes) -->\n                    <div class="flex flex-col gap-6 w-full lg:w-[35%] relative z-20 eco-col">')
# Right Column
content = content.replace('<!-- Right Column (3 Nodes) -->\n                    <div class="flex flex-col gap-6 w-full lg:w-[35%] relative z-20">', '<!-- Right Column (3 Nodes) -->\n                    <div class="flex flex-col gap-6 w-full lg:w-[35%] relative z-20 eco-col">')

# Add class 'eco-node' to all 6 nodes. They currently start with: <div class="flex items-center gap-4 bg-white p-4 rounded-full... group">
# Node 1 (MÁY TÍNH & LAPTOP - Rose): <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-rose-500
content = content.replace('hover:-translate-y-1 group"', 'hover:-translate-y-1 group eco-node"')

# 4. Inject JS script before </body>
js_script = """
    <!-- Script to draw Ecosystem Lines -->
    <script>
        function drawEcoLines() {
            const svg = document.getElementById('eco-lines');
            if (!svg) return;
            
            // Only draw on large screens (lg: 1024px)
            if (window.innerWidth < 1024) {
                svg.innerHTML = '';
                return;
            }

            const container = svg.parentElement;
            const containerRect = container.getBoundingClientRect();
            
            const centerEl = document.getElementById('eco-center');
            if (!centerEl) return;
            const centerRect = centerEl.getBoundingClientRect();
            
            // Center of the logo
            const cx = centerRect.left - containerRect.left + centerRect.width / 2;
            const cy = centerRect.top - containerRect.top + centerRect.height / 2;

            let svgHTML = '';
            
            // The nodes
            const nodes = container.querySelectorAll('.eco-node');
            nodes.forEach(node => {
                const nodeRect = node.getBoundingClientRect();
                
                // Find node center Y
                const ny = nodeRect.top - containerRect.top + nodeRect.height / 2;
                
                // Find which side it is on
                const isLeft = (nodeRect.left - containerRect.left) < (containerRect.width / 2);
                
                // X position is the inner edge of the node card
                const nx = isLeft ? (nodeRect.right - containerRect.left) : (nodeRect.left - containerRect.left);

                // Get color from the icon's gradient class or fallback to slate-300
                let color = '#cbd5e1'; // default
                if (node.innerHTML.includes('from-rose-500')) color = '#e11d48';
                if (node.innerHTML.includes('from-purple-600')) color = '#7e22ce';
                if (node.innerHTML.includes('from-cyan-500')) color = '#0e7490';
                if (node.innerHTML.includes('from-blue-600')) color = '#1d4ed8';
                if (node.innerHTML.includes('from-emerald-500')) color = '#047857';
                if (node.innerHTML.includes('from-orange-400')) color = '#ea580c';

                // Draw a beautiful curved path (cubic bezier) from cx,cy to nx,ny
                // Control points to make it start horizontally from center and end horizontally at node
                const cp1x = cx + (isLeft ? -50 : 50);
                const cp1y = cy;
                const cp2x = nx + (isLeft ? 50 : -50);
                const cp2y = ny;

                const pathD = `M ${cx} ${cy} C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${nx} ${ny}`;

                svgHTML += `<path d="${pathD}" fill="none" stroke="${color}" stroke-width="2" class="opacity-60 transition-all duration-500" />`;
                // Add a small dot at the node connection point
                svgHTML += `<circle cx="${nx}" cy="${ny}" r="4" fill="white" stroke="${color}" stroke-width="2" />`;
            });

            svg.innerHTML = svgHTML;
        }

        window.addEventListener('resize', drawEcoLines);
        window.addEventListener('load', drawEcoLines);
        setTimeout(drawEcoLines, 100);
        setTimeout(drawEcoLines, 500); // extra fallback
    </script>
</body>
"""

content = content.replace('</body>', js_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ecosystem lines fixed.")
