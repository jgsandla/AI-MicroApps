PUBLISHED = True
APP_URL = "https://microapp-demo1.streamlit.app"

APP_TITLE = "Basic Prototype of Course Recommender System"
APP_INTRO = """This app uses ChatGPT to recommend a course to a student. To do this, we provide ChatGPT with information about our courses as well as answers that the student provides to a series of questions.
"""



SHARED_ASSET = {
}



SYSTEM_PROMPT = """You are helping the user select a class. Based on their goals, backgrounds, and previous course history, make a suggestion as to the next class the user should take.  Be polite and friendly. The list of all available courses is available at https://www.dropbox.com/scl/fi/ixywhox3fjw5691mccbqa/MSE-Courses.pdf?rlkey=dl9i8nszaflubk4f1wmsv3o3d&st=tvdornrw&dl=0 Please base your advice on this document."""

SYSTEM_PROMPT = """Here is the course information that you will need to base your course recommendations on.  Only recommend courses outlined in this document or prerequisite courses that would allow the student to take one of the outlined courses.


Course title: Thermodynamics of Materials

Prerequisites: Chemistry, Calculus

Learning goals: Thermodynamics of Materials is an online course that introduces you to the laws of thermodynamics and the concepts of equilibrium and thermodynamic potentials, and teaches you how to apply these ideas to solve materials science and engineering problems. Learn how to use materials data, computational techniques, and thermodynamics software for materials selection, process design, predictions, and more.  With an emphasis on classical thermodynamics, this course will teach you both classical and statistical interpretations of entropy, as well as the concept of constrained equilibrium, the mathematical structure of classical thermodynamics, and free energy-composition diagrams that underpin binary phase diagrams.
Syllabus:
Topic 1: Equilibrium
•	Introduction to thermodynamics: enthalpy, entropy, and an atomic view
•	Systems, states, and material properties
•	Processes and the First Law of Thermodynamics
•	Irreversible processes, the Second Law of Thermodynamics, and equilibrium
•	The combined statement and differential forms
•	Equilibrium conditions
Topic 2: Phase Diagrams
•	Unary systems and phase diagrams
•	Systems of reacting gases
•	Introduction to binary phase diagrams
•	The lever rule
•	Partial molar properties and the common tangent construction
•	Heterogeneous binary systems and ideal solutions
•	Non-ideal solutions: Dilute and regular models
•	Heterogeneous binary systems: Gibbs phase rule; eutectic, and peritectic reactions
•	Reference states
•	Intermediate phases and line compounds
•	Ternary phase diagrams
•	Reacting systems: Metal oxidation
Topic 3: Foundations
•	Clausius’ statement and the Carnot efficiency limit
•	Reversible and irreversible heat engines
•	Introduction to statistical thermodynamics
Format: Online course
Course Title: Electronic, Optical and Magnetic Properties of Materials
Prerequisites: Calculus, Physics Electricity and Magnetism, Chemistry

Learning Goals: This course from MIT’s Department of Materials Science and Engineering introduces the fundamental principles of quantum mechanics, solid state physics, and electricity and magnetism. We use these principles to describe the origins of the electronic, optical, and magnetic properties of materials, and we discuss how these properties can be engineered to suit particular applications, including diodes, optical fibers, LEDs, and solar cells.

In this course, you will find out how the speed of sound is connected to the electronic band gap, what the difference is between a metal and a semiconductor, and how many magnetic domains fit in a nanoparticle. You will explore a wide range of topics in the domains of materials engineering, quantum mechanics, solid state physics that are essential for any engineer or scientist who wants to gain a fuller understanding of the principles underlying modern electronics.

Syllabus:  We don’t have a syllabus for this course

Format: Online course


Course Title: Cellular Solids

Prerequisites:  Mechanical Behavior of Materials or similar

Learning Goals: In this engineering course, we will explore the processing and structure of cellular solids as they are created from polymers, metals, ceramics, glasses and composites.

We will begin the course by deriving models for the mechanical properties of honeycombs and foams, and we will discover how the unique properties of these materials can be exploited in applications such as lightweight structural panels, energy absorption devices, and thermal insulation.
Next, we will explore cellular solids in medicine, including trabecular bone mechanics, the increased risk of bone fracture due to trabecular bone loss in patients with osteoporosis, the development of metal foam coatings for orthopedic implants, applying foam models to tissue engineering scaffolds and the design of a porous scaffold for tissue engineering that mimics the body's own extracellular matrix.
Finally, we will explore sandwich structures and cellular solids that occur in nature, and we will consider examples of engineering design inspired by natural materials.
Syllabus: Not available

Course Title: Mechanical Behavior of Materials

Prerequisites: Classical mechanics, Chemistry, Calculus

Learning Goals: The 3.032x series provides an introduction to the mechanical behavior of materials, from both the continuum and atomistic points of view. At the continuum level, we learn how forces and displacements translate into stress and strain distributions within the material. At the atomistic level, we learn the mechanisms that control the mechanical properties of materials. Examples are drawn from metals, ceramics, glasses, polymers, biomaterials, composites and cellular materials.
Part 1 covers stress-strain behavior, topics in linear elasticity and the atomic basis for linear elasticity, and composite materials.
Part 2 covers stress transformations, beam bending, column buckling, and cellular materials.
Part 3 covers viscoelasticity (behavior intermediate to that of an elastic solid and that of a viscous fluid), plasticity (permanent deformation), creep in crystalline materials (time dependent behavior), brittle fracture (rapid crack propagation) and fatigue (failure due to repeated loading of a material).
Syllabus: Not available

Format: Online course


Course Title: Microstructural Evolution of Materials

Prerequisites: Calculus, Structure of Materials, Thermodynamics

Learning Goals: A four-part series of online modules, Microstructural Evolution of Materials introduces various phenomena in various classes of materials. In this course, you will learn how materials develop different microstructures based on the processing technique used, and how these microstructures relate to the properties of the material.

Covering similar content to the MIT course 3.022: Microstructural Evolution of Materials, this online version is intended for undergraduate engineering and science students, as well as professionals, who are interested in materials statistics, kinetics, and microstructural transformations.

In this first module of a four-part series of online modules, you will get an introduction to important concepts in statistical mechanics that are especially relevant to materials scientists. Topics include solid solutions, the canonical ensemble, and heat capacity.

This second module focuses on point defect evolution, including diffusion, substitutional diffusion, ionic defects, and ionic conductivity.

This third module discusses surfaces and surface-driven reactions. Topics include surface energy, faceted and non-faceted growth, and growth and ripening.

This fourth module focuses on phase transformations, including nucleation and growth, precipitate growth, interface stability, and glass transition.

Syllabus: Not available

Format: Online course


Course Title: Organic and Biomaterials Chemistry, Part 1

Prerequisites: Chemistry, Calculus

Learning Goals: Organic and Biomaterials Chemistry is a self-paced online course that focuses on the chemistry and chemical structure-property relationships of soft synthetic and biologically derived materials.
Developed for engineers, scientists, and university-level STEM students interested in learning more about polymer, biomaterials, and organic chemistry from a materials science and engineering perspective, this course aims to help you develop a fundamental understanding of the molecular nature of materials.
This module is the first in a series of three modules based on the MIT course 3.034: Organic and Materials Chemistry. Part 1 of the course, An Introduction to Polymer Chemistry, will focus on methods for preparing synthetic polymers by step- and chain-growth polymerization, polymerization kinetics, and practical considerations of running a polymerization reaction.
Syllabus:  Not available

Format: Online course


Course Title: Structure of Materials

Prerequisites: Chemistry, Calculus

Learning Goals: Structure determines so much about a material: its properties, its potential applications, and its performance within those applications. This course from MIT’s Department of Materials Science and Engineering explores the structure of a wide variety of materials with current-day engineering applications.
The course begins with an introduction to amorphous materials. We explore glasses and polymers, learn about the factors that influence their structure, and learn how materials scientists measure and describe the structure of these materials.
Then we begin a discussion of the crystalline state, exploring what it means for a material to be crystalline, how we describe directions in a crystal, and how we can determine the structure of crystal through x-ray diffraction. We explore the underlying crystalline structures that underpin so many of the materials that surround us. Finally, we look at how tensors can be used to represent the properties of three-dimensional materials, and we consider how symmetry places constraints on the properties of materials.
We move on to an exploration of quasi-, plastic, and liquid crystals. Then, we learn about the point defects that are present in all crystals, and we will learn how the presence of these defects lead to diffusion in materials. Next, we will explore dislocations in materials. We will introduce the descriptors that we use to describe dislocations, we will learn about dislocation motion, and will consider how dislocations dramatically affect the strength of materials. Finally, we will explore how defects can be used to strengthen materials, and we will learn about the properties of higher-order defects such as stacking faults and grain boundaries.
Syllabus: Not available

Format: Online course


Course Title: The Iterative Innovation Process

Prerequisites: none

Learning goals: People innovate, not organizations. This course is for anybody who wants to understand the innovation process - whether you want to foster innovation within your organization or whether you want to personally innovate.
As practicing innovators, we teach you the fundamentals of how to think like an innovator. Innovation is an iterative process, not a linear one. When innovating, there are thousands of sources of uncertainty in Technology, Implementation, and Markets. We teach you how to cycle through these sources of uncertainty until the right pieces come together in an innovation.
Throughout the course, we build up the innovation process model step by step with real examples and exercises. The goal of this course is to change and refine the way you view the innovation process, providing you with the foundation on which to build your future innovation
Syllabus: Not available
Format: Online course

Structural Materials: Selection and Economics
Prerequisites: none
Learning goals: From skyscrapers to transportation infrastructure, structural materials dominate the human landscape. Learning the principles that govern their selection is essential for any aspiring or practicing engineer.
This engineering course will introduce you to the key principles of structural materials selection through a practical curriculum rooted in the real world. The principles taught are general enough to be applied across many domains. Key points are emphasized with interesting examples and anecdotes from industry and academia.
This course benefits aspiring engineers and students with no previous experience as well as the seasoned professional.
Syllabus: Lecture 1: Introduction to externalities of materials selection, comprising social, political, economic, military, cultural, environmental and other effects.
Lecture 2: Introduction to relationship between material cost, abundance and usage. Factors influencing availability such as energy density and recyclability are also discussed.
Lecture 3: Introduction to the properties of materials that influence use in structural applications. Discussion of ratio analysis using among other examples steel, aluminum, and titanium.
Lecture 4: Discusses manufacturing and processing factors that effect material choice in various applications. Introduction to causes of material failures.

Format: Online course


Course Title: Solid State Chemistry
Prerequisites: none
Learning goals: Introduction to Solid State Chemistry is a one-semester college course on the principles of chemistry. This unique and popular course satisfies MIT’s general chemistry degree requirement, with an emphasis on solid-state materials and their application to engineering systems. You’ll begin with an exploration of the fundamental relationship between electronic structure, chemical bonding, and atomic order, then proceed to the chemical properties of “aggregates of molecules,” including crystals, metals, glasses, semiconductors, solutions and acid-base equilibria, polymers, and biomaterials. Real-world examples are drawn from industrial practice (e.g. semiconductor manufacturing), energy generation and storage (e.g. automobile engines, lithium batteries), emerging technologies (e.g. photonic and biomedical devices), and the environmental impact of chemical processing (e.g. recycling glass, metal, and plastic).
•	Syllabus:  Foundations 
o	Structure of the Atom - The periodic table, elements and compounds, chemical formulas. Evolution of atomic theory: Thomson & Rutherford, Bohr model of hydrogen, Bohr-Sommerfeld model and multi-electron atoms, atomic spectra, Schrödinger equation. Electron orbitals: Aufbau principle, Pauli exclusion principle, and Hund’s rules.
	Sessions 1, 2, 3, 4, 5, 6, 7
o	Bonding and Molecules - Primary bonding: ionic, covalent, metallic. Secondary bonding: dipole-dipole, induced dipole-induced dipole, London dispersion/van der Waals, hydrogen. Shapes of molecules: hybridization, LCAO-MO, VSEPR theory.
	Sessions 8, 9, 10, 11, 12
o	Reactions and Kinetics - Reaction kinetics: rate laws, thermal activation, and the Arrhenius equation. Diffusion: Fick’s first and second laws.
	Sessions 22 (second part), 23, 24
•	Applications 
o	Electronic Materials - Band theory: metals, insulators, and semiconductors. Band gaps, doping, and devices.
	Sessions 13, 14, 15 (first part)
o	Crystalline Materials - Crystal structure: 7 crystal systems, 14 Bravais lattices, Miller indices. Properties of cubic crystals. X-ray diffraction. Defects: point, line, surface, bulk.
	Sessions 15 (second part), 16, 17, 18, 19, 20
o	Amorphous Materials - Inorganic glasses: silicates, other oxides, metallics.
	Sessions 21, 22 (first part)
o	Aqueous Solutions - Liquids and solutions: solubility rules, acids, bases, pH.
	Sessions 25, 26
o	Organic Materials - Organic compounds: nomenclature, alkanes, alkenes, alkynes, aromatics, functional groups. Polymers: structure, composition, synthesis and applications. Biochemistry: amino acids, peptides and proteins, lipids, nucleic acids, protein biosynthesis.
	Sessions 27, 28, 29, 30, 31, 32
o	Solid Solutions - Phase stability: unary and binary phase diagrams.
	Sessions 33, 34, 35
Format: Self-study

Course Title: Symmetry, Structure, and Tensor Properties of Materials
Prerequisites: Linear Algebra
Learning Goals: This course covers the derivation of symmetry theory; lattices, point groups, space groups, and their properties; use of symmetry in tensor representation of crystal properties, including anisotropy and representation surfaces; and applications to piezoelectricity and elasticity.
Format: Self-study

Course Title: Elecronic, Optical, and Magnetic Materials and Devices
Prerequisites: Electrical, Optical, and Magnetic Properties of Materials
Learning Goals: This course is a three-part series which explains the basis of the electrical, optical, and magnetic properties of materials including semiconductors, metals, organics, and insulators. We will show how devices are built to take advantage of these properties. This is illustrated with a wide range of devices, placing a strong emphasis on new and emerging technologies.
The first part of the course covers electronic materials and devices, including diodes, bipolar junction transistors, MOSFETs, and semiconductor properties. The second part covers optical materials and devices, including photodetectors, solar cells (photovoltaics), displays, light emitting diodes, lasers, optical fibers, optical communications, and photonic devices. The final part of the series covers magnetic materials and devices, including magnetic data storage, motors, transformers, and spintronics.
Format: Online course
Syllabus: not available







"""









