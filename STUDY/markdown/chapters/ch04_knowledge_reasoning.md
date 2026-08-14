# Chapter 4: Knowledge Representation, Inference & Reasoning
### *8 hours | 14 marks — HIGHEST PRIORITY (tied with Ch.7)*

> **"Logic is the cement of our civilization with which we ascend from chaos using reason as our guide."**  
> — Gene Roddenberry

---

## 🌍 The Hook — What Does It Mean to "Know" Something?

Your brain stores billions of facts:
- "Kathmandu is in Nepal"
- "If it's raining, I should carry an umbrella"
- "All humans are mortal"

And you can *reason* with these facts:
- From "Socrates is human" and "All humans are mortal" → "Socrates is mortal"

**AI needs to do the same thing.** But a machine can't hold informal knowledge — it needs a **formal language** for representing facts and a **formal system** for drawing conclusions.

This chapter is about exactly that: **formal logic as a tool for AI reasoning**.

---

## 4.1 Formal Logic — The Foundation

### Why Logic?

Logic gives us:
1. **Precision** — no ambiguity
2. **Soundness** — if premises are true, conclusions must be true
3. **Completeness** — all true things can be proven

These properties make logic a foundation for AI systems that need to reason reliably.

### Core Concepts

#### 4.1.1 Logical Connectives

These are the building blocks of logical statements:

| Symbol | Name | Meaning | Example |
|--------|------|---------|---------|
| ¬ | NOT (Negation) | Opposite | ¬P = "not P" |
| ∧ | AND (Conjunction) | Both true | P ∧ Q = "P and Q" |
| ∨ | OR (Disjunction) | At least one true | P ∨ Q = "P or Q" |
| → | IMPLIES (Implication) | If P then Q | P → Q |
| ↔ | IFF (Biconditional) | P if and only if Q | P ↔ Q |

#### 4.1.2 Truth Tables

Truth tables show the value of a formula for all possible input values.

**For P → Q (implication):**

| P | Q | P → Q |
|---|---|-------|
| T | T | **T** |
| T | F | **F** |
| F | T | **T** |
| F | F | **T** |

> 🧠 **Why is F→T true?** This is called "vacuous truth." If the premise is false, the implication doesn't fire at all. Think: "If it rains, I'll carry an umbrella" — if it doesn't rain, I haven't broken my promise regardless of what I do.

**For P ↔ Q (biconditional):**

| P | Q | P ↔ Q |
|---|---|-------|
| T | T | **T** |
| T | F | **F** |
| F | T | **F** |
| F | F | **T** |

#### 4.1.3 Tautology and Contradiction

> **Tautology:** A formula that is **always true** regardless of variable values.
> **Contradiction:** A formula that is **always false**.
> **Contingency:** Neither — sometimes true, sometimes false.

**Examples:**
- P ∨ ¬P — always true (tautology) — "Either it rains or it doesn't"
- P ∧ ¬P — always false (contradiction) — "It rains and doesn't rain simultaneously"
- P → Q — depends on P and Q (contingency)

**How to check:** Build the truth table. If last column is all T → tautology. All F → contradiction.

#### 4.1.4 Well-Formed Formulas (WFF)

A WFF is a valid, grammatically correct logical expression.

**Rules:**
- Any single atom (P, Q, R...) is a WFF
- If A is a WFF, so is ¬A
- If A and B are WFFs, so are: A∧B, A∨B, A→B, A↔B
- Nothing else is a WFF

**Valid WFFs:** P, ¬Q, P∧Q, (P→Q)↔(¬Q→¬P)  
**Invalid:** ∧P, Q∧∧R, →P

#### 4.1.5 Syntax vs. Semantics

| Aspect | Syntax | Semantics |
|--------|--------|-----------|
| **Meaning** | Grammar — *how* to write it | Meaning — *what* it says |
| **Focus** | Form of the formula | Truth value of the formula |
| **Example** | "P∧Q" is syntactically valid | Under P=T, Q=F, its value is F |

---

## 4.2 Propositional Logic

### What Is It?

Propositional logic deals with **propositions** — statements that are either true or false.

