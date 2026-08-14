# Chapter 5: Structured Knowledge Representation
### *4 hours | 7 marks*

> **"Knowledge has a structure. If we represent it well, reasoning becomes trivial."**  
> — Marvin Minsky

---

## 🌍 The Hook — How Do You Store "What You Know"?

Logic (Chapter 4) is powerful but verbose. Writing everything as FOPL sentences is tedious.

Consider trying to represent everything you know about a "bird":
- It has wings
- It has a beak
- It can fly (usually)
- It lays eggs
- It has feathers
- It is an animal
- It has a Latin name
- It has a mass
- It has a habitat...

Logic would require a separate sentence for each fact. What if we could organize knowledge more naturally — like a **mental model** or a **filing cabinet**?

That's the goal of **structured knowledge representation**.

---

## 5.1 Representations and Mappings

### The Core Challenge

> **"How do we translate the real world into a form a machine can reason about?"**

This mapping has two components:

```
REAL WORLD          REPRESENTATION
────────────        ──────────────
Objects      ──────► Symbols/Nodes
Properties   ──────► Attributes/Slots
Relations    ──────► Links/Arcs
Events       ──────► State changes
```

Any representation must balance:

| Concern | Trade-off |
|---------|-----------|
| **Expressiveness** | More powerful = harder to compute |
| **Efficiency** | Faster = less expressive |
| **Completeness** | Can we represent everything needed? |
| **Naturalness** | Does it match human intuition? |

---

## 5.2 Approaches to Knowledge Representation

There are four main paradigms in AI:

### Approach 1: Logical (Declarative)

What we covered in Chapter 4 — facts and rules in formal logic.

```
All(x: Bird(x) → CanFly(x))
Bird(Tweety)
→ CanFly(Tweety)
```

**Pros:** Rigorous, supports automated reasoning  
**Cons:** Verbose, doesn't handle exceptions well

---

### Approach 2: Procedural

Knowledge stored as **how to do something** — procedures and algorithms.

```
HOW_TO: Find_Shortest_Path(graph, start, goal):
    1. Initialize open_list with start
    2. While open_list not empty...
    ...
```

**Pros:** Efficient for known procedures  
**Cons:** Hard to generalize or modify

---

### Approach 3: Network-Based

Knowledge stored as a **graph** — nodes connected by labeled relationships.

This is where **Semantic Nets** live.

---

### Approach 4: Structured Objects

Knowledge stored as **structured records** with named slots.

This is where **Frames** live.

---

## 5.3 Issues in Knowledge Representation

Before diving into specific methods, understand the challenges:

### Issue 1: The Frame Problem

> "When I pick up a block, what else changes?"

In the real world, we implicitly know: moving a block doesn't change the color of the sky, the temperature of the room, etc. But a machine needs to be told explicitly what stays the same.

**The frame problem:** How to represent which things stay unchanged when an action is performed?

### Issue 2: The Qualification Problem

Rules have exceptions:
- "Birds can fly" — except penguins, ostriches, dead birds, birds with broken wings...

How many qualifications do we add before we've covered everything?

### Issue 3: Closed World Assumption (CWA)

If we don't know something is true, is it false?

**CWA:** If the knowledge base doesn't contain P, assume ¬P.  
Example: "Who flies to Kathmandu on Sundays?" If the schedule doesn't list it → no one does.

This works for databases but fails for open-world reasoning.

### Issue 4: The Completeness Problem

Can we ever represent ALL knowledge? No — knowledge representation is always a useful **partial model**, not a complete one.

---

## 5.4 Semantic Networks

### What Are They?

A **semantic network** is a graph where:
- **Nodes** = concepts or objects
- **Arcs (edges)** = labeled relationships between concepts

```
         IS-A                   HAS
Animal ◄──────── Bird ──────────────► Wings
         IS-A        │
                     │ CAN
                     ▼
                    Fly
                     ▲
              IS-A   │
           ┌─────────┘
           │
          Eagle ──── IS-A ──► Raptor
           │
           └─── HAS-A ──► Talons
```

### Key Relationships in Semantic Networks

| Relationship | Meaning | Example |
|-------------|---------|---------|
| **IS-A** | Class membership | Eagle IS-A Bird |
| **AKO (A-Kind-Of)** | Subclass | Bird AKO Animal |
| **HAS-PART** | Part-of relationship | Bird HAS-PART Wings |
| **CAN** | Capability | Bird CAN Fly |
| **LOCATION** | Where something is | Eagle LOCATION Mountain |

