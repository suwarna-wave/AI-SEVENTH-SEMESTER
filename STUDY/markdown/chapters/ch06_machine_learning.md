# Chapter 6: Machine Learning
### *6 hours | 10 marks*

> **"A computer program is said to learn from experience E with respect to some task T and performance measure P, if its performance at T, as measured by P, improves with experience E."**  
> — Tom Mitchell (the canonical definition, 1997)

---

## 🌍 The Hook — The Fundamental Shift

For all of classical AI (Chapters 1-5), someone had to *program* the knowledge in:
- Write the rules
- Define the logic
- Specify the heuristics

But here's the problem: **the world is too complex to program by hand.**

How do you write rules for:
- Recognizing a handwritten digit?
- Detecting spam email?
- Translating language?

You can't enumerate all the cases. There are too many.

**Machine Learning's solution:** Instead of programming what to do, **show the machine examples and let it figure out the patterns itself.**

This was a *philosophical revolution* in AI. Let's understand it from first principles.

---

## 6.1 Concepts of Learning

### The Three Ways to Learn

#### Supervised Learning
> "Here are thousands of examples. Each one has the right answer labeled."

```
Input: [Photo of cat]  → Label: "Cat"
Input: [Photo of dog]  → Label: "Dog"
Input: [Photo of ????] → Machine must predict
```

The machine learns a **mapping** from inputs to outputs.

**Analogy:** Learning with a teacher who gives you flashcards with answers on the back.

#### Unsupervised Learning
> "Here are thousands of examples. No labels. Find the patterns yourself."

```
Input: [1000 customer purchases]
Output: "These customers form 4 natural groups"
```

The machine discovers **structure** in unlabeled data.

**Analogy:** Sorting a pile of toys by color without being told what colors are.

#### Reinforcement Learning
> "Try things. Get rewards or punishments. Learn what works."

```
Agent takes action → Environment gives reward/penalty
→ Agent learns which actions maximize total reward
```

**Analogy:** Training a dog with treats. The dog doesn't know the rules — it learns them through trial and error.

---

### The Learning Problem (Formally)

Given:
- **Training data:** (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)
- **Hypothesis space H:** All possible models we could learn

Find:
- A **hypothesis h ∈ H** that approximates the true function f: x → y

```
                Training Data
                      │
                       ▼
             ┌─────────────────┐
             │   Learning      │
             │   Algorithm     │
             └────────┬────────┘
                      │
                       ▼
               Learned Model (h)
                      │
            New Input ▼
              x_new → h(x_new) → Predicted y
```

The fundamental challenge: the model must **generalize** — work well on examples it has never seen.

---

## 6.2 Learning by Analogy

### What Is It?

> "This new situation is similar to one I've seen before. Apply the same solution."

**Case-Based Reasoning (CBR)** is the formal AI system built on this principle.

### How CBR Works

```
New Problem
     │
     ▼
┌─────────────────────────────┐
│  RETRIEVE: Find similar     │
│  cases from memory          │
│  (using similarity metric)  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  REUSE: Adapt the solution  │
│  from old case to new       │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  REVISE: Test and fix the   │
│  solution if needed         │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  RETAIN: Store this new     │
│  case for future reference  │
└─────────────────────────────┘
```

**Real-world examples:**
- Legal systems use precedents (case law)
- Doctors think "this looks like that case from 2019"
- Customer support uses ticket history

---

## 6.3 Inductive Learning

### The Concept

> "Look at specific examples. Generalize to a rule."

This is the most common form of machine learning.

**Example — Learning "positive" examples:**

```
Examples:
  (height=tall, hair=dark, nationality=Nepali) → Person A
  (height=short, hair=light, nationality=Swiss) → Person B
  (height=medium, hair=dark, nationality=Indian) → Person C
```

The learner must find a **general rule** that classifies people.

### Decision Tree Learning

The most intuitive inductive learner:

```
Decision Tree for "Should I play tennis today?":

                   Outlook?
                  /    |    \
            Sunny  Overcast  Rain
              |       |       |
          Humidity   YES   Wind?
           /    \         /     \
         High  Normal  Strong  Weak
          |       |       |      |
          NO     YES      NO    YES
```

