---
declaration: theorem
origin: cited
lean: Erdos1128.erdos_1128.prikryMills, Erdos1128.erdos_1128, Erdos1128.erdos_1128.variants.prikryMills_explicit, Erdos1128.erdos_1128.variants.two_dimensional_false
statement: formalized
---

# Erdős Problem 1128

> *Reference:* [erdosproblems.com/1128](https://www.erdosproblems.com/1128)

*Quoted from [FormalConjectures/ErdosProblems/1128.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1128.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1128](https://www.erdosproblems.com/1128).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1128.erdos_1128.prikryMills`

Solved: stated here without proof.

> **Prikry–Mills counterexample** (key lemma):
>
> There exists a 2-colouring $f$ of a set of cardinality $\aleph_1$ cubed such that
> no countable box $A_1 \times B_1 \times C_1$ is monochromatic.
>
> This is the unpublished result of Prikry and Mills (1978). The proof proceeds by
> transfinite induction along $\omega_1$, which has uncountable cofinality, ensuring
> every countable box is non-monochromatic.

```lean
theorem erdos_1128.prikryMills :
    ∃ (X : Type) (_ : #X = aleph 1) (f : X → X → X → Fin 2),
      ∀ (A₁ B₁ C₁ : Set X),
        #A₁ = aleph 0 → #B₁ = aleph 0 → #C₁ = aleph 0 →
        ¬ IsMonochromaticBox f A₁ B₁ C₁
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1128.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1128.lean#L106).

## `Erdos1128.erdos_1128`

Proved here.

> **Erdős Problem 1128** (disproved by Prikry–Mills, 1978):
>
> Erdős asked whether every 2-colouring of $A \times B \times C$, where
> $|A| = |B| = |C| = \aleph_1$, must contain a monochromatic countable box
> $A_1 \times B_1 \times C_1$ with $|A_1| = |B_1| = |C_1| = \aleph_0$.
>
> The answer is **No**: Prikry and Mills constructed a 2-colouring of $\omega_1^3$
> with no monochromatic countable box.
>
> Note: The positive statement asserts that every 2-colouring of every $\aleph_1^3$
> contains a monochromatic countably infinite box. Since the answer is False, this
> positive statement fails.

```lean
theorem erdos_1128 :
    ¬ ∀ (A B C : Type) (_ : #A = aleph 1) (_ : #B = aleph 1) (_ : #C = aleph 1)
      (f : A → B → C → Fin 2),
      ∃ (A₁ : Set A) (B₁ : Set B) (C₁ : Set C),
        #A₁ = aleph 0 ∧ #B₁ = aleph 0 ∧ #C₁ = aleph 0 ∧
        IsMonochromaticBox f A₁ B₁ C₁
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1128.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1128.lean#L151).

## `Erdos1128.erdos_1128.variants.prikryMills_explicit`

Solved: stated here without proof.

> **Explicit form of Prikry–Mills**:
>
> There exists a 2-colouring of $\omega_1 \times \omega_1 \times \omega_1$ such that
> for every countably infinite $A_1, B_1, C_1 \subseteq \omega_1$, the box
> $A_1 \times B_1 \times C_1$ is not monochromatic.
>
> This is the content of the Prikry–Mills theorem (1978, unpublished), stated
> using Lean's ordinal type `{o : Ordinal // o < ω_ 1}` as the
> representation of $\omega_1$.

```lean
theorem erdos_1128.variants.prikryMills_explicit :
    ∃ (f : {o : Ordinal // o < ω_ 1} →
           {o : Ordinal // o < ω_ 1} →
           {o : Ordinal // o < ω_ 1} → Fin 2),
      ∀ (A₁ B₁ C₁ : Set {o : Ordinal // o < ω_ 1}),
        #A₁ = aleph 0 → #B₁ = aleph 0 → #C₁ = aleph 0 →
        ¬ IsMonochromaticBox f A₁ B₁ C₁
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1128.lean, line 181](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1128.lean#L181).

## `Erdos1128.erdos_1128.variants.two_dimensional_false`

Proved here.

> The claim that every 2-colouring of $\omega_1 \times \omega_1$ has an uncountable
> monochromatic product rectangle is **false** in ZFC.
>
> **Counterexample:** The ordering colouring $f(\alpha, \beta) = 0$ iff $\alpha < \beta$
> has no uncountable monochromatic product rectangle $A_1 \times B_1$.
>
> **Proof:** If $A_1 \times B_1$ were monochromatic with colour 0, then every element of
> $A_1$ would be strictly less than every element of $B_1$, making $A_1$ bounded above in
> $\omega_1$; but any bounded subset of $\omega_1$ is countable (since initial segments are
> countable), contradicting $A_1$ being uncountable. The colour-1 case is symmetric with
> the roles of $A_1$ and $B_1$ swapped.
>
> Note: For 2-colourings of unordered pairs the analogous statement also fails: Sierpiński
> showed $\omega_1 \not\to (\omega_1)^2_2$. The Erdős–Rado theorem gives
> $(2^{\aleph_0})^+ \to (\aleph_1)^2_{\aleph_0}$ instead.

```lean
theorem erdos_1128.variants.two_dimensional_false :
    ¬ ∀ (f : Omega1 → Omega1 → Fin 2),
        ∃ (A₁ B₁ : Set Omega1),
          ¬ A₁.Countable ∧ ¬ B₁.Countable ∧
          ∃ c : Fin 2, ∀ a ∈ A₁, ∀ b ∈ B₁, f a b = c
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1128.lean, line 231](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1128.lean#L231).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1128.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1128.lean)
- [erdosproblems.com/1128](https://www.erdosproblems.com/1128)