### Inheritance in Semantic Networks

The power of IS-A hierarchies: **properties are inherited down the hierarchy**.

```
Animal ─── HAS ──► Heart
  ↑ IS-A
Bird ─── CAN ──► Fly
  ↑ IS-A
Eagle
```

Eagle inherits from Bird:
- Eagle CAN Fly (inherited from Bird)
- Eagle HAS Heart (inherited from Animal via Bird)

We don't need to repeat "has heart" for every animal — inheritance handles it automatically!

### Exception Handling in Semantic Networks

```
Animal ─── CAN ──► Breathe
  ↑ IS-A
Bird ─── CAN ──► Fly
  ↑ IS-A
Penguin ─── CANNOT ──► Fly (overrides inherited CAN Fly!)
```

The **most specific** rule wins — Penguin's local property overrides the inherited one.

### A Complete Example: Transportation Network

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Vehicle ──HAS──► Engine                                        │
│    ↑IS-A                                                        │
│  ┌─────────────────────────────────────────────┐               │
│  │                                             │               │
│ Land Vehicle                               Air Vehicle          │
│  ↑IS-A                ↑IS-A                  ↑IS-A             │
│  │                    │                       │                │
│  Car               Motorcycle               Airplane           │
│  │HAS                 │HAS                   │HAS             │
│  ▼                    ▼                       ▼               │
│ 4 Wheels           2 Wheels               Wings               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

From this network, we can infer:
- Airplane IS-A Vehicle → Airplane HAS-A Engine (inherited)
- Car IS-A Land Vehicle IS-A Vehicle → Car HAS-A Engine

---

### Limitations of Semantic Networks

- Hard to represent **quantifiers** ("some", "all", "most")
- Hard to represent **negative** information
- Hard to represent **procedural** knowledge
- No standard notation — different systems use different labels
- Can become unclear for complex relationships

---

## 5.5 Frames

### What Are They?

A **frame** is a structured record (like a class in programming) that represents a **stereotyped situation**.

Think of it as a template: "What does a typical X look like?"

```
┌────────────────────────────────────┐
│ FRAME: Bird                        │
├────────────────┬───────────────────┤
│ SLOT           │ VALUE             │
├────────────────┼───────────────────┤
│ IS-A           │ Animal            │
│ Body-Covering  │ Feathers          │
│ Locomotion     │ Flying, Walking   │
│ Reproduction   │ Egg-laying        │
│ Number-of-legs │ 2                 │
│ Has-wings      │ True              │
└────────────────┴───────────────────┘
```

### Frame Hierarchy (Inheritance)

```
┌───────────────────────────────┐
│ FRAME: Animal                 │
│ IS-A: Living-Thing            │
│ Breathes: True                │
│ Reproduction: varies          │
└───────────────────────────────┘
              ↑ IS-A
┌───────────────────────────────┐
│ FRAME: Bird                   │
│ IS-A: Animal                  │
│ Body-Covering: Feathers        │ ← overrides Animal's default
│ Locomotion: Flying, Walking   │
│ Number-of-legs: 2             │
└───────────────────────────────┘
              ↑ IS-A
┌───────────────────────────────┐
│ FRAME: Eagle                  │
│ IS-A: Bird                    │
│ Diet: Carnivore               │ ← adds new slot
│ Habitat: Mountains            │
│ Wingspan: 2 meters            │
└───────────────────────────────┘
```

Eagle inherits from Bird and Animal. Its own slots **override** inherited ones where specified.

### Slots and Facets

Each slot in a frame can have multiple **facets**:

```
FRAME: Person
  Slot: Age
    VALUE: (blank — to be filled)
    DEFAULT: 30
    CONSTRAINT: Integer, 0-150
    IF-ADDED: Update-age-dependent-calculations
    IF-REMOVED: Warn-about-data-deletion
    IF-NEEDED: Ask-user-for-age
```

**Demons** (IF-ADDED, IF-NEEDED, IF-REMOVED) make frames **active** — they can trigger procedures when slots change!

### Frame Example: Medical Knowledge

```
FRAME: Patient
  Name: (value)
  Age: (value, default 0)
  Symptoms: (value, multiple allowed)
  Diagnosis: (inferred from symptoms)
  Treatment: (IF-NEEDED: call treatment-selection-procedure)

FRAME: COVID-19-Patient
  IS-A: Patient
  Symptoms: Fever, Cough, Fatigue
  Quarantine-required: True
  Treatment: Antiviral + Rest
```

