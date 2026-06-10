import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the start and end of the cube section
start_marker = '<!-- 3D Cube Right Side -->'
end_marker = '</div>\n                  </div>\n              </div>\n          </section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # The end_marker includes the closing div of the hero container, so we need to be careful
    # We just want to replace from start_marker up to the end of the cube wrapper
    # Let's find the closing tag of the cube wrapper explicitly
    cube_end = content.find('</div>\n                      </div>\n                  </div>', start_idx) + len('</div>\n                      </div>\n                  </div>')
    
    map_html = """<!-- Google Maps Location Right Side -->
                <div class="relative hidden lg:flex items-center justify-center z-20">
                    <div class="w-full max-w-md h-[400px] rounded-2xl overflow-hidden shadow-2xl shadow-secondary/20 border-4 border-white/40 bg-white/10 backdrop-blur-sm p-2 transform transition-transform hover:scale-105 duration-500">
                        <iframe 
                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.066465365518!2d106.63665791480112!3d10.806222892301142!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752b1e3271221b%3A0x7d0231d6833130d!2zNDkxLzEgVHLGsOG7nW5nIENoaW5oLCBQaMaw4budbmcgMTQsIFTDom4gQsOsbmgsIEjhu5MgQ2jDrSBNaW5oLCBWaWV0bmFt!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s" 
                            width="100%" 
                            height="100%" 
                            style="border:0; border-radius: 12px;" 
                            allowfullscreen="" 
                            loading="lazy" 
                            referrerpolicy="no-referrer-when-downgrade">
                        </iframe>
                    </div>
                </div>"""
                
    new_content = content[:start_idx] + map_html + content[cube_end:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced Rubik cube with Google Maps.")
else:
    print("Could not find the markers for replacement.")