**Propositions:** "It is raining" (P), "The road is wet" (Q)  
**Not propositions:** "Is it raining?" (question), "Close the door!" (command)

### Key Laws

These are fundamental identities you must know:

| Law | Formula |
|-----|---------|
| **De Morgan's (AND)** | ¬(P∧Q) ≡ ¬P∨¬Q |
| **De Morgan's (OR)** | ¬(P∨Q) ≡ ¬P∧¬Q |
| **Double Negation** | ¬¬P ≡ P |
| **Contrapositive** | P→Q ≡ ¬Q→¬P |
| **Modus Ponens** | P, P→Q ⊢ Q |
| **Modus Tollens** | ¬Q, P→Q ⊢ ¬P |

> **De Morgan's Law intuition:** "Not (A and B)" = "Not A or Not B"  
> Think: "It's not true that (it's both raining AND sunny)" = "Either it's not raining OR it's not sunny"

### Limitations of Propositional Logic

Propositional logic cannot express:
- **Generalizations:** "All birds can fly" — would need one proposition per bird
- **Relationships:** "Socrates is taller than Plato"
- **Quantification:** "There exists an x such that..."

This is why we need **Predicate Logic.**

---

## 4.3 Predicate Logic (First-Order Predicate Logic — FOPL)

### The Big Upgrade

FOPL adds two powerful things to propositional logic:

1. **Objects** and **predicates** about them
2. **Quantifiers** (∀ and ∃)

### 4.3.1 Syntax of FOPL

**Terms:**
- Constants: specific objects (John, Kathmandu, 5)
- Variables: stand for any object (x, y, z)
- Functions: map objects to objects (father(John), add(2,3))

**Predicates:** Express properties or relationships
- Unary: Human(Socrates) — "Socrates is human"
- Binary: Loves(John, Mary) — "John loves Mary"
- n-ary: Between(x, y, z) — "x is between y and z"

**Formulas:** Built with predicates, connectives, and quantifiers

---

### 4.3.2 Quantification

#### Universal Quantifier: ∀ (For All)

> ∀x P(x) = "For every object x, P(x) is true"

**Example:** ∀x [Human(x) → Mortal(x)]  
= "For all x, if x is human, then x is mortal"

#### Existential Quantifier: ∃ (There Exists)

> ∃x P(x) = "There exists some object x such that P(x) is true"

**Example:** ∃x [Loves(John, x)]  
= "There exists someone that John loves"

#### Quantifier Interaction

| Formula | Meaning |
|---------|---------|
| ∀x∀y P(x,y) | Everyone relates P to everyone |
| ∃x∃y P(x,y) | Someone relates P to someone |
| ∀x∃y P(x,y) | Everyone has someone they relate P to |
| ∃x∀y P(x,y) | Someone relates P to everyone |

> ⚠️ **Order matters!** ∀x∃y ≠ ∃x∀y  
> ∀x∃y Loves(x,y) = "Everyone loves someone" (each person may love a different person)  
> ∃x∀y Loves(x,y) = "There is someone who loves everyone" (much stronger!)

#### De Morgan's for Quantifiers

| Formula | Equivalent |
|---------|-----------|
| ¬∀x P(x) | ∃x ¬P(x) |
| ¬∃x P(x) | ∀x ¬P(x) |

"Not everyone is tall" = "Someone is not tall"  
"No one is perfect" = "Everyone is not perfect"

---

### 4.3.3 Worked Example: Translating English → FOPL

**Sentence:** "Every student who studies hard passes the exam."

Let:
- Student(x) = "x is a student"
- Studies(x) = "x studies hard"
- Passes(x) = "x passes the exam"

**Translation:**  
∀x [Student(x) ∧ Studies(x) → Passes(x)]

---

**Sentence:** "Some professors are both researchers and teachers."

Let:
- Prof(x) = "x is a professor"
- Researcher(x) = "x is a researcher"
- Teacher(x) = "x is a teacher"

**Translation:**  
∃x [Prof(x) ∧ Researcher(x) ∧ Teacher(x)]

---

### 4.3.4 Interpretation in FOPL