The tree is learned from training examples using a measure called **Information Gain** (how much does this attribute reduce uncertainty?).

### Overfitting — The Curse of Learning

```
UNDERFITTING:                GOOD FIT:              OVERFITTING:
Too simple model             Captures the pattern   Memorizes training data
                                                    Fails on new data

   ___                         /\   /\                 /|  |\   /\  /|
  /   \                       /  \_/  \               / |  | \_/  \/ |
 /     \                     /         \             /  |  |         |
*   *   *   *               * * * * * *             *   *   *   *   *

Learns nothing           Generalizes well         Too specific
```

**The goal:** Find the sweet spot between underfitting and overfitting.

---

## 6.4 Explanation-Based Learning (EBL)

### The Concept

> "I don't need thousands of examples. I just need ONE example and a domain theory to explain WHY it's an example."

**EBL uses prior domain knowledge to learn from a single example.**

**Example:**
- Domain theory: Physics laws about momentum, gravity
- Single example: A ball thrown at a window breaks it
- Learned concept: "Fragile objects break when hit by fast-moving projectiles"

The system **explains** the example using background knowledge, then **generalizes** the explanation.

**Analogy:** You don't need to see 10,000 fires to know fire is dangerous — once you understand what fire is, one explanation generalizes to all fires.

---

## 6.5 Neural Networks — Introduction

*Full deep dive in Chapter 7 — here we introduce the concept.*

### The Biological Inspiration

```
           Dendrites                   Cell Body           Axon
           (inputs)                    (processing)        (output)
        ─────┬─────                   ┌─────────┐          ─────►
Signal ──────┤                        │         │
             │     Synapse ──────────►│  Neuron │──────────► Next Neuron
Signal ──────┤    (weighted)          │         │
        ─────┘                        └─────────┘
```

An **artificial neural network** mimics this with:

```
         Inputs        Weights        Activation
          x₁ ────── w₁ ────┐
                             ├── Σ(xᵢwᵢ) + b → f(.) → Output
          x₂ ────── w₂ ────┘
```

- **Inputs (x):** features of the data
- **Weights (w):** learned importance of each input
- **Bias (b):** offset term
- **Activation f(.):** Non-linear function that "fires" the neuron

**Learning:** Adjust weights to minimize prediction error.

### The XOR Problem — Why One Neuron Isn't Enough

```
XOR truth table:
Input A  Input B  Output
  0        0        0
  0        1        1
  1        0        1
  1        1        0

Plotting it:
B |
1 |  .  X  ← (0,1)=1   (1,1)=0
  |
0 |  X  .  ← (0,0)=0   (1,0)=1
  |____________
       0  1    A

Notice: No single straight line can separate X from . !
→ XOR is NOT linearly separable
→ One neuron (single-layer) CANNOT solve XOR
→ We need MULTIPLE LAYERS → Deep Networks!
```

---

## 6.6 Genetic Algorithms

### The Beautiful Analogy

Nature solved optimization through **evolution**. Why not copy it?

```
BIOLOGICAL EVOLUTION          GENETIC ALGORITHMS
─────────────────────         ───────────────────
Population of organisms  →   Population of solutions
Fitness (survival)       →   Fitness function
Reproduction             →   Crossover (mixing solutions)
Mutation                 →   Random changes to solutions
Natural selection        →   Keep best solutions
Generations              →   Iterations
```

### The GA Process

```
Step 1: INITIALIZE
  Create random population of candidate solutions
  (Each solution = a "chromosome" = sequence of bits/numbers)

Step 2: EVALUATE
  Compute fitness of each solution
  Fitness = how good is this solution at the problem?

Step 3: SELECT
  Select parents, biased toward higher fitness
  (Better solutions more likely to reproduce)

Step 4: CROSSOVER
  Combine two parents to create offspring
  
  Parent 1: [1 0 1 | 1 0 0]
  Parent 2: [0 1 0 | 0 1 1]
  Child:     [1 0 1 | 0 1 1]  ← takes front from P1, back from P2
                  ↑
              crossover point

Step 5: MUTATION
  With small probability, randomly flip a bit
  [1 0 1 0 1 1] → [1 0 0 0 1 1]
                        ↑
                   mutated here

Step 6: REPEAT from Step 2
  Until fitness is good enough or max generations reached
```