When we create an instance of COVID-19-Patient with a name and age, it automatically inherits treatment protocols!

---

## 5.6 Conceptual Dependencies

### The Idea

Developed by **Roger Schank** in the 1970s, Conceptual Dependency (CD) theory says:

> **"Any meaning that can be expressed in any human language can be represented using a small set of primitive actions."**

Schank identified **~12 primitive actions** (ACTs):

| Primitive | Meaning | Example |
|-----------|---------|---------|
| **ATRANS** | Transfer of abstract relationship | Give, take |
| **PTRANS** | Physical transfer of location | Go, carry |
| **MTRANS** | Transfer of mental information | Tell, read |
| **MBUILD** | Mental construction | Infer, decide |
| **INGEST** | Take into body | Eat, drink, breathe |
| **EXPEL** | Expel from body | Bleed, cry |
| **PROPEL** | Apply force | Hit, throw, push |
| **MOVE** | Move body part | Nod, wave hand |
| **GRASP** | Physical grip | Grab, release |
| **SPEAK** | Produce sounds | Say, sing |

### Example: "John gave Mary a book"

In CD notation:

```
John ─── ATRANS ──► book
     ─── FROM ──► John
     ─── TO ──► Mary
     ─── TIME ──► past
```

And "Mary gave John money":

```
Mary ─── ATRANS ──► money
     ─── FROM ──► Mary
     ─── TO ──► John
     ─── TIME ──► past
```

**Notice:** Although the English sentences look different, similar deep structures emerge for the same type of action.

### Why This Matters

CD theory allows AI to:
- Understand that "John transferred the book to Mary" and "John gave Mary the book" mean the same thing
- Make inferences ("If X AINGESTed food, then X is less hungry")
- Translate between languages by working at the conceptual level

---

## 5.7 Scripts

### What Are Scripts?

A **script** is a frame-like structure that represents a **stereotyped sequence of events** — a story template.

Developed by Schank and Abelson in their famous book "Scripts, Plans, Goals and Understanding" (1977).

### The Restaurant Script

This is the canonical example:

```
SCRIPT: Restaurant
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRACK: Fancy-Restaurant (specific variation)

PROPS:    Tables, chairs, menus, food, money, waiter, kitchen

ROLES:    Customer (C), Waiter (W), Chef (Ch), Cashier

ENTRY CONDITIONS:
  - Customer is hungry
  - Customer has money

SCENE 1: Entering
  C PTRANS into restaurant
  C MBUILD where-to-sit
  C PTRANS to table
  C MOVE body to sitting-position

SCENE 2: Ordering
  W PTRANS to table
  W MTRANS menu to C
  C MBUILD what-to-order
  C MTRANS order to W
  W PTRANS to kitchen
  W MTRANS order to Ch

SCENE 3: Eating
  Ch INGEST (prepares food)
  W PTRANS food to C
  C INGEST food

SCENE 4: Leaving
  W MTRANS bill to C
  C ATRANS money to W or cashier
  C PTRANS out of restaurant

EXIT CONDITIONS:
  - Customer is not hungry
  - Customer has less money
  - Restaurant has more money
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Why Scripts Are Powerful

When an AI reads: *"John went to a restaurant. He left a big tip."*

Without a script, the AI can't connect these sentences.  
With the restaurant script, the AI can infer:
- John was hungry (entry condition)
- John ate food (Scene 3)
- The service was apparently good (explanation for big tip)
- John paid (Scene 4)

**Scripts allow AI to fill in the blanks — to "understand" by recognizing familiar patterns.**

### Script Variations

Scripts have:
- **Tracks:** Variations (fancy restaurant vs. fast food)
- **Default values:** What usually happens if not specified
- **Open slots:** What must be filled in (what he ordered)
- **Interference conditions:** What might disrupt the script (restaurant out of food)

---

## 📐 Math Intuition Corner

### Set Theory Foundation of Semantic Nets

Semantic network IS-A and AKO hierarchies correspond to set theory:

```
If Eagle IS-A Bird and Bird IS-A Animal:

  Eagle ⊆ Bird ⊆ Animal

Any property P of Animal:
  ∀x ∈ Animal: P(x) is true
  Since Eagle ⊆ Animal: ∀x ∈ Eagle: P(x) is true