An **interpretation** assigns meaning to:
- A **domain** (set of objects)
- Meaning to constants (which object each constant refers to)
- Meaning to predicates (which tuples satisfy them)
- Meaning to functions (what they compute)

**Example:**
Domain = {people in a classroom}  
Constant "Alice" → refers to Alice  
Predicate Smart(x) → {Alice, Bob, Charlie}  
Under this interpretation: Smart(Alice) is TRUE

A formula is **valid** if it's true under ALL interpretations.  
A formula is **satisfiable** if it's true under SOME interpretation.

---

## 4.4 Horn Clauses

### What Are They?

A **Horn clause** is a special form of logical statement:

```
p₁ ∧ p₂ ∧ ... ∧ pₙ → q
```

Where:
- p₁...pₙ are **positive** literals (the conditions)
- q is a **single positive** conclusion

Or equivalently in clause form: ¬p₁ ∨ ¬p₂ ∨ ... ∨ ¬pₙ ∨ q  
(At most ONE positive literal)

**Why Horn clauses matter:**  
- They are the basis of **Prolog** (the AI programming language)
- Resolution on Horn clauses is efficient — **linear time!**
- Most real knowledge bases can be expressed as Horn clauses

**Example Horn clauses:**
```
parent(tom, bob)        ← fact (no conditions)
parent(bob, ann)        ← fact
ancestor(X, Y) :- parent(X, Y)         ← rule
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y)  ← recursive rule
```

---

## 4.5 Rules of Inference

These are the valid patterns of reasoning — formal "moves" you can make:

### The Essential Set

#### 1. Modus Ponens (MP) — Most Important!

```
P
P → Q
──────
Q
```

*"If P is true, and P implies Q, then Q is true."*

**Example:**
- It is raining. (P)
- If it rains, the road is wet. (P → Q)
- Therefore: The road is wet. (Q) ✅

---

#### 2. Modus Tollens (MT)

```
¬Q
P → Q
──────
¬P
```

*"If Q is false, and P would imply Q, then P must be false."*

**Example:**
- The road is NOT wet. (¬Q)
- If it rains, the road is wet. (P → Q)
- Therefore: It is NOT raining. (¬P) ✅

---

#### 3. And-Introduction

```
P
Q
──────
P ∧ Q
```

#### 4. And-Elimination

```
P ∧ Q
──────
P   (or Q)
```

#### 5. Hypothetical Syllogism (Chain Rule)

```
P → Q
Q → R
──────
P → R
```

*"If A leads to B, and B leads to C, then A leads to C."*

---

#### 6. Disjunctive Syllogism

```
P ∨ Q
¬P
──────
Q
```

*"Either P or Q. P is false. Therefore Q."*

---

#### 7. Resolution (Generalization of MP — key for AI!)

```
P ∨ Q
¬P ∨ R
────────
Q ∨ R
```

This is the most powerful rule — it's the basis of automated theorem proving!

---

## 4.6 Unification

### What Is It?

**Unification** is the process of making two logical expressions identical by substituting variables.

It's like pattern matching — "Can these two expressions be made to match?"

### How It Works

Given two atoms, find a **substitution** (θ) that makes them identical.

**Example:**

Unify: f(x, b) and f(a, y)

Substitution: {x ← a, y ← b}

Result: f(a, b) = f(a, b) ✅ **Unified!**

**Another example:**

Unify: P(x, f(x)) and P(a, f(a))

Substitution: {x ← a}

Result: P(a, f(a)) = P(a, f(a)) ✅

**Failure case:**

Unify: P(a, b) and P(a, c) — b and c are different constants → **FAIL** ❌

### The Occur Check

The substitution {x ← f(x)} would create an infinite loop:
x = f(x) = f(f(x)) = f(f(f(x))) ...

**Never substitute a variable with a term that contains itself!**

---

## 4.7 Resolution Refutation System (RRS)

### The Big Idea

> **"To prove a statement is true, assume it's false and derive a contradiction."**

This is called **Proof by Contradiction** or **Refutation**.

### The Steps

1. **Negate** the goal (what you want to prove)
2. **Convert** all sentences to **Conjunctive Normal Form (CNF)**
3. **Apply Resolution** repeatedly until you get the empty clause (contradiction!)
4. **Conclusion:** The original goal is TRUE.