### Example: Traveling Salesman Problem

**Problem:** Find the shortest route visiting N cities and returning to start.

**Chromosome:** A permutation of cities = [Kathmandu, Pokhara, Biratnagar, Janakpur, ...]  
**Fitness:** Total distance of this route (lower = better)  
**Crossover:** Order crossover — preserving city order from each parent  
**Mutation:** Randomly swap two cities

After many generations, the population converges on near-optimal routes!

### Why GAs Work (Intuitively)

GAs search many points simultaneously (population-based).  
They don't get stuck in local optima as easily as hill climbing.  
The "schema theorem" (Holland, 1975) shows: good building blocks (substrings) that contribute to fitness are amplified exponentially across generations.

---

## 6.7 Fuzzy Learning

### The Problem with "Crisp" Logic

In classical logic, everything is **binary**: True or False, 0 or 1.

But reality has **degrees**:
- Is 30°C hot? Kind of.
- Is a person who is 5'11" tall? Somewhat.
- Is a 3-second response time fast? Depends.

**Fuzzy logic** handles this gracefully.

### Fuzzy Sets and Membership Functions

Instead of: x ∈ A (either completely in or completely out)  
Fuzzy: μ_A(x) ∈ [0, 1] (degree of membership)

**Example: "Tall" person**

```
Membership in "Tall"
μ
1.0 ─────────────────────────────────
         /
0.5 ───/──── ← 50% tall at ~5'8"
      /
0.0 /──────────────────────────────
   5'0"  5'6"  5'9"  6'0"  6'6"  Height
```

At 5'9": μ_Tall(5'9") = 0.7 (70% "tall")

### Fuzzy Operations

| Operation | Formula | Interpretation |
|-----------|---------|---------------|
| NOT A | 1 - μ_A(x) | "Not tall" at 5'9" = 0.3 |
| A AND B | min(μ_A(x), μ_B(x)) | "Tall AND Young" |
| A OR B | max(μ_A(x), μ_B(x)) | "Tall OR Young" |

### Fuzzy Rules

```
IF temperature is HOT AND humidity is HIGH
THEN fan speed is VERY HIGH

IF temperature is WARM AND humidity is MEDIUM
THEN fan speed is MEDIUM

IF temperature is COLD
THEN fan speed is LOW
```

Each of "HOT", "HIGH", "VERY HIGH" etc. are fuzzy sets with membership functions.

### Defuzzification

After applying fuzzy rules, we get a fuzzy output. To get a **crisp (concrete) number**:

**Centroid Method:** Find the center of mass of the output membership function.

```
Fuzzy output:
         ___________
        /           \
       /             \
──────/               \───
     30%    50%    70%  Fan speed (%)

Centroid ≈ 50% fan speed (crisp output)
```

### Fuzzy Learning Applications

- Air conditioners (Mitsubishi Electric uses fuzzy control!)
- Camera auto-focus systems
- Anti-lock braking systems (ABS)
- Washing machines (water level + time = fuzzy decision)

---

## 6.8 Boltzmann Machines

### The Concept

A **Boltzmann Machine** is a stochastic (probabilistic) neural network.

Named after physicist Ludwig Boltzmann because it uses the **Boltzmann distribution** from statistical physics.

### The Physics Analogy

In thermodynamics, a system seeks its **minimum energy state** (equilibrium).  
A Boltzmann Machine seeks a minimum "energy" state that best fits the training data.

```
Energy of a configuration:

E(v, h) = -Σᵢⱼ wᵢⱼ vᵢ hⱼ - Σᵢ aᵢ vᵢ - Σⱼ bⱼ hⱼ

where:
  v = visible units (observed data)
  h = hidden units (latent features)
  w = connection weights
  a, b = biases
```

### The Boltzmann Distribution

