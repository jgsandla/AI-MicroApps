PUBLISHED = True
APP_URL = "https://microapp-demo1.streamlit.app"

APP_TITLE = "Basic Prototype of Course Recommender System"
APP_INTRO = """This app uses ChatGPT to recommend a course to a student. To do this, we provide ChatGPT with information about our courses as well as answers that the student provides to a series of questions.
"""

HTML_BUTTON = {
    "url":"https://www.dropbox.com/scl/fi/ixywhox3fjw5691mccbqa/MSE-Courses.pdf?rlkey=dl9i8nszaflubk4f1wmsv3o3d&st=fztczec8&dl=0",
    "button_text":"Hi!  Click here if you want to see the current course information this recommender is based off of."
}

SHARED_ASSET = {
}



SYSTEM_PROMPT = """You are helping the user select a class. Based on their goals, backgrounds, and previous course history, make a suggestion as to the next class the user should take.  Be polite and friendly. """

SYSTEM_PROMPT = """Here is the course information that you will need to base your course recommendations on.  Only recommend courses outlined in this document or prerequisite courses that would allow the student to take one of the outlined courses.


Course title: Thermodynamics of Materials

Thermodynamics of Materials Prerequisites: Chemistry, Calculus

Thermodynamics of Materials Learning goals: Thermodynamics of Materials is an online course that introduces you to the laws of thermodynamics and the concepts of equilibrium and thermodynamic potentials, and teaches you how to apply these ideas to solve materials science and engineering problems. Learn how to use materials data, computational techniques, and thermodynamics software for materials selection, process design, predictions, and more.  With an emphasis on classical thermodynamics, this course will teach you both classical and statistical interpretations of entropy, as well as the concept of constrained equilibrium, the mathematical structure of classical thermodynamics, and free energy-composition diagrams that underpin binary phase diagrams.
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
Thermodynamics of Materials Format: Online course
Thermodynamics of Materials Depth:  This is not a good course to begin with.  It is best recommended to students studying engineering at university or to students who have expressed direct interest in the topics covered in this course. If another course could meet the student's needs, consider recommending that one instead.
Thermodynamics of Materials Difficulty: This is a challenging course


Course Title: Electronic, Optical and Magnetic Properties of Materials
Electronic, Optical and Magnetic Properties of Materials Prerequisites: Calculus, Physics Electricity and Magnetism, Chemistry

Electronic, Optical and Magnetic Properties of Materials Learning Goals: This course from MIT’s Department of Materials Science and Engineering introduces the fundamental principles of quantum mechanics, solid state physics, and electricity and magnetism. We use these principles to describe the origins of the electronic, optical, and magnetic properties of materials, and we discuss how these properties can be engineered to suit particular applications, including diodes, optical fibers, LEDs, and solar cells.

In this course, you will find out how the speed of sound is connected to the electronic band gap, what the difference is between a metal and a semiconductor, and how many magnetic domains fit in a nanoparticle. You will explore a wide range of topics in the domains of materials engineering, quantum mechanics, solid state physics that are essential for any engineer or scientist who wants to gain a fuller understanding of the principles underlying modern electronics.

Electronic, Optical and Magnetic Properties of Materials Syllabus:  We don’t have a syllabus for this course

Electronic, Optical and Magnetic Properties of Materials Format: Online course


Electronic, Optical and Magnetic Properties of Materials Difficulty: This is a challenging course

Course Title: Cellular Solids

Cellular Solids Prerequisites:  Mechanical Behavior of Materials or similar

Cellular Solids Learning Goals: In this engineering course, we will explore the processing and structure of cellular solids as they are created from polymers, metals, ceramics, glasses and composites.

We will begin the course by deriving models for the mechanical properties of honeycombs and foams, and we will discover how the unique properties of these materials can be exploited in applications such as lightweight structural panels, energy absorption devices, and thermal insulation.
Next, we will explore cellular solids in medicine, including trabecular bone mechanics, the increased risk of bone fracture due to trabecular bone loss in patients with osteoporosis, the development of metal foam coatings for orthopedic implants, applying foam models to tissue engineering scaffolds and the design of a porous scaffold for tissue engineering that mimics the body's own extracellular matrix.
Finally, we will explore sandwich structures and cellular solids that occur in nature, and we will consider examples of engineering design inspired by natural materials.

Cellular Solids Syllabus: Not available

Cellular Solids Format: Online course

Course Title: Mechanical Behavior of Materials

Mechanical Behavior of Materials Prerequisites: Classical mechanics, Chemistry, Calculus

Mechanical Behavior of Materials Learning Goals: The 3.032x series provides an introduction to the mechanical behavior of materials, from both the continuum and atomistic points of view. At the continuum level, we learn how forces and displacements translate into stress and strain distributions within the material. At the atomistic level, we learn the mechanisms that control the mechanical properties of materials. Examples are drawn from metals, ceramics, glasses, polymers, biomaterials, composites and cellular materials.
Part 1 covers stress-strain behavior, topics in linear elasticity and the atomic basis for linear elasticity, and composite materials.
Part 2 covers stress transformations, beam bending, column buckling, and cellular materials.
Part 3 covers viscoelasticity (behavior intermediate to that of an elastic solid and that of a viscous fluid), plasticity (permanent deformation), creep in crystalline materials (time dependent behavior), brittle fracture (rapid crack propagation) and fatigue (failure due to repeated loading of a material).
Syllabus: Not available

Mechanical Behavior of Materials Format: Online course


Course Title: Microstructural Evolution of Materials

Microstructural Evolution of Materials Prerequisites: Calculus, Structure of Materials, Thermodynamics

Microstructural Evolution of Materials Learning Goals: A four-part series of online modules, Microstructural Evolution of Materials introduces various phenomena in various classes of materials. In this course, you will learn how materials develop different microstructures based on the processing technique used, and how these microstructures relate to the properties of the material.

Covering similar content to the MIT course 3.022: Microstructural Evolution of Materials, this online version is intended for undergraduate engineering and science students, as well as professionals, who are interested in materials statistics, kinetics, and microstructural transformations.

In this first module of a four-part series of online modules, you will get an introduction to important concepts in statistical mechanics that are especially relevant to materials scientists. Topics include solid solutions, the canonical ensemble, and heat capacity.

This second module focuses on point defect evolution, including diffusion, substitutional diffusion, ionic defects, and ionic conductivity.

This third module discusses surfaces and surface-driven reactions. Topics include surface energy, faceted and non-faceted growth, and growth and ripening.

This fourth module focuses on phase transformations, including nucleation and growth, precipitate growth, interface stability, and glass transition.

Microstructural Evolution of Materials Syllabus: Not available

Microstructural Evolution of Materials Format: Online course

Microstructural Evolution of Materials Depth:  This is not a good course to begin with.  It is best recommended to students studying engineering at university or to students who have expressed direct interest in the topics covered in this course, or to students who have completed Thermodynamics and are looking for a next course. If another course could meet the student's needs, consider recommending that one instead.

Microstructural Evolution of Materials Difficulty: This is a challenging course


Course Title: Organic and Biomaterials Chemistry, Part 1

Organic and Biomaterials Chemistry, Part 1 Prerequisites: Chemistry, Calculus

Learning Goals: Organic and Biomaterials Chemistry is a self-paced online course that focuses on the chemistry and chemical structure-property relationships of soft synthetic and biologically derived materials.
Developed for engineers, scientists, and university-level STEM students interested in learning more about polymer, biomaterials, and organic chemistry from a materials science and engineering perspective, this course aims to help you develop a fundamental understanding of the molecular nature of materials.
This module is the first in a series of three modules based on the MIT course 3.034: Organic and Materials Chemistry. Part 1 of the course, An Introduction to Polymer Chemistry, will focus on methods for preparing synthetic polymers by step- and chain-growth polymerization, polymerization kinetics, and practical considerations of running a polymerization reaction.

Organic and Biomaterials Chemistry, Part 1 Syllabus:  Not available

Organic and Biomaterials Chemistry, Part 1 Format: Online course


Course Title: Structure of Materials

Structure of Materials Prerequisites: Chemistry, Calculus

Structure of Materials Learning Goals: Structure determines so much about a material: its properties, its potential applications, and its performance within those applications. This course from MIT’s Department of Materials Science and Engineering explores the structure of a wide variety of materials with current-day engineering applications.
The course begins with an introduction to amorphous materials. We explore glasses and polymers, learn about the factors that influence their structure, and learn how materials scientists measure and describe the structure of these materials.
Then we begin a discussion of the crystalline state, exploring what it means for a material to be crystalline, how we describe directions in a crystal, and how we can determine the structure of crystal through x-ray diffraction. We explore the underlying crystalline structures that underpin so many of the materials that surround us. Finally, we look at how tensors can be used to represent the properties of three-dimensional materials, and we consider how symmetry places constraints on the properties of materials.
We move on to an exploration of quasi-, plastic, and liquid crystals. Then, we learn about the point defects that are present in all crystals, and we will learn how the presence of these defects lead to diffusion in materials. Next, we will explore dislocations in materials. We will introduce the descriptors that we use to describe dislocations, we will learn about dislocation motion, and will consider how dislocations dramatically affect the strength of materials. Finally, we will explore how defects can be used to strengthen materials, and we will learn about the properties of higher-order defects such as stacking faults and grain boundaries.

Structure of Materials Syllabus: Not available

Structure of Materials Format: Online course


Course Title: The Iterative Innovation Process

The Iterative Innovation Process Prerequisites: none

The Iterative Innovation Process Learning goals: People innovate, not organizations. This course is for anybody who wants to understand the innovation process - whether you want to foster innovation within your organization or whether you want to personally innovate.
As practicing innovators, we teach you the fundamentals of how to think like an innovator. Innovation is an iterative process, not a linear one. When innovating, there are thousands of sources of uncertainty in Technology, Implementation, and Markets. We teach you how to cycle through these sources of uncertainty until the right pieces come together in an innovation.
Throughout the course, we build up the innovation process model step by step with real examples and exercises. The goal of this course is to change and refine the way you view the innovation process, providing you with the foundation on which to build your future innovation

The Iterative Innovation Process Syllabus: Not available

The Iterative Innovation Process Format: Online course

Structural Materials: Selection and Economics

Structural Materials: Selection and Economics Prerequisites: none

Structural Materials: Selection and Economics Learning goals: From skyscrapers to transportation infrastructure, structural materials dominate the human landscape. Learning the principles that govern their selection is essential for any aspiring or practicing engineer.
This engineering course will introduce you to the key principles of structural materials selection through a practical curriculum rooted in the real world. The principles taught are general enough to be applied across many domains. Key points are emphasized with interesting examples and anecdotes from industry and academia.
This course benefits aspiring engineers and students with no previous experience as well as the seasoned professional.

Structural Materials: Selection and Economics Syllabus: Lecture 1: Introduction to externalities of materials selection, comprising social, political, economic, military, cultural, environmental and other effects.
Lecture 2: Introduction to relationship between material cost, abundance and usage. Factors influencing availability such as energy density and recyclability are also discussed.
Lecture 3: Introduction to the properties of materials that influence use in structural applications. Discussion of ratio analysis using among other examples steel, aluminum, and titanium.
Lecture 4: Discusses manufacturing and processing factors that effect material choice in various applications. Introduction to causes of material failures.

Structural Materials: Selection and Economics Format: Online course


Course Title: Solid State Chemistry

Solid State Chemistry Prerequisites: none

Solid State Chemistry Learning goals: Introduction to Solid State Chemistry is a one-semester college course on the principles of chemistry. This unique and popular course satisfies MIT’s general chemistry degree requirement, with an emphasis on solid-state materials and their application to engineering systems. You’ll begin with an exploration of the fundamental relationship between electronic structure, chemical bonding, and atomic order, then proceed to the chemical properties of “aggregates of molecules,” including crystals, metals, glasses, semiconductors, solutions and acid-base equilibria, polymers, and biomaterials. Real-world examples are drawn from industrial practice (e.g. semiconductor manufacturing), energy generation and storage (e.g. automobile engines, lithium batteries), emerging technologies (e.g. photonic and biomedical devices), and the environmental impact of chemical processing (e.g. recycling glass, metal, and plastic).
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

Solid State Chemistry Format: Do not recommend this course to students looking for online-only courses. This course contains self-study materials

Course Title: Symmetry, Structure, and Tensor Properties of Materials

Symmetry, Structure, and Tensor Properties of Materials Prerequisites: Linear Algebra

Symmetry, Structure, and Tensor Properties of Materials Learning Goals: This course covers the derivation of symmetry theory; lattices, point groups, space groups, and their properties; use of symmetry in tensor representation of crystal properties, including anisotropy and representation surfaces; and applications to piezoelectricity and elasticity.

Symmetry, Structure, and Tensor Properties of Materials Format: Do not recommend this course to students looking for online-only courses. This course contains self-study materials

Course Title: Elecronic, Optical, and Magnetic Materials and Devices

Elecronic, Optical, and Magnetic Materials and Devices Prerequisites: Electrical, Optical, and Magnetic Properties of Materials

Elecronic, Optical, and Magnetic Materials and Devices Learning Goals: This course is a three-part series which explains the basis of the electrical, optical, and magnetic properties of materials including semiconductors, metals, organics, and insulators. We will show how devices are built to take advantage of these properties. This is illustrated with a wide range of devices, placing a strong emphasis on new and emerging technologies.
The first part of the course covers electronic materials and devices, including diodes, bipolar junction transistors, MOSFETs, and semiconductor properties. The second part covers optical materials and devices, including photodetectors, solar cells (photovoltaics), displays, light emitting diodes, lasers, optical fibers, optical communications, and photonic devices. The final part of the series covers magnetic materials and devices, including magnetic data storage, motors, transformers, and spintronics.

Elecronic, Optical, and Magnetic Materials and Devices Format: Online course

Elecronic, Optical, and Magnetic Materials and Devices Syllabus: not available

Course Title: 6.00.1x

6.00.1x Learning Goals:  In this course you’ll be learning the basics of computer programming in Python and the fundamentals of computation, as well as getting the opportunity to implement your own Python functions.

* A Notion of computation
* The Python programming language
* Some simple algorithms
* Testing and debugging
* An informal introduction to algorithmic complexity
* Data structures

6.00.1x Syllabus:

Lecture 1 - Introduction to Python:
* Knowledge
* Machines
* Languages
* Types
* Variables
* Operators and Branching

Lecture 2 - Core elements of programs:
* Bindings
* Strings
* Input/Output
* IDEs
* Control Flow
* Iteration
* Guess and Check

Lecture 3 - Simple Programs:
* Approximate Solutions
* Bisection Search
* Floats and Fractions
* Newton-Raphson

Lecture 4 - Functions:
* Decomposition and Abstraction
* Functions and Scope
* Keyword Arguments
* Specifications
* Iteration vs Recursion
* Inductive Reasoning
* Towers of Hanoi
* Fibonacci
* Recursion on non-numerics
* Files

Lecture 5 - Tuples and Lists:
* Tuples
* Lists
* List Operations
* Mutation, Aliasing, Cloning

Lecture 6 - Dictionaries:
* Functions as Objects
* Dictionaries
* Example with a Dictionary
* Fibonacci and Dictionaries
* Global Variables

Lecture 7 - Debugging:
* Programming Challenges
* Classes of Tests
* Bugs
* Debugging
* Debugging Examples

Lecture 8 - Assertions and Exceptions
* Assertions
* Exceptions
* Exception Examples

Lecture 9 - Classes and Inheritance:
* Object Oriented Programming
* Class Instances
* Methods
* Classes Examples
* Why OOP
* Hierarchies
* Your Own Types

Lecture 10 - An Extended Example:
* Building a Class
* Viualizing the Hierarchy
* Adding another Class
* Using Inherited Methods
* Gradebook Example
* Generators

Lecture 11 - Computational Complexity:
* Program Efficiency
* Big Oh Notation
* Complexity Classes
* Analyzing Complexity

Lecture 12 - Searching and Sorting Algorithms:
* Indirection
* Linear Search
* Bisection Search
* Bogo and Bubble Sort
* Selection Sort
* Merge Sort

Lecture 13 - Visualization of Data:
* Visualizing Results
* Overlapping Displays
* Adding More Documentation
* Changing Data Display
* An Example

Lecture 14 - Summary

6.00.1x Format: Online


Course title: Mechanics-- Kinematics and Dynamics

Mechanics-- Kinematics and Dynamics Prerequisites: Single-Variable Calculus

Mechanics-- Kinematics and Dynamics  Learning goals: Mechanics is the study of the physics of motion and how it relates to applied forces. It lays the foundation of understanding the world around us through the how and why of motion.

This physics course is the first in a series of modules that covers calculus-based mechanics. This module reviews kinematics (the geometrical description of motion) in the context of one-dimensional, multi-dimensional, and circular motion. It also reviews Newton’s laws of motion and examines their application to a wide variety of cases.

Mechanics-- Kinematics and Dynamics Syllabus:
Topic 1: Kinematics
•	Position, distance, speed, velocity, and acceleration in 1D and 2D
•	Integration and differentiation 
•	Kinematics problems
Topic 2: Newton’s Laws
•	Free body diagrams
•	Forces: gravity, spring force, tension, friction
•	Newton’s 3 laws of motion
•	Dynamics
Topic 3: Circular Motion
•	Polar coordinates to describe circular motion
•	Inward acceleration to maintain circular motion
Topic 4: Resistive Forces, Constraints, and Massive Ropes
•	Tension along a massive rope
•	Differential equations for resistive forces
•	Pulley and string constraint equations
Mechanics-- Kinematics and Dynamics  Format: Online course, run annually on MITx Fall-winter asynchronously
Mechanics-- Kinematics and Dynamics  Depth:  This is a good introductory course for a high school student with some physics background and a strong math/calculus background.

Mechanics-- Kinematics and Dynamics Next recommendation: The next course, Mechanics: Momentum and Energy is a good follow up. 

Course title: Mechanics-- Momentum and Energy

Mechanics-- Momentum and Energy Prerequisites: Single-Variable Calculus, Kinematics and Dynamics

Mechanics-- Momentum and Energy Learning goals: This course is the second of a series of modules that cover calculus-based mechanics.  You will learn about the concepts of momentum, impulse, energy, and work, as well as the powerful idea of conservation laws. You will apply these concepts as powerful techniques to solve interesting mechanics problems such as collisions and rockets.

Mechanics-- Momentum and Energy Syllabus:
Topic 1: Momentum and Impulse
•	Definition of momentum
•	Impulse from force and change in momentum
Topic 2: Continuous Mass Flow
•	Rocket problem
Topic 3: Work, Kinetic Energy, Potential Energy, and Mechanical Energy
•	Conservative and non-conservative forces
•	Work calculations
•	Kinetic energy
•	Potential energy definition and practical examples
•	Potential energy diagrams
•	Mechanical energy
Topic 4: Collisions
•	Conservation of momentum in collisions
•	Elastic versus inelastic collisions
•	1D and 2D collisions


Mechanics-- Momentum and Energy Format: Online course, run annually on MITx Fall-winter asynchronously



Mechanics-- Momentum and Energy Depth:  This is a good introductory course, especially if you have taken the earlier course in this series: Mechanics: Kinematics and Dynamics

Mechanics-- Momentum and Energy Next recommendation: The next course, Rotational Dynamics, is a good follow up. If you also have multivariable calculus, you may be interested in Electricity and Magnetism or Vibrations and Waves.



Course title: Mechanics-- Rotational Dynamics

Mechanics-- Rotational Dynamics  Prerequisites: Single-Variable Calculus, Kinematics, Dynamics, Momentum and Energy

Mechanics-- Rotational Dynamics  Learning goals: This is the third of a series of modules that cover calculus-based mechanics. You will explore rotational motion and learn about the concepts of torque and angular momentum. You will learn about the conservation of angular momentum, and use it with other conservation laws to solve complex problems in rotational dynamics.

Mechanics-- Rotational Dynamics  Syllabus:
Topic 1: Rigid Bodies and Moment of Inertia
•	Rigid bodies
•	Moment of inertial calculations and intuition
•	Rotational velocity and acceleration; rotational kinematics
Topic 2: Torque
•	Torque 
•	Right hand rule for torque direction calculation
•	Rotational dynamics; torque causes rotational acceleration
Topic 3: Angular Momentum
•	Angular momentum
•	Torque changes angular momentum
Topic 4: Gyroscopes
Mechanics-- Rotational Dynamics  Format: Online course, run annually on MITx Fall-winter asynchronously
Mechanics-- Rotational Dynamics  Depth:  This is a good introductory course, especially if you have taken the earlier courses in this series: Mechanics: Kinematics and Dynamics

Mechanics-- Rotational Dynamics  Next recommendation: The last course, Mechanics: Simple Harmonic Motion and Non-Inertial Reference Frames is a good follow up. If you also have multivariable calculus, you may be interested in Electricity and Magnetism or Vibrations and Waves.



Course title: Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames

Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames  Prerequisites: Single-Variable Calculus, Kinematics, Dynamics, Momentum, Energy and Rotational Dynamics

Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames  Learning goals: This is the fourth of a series of modules that cover calculus-based mechanics. You will first explore simple harmonic motion (SHM) through springs and pendulums. You will learn to solve the SHM differential equation and to use the Taylor Formula for small oscillations. 

Next, you will learn how to modify Newton’s second law for both linear and rotational non-inertial reference frames. In particular, you will learn about the centrifugal and Coriolis fictitious forces. You will then study applications, such dynamics in the Earth’s atmosphere.

Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames  Syllabus:
Topic 1: Simple Harmonic Motion
•	Solve for the second order differential equation
•	Guess solution and solve for initial conditions
•	Application of Simple Harmonic Motion to various problems
Topic 2: Non-Inertial Reference Frames
•	Linear non-inertial terms in acceleration
•	Circular motion non-inertial fictious forces: Coriolis and centrifugal
•	Pressure gradient forces
•	Application of non-inertial fictitious forces to atmospheric physics
Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames  Format: Online course, run annually on MITx Fall-winter asynchronously
Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames  Depth:  This is a good introductory course, especially if you have taken the others in this series: Mechanics: Kinematics and Dynamics, Mechanics: Momentum and Energy, Mechanics: Rotational Dynamics 

Mechanics-- Simple Harmonic Motion and Non-Inertial Reference Frames  Next recommendation: If you also have multivariable calculus, you may be interested in Electricity and Magnetism or Vibrations and Waves.



Course title: Electricity and Magnetism- Electrostatics

Electricity and Magnetism- Electrostatics Prerequisites: Multi-Variable Calculus, Forces and Dynamics

Electricity and Magnetism- Electrostatics Learning goals: Electricity and Magnetism dominate much of the world around us – from the most fundamental processes in nature to cutting edge electronic devices. Electric and Magnet fields arise from charged particles. Charged particles also feel forces in electric and magnetic fields. Maxwell’s equations, in addition to describing this behavior, also describe electromagnetic radiation. 
In this course, we focus on Electrostatics. We examine the forces between charges, electric fields, and electric potential, looking at different ways of calculating each. We also look at dipoles and the difference between conductors and insulators. The course ends by explaining capacitors and dielectrics.

Electricity and Magnetism- Electrostatics Syllabus:
•	Electric Fields
•	Dipoles
•	Gauss’s Law
•	Electric Potential
•	Conductors, Insulators, and Capacitors 

Electricity and Magnetism- Electrostatics Format: Online course, run annually on MITx winter-spring  asynchronously

Electricity and Magnetism- Electrostatics Depth:  This should only be recommended to students who have a strong mechanics background, some familiarity with electricity and magnetism, and strong multivariable calculus.

Electricity and Magnetism- Electrostatics Next recommendation: The next course, Mechanics: Momentum and Energy is a good follow up. Students may be interested in Vibrations and Waves.



Course title: Electricity and Magnetism- Magnetic Fields and Forces

Electricity and Magnetism- Magnetic Fields and Forces  Prerequisites: Multi-Variable Calculus, Forces and Dynamics, Torque, Electrostatics,

Electricity and Magnetism- Magnetic Fields and Forces  Learning goals: Electricity and Magnetism dominate much of the world around us – from the most fundamental processes in nature to cutting edge electronic devices. Electric and Magnet fields arise from charged particles. Charged particles also feel forces in electric and magnetic fields. Maxwell’s equations, in addition to describing this behavior, also describe electromagnetic radiation. 
In this course, we focus on Magnetic fields and forces on charged particles in magnetic fields. We examine different ways of calculating the magnetic field, as well as introducing the ideas of current, resistance and simple DC circuits.

Electricity and Magnetism- Magnetic Fields and Forces  Syllabus:
•	Simple DC circuits
•	How charged particles move in magnetic fields
•	What creates magnetic fields
•	Calculating magnetic field strength and direction 
•	Magnetic Dipoles 

Electricity and Magnetism- Magnetic Fields and Forces  Format: Online course, run annually on MITx winter-spring  asynchronously

Electricity and Magnetism- Magnetic Fields and Forces  Depth:  This should only be recommended to students who have a strong mechanics background, some familiarity with electrostatics, and strong multivariable calculus.

Electricity and Magnetism- Magnetic Fields and Forces  Next recommendation: The next course, Electricity and Magnetism: Maxwell’s Equations is a good follow up. Students may also be interested in Vibrations and Waves.



Course title: Electricity and Magnetism-- Maxwell’s Equations


Electricity and Magnetism-- Maxwell’s Equations Prerequisites: Multi-Variable Calculus, Forces and Dynamics, Torque, Electrostatics, magnetostatics

Electricity and Magnetism-- Maxwell’s Equations Learning goals: Electricity and Magnetism dominate much of the world around us – from the most fundamental processes in nature to cutting edge electronic devices. Electric and Magnet fields arise from charged particles. Charged particles also feel forces in electric and magnetic fields. Maxwell’s equations, in addition to describing this behavior, also describe electromagnetic radiation. 
In this course, we finish up this introduction to Electricity and Magnetism. We begin by thinking about magnetic fields that change in time, working through Faraday’s Law and Inductors in Circuits. With the addition of Displacement Current, we complete Maxwell’s Equations. We finish the course by exploring the solution to Maxwell’s equations in free space – electromagnetic radiation. 

Electricity and Magnetism-- Maxwell’s Equations Syllabus:
•	Faraday’s Law
•	Inductors in DC and AC Circuits
•	Displacement Current
•	Maxwell’s Equations
•	Properties of Electromagnetic Radiation
•	Poynting Vector and Energy flow

Electricity and Magnetism-- Maxwell’s Equations Format: Online course, run annually on MITx winter-spring  asynchronously

Electricity and Magnetism-- Maxwell’s Equations Depth:  This should only be recommended to students who have a strong mechanics background, some familiarity with electricity and magnetism, and strong multivariable calculus.

Electricity and Magnetism-- Maxwell’s Equations Next recommendation: Students may be interested in Vibrations and Waves.




Course title: Quantum Mechanics-- A First Course

Quantum Mechanics-- A First Course  Prerequisites: Multi-Variable Calculus, differential equations, introductory mechanics and electricity and magnetism

Quantum Mechanics-- A First Course  Learning goals: In this quantum physics course you will learn the basics of quantum mechanics.  We begin with de Broglie waves, the wavefunction, and its probability interpretation. We then introduce the Schrodinger equation, inner products, and Hermitian operators.  We also study the time-evolution of wave-packets, Ehrenfest’s theorem, and uncertainty relations. 

Next we return to the Schrodinger equation, solving it for important classes of one-dimensional potentials.  We study the associated energy eigenstates and bound states. The harmonic oscillator is solved using the differential equation as well as algebraically, using creation and annihilation operators.  We discuss barrier penetration and the Ramsauer-Townsend effect.  

Finally, you will learn the basic concepts of scattering – phase-shifts, time delays, Levinson’s theorem, and resonances – in the simple context of one-dimensional problems.  We then turn to the study of angular momentum and the motion of particles in three-dimensional central potentials.  We learn about the radial equation and study the case of the hydrogen atom in detail.

This course is based on MIT 8.04: Quantum Mechanics I. At MIT, 8.04 is the first of a three-course sequence in Quantum Mechanics, a cornerstone in the education of physics majors that prepares them for advanced and specialized studies in any field related to quantum physics.

Quantum Mechanics-- A First Course  Syllabus:
●	The wavefunction and its probability interpretation. 
●	Time-evolution of wave-packets. 
●	Ehrenfest’s theorem and uncertainty relations. 
●	Solutions of the Schrodinger equation for one-dimensional potentials: the square well and the harmonic oscillator.
●	Barrier penetration and the Ramsauer-Townsend effect.  
●	Basics of quantum scattering in one dimension.
●	Phase-shifts, time delay, Levinson’s theorem, and resonances.
●	Angular momentum in Quantum Mechanics. 
●	Three-dimensional central potentials.  
●	Solution of the hydrogen atom.

Quantum Mechanics-- A First Course  Format: Online course, run every other year on MITx Online instructor paced 
Quantum Mechanics-- A First Course  Depth:  This should only be recommended to students who have a strong introductory physics and math (including calculus and differential equations) background

Quantum Mechanics-- A First Course  Next recommendation: Students may be interested in Vibrations and Waves if they haven’t taken it. Otherwise, may be interested in next course in quantum mechanics, 8.05x: Mastering Quantum Mechanics




Course title: Mastering Quantum Mechanics

Mastering Quantum Mechanics  Prerequisites: Multi-Variable Calculus, differential equations, introductory mechanics, electricity and magnetism, and a first course in quantum mechanics

Mastering Quantum Mechanics  Learning goals: This course offers a sophisticated view of quantum mechanics and its proper mathematical foundation. Completing the course will give you the tools needed to do research in quantum mechanics and to understand many current developments.
The first part of the course reviews basic knowledge of quantum mechanics as it gives an in-depth look into linear algebra to establish the mathematical foundation necessary to do quantum mechanics. It discusses in detail spin one-half states and spin operators, orthogonal projectors, Hermitian and unitary operators. It develops the Dirac bra-ket notation.
The second part covers the uncertainty principle and the concept of compatible operators. This includes the spectral theorem and the concept of a complete set of observables. It continues to develop the Heisenberg and the Schrödinger pictures of quantum mechanics. It discusses the axioms of quantum mechanics. This part also covers the coherent states of the harmonic oscillator, two-state systems and their applications to NMR.
The third part introduces the concept of tensor product states to discuss entanglement and Bell inequalities. This part also covers angular momentum and the representations of angular momentum. This is used to understand the spectrum of central potentials and to introduce hidden symmetries. It is followed by the subject of addition of angular momentum. This part of the course ends with a look into density matrices and decoherence. 
This course follows MIT’s on campus 8.05, the second semester of the three-course sequence on undergraduate quantum mechanics, and will be equally rigorous. 8.05 is a signature course in MIT's physics program and a keystone in the education of physics majors.
Before starting, you will need some basic familiarity with quantum mechanics. You must have seen the Schrodinger equation and studied its solutions for the square well potential, the harmonic oscillator, and the hydrogen atom. You may have learned this by self-study or by taking an introductory one-quarter or one-semester course on the subject. You must be proficient in calculus and have some knowledge of linear algebra.
Completing the course provides the necessary foundation to pursue advanced study or research at the graduate level in areas related to quantum mechanics.

Mastering Quantum Mechanics Syllabus:
•  Spin one-half and Spin Operators.
•  Vector spaces and linear operators.
•  Dirac’s Bra-ket notation.
•  Uncertainty Principle and compatible operators.
•  The Schrodinger and Heisenberg pictures of quantum mechanics. Axioms of quantum mechanics. 
•  Coherent States. Two state systems and applications to NMR.
•  Entanglement and Bell’s inequality. Teleportation.  No cloning. 
•  Angular momentum and central potentials. Addition of angular momentum
•  Density matrices and decoherence.
Mastering Quantum Mechanics  Format: Online course, run every other year on MITx Online instructor paced 
Mastering Quantum Mechanics  Depth:  This should only be recommended to students who have a strong introductory physics and math (including calculus and differential equations) background and a strong background in quantum mechanics

Mastering Quantum Mechanics  Next recommendation: Students may be interested in Vibrations and Waves if they haven’t taken it. Otherwise, may be interested in next course in quantum mechanics, 8.06x



Course Title: 7.00x Introduction to Biology – the Secret of Life


7.00x Introduction to Biology – the Secret of Life Topics:

Introduction and the Biochemistry of Life
Biochemistry - Proteins, Enzymes, and Glycolysis
Genetics - The Work of Mendel and T.H. Morgan
Human and Biochemical Genetics, Incomplete section
Molecular Biology - DNA and Replication
Molecular Biology - Transcription, Translation, and Variations
Recombinant DNA - Cloning and Analyzing a Gene
Genomics - Human Genome
Genomics - Observing and Perturbing the Genome to Probe Function
Disease and Science and Society


Course Title: 7.03.1x Genetics: The Fundamentals
7.03.1x Genetics: The Fundamentals Recommended prerequisites
7.00x Introduction to Biology

7.03.1x Genetics: The Fundamentals Topics:
Unit: Introduction to Genetics
Learning Sequence: Genetics Overview and Review
Learning Sequence: Gene Function and Complementation
Unit: Mendelian Genetics
Learning Sequence: How Do You Explain a Phenotype?
Learning Sequence: Mendel's Laws of Inheritance
Learning Sequence: More Complex Modes of Inheritance
Unit: Inheritance Patterns and Pedigrees
Learning Sequence: Inferring Patterns of Inheritance from Pedigrees
Learning Sequence: Calculating Conditional Probability
Unit: Recombination and Linkage
Learning Sequence: Chromosomes, Mitosis, and Meiosis
Learning Sequence: Mapping Genetic Linkage
Unit: Tools for Analyzing Linkage
Learning Sequence: Tetrad Analysis
Learning Sequence: DNA Markers
Learning Sequence: Mapping with SNPs 
Unit: Analyzing Human Mendelian Traits 
Learning Sequence: Human Mendelian Genetics
Learning Sequence: LOD Scores from Pedigrees 

7.03.1x Genetics: The Fundamentals Course Goals
Our goals for this course are for you to: 
Appreciate the applications of genetics to everyday life.
Apply terminology appropriately to concepts in genetics. 
Justify the use of specific techniques and methods for answering different genetic questions.  
Design genetic crosses to make conclusions about genotypes, modes of inheritance, and linkage.
Use a quantitative approach to determine different genetic probabilities and calculate genetic distances.
Interpret genetic relationships and modes of inheritance of a trait given a pedigree.

Course Title: 7.03.2x Genetics: Analysis and Application
7.03.2x Genetics: Analysis and Application Recommended prerequisites
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals

7.03.2x Genetics: Analysis and Application Course Goals
Our goals for this course are for you to: 
Appreciate the applications of genetics to everyday life.
Apply terminology appropriately to concepts in genetics. 
Justify the use of specific techniques and methods for answering different genetic questions.
Analyze the location and type of mutation or chromosomal change.
Find or create mutants of interest.
Explain the impact of genetics on development and behavior.


Course Title: 7.03.3x Genetics: Population Genetics and Human Traits

7.03.3x Genetics: Population Genetics and Human Traits Recommended prerequisites
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application

7.03.3x Genetics: Population Genetics and Human Traits Course Goals:
Our goals for this course are for you to: 
Appreciate the applications of genetics to everyday life.
Apply terminology appropriately to concepts in genetics.
Justify the use of specific sequencing methods for answering genetic questions.
How to interpret the patterns and driving forces of genetic variation within and between human populations.
Analyze results from genome-wide association studies.
Use a quantitative approach to determine genetic features of different populations.
Explain the impact of genetic tools on human society.


Course Title: 7.05x Biochemistry: Biomolecules, Methods, and Mechanisms

7.05x Biochemistry: Biomolecules, Methods, and Mechanisms Recommended prerequisites
7.05 Biochemistry, Pathways and Metabolism

7.05x Biochemistry: Biomolecules, Methods, and Mechanisms Topics: 

Unit: Buffers and Amino Acids
Learning Sequence: Introduction to Biochemistry; pH and Buffers
Learning Sequence: Amino Acids and Proteins
Unit: Protein Purification
Learning Sequence: Protein Purification
Unit: Protein Structure and Folding
Learning Sequence: Protein Structure 
Learning Sequence: Protein Folding
Unit: Hemoglobin
Learning Sequence: Hemoglobin and Allostery
Learning Sequence: Hemoglobin and the Bohr Effect
Unit: Enzymes Part I
Learning Sequence: Enzyme Chemistry
Learning Sequence: Enzymes as Catalysts
Unit: Enzymes Part II
Learning Sequence: Enzyme Kinetics
Learning Sequence: Membranes and Blood Clotting
Unit: Membranes, Blood Clotting, Channels, Transporters, and Pumps
Learning Sequence: Channels, Transporters, and Pumps
Unit: Signal Transduction
Learning Sequence: Signal Transduction

7.05x Biochemistry: Biomolecules, Methods, and Mechanisms Course Goals: 

Our goals for this course are for you to learn how: 
Apply the scientific method to pursue research questions.
Analyze protein purification schemes.
Scientists determine the structure of a protein.
Structure, allostery, and the Bohr effect influence hemoglobin function.
To interpret graphs, plot behaviors, and calculate constants related to enzyme function.
Pumps, transporters, and channels differ to regulate molecule transfer across membranes.
G proteins play a key role in signaling.


Course Title: 7.06.1x Cell Biology: Transport and Signaling

7.06.1x Cell Biology: Transport and Signaling Recommended prerequisites
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application and 7.03.3x: Genetics: Population Genetics and Human Traits and 7.05x: Biochemistry: Biomolecules, Methods, and Mechanisms

7.06.1x Cell Biology: Transport and Signaling Topics:
Unit: Membranes, Lipids, and Proteins 
Learning Sequence: Components of Biological Membranes 
Learning Sequence: Lipid Heterogeneity and Asymmetry 
Learning Sequence: Protein Asymmetry and Prediction
Unit: Intracellular Transport and Protein Secretion 
Learning Sequence: Mechanisms of Transport
Learning Sequence: Transport to Cellular Compartments
Learning Sequence: Endocytosis and Exocytosis
Unit: Nuclear-Cytoplasmic Transport 
Learning Sequence: The Nuclear Pore
Learning Sequence: Molecular Mechanisms of Nuclear Transport
Learning Sequence: Quantifying and Regulating Nuclear Transport
Unit: Principles of Signal Transduction 
Learning Sequence: Signaling Themes
Learning Sequence: Receptor-Ligand Interactions and G Proteins
Learning Sequence: Monitoring Signaling
Unit: Signaling Pathways and Regulatory Paradigms 
Learning Sequence: Examples of Signaling Pathways
Learning Sequence: Regulation of Signaling: Phosphorylation
Learning Sequence: Regulation of Signaling: Proteolysis


7.06.1x Cell Biology: Transport and Signaling Course Goals: 
Our goals for this course are for you to: 
Appreciate biochemical and genetic approaches to address fundamental questions in cell biology.
Evaluate how scientists draw conclusions and develop models about cell biology from experimental approaches and results.
Understand how to select specific empirical methods and techniques based on the different kinds of questions scientists ask.
Design experiments to answer cell biology experiments with proper controls.
Assess biological necessity and sufficiency from experimental results.
Compare and contrast protein transport processes.
Compare and contrast signaling pathway mechanisms and regulation. 
Identify recurring themes in protein transport and signal transduction.

Course Title: 7.06.2x Cell Biology: The Cytoskeleton and Cell Cycle

7.06.2x Cell Biology: The Cytoskeleton and Cell Cycle Recommended prerequisites
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application and 7.03.3x: Genetics: Population Genetics and Human Traits and 7.05x: Biochemistry: Biomolecules, Methods, and Mechanisms and 7.06.1x Cell Biology: Transport and Signaling

7.06.2x Cell Biology: The Cytoskeleton and Cell Cycle Topics:
Unit: Microscopy
Learning Sequence: Microscopy and Cell Biology
Learning Sequence: Fluorescence Microscopy
Unit: The Actin Cytoskeleton 
Learning Sequence: Actin and the Cytoskeleton
Learning Sequence: Regulation of Actin
Unit: The Microtubule Cytoskeleton 
Learning Sequence: Tubulin and the Microtubule Cytoskeleton
Learning Sequence: Control of the Microtubule Cytoskeleton in Cells
Unit: Force Generation and Movement 
Learning Sequence: Measuring Movement: Overview and TIRF
Learning Sequence: Measuring Movement: Assays
Learning Sequence: Force Generation
Unit: Cell Division
Learning Sequence: Replication
Learning Sequence: Pairing and Condensation
Learning Sequence: Segregation
Learning Sequence: Cytokinesis and Meiosis
Unit: Cell Cycle Regulation 
Learning Sequence: Approaches to Cell Cycle Regulation
Learning Sequence: Cyclins and Cyclin-Dependent Kinases
Learning Sequence: Checkpoints

7.06.2x Cell Biology: The Cytoskeleton and Cell Cycle Course Goals:
Our goals for this course are for you to: 
Appreciate biochemical and genetic approaches for addressing fundamental questions regarding the regulation of cell structure and division.
Evaluate how scientists draw conclusions (the 'facts’) about cell biology from experimental approaches and results.
Assess biological necessity and sufficiency from experimental results.
Understand why specific empirical methods and techniques are appropriate for different kinds of questions.
Design experiments with proper controls.
Interpret microscopy images.
Compare and contrast the roles of actin and microtubule cytoskeletal elements.
Identify recurring themes in maintaining cellular architecture throughout the cell cycle.

Course Title: 7.06.3x Cell Biology: Cell-Cell Interactions
7.06.3x Cell Biology: Cell-Cell Interactions Recommended prerequisites
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application and 7.03.3x: Genetics: Population Genetics and Human Traits and 7.05x: Biochemistry: Biomolecules, Methods, and Mechanisms and 7.06.1x Cell Biology: Transport and Signaling and 7.06.2x Cell Biology: The Cytoskeleton and Cell Cycle

7.06.3x Cell Biology: Cell-Cell Interactions Topics:
Unit: Cell Adhesion and Polarity
Learning Sequence: Introduction to Cell-Cell Interactions
Learning Sequence: Cadherins
Learning Sequence: Mechanotransduction
Learning Sequence: Tight Junctions
Learning Sequence: Cell-Matrix Junctions
Unit: Morphogenesis, Stem Cells, and Regeneration 
Learning Sequence: Morphological Specialization and Building Complexity
Learning Sequence: Signaling Pathways in Morphogenesis
Learning Sequence: The Regenerative Capacity of Stem Cells
Learning Sequence: Intestinal Stem Cells as a Case Study
Unit: Cell Death and Autophagy 
Learning Sequence: Introduction to Apoptosis
Learning Sequence: Ways to Study Apoptosis
Learning Sequence: Mechanisms and Pathways of Apoptosis
Learning Sequence: Autophagy
Unit: Host-Pathogen Interactions 
Learning Sequence: Introduction to Pathogens
Learning Sequence: Salmonella typhimurium Pathogenesis
Learning Sequence: Listeria monocytogenes Pathogenesis
Unit: Cell Biology of Immune Systems
Learning Sequence: Components of Immune Responses
Learning Sequence: Antigen Presentation
Learning Sequence: T-Cell Activation, Organization, and Function
Unit: Cancer and Metastasis 
Learning Sequence: Cancer in the Context of Multicellularity
Learning Sequence: Cancer Microevolution
Learning Sequence: Cancer Metastasis

7.06.3x Cell Biology: Cell-Cell Interactions Course Goals:
Our goals for this course are for you to: 
How to apply biochemical and genetic approaches to address fundamental questions regarding regulation of cellular functions and interactions.
How to evaluate the conclusions and models that scientists develop about cell biology from experimental approaches and results.
How to select specific empirical methods and techniques based on the different types of questions scientists ask.
How to design experiments to answer cell biology experiments with proper controls.
How to compare and contrast the properties of different cell types.
How to identify recurring themes in cell biology impacting human health.


Course Title: 7.28.1x Molecular Biology: DNA Replication & Repair

7.28.1x Molecular Biology: DNA Replication & Repair Recommended prerequisites:
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application and 7.03.3x: Genetics: Population Genetics and Human Traits and 7.05x: Biochemistry: Biomolecules, Methods, and Mechanisms


7.28.1x Molecular Biology: DNA Replication & Repair Topics:
Unit: DNA Replication: DNA Polymerase
Learning Sequence: DNA Polymerase 
Learning Sequence: Measuring DNA Polymerase Activity
Unit: DNA Replication: The Other Players,
Learning Sequence: The Replication Fork, Helicase, and Single-Stranded Binding Protein
Learning Sequence: Topoisomerase, Okazaki Fragment Repair, and the Trombone Model
Unit: DNA Replication and the DNA
Learning Sequence: Origins of Replication 
Learning Sequence: Identifying Origins
Unit: DNA Replication: Discovery and More Assays
Learning Sequence: Discovering Replication Genes 
Learning Sequence: EMSA, Footprinting, Unwinding, and Template Association Assays
Unit: DNA Replication: Initiation
Learning Sequence: Replication Initiation and Telomeres
Learning Sequence: Chromatin, Histones, and Nucleosomes
Unit: Mismatch Repair
Learning Sequence: Mismatch Repair
Learning Sequence: Measuring Mismatch Repair
Unit: DNA Damage, DNA Repair, and DNA Damage Tolerance
Learning Sequence: DNA Damage 
Learning Sequence: DNA Damage Repair and Tolerance Pathways
Unit: Double-Stranded Break Repair
Learning Sequence: Double-Stranded Breaks and NHEJ 
Learning Sequence: Homologous Recombination

7.28.1x Molecular Biology: DNA Replication & Repair Course Goals
Our goals for this course are for you to: 
Compare and contrast the mechanisms of DNA replication in prokaryotes and eukaryotes
Describe several enzymatic mechanisms that the cell uses to repair or tolerate DNA damage
Analyze protein structures to infer functional information
Design methods for the best experiment to test a hypothesis related to DNA replication or repair proteins
Interpret data from DNA replication and repair experiments

Course Title: 7.28.2x Molecular Biology: Transcription & Transposition

7.28.2x Molecular Biology: Transcription & Transposition Recommended prerequisites
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application and 7.03.3x: Genetics: Population Genetics and Human Traits and 7.05x: Biochemistry: Biomolecules, Methods, and Mechanisms and 7.28.1x Molecular Biology: DNA Replication & Repair

7.28.2x Molecular Biology: Transcription & Transposition Topics:
Machinery and Promoters of Bacterial Transcription
Bacterial Regulation of Bacterial Transcription
Machinery and Promoters of Eukaryotic Transcription
Regulation of Eukaryotic Transcription I
Regulation of Eukaryotic Transcription II
Transposition
CRISPR

7.28.2x Molecular Biology: Transcription & Transposition Course Goals:
Our goals for this course are for you to: 
Compare and contrast transcription in prokaryotes and eukaryotes
Describe several mechanisms of transposition
Analyze protein structures to infer functional information
Design the best experiment to test a hypothesis
Interpret data from transcription and transposition experiments

Course Title: 7.28.3x Molecular Biology: RNA Processing & Translation

7.28.3x Molecular Biology: RNA Processing & Translation Recommended prerequisites:
7.00x Introduction to Biology and 7.03.1x Genetics: The Fundamentals and 7.03.2x Genetics: Analysis and Application and 7.03.3x: Genetics: Population Genetics and Human Traits and 7.05x: Biochemistry: Biomolecules, Methods, and Mechanisms and 7.28.1x Molecular Biology: DNA Replication & Repair and 7.28.2x Molecular Biology: Transcription & Transposition

7.28.3x Molecular Biology: RNA Processing & Translation Topics:
Translation I – Overview and Key Players
Translation II – Elongation
Translation III – Initiation and Termination
Translation IV – Regulation of Translation
RNA Splicing I – Mechanisms
RNA Splicing II – Proofreading and Alternative Splicing
RNA Turnover I – Assays and General Mechanisms
RNA Turnover II – Specific Bacterial and Eukaryotic Mechanisms

7.28.3x Molecular Biology: RNA Processing & Translation Course Goals:
Our goals for this course are for you to: 
Compare and contrast translation in bacteria and eukaryotes
Describe several mechanisms of RNA turnover and RNA splicing
Analyze protein structures to infer functional information
Design the best experiment to test a hypothesis
Interpret data from translation and RNA processing experiments

Course Title: 7.QBWx Quantitative Biology Workshop

7.QBWx Quantitative Biology Workshop Topics:
Learning Sequence: MATLAB Introduction
Learning Sequence: Fitting Biochemical Data: Equilibrium and Kinetics
Learning Sequence: Molecular Modeling with PyMOL
Learning Sequence: Visual Neuroscience with MATLAB
Learning Sequence: Neuroscience Using Machine Learning Concepts
Learning Sequence: Genomics Data Analysis Using Python
Learning Sequence: Gene Expression Application Using Python
Learning Sequence: Statistical Data Analysis Using R
Learning Sequence: Analyzing Single-Cell Gene Expression Using Multiple Methods

7.QBWx Quantitative Biology Workshop: Course Goals
Our goals for this course are for you to: 
Apply quantitative methods to biological problems
Define computational vocabulary
Write Python, MATLAB, and R code to analyze biological data
Examine any protein structure in PyMOL
Analyze how to answer a scientific question through a step-by-step thought process.




"""