### CNF Conversion Steps

To convert to CNF:
1. Eliminate ↔ using: P↔Q ≡ (P→Q)∧(Q→P)
2. Eliminate → using: P→Q ≡ ¬P∨Q
3. Move ¬ inward using De Morgan's and double negation
4. Distribute ∨ over ∧

### Worked Example: RRS

**Knowledge Base:**
1. Human(Socrates) — "Socrates is human"
2. ∀x [Human(x) → Mortal(x)] — "All humans are mortal"

**Goal to prove:** Mortal(Socrates)

**Steps:**

Step 1: Negate goal → ¬Mortal(Socrates)

Step 2: Convert KB to clause form:
- Clause 1: Human(Socrates)
- Clause 2: ¬Human(x) ∨ Mortal(x) [from rule 2 after conversion]
- Clause 3: ¬Mortal(Socrates) [negated goal]

Step 3: Apply Resolution:

```
Resolve Clause 1 and Clause 2 (with x = Socrates):
Human(Socrates) + ¬Human(Socrates) ∨ Mortal(Socrates)
→ Mortal(Socrates)

Resolve this with Clause 3:
Mortal(Socrates) + ¬Mortal(Socrates)
→ □ (empty clause — CONTRADICTION!)
```

Step 4: Contradiction found → Original goal **Mortal(Socrates)** is TRUE ✅

---

## 4.8 Answer Extraction from RRS

The RRS can also be modified to **extract answers** to queries, not just verify them.

**Example:**

**Query:** "Who is mortal?" = ∃x Mortal(x)?

**Modified approach:** Add "answer literal" to negated goal.

Negate and add answer literal:  
¬Mortal(x) ∨ Answer(x)

When resolution produces Answer(Socrates) — that's your answer!

---

## 4.9 Rule-Based Deduction Systems

### Two Directions of Reasoning

#### Forward Chaining (Data-Driven)

> **"Start from what you know. Apply rules. See what new facts you can derive. Repeat."**

```
Known Facts:     Rules:             Derived:
{A, B}     →    A ∧ B → C    →    {A, B, C}
                C → D         →    {A, B, C, D}
                A ∧ D → E     →    {A, B, C, D, E} ← GOAL!
```

Good for: **generating all consequences** of a set of facts.

#### Backward Chaining (Goal-Driven)

> **"Start from the goal. Work backward to see what facts would prove it."**

```
Goal: Prove E
      ↓
What proves E? → A ∧ D → E
      ↓
Sub-goals: Prove A, Prove D
      ↓
A is a fact ✅. What proves D? → C → D
      ↓
Sub-goal: Prove C → C is a fact ✅
DONE!
```

Good for: **answering specific queries** — only explores relevant rules.

### Comparison

| Feature | Forward Chaining | Backward Chaining |
|---------|-----------------|------------------|
| Direction | Facts → Goals | Goals → Facts |
| Driven by | Available data | Query/Goal |
| Good for | Deriving all consequences | Answering specific questions |
| Used in | Expert systems, databases | Prolog, query answering |

---

## 4.10 Statistical Reasoning — Probability and Bayes' Theorem

### Why Probability in AI?

The world is **uncertain**. Logic gives us certainty. But:
- "Will it rain tomorrow?" — we can't know for sure
- "Does this patient have cancer?" — symptoms give evidence, not certainty

We need a way to **reason under uncertainty** → **Probability Theory**.

### 4.10.1 Basic Probability

```
P(A) = probability that event A occurs
0 ≤ P(A) ≤ 1

P(Ω) = 1 (something must happen)
P(∅) = 0 (impossible event)
```

**Joint Probability:**
P(A ∧ B) = P(A) × P(B|A)

Where P(B|A) = conditional probability of B given A.

### 4.10.2 Bayes' Theorem — The Crown Jewel of Statistical AI

```
         P(B|A) × P(A)
P(A|B) = ─────────────
               P(B)
```