The probability of a configuration:

```
P(v, h) = exp(-E(v,h)) / Z

where Z = Σ exp(-E(v,h)) over all configurations
```

Low energy → high probability → the network "prefers" this configuration.

### Architecture

```
┌──────────────────────────────┐
│         VISIBLE UNITS        │
│  ● ── ● ── ● ── ● ── ●       │  ← Data you can see
│  │╲   │╲  │╲   │╲  │         │
│  │ ╲  │ ╲ │ ╲  │ ╲ │         │
│  │  ╲ │  ╲│  ╲ │  ╲│         │
│  ● ── ● ── ● ── ● ── ●       │  ← Hidden features
│         HIDDEN UNITS         │
└──────────────────────────────┘
     All connected to all!
```

All units are connected to all other units (fully connected). No layers!

### Restricted Boltzmann Machine (RBM)

The practical version: **no connections within a layer** — only between visible and hidden.

```
Visible: ● ── ● ── ● ── ●   (observed data)
          ╲  ╲│╱  ╱│╲  ╲│
           ╲  ╲   ╱  ╲  ╲
Hidden:   ● ── ● ── ●       (learned features)
```

RBMs are the building blocks of **Deep Belief Networks** — one of the early successes of deep learning (Hinton, 2006).

### Learning in Boltzmann Machines

The learning rule (Contrastive Divergence):

1. Show data to visible units
2. Let hidden units respond
3. Reconstruct visible units from hidden
4. Compare original vs. reconstructed
5. Update weights to make reconstruction better

**Intuition:** The machine learns to "remember" patterns by minimizing reconstruction error.

---

## 📐 Math Intuition Corner

### The Bias-Variance Tradeoff

Every learning algorithm faces this fundamental tradeoff:

```
Total Error = Bias² + Variance + Irreducible Noise

Bias: Error from wrong assumptions (underfitting)
Variance: Error from sensitivity to training data (overfitting)
```

```
High Bias             Optimal               High Variance
(Underfitting)                              (Overfitting)
─────────────         ──────────            ─────────────
Too simple model      Right balance         Too complex model
Misses the pattern    Good generalization   Memorizes training
```

**The tradeoff:** Decrease bias → increase variance, and vice versa.

The goal of every ML algorithm is to find the sweet spot.

### Information Entropy (Foundation of Decision Trees)

Claude Shannon's entropy formula:

```
H(S) = -Σ pᵢ × log₂(pᵢ)
```

Where pᵢ = fraction of class i in set S.

**Interpretation:** Entropy measures **impurity** or **uncertainty** in a dataset.

**Examples:**
- All examples same class: H = 0 (pure, certain)
- 50/50 split: H = 1 (maximum uncertainty for binary)
- 25/75 split: H = 0.811

Decision trees choose splits that **maximize information gain**:
```
Gain(S, A) = H(S) - Σ (|Sᵥ|/|S|) × H(Sᵥ)
```

Where Sᵥ is the subset of S where attribute A = value v.

---

## 🎬 Video Resources