PHASES = {

 
    "phase1": {
        "name": "Recommendation",
        "fields": {
            "student_query": {
                "type": "text_area",
                "height": 200,
                "label": """What would you like to learn about and why?""",
               
            },

        

          "more": {
                "type": "radio",
                "label": "Would you like to answer a few more questions that might help us make a better recommendation?",
                "options": ["No", "Yes"],
                
            },

        

        

          "background": {
                "type": "text_area",
                "height": 100,
                "label": """Tell us something about your academic and/or work background.  Questions you might want to answer: What is the highest level of education you've completed? In what field? What do you do professionally?""",
                "showIf": {"more": {"$eq": "Yes"}},
               
            },

        
            "Calculus": {
                "type": "radio",
                "options": ['Yes', 'No'],
                "label": "Have you taken Calculus?",
                "showIf": {"more": {"$eq": "Yes"}},
               
            }, 

           "Python": {
                "type": "radio",
                "options": ['Beginner', 'Intermediate', 'Advanced'],
                "label": "How would you rank your Python skills?",
                "showIf": {"more": {"$eq": "Yes"}},
               
            }, 

           "Self_study": {
                "type": "radio",
                "options": ['Please only recommend courses that are entirely online', 'Self-study works for me, too'],
                "label": "Some of our courses are entirely online, which allows you to take course assessments online. Others contain self-study materials that you would need to grade yourself.  Are you interested in self-study courses?",
                "showIf": {"more": {"$eq": "Yes"}},
                
            }, 


            "next_course": {
                "type": "radio",
                "label": "Have you already taken a course and are looking for a recommendation for the next course to take?",
                "options": ["No", "Yes"],
                 "showIf": {"more": {"$eq": "Yes"}},
               
            },

           "previous_course": {
                "type": "text_input",
                "label": """What was the name of the course?""",
                "showIf": {"next_course": {"$eq": "Yes"}}
       
            },

        },
        "phase_instructions": "Please recommend a course to the student. Please recommend only one course. If the student indicated that they are interested in online-only courses, please do not recommend courses where the Format includes self-study",
        "user_prompt": [
           
            {
                "condition": {"more": {"$eq": "No"}},
                "prompt": "Here is what I am interested in learning about: {student_query}"
            },
            {
                "condition": {"$and": [
                    {"more": "Yes"},
                    {"next_course": "No"}
                ]},
                "prompt": "Here is what I am interested in learning about: {student_query}  Here's some information about my academic and work background: {background}.  This is how I answered the question Have you taken Calculus? {Calculus}  This is how I answered the question How would you rank your Python skills? {Python} This is how I answered the queestion  Are you interested in self-study courses? {Self_study} "
            },

          {
                "condition": {"$and": [
                    {"more": "Yes"},
                    {"next_course": "Yes"}
                ]},
                "prompt": "Here is what I am interested in learning about: {student_query}  Here's some information about my academic and work background: {background}.  This is how I answered the question Have you taken Calculus? {Calculus}  This is how I answered the question How would you rank your Python skills? {Python} This is how I answered the queestion  Are you interested in self-study courses? {Self_study}.  I have already taken {previous_course}, and I am looking for a recommendation as to what course to take next. "
            },

            

         
        ],
        "allow_skip": True,
        "show_prompt": True
    },
    "phase2": {
        "name": "Revised Recommendation",
        "fields": {
             "revise_it": {
                "type": "radio",
                "label": "Are you happy with the recommendation, or would you like a revised recommendation?",
                "options": ["I'm happy", "Revise it"],
                
            },

         "revised_query": {
                "type": "text_area",
                "height": 200,
                "label": """Is there anything you would like us to know that might improve the recommendation?""",
                "showIf": {"revise_it": {"$eq": "Revise it"}}
               
            },
        },
        "phase_instructions": "The user will introduce their hobbies now, and I'll say what I like about one of those hobbies. ",
        "user_prompt": "{hobbies}",
        "allow_skip": True,
  
    },
 
   

}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Demo 1",
    "page_icon": "️🖥️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