```

**Inheritance = subset transitivity!**

---

## 🎬 Video Resources

| Topic | Video | Why Watch |
|-------|-------|-----------|
| Semantic Networks | [Semantic Networks — AI lecture](https://www.youtube.com/watch?v=4tKFaG3eNcs) | Visual walkthrough |
| Frames in AI | [Frames and Schemas](https://www.youtube.com/watch?v=wRo5fkq_56I) | Clear explanation |
| Knowledge Representation overview | [Knowledge Rep — MIT OpenCourseWare](https://www.youtube.com/watch?v=9WfNjB8vPo4) | Academic depth |
| Conceptual Dependency | [Roger Schank on Scripts and CD](https://www.youtube.com/watch?v=Qnqnxt1y-Is) | From the creator himself! |

---

## 🔁 Worked Examples

### Example 1: Build a Semantic Network

**Domain:** Computer Science classes

```
Knowledge:
- Data Structures IS-A Course
- Algorithms IS-A Course
- Algorithms AKO Data-Structures (algorithms builds on it)
- Algorithms HAS-TOPIC: Sorting, Searching, Graphs
- Data Structures HAS-TOPIC: Arrays, Trees, Linked-Lists
- Course IS-A University-Subject
- University-Subject HAS: Credits, Grade
```

**Draw:** Connect these as a semantic net with labeled arcs.

**Inference from the net:**
- What topics does Algorithms have? → Sorting, Searching, Graphs (direct)
- Does Algorithms have Credits? → Yes (inherited: Algorithms IS-A Course IS-A University-Subject HAS Credits)

---

### Example 2: Create a Frame

**Create a frame for a University Student:**

```
FRAME: University-Student
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IS-A:      Person
Name:      (required, string)
Student-ID: (required, unique integer)
Semester:  (value: 1-8, default: 1)
Courses:   (multiple values allowed)
CGPA:      (float 0.0-4.0, computed from grades)
Status:    (options: Active/Inactive/Graduated)

Slot: CGPA
  IF-NEEDED: Calculate from grade history

Slot: Status
  IF-ADDED: If Status = Graduated, archive record
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Example 3: Apply a Script

**Story:** "Maria went to the bank. She waited in line. Then she handed the teller her check and got cash."

**Script:** Withdraw-Money-from-Bank

Without the script, each sentence is independent.  
With the script, the AI fills in:
- Maria had an account
- Maria filled out a withdrawal form (implicit)
- The teller verified her identity (implicit)
- Maria now has less money in her account (exit condition)

---

## ⚡ Exam-Ready Summary

### 4 Approaches to Knowledge Representation

| Approach | Method | Best For |
|----------|--------|----------|
| Logical | FOPL sentences | Formal reasoning, proofs |
| Procedural | Algorithms, programs | "How to do" knowledge |
| Network | Semantic nets | Taxonomies, relationships |
| Structured | Frames, Scripts | Stereotyped situations |

### Semantic Networks: Key Points

- Nodes = concepts, Edges = labeled relationships
- IS-A enables inheritance (properties flow downward)
- Most-specific rule wins (exceptions override inherited properties)
- AKO = subclass relationship between classes

### Frames: Key Points

- Template for a stereotyped concept or situation
- Has **slots** (attributes) with **facets** (metadata)
- Supports inheritance through IS-A hierarchy
- **Demons** (IF-ADDED, IF-NEEDED) add active behavior

### Scripts: Key Points

- Represent sequences of events in typical situations
- Components: Props, Roles, Entry/Exit conditions, Scenes
- Enable understanding through pattern recognition and default filling
- Developed by Roger Schank

### Conceptual Dependencies: Key Points

- ALL meanings reducible to ~12 primitive actions
- Enables language-independent reasoning
- Key primitives: ATRANS, PTRANS, MTRANS, INGEST, PROPEL

---

## ✅ Chapter 5 Checklist

- [ ] Explain what a semantic network is and draw one with IS-A and HAS relationships
- [ ] Demonstrate inheritance in a semantic network
- [ ] Explain how exceptions are handled in semantic nets
- [ ] Create a frame for a given concept with appropriate slots and facets
- [ ] Explain the role of demons (IF-ADDED, IF-NEEDED)
- [ ] Write out the restaurant script from memory
- [ ] Name 5 CD primitives and give examples
- [ ] Explain the frame problem and why it's important
- [ ] Compare semantic nets vs. frames vs. scripts

---

## 🔗 Navigation

**← Previous:** [Chapter 4 — Knowledge Representation](ch04_knowledge_reasoning.md)  
**→ Next:** [Chapter 6 — Machine Learning](ch06_machine_learning.md)  
**🏠 Home:** [README](../README.md)