| Topic | Video | Why Watch |
|-------|-------|-----------|
| ML introduction | [But what IS machine learning? — 3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk) | Perfect conceptual intro |
| Genetic Algorithms | [Genetic Algorithms — The Coding Train](https://www.youtube.com/watch?v=9zfeTw-uFCw) | Watch them evolve live! |
| Fuzzy Logic | [Fuzzy Logic explained — TechLead](https://www.youtube.com/watch?v=r804UF8Ia8c) | Practical examples |
| Boltzmann Machines | [RBM — Geoffrey Hinton lecture](https://www.youtube.com/watch?v=AyzOUbkUf3M) | From the inventor! |
| Decision Trees | [Decision Trees — StatQuest](https://www.youtube.com/watch?v=7VeUPuFGJHk) | Crystal clear |
| Bias-Variance | [Bias-Variance Tradeoff — StatQuest](https://www.youtube.com/watch?v=EuBBz3bI-aA) | The best explanation |

---

## 🔁 Worked Examples

### Example 1: Classify ML Approaches

| Scenario | Type of Learning |
|----------|----------------|
| Emails labeled spam/not-spam used to train filter | **Supervised** |
| Customer purchase data grouped into segments | **Unsupervised** |
| Robot learning to walk by trying movements | **Reinforcement** |
| Broken appliance diagnosed from 1 example + physics | **EBL** |
| Medical diagnosis based on similar patient records | **Analogy-based** |

---

### Example 2: Genetic Algorithm Trace

**Problem:** Maximize f(x) = x² where x is a 3-bit binary number (x ∈ 0-7)

**Population of 4:** [001, 011, 110, 100] = [1, 3, 6, 4]

**Fitness:** f(x) = x²
- 1² = 1, 3² = 9, 6² = 36, 4² = 16

**Selection** (proportional to fitness):
- Total fitness = 1+9+36+16 = 62
- Probabilities: 1/62, 9/62, 36/62, 16/62
- Most likely to select: 110 (x=6, highest fitness)

**Crossover** (parent 1: 110, parent 2: 011, crossover at position 1):
- Child 1: 1|11 = 111 (x=7, f=49 — better!)
- Child 2: 0|10 = 010 (x=2, f=4)

The GA discovered x=7 by combining good "building blocks" (the leading 1 from x=6, the ending 1 from x=3)!

---

### Example 3: Fuzzy Logic Inference

**System:** Temperature control

**Fuzzy sets for Temperature:**
- COLD: μ = max(0, (20-T)/20) for T < 20
- WARM: μ = 1 - |T-30|/10 for 20 ≤ T ≤ 40
- HOT: μ = max(0, (T-35)/15) for T > 35

At T = 32°C:
- μ_COLD(32) = 0 (not cold at all)
- μ_WARM(32) = 1 - |32-30|/10 = 0.8 (80% warm)
- μ_HOT(32) = max(0, (32-35)/15) = 0 (not hot yet)

**Rule:** IF temperature is WARM THEN set AC to MEDIUM speed.

With μ_WARM = 0.8, the AC is set to 80% of "MEDIUM" speed.

---

## ⚡ Exam-Ready Summary

### Types of Learning

| Type | Labeled Data | Goal | Example |
|------|-------------|------|---------|
| Supervised | Yes | Learn input-output mapping | Email spam filter |
| Unsupervised | No | Discover structure | Customer clustering |
| Reinforcement | Rewards | Maximize cumulative reward | Game-playing AI |
| EBL | One example + theory | Generalize from 1 | Robot learning from 1 demo |

### Genetic Algorithm Steps

1. Initialize random population
2. Evaluate fitness of each solution
3. Select parents (fitness-proportionate)
4. Crossover (combine parents)
5. Mutation (random change)
6. Repeat until convergence

### Fuzzy Logic Concepts

- **Membership function:** μ_A(x) ∈ [0,1] — degree of belonging
- **Fuzzy rules:** IF-THEN with fuzzy sets
- **Defuzzification:** Convert fuzzy output to crisp value (centroid method)
- **Operations:** NOT = 1-μ, AND = min, OR = max

### Boltzmann Machine Key Points

- Probabilistic neural network
- Energy-based model (lower energy = more probable)
- RBM: Restricted version — no within-layer connections
- Learning via Contrastive Divergence
- Foundation for Deep Belief Networks

---

## ✅ Chapter 6 Checklist

- [ ] Define the three types of ML with examples
- [ ] Explain what overfitting is and why it's a problem
- [ ] Draw and explain the GA process in 5 steps
- [ ] Perform a crossover operation on two binary chromosomes
- [ ] Explain what a fuzzy membership function is
- [ ] Calculate membership degrees for given values
- [ ] Explain the Boltzmann Machine energy function conceptually
- [ ] Explain what an RBM is and how it differs from a BM
- [ ] Define bias-variance tradeoff

---

## 🔗 Navigation

**← Previous:** [Chapter 5 — Structured Knowledge](ch05_structured_knowledge.md)  
**→ Next:** [Chapter 7 — Applications of AI](ch07_applications.md)  
**🏠 Home:** [README](../README.md)
