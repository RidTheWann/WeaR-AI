"""
WeaR AI Knowledge - Art, Design, Colors & Creative Fields
Pengetahuan tentang seni, desain, warna, dan bidang kreatif.
Created by RidTheWann
"""

KNOWLEDGE_CREATIVE = {
    # ============================================
    # COLORS
    # ============================================
    "color_theory": {
        "category": "Design",
        "definition": "Color theory adalah study of color mixing dan visual effects.",
        "wheel": "Primary → Secondary → Tertiary colors",
        "harmonies": ["Complementary", "Analogous", "Triadic", "Split-complementary"]
    },
    "primary_colors": {
        "category": "Design",
        "definition": "Primary colors tidak bisa dibuat dari mixing colors lain.",
        "additive_rgb": "Red, Green, Blue (light/screens)",
        "subtractive_cmyk": "Cyan, Magenta, Yellow (print/paint)",
        "traditional": "Red, Yellow, Blue"
    },
    "hex_colors": {
        "category": "Design",
        "definition": "Hex colors menggunakan 6 digit hexadecimal untuk represent warna.",
        "format": "#RRGGBB",
        "examples": {
            "#FF0000": "Red",
            "#00FF00": "Green",
            "#0000FF": "Blue",
            "#FFFFFF": "White",
            "#000000": "Black"
        }
    },
    "rgb_vs_cmyk": {
        "category": "Design",
        "definition": "RGB untuk digital, CMYK untuk print.",
        "rgb": "Additive color (light), 0-255 per channel",
        "cmyk": "Subtractive color (ink), 0-100% per channel",
        "conversion": "Some RGB colors can't be perfectly printed"
    },
    "color_psychology": {
        "category": "Design",
        "definition": "Warna memengaruhi emosi dan persepsi.",
        "meanings": {
            "Red": "Passion, energy, danger, urgency",
            "Blue": "Trust, calm, professional",
            "Green": "Nature, growth, money, health",
            "Yellow": "Optimism, warning, attention",
            "Orange": "Creativity, enthusiasm, warmth",
            "Purple": "Luxury, mystery, spirituality",
            "Black": "Elegance, power, sophistication",
            "White": "Purity, simplicity, cleanliness"
        }
    },
    "gradient": {
        "category": "Design",
        "definition": "Gradient adalah transisi smooth antara warna.",
        "types": ["Linear", "Radial", "Conic"],
        "css": "background: linear-gradient(to right, red, blue);"
    },
    
    # ============================================
    # DESIGN PRINCIPLES
    # ============================================
    "design_principles": {
        "category": "Design",
        "definition": "Fundamental principles of good design.",
        "principles": [
            "Contrast - Make elements stand out",
            "Alignment - Create visual connections",
            "Repetition - Strengthen unity",
            "Proximity - Group related items",
            "Balance - Distribute visual weight",
            "Hierarchy - Show importance"
        ]
    },
    "whitespace": {
        "category": "Design",
        "definition": "Whitespace (negative space) adalah area kosong dalam design.",
        "benefits": ["Improves readability", "Creates focus", "Feels premium", "Reduces clutter"],
        "apple": "Apple famously uses whitespace effectively"
    },
    "typography": {
        "category": "Design",
        "definition": "Typography adalah art of arranging text.",
        "terms": {
            "Serif": "Fonts with decorative strokes (Times New Roman)",
            "Sans-serif": "Clean fonts without strokes (Arial, Helvetica)",
            "Kerning": "Space between characters",
            "Leading": "Space between lines",
            "Tracking": "Overall character spacing"
        }
    },
    "golden_ratio_design": {
        "category": "Design",
        "definition": "Golden ratio (1:1.618) creates aesthetically pleasing proportions.",
        "applications": ["Logo design", "Layout", "Photography composition"],
        "examples": ["Apple logo", "Twitter logo", "Parthenon"]
    },
    "rule_of_thirds": {
        "category": "Design",
        "definition": "Divide image into 3x3 grid, place subjects on lines/intersections.",
        "use": "Photography, video, graphic design",
        "result": "More dynamic composition than centering"
    },
    "gestalt_principles": {
        "category": "Design",
        "definition": "How humans perceive visual elements as unified wholes.",
        "principles": {
            "Similarity": "Similar elements grouped together",
            "Proximity": "Close elements seen as group",
            "Continuity": "Eyes follow paths",
            "Closure": "Mind completes incomplete shapes",
            "Figure-Ground": "Distinguish foreground from background"
        }
    },
    
    # ============================================
    # UI/UX DESIGN
    # ============================================
    "ui_design": {
        "category": "Design",
        "definition": "UI (User Interface) Design focuses on visual elements.",
        "elements": ["Buttons", "Icons", "Colors", "Typography", "Spacing", "Forms"],
        "tools": ["Figma", "Sketch", "Adobe XD", "Framer"]
    },
    "ux_design": {
        "category": "Design",
        "definition": "UX (User Experience) Design focuses on overall user journey.",
        "process": ["Research", "Wireframes", "Prototyping", "Testing", "Iteration"],
        "goal": "Make products useful, usable, and delightful"
    },
    "wireframe": {
        "category": "Design",
        "definition": "Wireframe adalah low-fidelity layout sketch.",
        "purpose": "Plan structure before visual design",
        "fidelity": ["Low-fi (sketches)", "Mid-fi (basic shapes)", "High-fi (detailed)"]
    },
    "prototype": {
        "category": "Design",
        "definition": "Prototype adalah interactive model of product.",
        "tools": ["Figma", "InVision", "Principle", "ProtoPie"],
        "purpose": "Test interactions before development"
    },
    "user_persona": {
        "category": "Design",
        "definition": "User persona adalah fictional representation of target user.",
        "includes": ["Demographics", "Goals", "Pain points", "Behaviors"],
        "purpose": "Keep design user-centered"
    },
    "usability_testing": {
        "category": "Design",
        "definition": "Testing product dengan real users untuk find issues.",
        "methods": ["Moderated", "Unmoderated", "A/B testing", "Card sorting"],
        "rule": "5 users find 85% of usability problems"
    },
    "accessibility_design": {
        "category": "Design",
        "definition": "Making design usable untuk people with disabilities.",
        "wcag": "Web Content Accessibility Guidelines",
        "considerations": ["Color contrast", "Keyboard navigation", "Screen readers", "Alt text"]
    },
    "responsive_design": {
        "category": "Design",
        "definition": "Design yang adapts ke different screen sizes.",
        "approach": ["Mobile first", "Fluid grids", "Flexible images", "Media queries"],
        "breakpoints": "Common: 320, 768, 1024, 1440px"
    },
    "design_system": {
        "category": "Design",
        "definition": "Collection of reusable components dan standards.",
        "includes": ["Colors", "Typography", "Components", "Patterns", "Guidelines"],
        "examples": ["Material Design (Google)", "Human Interface Guidelines (Apple)", "Carbon (IBM)"]
    },
    
    # ============================================
    # ART MOVEMENTS
    # ============================================
    "renaissance_art": {
        "category": "Art",
        "definition": "Renaissance art (14-17th century) emphasized realism dan classical ideals.",
        "artists": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Botticelli"],
        "works": ["Mona Lisa", "Sistine Chapel", "The Birth of Venus"]
    },
    "impressionism": {
        "category": "Art",
        "definition": "Impressionism captures light dan momentary effects.",
        "era": "1860s-1880s, France",
        "artists": ["Monet", "Renoir", "Degas", "Manet"],
        "characteristics": "Visible brushstrokes, light colors, ordinary subjects"
    },
    "cubism": {
        "category": "Art",
        "definition": "Cubism shows objects from multiple viewpoints simultaneously.",
        "founders": ["Pablo Picasso", "Georges Braque"],
        "era": "Early 1900s",
        "characteristics": "Geometric shapes, fragmented forms"
    },
    "surrealism": {
        "category": "Art",
        "definition": "Surrealism explores unconscious mind and dreams.",
        "artists": ["Salvador Dalí", "René Magritte", "Max Ernst"],
        "works": ["The Persistence of Memory", "The Son of Man"]
    },
    "pop_art": {
        "category": "Art",
        "definition": "Pop art uses imagery from popular culture.",
        "era": "1950s-1960s",
        "artists": ["Andy Warhol", "Roy Lichtenstein", "Keith Haring"],
        "works": ["Campbell's Soup Cans", "Marilyn Diptych"]
    },
    "minimalism_art": {
        "category": "Art",
        "definition": "Minimalism strips art to essential elements.",
        "philosophy": "Less is more",
        "artists": ["Donald Judd", "Dan Flavin", "Agnes Martin"]
    },
    "street_art": {
        "category": "Art",
        "definition": "Art created di public spaces.",
        "forms": ["Graffiti", "Murals", "Stencils", "Wheat-pasting"],
        "artists": ["Banksy", "Keith Haring", "Jean-Michel Basquiat"]
    },
    
    # ============================================
    # PHOTOGRAPHY
    # ============================================
    "photography_basics": {
        "category": "Photography",
        "definition": "Fundamental concepts dalam photography.",
        "exposure_triangle": ["Aperture", "Shutter Speed", "ISO"],
        "focus": "Sharp subject vs blurred background"
    },
    "aperture": {
        "category": "Photography",
        "definition": "Aperture adalah opening in lens yang controls light.",
        "f_stop": "Lower f-number = wider opening = more light",
        "depth_of_field": "Wide aperture (f/1.8) = shallow DoF (blurred background)"
    },
    "shutter_speed": {
        "category": "Photography",
        "definition": "Shutter speed adalah how long sensor exposed to light.",
        "fast": "1/1000s freezes action",
        "slow": "1s+ creates motion blur, needs tripod"
    },
    "iso": {
        "category": "Photography",
        "definition": "ISO adalah sensor sensitivity to light.",
        "low_iso": "100-400, clean image, needs more light",
        "high_iso": "1600+, brighter but more noise/grain"
    },
    "composition_photo": {
        "category": "Photography",
        "definition": "How elements are arranged in frame.",
        "techniques": ["Rule of thirds", "Leading lines", "Framing", "Symmetry", "Golden ratio"]
    },
    
    # ============================================
    # VIDEO & FILM
    # ============================================
    "frame_rate": {
        "category": "Video",
        "definition": "Frame rate adalah number of images shown per second.",
        "common": {
            "24fps": "Cinematic (film standard)",
            "30fps": "TV, web video",
            "60fps": "Sports, gaming",
            "120fps+": "Slow motion"
        }
    },
    "resolution": {
        "category": "Video",
        "definition": "Resolution adalah number of pixels in video.",
        "common": {
            "720p": "1280x720 (HD)",
            "1080p": "1920x1080 (Full HD)",
            "4K": "3840x2160 (Ultra HD)",
            "8K": "7680x4320"
        }
    },
    "aspect_ratio": {
        "category": "Video",
        "definition": "Aspect ratio adalah width to height relationship.",
        "common": {
            "16:9": "Standard widescreen",
            "4:3": "Old TV format",
            "21:9": "Ultrawide/Cinema",
            "9:16": "Vertical/Mobile (TikTok, Reels)",
            "1:1": "Square (Instagram)"
        }
    },
    "cinematography": {
        "category": "Film",
        "definition": "Art of visual storytelling through camera work.",
        "elements": ["Shot composition", "Camera movement", "Lighting", "Color grading"],
        "shots": ["Wide", "Medium", "Close-up", "POV", "Over-the-shoulder"]
    },
    
    # ============================================
    # MUSIC THEORY
    # ============================================
    "music_notes": {
        "category": "Music",
        "definition": "Musical notes represent pitches.",
        "notes": ["C", "D", "E", "F", "G", "A", "B"],
        "sharps_flats": "# raises, ♭ lowers by half step"
    },
    "chord": {
        "category": "Music",
        "definition": "Chord adalah 3+ notes played together.",
        "types": {
            "Major": "Happy sound (C-E-G)",
            "Minor": "Sad sound (C-E♭-G)",
            "7th": "Jazzy (adds 7th note)"
        }
    },
    "tempo": {
        "category": "Music",
        "definition": "Tempo adalah speed of music (BPM).",
        "ranges": {
            "Largo": "40-60 BPM (very slow)",
            "Andante": "76-108 BPM (walking pace)",
            "Allegro": "120-168 BPM (fast)",
            "Presto": "168-200 BPM (very fast)"
        }
    },
    "time_signature": {
        "category": "Music",
        "definition": "Time signature menunjukkan beats per measure.",
        "common": {
            "4/4": "Common time (most pop music)",
            "3/4": "Waltz time",
            "6/8": "Compound duple"
        }
    },
    "music_production": {
        "category": "Music",
        "definition": "Creating music dengan technology.",
        "daws": ["Ableton Live", "FL Studio", "Logic Pro", "Pro Tools"],
        "elements": ["Arrangement", "Mixing", "Mastering"]
    },
}
