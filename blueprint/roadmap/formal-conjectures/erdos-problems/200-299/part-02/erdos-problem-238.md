---
declaration: theorem
origin: cited
lean: Erdos238.erdos_238, Erdos238.erdos_238.variants.small_c1
statement: formalized
---

# Erdős Problem 238

> *Reference:* [erdosproblems.com/238](https://www.erdosproblems.com/238)

*Quoted from [FormalConjectures/ErdosProblems/238.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/238.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/238](https://www.erdosproblems.com/238).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos238.erdos_238`

Open: stated without proof.

> Let `c₁, c₂ > 0`. Is it true that for any sufficiently large `x`, there exists more than
> `c₁ * log x` many consecutive primes `≤ x` such that the difference between any two is `> c₂`?

```lean
theorem erdos_238 : ∀ᵉ (c₁ > 0) (c₂ > 0), ∀ᶠ (x : ℝ) in atTop, ∃ (k : ℕ),
    c₁ * log x < k ∧ ∃ f : Fin k → ℕ, ∃ m, (∀ i, f i ≤ x ∧ f i = (m + i.1).nth Nat.Prime)
    ∧ ∀ i : Fin (k - 1), c₂ < primeGap (m + i.1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/238.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/238.lean#L38).

## `Erdos238.erdos_238.variants.small_c1`

Solved: stated here without proof.

> It is well-known that the conjecture above is true when `c₁` is sufficiently small.

```lean
theorem erdos_238.variants.small_c1 : ∀ c₂ > 0, ∀ᶠ c₁ in 𝓝[>] 0, ∀ᶠ (x : ℝ) in atTop, ∃ (k : ℕ),
    c₁ * log x < k ∧ ∃ f : Fin k → ℕ, ∃ m, (∀ i, f i ≤ x ∧ f i = (m + i.1).nth Nat.Prime)
    ∧ ∀ i : Fin (k - 1), c₂ < primeGap (m + i.1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/238.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/238.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/238.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/238.lean)
- [erdosproblems.com/238](https://www.erdosproblems.com/238)