**In words:**
```
            P(Evidence | Hypothesis) × P(Hypothesis)
P(Hypothesis | Evidence) = ────────────────────────────────
                                   P(Evidence)
```

**Or using intuitive names:**

```
         Likelihood × Prior
Posterior = ──────────────────
               Evidence
```

> This is the fundamental formula for **updating beliefs given new evidence**.

#### Example: Medical Diagnosis

A disease affects 1% of the population. A test is:
- 99% accurate (if sick, 99% chance positive)
- 1% false positive rate (if healthy, 1% chance positive)

**Question:** If you test positive, what's the probability you're actually sick?

Using Bayes:
- P(Sick) = 0.01 (prior — disease rate)
- P(+|Sick) = 0.99 (likelihood — true positive rate)
- P(+) = P(+|Sick)×P(Sick) + P(+|Healthy)×P(Healthy)
        = 0.99×0.01 + 0.01×0.99
        = 0.0099 + 0.0099 = 0.0198

```
         0.99 × 0.01
P(Sick|+) = ──────────── = 0.0099/0.0198 ≈ 50%
               0.0198
```

**Shocking result!** Even with a 99% accurate test and a positive result, you're only ~50% likely to be sick!

This is the **base rate fallacy** — the rarity of the disease matters enormously.

---

### 4.10.3 Causal Networks (Bayesian Networks)

A **Bayesian network** is a directed graph where:
- **Nodes** = random variables
- **Edges** = causal relationships (A → B means A causes B)
- Each node has a **conditional probability table (CPT)**

**Example: Alarm Network (classic AI example)**

```
[Burglary]  [Earthquake]
     \          /
      ↓        ↓
      [Alarm]
      /     \
     ↓       ↓
[JohnCalls] [MaryCalls]
```

Given probability tables:
- P(Burglary) = 0.001
- P(Earthquake) = 0.002
- P(Alarm | Burglary, Earthquake) = various conditional probabilities

**Query:** P(Burglary | JohnCalls, MaryCalls) ?

This is what Bayesian networks excel at — **probabilistic inference** through a causal model.

### Reasoning in Belief Networks

Three types of inference:

| Type | Direction | Example |
|------|-----------|---------|
| **Causal** | Parents → Children | Burglary → Alarm → JohnCalls |
| **Diagnostic** | Children → Parents | JohnCalls → Alarm → Burglary |
| **Intercausal** | Between parents via child | Burglary ↔ Earthquake (given Alarm) |

"Explaining away" phenomenon: If we know the alarm is on AND we learn there was an earthquake, our belief in burglary goes DOWN — the earthquake "explains away" the alarm.

---

## 📐 Math Intuition Corner

### Why Resolution is Complete

The Resolution rule is **refutation complete** for first-order logic:
- If a set of clauses is unsatisfiable, resolution will derive the empty clause
- This takes at most exponential time in the worst case
- For Horn clauses: linear time!

### The Connection Between Logic and Probability

| Logic | Probability |
|-------|------------|
| P is True/False | P(A) ∈ [0,1] |
| P → Q | P(Q|P) = 1 |
| P ∧ Q | P(A∩B) |
| P ∨ Q | P(A∪B) |

Probability is logic under uncertainty.

---

## 🎬 Video Resources