PHASES = {

 
    "phase1": {
        "name": "Recommendation",
        "fields": {


              "next_course": {
                "type": "radio",
                "label": "Have you already taken a course and are looking for a recommendation for the next course to take?",
                "options": ["No", "Yes"],
                
               
            },

           "previous_course": {
                "type": "text_input",
                "label": """What was the name of the course?""",
                "showIf": {"next_course": {"$eq": "Yes"}}
       
            },

         
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


         

        },
        "phase_instructions": "Please recommend a course to the student. Please recommend only one course. If the student indicated that they are interested in online-only courses, please do not recommend courses where the Format includes self-study. If a course is indicated to be of challenging difficulty, lead by asking if they're looking for a challenge, or saying something that lets them know that the course is challenging. You may ask leading questions, but please don't ask any questions that require an answer. ",
        "user_prompt": [


             {
                "condition": {"$and": [
                    {"more": "No"},
                    {"next_course": "No"}
                ]},
                 "prompt": "Here is what I am interested in learning about: {student_query}"
            },

             {
                "condition": {"$and": [
                    {"more": "No"},
                    {"next_course": "Yes"}
                ]},
                "prompt": "Here is what I am interested in learning about: {student_query}  I have already taken {previous_course}, and I am looking for a recommendation as to what course to take next."
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
        "phase_instructions": "Revise your previous recommendation based on the new information provided by the user. Suggest only one course. If the user says that they were happy with their recommendation, don't suggest a course and thank them for their time.",
         "user_prompt": [


            {
                "condition": {"revise_it": {"$eq": "I'm happy"}},
                "prompt": "I'm happy with my recommendation.  Thank you."
            },


          {
                "condition": {"revise_it": {"$eq": "Revise it"}},
                "prompt": "The student feels that this information might help you make a better recommendation: {revised_query}.  Please incorporate that information to revise your recommendation. If you are unable to make a better recommendation, let the student know why and appologize for not being able to be of more help."
            },
          #  {
          #    "condition": {"$and": [
          #          {"more": "No"},
          #         {"revise_it": "Revise it"}
          #      ]},  
          #    "prompt": "Here is what I am interested in learning about: {student_query}"
          #   
          #  },
          #  {
          #      "condition": {"$and": [
          #          {"more": "Yes"},
          #          {"next_course": "No"},
          #          {"revise_it": "Revise it"}
          #      ]},
          #      "prompt": "Here is what I am interested in learning about: {student_query}  Here's some information about my academic and work background: {background}.  This is how I answered the question Have you taken Calculus? {Calculus}  This is how I answered the question How would you rank your Python skills? {Python} This is how I answered the queestion  Are you interested in self-study courses? {Self_study} "
          #  },

      #    {
      #         "condition": {"$and": [
      #              {"more": "Yes"},
      #              {"next_course": "Yes"},
      #              {"revise_it": "Revise it"}
      #          ]},
      #          "prompt": "Here is what I am interested in learning about: {student_query}  Here's some information about my academic and work background: {background}.  This is how I answered the question Have you taken Calculus? {Calculus}  This is how I answered the question How would you rank your Python skills? {Python} This is how I answered the queestion  Are you interested in self-study courses? {Self_study}.  I have already taken {previous_course}, and I am looking for a recommendation as to what course to take next. Do not recommend that I take {previous_course}.  Make a different recommendation "
      #      },

            

         
         ],
        "allow_skip": True,
        "show_prompt": True
    },
       
   

}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True


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
