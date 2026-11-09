---
declaration: theorem
origin: cited
lean: Erdos868.erdos_868.parts.i, Erdos868.erdos_868.parts.ii, Erdos868.erdos_868.variants.fixed_ε, Erdos868.erdos_868.variants.Hartter_Nathanson
statement: formalized
---

# Erdős Problem 868

> *References:*
> - [erdosproblems.com/868](https://www.erdosproblems.com/868)
> - [LaLa26] Larsen and Larsen, [Erdős problem 868](https://github.com/Larsen-Daniel/Erdos-868/blob/main/868.pdf) (2026)

*Quoted from [FormalConjectures/ErdosProblems/868.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/868.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/868](https://www.erdosproblems.com/868).

The file states 4 research or textbook statements: 4 solved.

## `Erdos868.erdos_868.parts.i`

Solved: stated here without proof.

> Let $A$ be an additive basis of order $2$, let $f(n)$ denote the number of ways in which
> $n$ can be written as the sum of two elements from $A$. If $f(n) \to \infty$ as $n \to \infty$, then
> must $A$ contain a minimal additive basis of order $2$?
>
> Larsen and Larsen [LaLa26] answered this in the negative.

```lean
theorem erdos_868.parts.i :
    ¬ ∀ (A : Set ℕ), A.IsAsymptoticAddBasisOfOrder 2 →
      atTop.Tendsto (fun n => ncard_add_repr A 2 n) atTop → ∃ B ⊆ A,
      B.IsAsymptoticAddBasisOfOrder 2 ∧ ∀ b ∈ B, ¬(B \ {b}).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/868.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/868.lean#L50).

## `Erdos868.erdos_868.parts.ii`

Solved: stated here without proof.

> Let $A$ be an additive basis of order $2$, let $f(n)$ denote the number of ways in which
> $n$ can be written as the sum of two elements from $A$. If $f(n) > \epsilon \log n$ for large $n$
> and an arbitrary fixed $\epsilon > 0$, then must $A$ contain a minimal additive
> basis of order $2$?
>
> Larsen and Larsen [LaLa26] constructed a counterexample with $f(n) > c \log n$ for all large $n$.

```lean
theorem erdos_868.parts.ii :
    ¬ ∀ᵉ (A : Set ℕ) (ε > 0), A.IsAsymptoticAddBasisOfOrder 2 →
      (∀ᶠ (n : ℕ) in atTop, ε * Real.log n < ncard_add_repr A 2 n) → ∃ B ⊆ A,
      B.IsAsymptoticAddBasisOfOrder 2 ∧ ∀ b ∈ B, ¬(B \ {b}).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/868.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/868.lean#L64).

## `Erdos868.erdos_868.variants.fixed_ε`

Solved: stated here without proof.

> Erdős and Nathanson proved that this is true if $f(n) > c \log n$ for all large $n$, for
> some fixed constant $c > (\log \frac{4}{3})^{-1}$.

```lean
theorem erdos_868.variants.fixed_ε :
    ∀ᵉ (A : Set ℕ) (c > (Real.log (4 / 3))⁻¹), A.IsAsymptoticAddBasisOfOrder 2 →
      (∀ᶠ (n : ℕ) in atTop, c * Real.log n < ncard_add_repr A 2 n) → ∃ B ⊆ A,
      B.IsAsymptoticAddBasisOfOrder 2 ∧ ∀ b ∈ B, ¬(B \ {b}).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/868.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/868.lean#L73).

## `Erdos868.erdos_868.variants.Hartter_Nathanson`

Solved: stated here; a Lean proof is at [https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/868.lean#L132](https://github.com/hjyuh/formal-conjectures/blob/e0da6ec78953b17618895a093d4bee90fd3f6f67/FormalConjectures/ErdosProblems/868.lean#L132).

> Härtter and Nathanson proved that there exist additive bases which do not contain
> any minimal additive bases.

```lean
theorem erdos_868.variants.Hartter_Nathanson (o : ℕ) (ho : 1 < o) : ∃ (A : Set ℕ),
    A.IsAsymptoticAddBasisOfOrder o ∧ ∀ B ⊆ A, B.IsAsymptoticAddBasisOfOrder o →
    ∃ b ∈ B, (B \ {b}).IsAsymptoticAddBasisOfOrder o
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/868.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/868.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/868.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/868.lean)
- [erdosproblems.com/868](https://www.erdosproblems.com/868)
