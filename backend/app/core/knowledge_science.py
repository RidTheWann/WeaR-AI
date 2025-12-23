"""
WeaR AI Knowledge - Science, Nature, Space & Physics
Pengetahuan tentang sains, alam semesta, fisika, biologi, dan kimia.
Created by RidTheWann
"""

KNOWLEDGE_SCIENCE = {
    # ============================================
    # SPACE & ASTRONOMY
    # ============================================
    "black_hole": {
        "category": "Space",
        "definition": "Black hole adalah region di space dimana gravity begitu kuat, tidak ada yang bisa escape termasuk cahaya.",
        "types": ["Stellar (collapsed star)", "Supermassive (galaxy centers)", "Intermediate"],
        "event_horizon": "Point of no return",
        "first_image": "M87* oleh Event Horizon Telescope (2019)"
    },
    "big_bang": {
        "category": "Cosmology",
        "definition": "Big Bang adalah teori bahwa universe bermula dari singularity ~13.8 billion years ago.",
        "evidence": ["Cosmic microwave background", "Redshift of galaxies", "Abundance of elements"],
        "not": "Bukan explosion di space, tapi expansion OF space"
    },
    "dark_matter": {
        "category": "Physics",
        "definition": "Dark matter adalah materi tak kasat mata yang tidak berinteraksi dengan cahaya tapi memiliki gravitational effects.",
        "evidence": "Galaxy rotation curves, gravitational lensing",
        "composition": "~27% of universe, identity unknown"
    },
    "dark_energy": {
        "category": "Physics",
        "definition": "Dark energy adalah mysterious force yang menyebabkan expansion of universe accelerating.",
        "composition": "~68% of universe",
        "mystery": "Completely unknown what it is"
    },
    "milky_way": {
        "category": "Space",
        "definition": "Milky Way adalah galaxy kita, barred spiral galaxy dengan 100-400 billion stars.",
        "diameter": "~100,000 light-years",
        "black_hole": "Sagittarius A* di center (4 million solar masses)"
    },
    "sun": {
        "category": "Space",
        "definition": "Matahari adalah bintang di pusat tata surya kita.",
        "type": "G-type main-sequence star (Yellow Dwarf)",
        "age": "~4.6 billion years old",
        "composition": "Mostly hydrogen (73%) and helium (25%)",
        "temperature": "Core: 15 million °C, Surface: 5,500 °C"
    },
    "moon": {
        "category": "Space",
        "definition": "Bulan adalah natural satellite Bumi.",
        "formation": "Giant impact hypothesis (Theia collision)",
        "phases": ["New Moon", "First Quarter", "Full Moon", "Last Quarter"],
        "first_landing": "Apollo 11, Neil Armstrong (1969)"
    },
    "mars": {
        "category": "Space",
        "definition": "Mars adalah planet keempat dari Matahari, dikenal sebagai Red Planet.",
        "color": "Merah karena iron oxide (rust)",
        "moons": "Phobos dan Deimos",
        "missions": ["Perseverance rover", "InSight", "Hope orbiter"]
    },
    "jupiter": {
        "category": "Space",
        "definition": "Jupiter adalah planet terbesar di tata surya, gas giant.",
        "great_red_spot": "Storm yang sudah ada 400+ tahun",
        "moons": "79+ moons, including Ganymede (largest moon in solar system)",
        "mass": "2.5x massa semua planet lain combined"
    },
    "exoplanet": {
        "category": "Space",
        "definition": "Exoplanet adalah planet di luar tata surya kita.",
        "discovered": "5,000+ confirmed exoplanets",
        "methods": "Transit method, Radial velocity, Direct imaging",
        "habitable_zone": "Goldilocks zone untuk potential life"
    },
    "light_year": {
        "category": "Space",
        "definition": "Light year adalah jarak yang ditempuh cahaya dalam satu tahun.",
        "distance": "9.46 trillion kilometers",
        "nearest_star": "Proxima Centauri: 4.24 light years"
    },
    "supernova": {
        "category": "Space",
        "definition": "Supernova adalah explosion bintang yang extremely luminous.",
        "types": ["Type Ia (white dwarf)", "Type II (core collapse)"],
        "creates": "Heavy elements (gold, uranium, etc.)"
    },
    "neutron_star": {
        "category": "Space",
        "definition": "Neutron star adalah collapsed core of massive star, extremely dense.",
        "density": "1 sendok teh = 6 billion tons",
        "pulsar": "Rotating neutron star yang emit radiation beams"
    },
    "telescope": {
        "category": "Space",
        "definition": "Telescope adalah instrument untuk observing distant objects.",
        "types": ["Optical", "Radio", "X-ray", "Infrared"],
        "famous": ["Hubble Space Telescope", "James Webb Space Telescope", "VLT"]
    },
    "james_webb": {
        "category": "Space",
        "definition": "James Webb Space Telescope adalah next-gen infrared telescope.",
        "launched": "December 2021",
        "location": "L2 Lagrange point (1.5 million km from Earth)",
        "mirror": "6.5 meter primary mirror (gold-coated beryllium)"
    },
    "spacex": {
        "category": "Space",
        "definition": "SpaceX adalah private space company founded by Elon Musk.",
        "achievements": ["Reusable rockets", "Falcon 9", "Dragon capsule", "Starlink"],
        "goal": "Mars colonization"
    },
    "nasa": {
        "category": "Space",
        "definition": "NASA adalah US government space agency.",
        "founded": "1958",
        "missions": ["Apollo", "Shuttle", "ISS", "Mars rovers", "Voyager", "Artemis"]
    },
    "international_space_station": {
        "category": "Space",
        "definition": "ISS adalah modular space station di low Earth orbit.",
        "partners": "NASA, Roscosmos, ESA, JAXA, CSA",
        "orbit": "~400 km altitude, 90 minutes per orbit",
        "continuous_occupation": "Since November 2000"
    },
    "satellite": {
        "category": "Space",
        "definition": "Satellite adalah object yang orbits larger body, baik natural atau artificial.",
        "types": ["Communication", "Weather", "GPS", "Spy", "Science"],
        "first_artificial": "Sputnik 1 (1957)"
    },
    
    # ============================================
    # PHYSICS
    # ============================================
    "relativity": {
        "category": "Physics",
        "definition": "Teori Relativitas Einstein mendeskripsikan hubungan space, time, gravity, dan speed of light.",
        "special_relativity": "E=mc², time dilation, length contraction",
        "general_relativity": "Gravity adalah curvature of spacetime"
    },
    "quantum_mechanics": {
        "category": "Physics",
        "definition": "Quantum mechanics adalah teori yang describe behavior pada atomic dan subatomic level.",
        "principles": ["Wave-particle duality", "Uncertainty principle", "Superposition", "Entanglement"],
        "applications": "Transistors, lasers, MRI, quantum computing"
    },
    "schrodinger_cat": {
        "category": "Physics",
        "definition": "Schrödinger's cat adalah thought experiment tentang quantum superposition.",
        "concept": "Cat di box simultaneously dead AND alive sampai observed",
        "real_meaning": "Illustrates absurdity of Copenhagen interpretation di macro scale"
    },
    "speed_of_light": {
        "category": "Physics",
        "definition": "Speed of light (c) adalah kecepatan maximum di universe.",
        "value": "299,792,458 m/s (~300,000 km/s)",
        "significance": "Nothing with mass can reach it"
    },
    "gravity": {
        "category": "Physics",
        "definition": "Gravitasi adalah force attraction antara objects dengan massa.",
        "newton": "F = G(m1*m2)/r²",
        "einstein": "Curvature of spacetime caused by mass"
    },
    "entropy": {
        "category": "Physics",
        "definition": "Entropy adalah measure of disorder dalam system.",
        "second_law": "Entropy of isolated system always increases",
        "example": "Ice melting, heat spreading evenly"
    },
    "thermodynamics": {
        "category": "Physics",
        "definition": "Thermodynamics adalah study of heat, energy, dan work.",
        "laws": [
            "0th: Thermal equilibrium",
            "1st: Conservation of energy",
            "2nd: Entropy increases",
            "3rd: Absolute zero unreachable"
        ]
    },
    "electromagnetic_spectrum": {
        "category": "Physics",
        "definition": "EM spectrum adalah range semua types of electromagnetic radiation.",
        "order": "Radio → Microwave → Infrared → Visible → UV → X-ray → Gamma",
        "visible_light": "400-700 nm wavelength"
    },
    "atom": {
        "category": "Physics/Chemistry",
        "definition": "Atom adalah unit terkecil of matter yang retain element properties.",
        "components": ["Protons (positive)", "Neutrons (neutral)", "Electrons (negative)"],
        "model": "Nucleus (protons+neutrons) + electron cloud"
    },
    "particle_physics": {
        "category": "Physics",
        "definition": "Particle physics study fundamental particles dan forces.",
        "standard_model": "Theory describing fundamental particles",
        "particles": ["Quarks", "Leptons (electrons)", "Bosons (force carriers)", "Higgs boson"]
    },
    "higgs_boson": {
        "category": "Physics",
        "definition": "Higgs boson adalah particle yang memberikan mass ke other particles.",
        "nickname": "God particle",
        "discovered": "2012 at CERN (Large Hadron Collider)"
    },
    "nuclear_energy": {
        "category": "Physics",
        "definition": "Nuclear energy berasal dari splitting (fission) atau combining (fusion) atomic nuclei.",
        "fission": "Uranium/Plutonium splitting (current reactors)",
        "fusion": "Hydrogen combining (sun, future reactors)"
    },
    
    # ============================================
    # CHEMISTRY
    # ============================================
    "periodic_table": {
        "category": "Chemistry",
        "definition": "Periodic table adalah arrangement of chemical elements by atomic number.",
        "elements": "118 confirmed elements",
        "groups": "Alkali metals, Noble gases, Halogens, Transition metals, etc."
    },
    "h2o": {
        "category": "Chemistry",
        "definition": "H₂O adalah rumus kimia air (2 hydrogen + 1 oxygen).",
        "properties": ["Universal solvent", "High heat capacity", "Expands when frozen"],
        "states": "Solid (ice), Liquid (water), Gas (steam)"
    },
    "carbon": {
        "category": "Chemistry",
        "definition": "Carbon adalah element basis kehidupan.",
        "atomic_number": "6",
        "allotropes": ["Diamond", "Graphite", "Graphene", "Fullerenes", "Carbon nanotubes"]
    },
    "photosynthesis": {
        "category": "Biology/Chemistry",
        "definition": "Photosynthesis adalah proses plants convert sunlight menjadi energy.",
        "equation": "6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂",
        "location": "Chloroplasts (chlorophyll)"
    },
    "ph_scale": {
        "category": "Chemistry",
        "definition": "pH scale mengukur acidity atau alkalinity dari solution.",
        "range": "0-14 (0 = acidic, 7 = neutral, 14 = basic)",
        "examples": "Lemon juice ~2, Water 7, Bleach ~12"
    },
    "chemical_reaction": {
        "category": "Chemistry",
        "definition": "Chemical reaction adalah transformation reactants menjadi products.",
        "types": ["Synthesis", "Decomposition", "Combustion", "Oxidation-reduction"]
    },
    "oxidation": {
        "category": "Chemistry",
        "definition": "Oxidation adalah kehilangan electrons (rusting, burning).",
        "mnemonic": "OIL RIG - Oxidation Is Loss, Reduction Is Gain"
    },
    
    # ============================================
    # BIOLOGY
    # ============================================
    "dna": {
        "category": "Biology",
        "definition": "DNA (Deoxyribonucleic Acid) adalah molecule yang carries genetic information.",
        "structure": "Double helix dengan base pairs (A-T, G-C)",
        "location": "Cell nucleus (mostly)",
        "discoverers": "Watson, Crick, Franklin, Wilkins"
    },
    "rna": {
        "category": "Biology",
        "definition": "RNA (Ribonucleic Acid) adalah molecule yang helps translate DNA ke protein.",
        "types": ["mRNA (messenger)", "tRNA (transfer)", "rRNA (ribosomal)"]
    },
    "cell": {
        "category": "Biology",
        "definition": "Cell adalah basic structural unit of life.",
        "types": ["Prokaryotic (no nucleus - bacteria)", "Eukaryotic (nucleus - plants/animals)"],
        "organelles": ["Nucleus", "Mitochondria", "Ribosomes", "ER", "Golgi"]
    },
    "mitochondria": {
        "category": "Biology",
        "definition": "Mitochondria adalah 'powerhouse of the cell' yang produce ATP (energy).",
        "meme": "THE MITOCHONDRIA IS THE POWERHOUSE OF THE CELL",
        "origin": "Endosymbiotic theory - dari ancient bacteria"
    },
    "evolution": {
        "category": "Biology",
        "definition": "Evolution adalah proses perubahan species over generations through natural selection.",
        "darwin": "Charles Darwin - Origin of Species (1859)",
        "mechanisms": ["Natural selection", "Mutation", "Genetic drift", "Gene flow"]
    },
    "natural_selection": {
        "category": "Biology",
        "definition": "Natural selection: organisms dengan favorable traits more likely survive dan reproduce.",
        "survival_of_the_fittest": "Not physically strongest, but best adapted",
        "example": "Peppered moths during Industrial Revolution"
    },
    "ecosystem": {
        "category": "Biology",
        "definition": "Ecosystem adalah community of organisms dan their physical environment.",
        "components": ["Biotic (living)", "Abiotic (non-living)"],
        "types": ["Forest", "Desert", "Ocean", "Grassland", "Tundra"]
    },
    "food_chain": {
        "category": "Biology",
        "definition": "Food chain menunjukkan flow of energy dari producers ke consumers.",
        "levels": ["Producers (plants)", "Primary consumers (herbivores)", "Secondary (carnivores)", "Decomposers"],
        "energy_transfer": "Only ~10% energy transfers to next level"
    },
    "biodiversity": {
        "category": "Biology",
        "definition": "Biodiversity adalah variety of life forms dalam ekosistem.",
        "importance": "Ecosystem stability, medicine sources, food security",
        "threats": "Habitat loss, climate change, pollution"
    },
    "virus": {
        "category": "Biology",
        "definition": "Virus adalah infectious agent yang replicate inside living cells.",
        "structure": "Genetic material (DNA/RNA) + protein coat",
        "not_alive": "Cannot reproduce without host cell",
        "examples": ["COVID-19", "Influenza", "HIV", "Rabies"]
    },
    "bacteria": {
        "category": "Biology",
        "definition": "Bacteria adalah single-celled prokaryotic organisms.",
        "types": ["Beneficial (gut flora)", "Pathogenic (cause disease)"],
        "shapes": ["Cocci (spheres)", "Bacilli (rods)", "Spirilla (spirals)"]
    },
    "immune_system": {
        "category": "Biology",
        "definition": "Immune system adalah defense mechanism tubuh melawan pathogens.",
        "components": ["White blood cells", "Antibodies", "Lymph nodes", "Spleen"],
        "types": ["Innate (general)", "Adaptive (specific)"]
    },
    "vaccine": {
        "category": "Biology/Medicine",
        "definition": "Vaccine train immune system untuk recognize dan fight pathogens.",
        "types": ["Live attenuated", "Inactivated", "mRNA", "Viral vector"],
        "herd_immunity": "Majority vaccination protects unvaccinated"
    },
    "brain": {
        "category": "Biology",
        "definition": "Brain adalah organ yang control thoughts, memory, emotions, dan bodily functions.",
        "neurons": "~86 billion neurons",
        "parts": ["Cerebrum", "Cerebellum", "Brainstem"],
        "weight": "~1.4 kg (average adult)"
    },
    "human_body": {
        "category": "Biology",
        "definition": "Human body memiliki complex systems yang work together.",
        "systems": ["Circulatory", "Respiratory", "Digestive", "Nervous", "Skeletal", "Muscular"],
        "facts": ["206 bones", "600+ muscles", "100 trillion cells"]
    },
    
    # ============================================
    # EARTH SCIENCE
    # ============================================
    "climate_change": {
        "category": "Earth Science",
        "definition": "Climate change adalah long-term shifts dalam temperatures dan weather patterns.",
        "causes": "Primarily human activities (fossil fuels, deforestation)",
        "effects": ["Rising temperatures", "Sea level rise", "Extreme weather", "Biodiversity loss"],
        "solution": "Reduce emissions, renewable energy, reforestation"
    },
    "greenhouse_effect": {
        "category": "Earth Science",
        "definition": "Greenhouse effect adalah trapping of heat oleh gases di atmosphere.",
        "gases": ["CO₂", "Methane", "Nitrous oxide", "Water vapor"],
        "natural": "Necessary for life, problem adalah enhanced greenhouse effect"
    },
    "tectonic_plates": {
        "category": "Geology",
        "definition": "Tectonic plates adalah massive slabs of Earth's lithosphere yang move.",
        "movement": "Convection currents dalam mantle",
        "results": "Earthquakes, volcanoes, mountains"
    },
    "earthquake": {
        "category": "Geology",
        "definition": "Earthquake adalah shaking ground dari sudden release of energy di Earth's crust.",
        "measurement": "Richter scale atau Moment magnitude scale",
        "terms": ["Epicenter (surface point)", "Hypocenter/Focus (origin point)"]
    },
    "volcano": {
        "category": "Geology",
        "definition": "Volcano adalah opening di Earth's surface dimana lava, gas, dan ash escape.",
        "types": ["Shield", "Stratovolcano", "Cinder cone"],
        "ring_of_fire": "Pacific rim dengan 75% of world's volcanoes"
    },
    "ocean": {
        "category": "Earth Science",
        "definition": "Oceans cover 71% of Earth's surface dan contain 97% of water.",
        "oceans": ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"],
        "deepest": "Mariana Trench (~11,000 meters)"
    },
    "water_cycle": {
        "category": "Earth Science",
        "definition": "Water cycle mendeskripsikan continuous movement of water.",
        "stages": ["Evaporation", "Condensation", "Precipitation", "Collection"],
        "driven_by": "Solar energy"
    },
    "atmosphere": {
        "category": "Earth Science",
        "definition": "Atmosphere adalah layer of gases surrounding Earth.",
        "layers": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere", "Exosphere"],
        "composition": "78% Nitrogen, 21% Oxygen, 1% other"
    },
    "renewable_energy": {
        "category": "Energy",
        "definition": "Renewable energy berasal dari naturally replenishing sources.",
        "types": ["Solar", "Wind", "Hydroelectric", "Geothermal", "Biomass"],
        "benefits": "Sustainable, low emissions, energy independence"
    },
    
    # ============================================
    # MATHEMATICS
    # ============================================
    "pi": {
        "category": "Mathematics",
        "definition": "Pi (π) adalah ratio circumference circle ke diameter-nya.",
        "value": "3.14159265358979323846...",
        "irrational": "Decimal never ends or repeats",
        "pi_day": "March 14 (3/14)"
    },
    "infinity": {
        "category": "Mathematics",
        "definition": "Infinity (∞) adalah concept of something without any limit.",
        "fun_fact": "Some infinities are larger than others (Cantor)",
        "symbol": "∞ (lemniscate)"
    },
    "prime_numbers": {
        "category": "Mathematics",
        "definition": "Prime numbers hanya bisa divided by 1 dan itself.",
        "first_primes": "2, 3, 5, 7, 11, 13, 17, 19, 23...",
        "fact": "2 adalah satu-satunya even prime number",
        "use": "Cryptography (RSA)"
    },
    "fibonacci_sequence": {
        "category": "Mathematics",
        "definition": "Fibonacci sequence: setiap number adalah sum of two preceding ones.",
        "sequence": "0, 1, 1, 2, 3, 5, 8, 13, 21, 34...",
        "nature": "Found in spirals (sunflowers, shells, galaxies)"
    },
    "golden_ratio": {
        "category": "Mathematics",
        "definition": "Golden ratio (φ) ≈ 1.618, found dalam nature dan art.",
        "formula": "(a+b)/a = a/b = φ",
        "appearances": "Spiral shells, art composition, architecture"
    },
    "pythagorean_theorem": {
        "category": "Mathematics",
        "definition": "Dalam right triangle: a² + b² = c² (c adalah hypotenuse).",
        "example": "3² + 4² = 5² (3-4-5 triangle)"
    },
    "algebra": {
        "category": "Mathematics",
        "definition": "Algebra menggunakan symbols untuk represent numbers dan relationships.",
        "example": "Solve for x: 2x + 3 = 7 → x = 2"
    },
    "calculus": {
        "category": "Mathematics",
        "definition": "Calculus adalah study of change (derivatives) dan accumulation (integrals).",
        "founders": "Newton dan Leibniz (independently)",
        "applications": "Physics, engineering, economics"
    },
    "statistics": {
        "category": "Mathematics",
        "definition": "Statistics adalah science of collecting dan analyzing data.",
        "concepts": ["Mean", "Median", "Mode", "Standard deviation", "Probability"]
    },
    "probability": {
        "category": "Mathematics",
        "definition": "Probability mengukur likelihood of event occurring.",
        "range": "0 (impossible) to 1 (certain)",
        "example": "Coin flip: P(heads) = 0.5"
    },
}