| Topic | Video | Why Watch |
|-------|-------|-----------|
| Propositional Logic | [Intro to Logic — Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic) | Interactive exercises |
| FOPL and Quantifiers | [First Order Logic — Computerphile](https://www.youtube.com/watch?v=GFjSJA0Sfrc) | Clear UK academic explanation |
| Bayes Theorem visual | [Bayes theorem geometry — 3Blue1Brown](https://www.youtube.com/watch?v=HZGCoVF3YvM) | Absolutely stunning visual proof |
| Bayes theorem clear | [Bayes Theorem — StatQuest](https://www.youtube.com/watch?v=9wCnvr7Xw4E) | Clearest step-by-step ever |
| Bayesian Networks | [Bayesian Networks explained](https://www.youtube.com/watch?v=TuGDMj43ehw) | Practical and conceptual |
| Resolution in logic | [Resolution principle explained](https://www.youtube.com/watch?v=sIwl3IUHG4Q) | Worked examples |

---

## 🔁 Worked Examples

### Example 1: Truth Table Verification

**Verify that the Contrapositive (P→Q) ≡ (¬Q→¬P) is a tautology:**

| P | Q | P→Q | ¬Q | ¬P | ¬Q→¬P |
|---|---|-----|----|----|-------|
| T | T | T | F | F | T |
| T | F | F | T | F | F |
| F | T | T | F | T | T |
| F | F | T | T | T | T |

Column 3 = Column 6 → **They are equivalent (tautology)** ✅

---

### Example 2: FOPL Translation

**English:** "No student failed both Math and Science."

**Step 1:** Let:
- Student(x), Failed_Math(x), Failed_Science(x)

**Step 2:** "No student failed both" = "For all x, if x is a student, then not (x failed math AND x failed science)"

**FOPL:** ∀x [Student(x) → ¬(Failed_Math(x) ∧ Failed_Science(x))]

**Equivalent:** ∀x [Student(x) → (¬Failed_Math(x) ∨ ¬Failed_Science(x))]

---

### Example 3: Resolution Step by Step

**Prove:** "John is mortal" given:
1. Human(John)
2. ∀x Human(x) → Mortal(x)

**CNF conversion:**
1. Human(John)
2. ¬Human(x) ∨ Mortal(x)
3. ¬Mortal(John) [negated goal]

**Resolution:**
- Step 1: Resolve (1) and (2) with {x ← John}:
  {Human(John)} and {¬Human(John) ∨ Mortal(John)}
  → {Mortal(John)}

- Step 2: Resolve {Mortal(John)} and (3) {¬Mortal(John)}
  → {} empty clause! ✅

**Conclusion:** Mortal(John) is proved!

---

## ⚡ Exam-Ready Summary

### Logical Connectives Quick Reference

| Symbol | Name | P=T,Q=T | P=T,Q=F | P=F,Q=T | P=F,Q=F |
|--------|------|---------|---------|---------|---------|
| ¬P | NOT | F | F | T | T |
| P∧Q | AND | T | F | F | F |
| P∨Q | OR | T | T | T | F |
| P→Q | IF-THEN | T | **F** | T | T |
| P↔Q | IFF | T | F | F | T |

### FOPL vs. Propositional Logic

| Feature | Propositional | Predicate (FOPL) |
|---------|--------------|-----------------|
| Objects | No | Yes |
| Predicates | No | Yes |
| Quantifiers | No | ∀ and ∃ |
| Expressiveness | Limited | Full (Turing complete) |

### Inference Rules to Memorize

1. **Modus Ponens:** P, P→Q ⊢ Q
2. **Modus Tollens:** ¬Q, P→Q ⊢ ¬P
3. **Hypothetical Syllogism:** P→Q, Q→R ⊢ P→R
4. **Resolution:** P∨Q, ¬P∨R ⊢ Q∨R

### Bayes' Theorem

```
P(H|E) = P(E|H) × P(H) / P(E)
```
- P(H) = Prior probability
- P(E|H) = Likelihood
- P(H|E) = Posterior probability
- P(E) = Evidence (normalizing constant)

---

## ✅ Chapter 4 Checklist

- [ ] Build truth tables for all 5 connectives
- [ ] Identify tautologies, contradictions, contingencies
- [ ] Translate 5 English sentences to FOPL
- [ ] Use ∀ and ∃ correctly, explain their difference
- [ ] Apply De Morgan's laws (both propositional and quantifier versions)
- [ ] Apply Modus Ponens and Modus Tollens
- [ ] Explain what unification is with an example
- [ ] Trace the RRS (Resolution Refutation) procedure step by step
- [ ] Apply Bayes' theorem to a medical diagnosis problem
- [ ] Explain what a Bayesian Network is and draw a simple one
- [ ] Explain forward vs. backward chaining with an example

---

## 🔗 Navigation

**← Previous:** [Chapter 3 — Search Techniques](ch03_search_techniques.md)  
**→ Next:** [Chapter 5 — Structured Knowledge](ch05_structured_knowledge.md)  
**🏠 Home:** [README](../README.md)
