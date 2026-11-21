---
declaration: theorem
origin: cited
lean: Erdos242.erdos_242, Erdos242.erdos_242.variants.schinzel_generalization
statement: formalized
---

# Erdős Problem 242

> *References:*
> - [erdosproblems.com/242](https://www.erdosproblems.com/242)
> - [Si56] Sierpiński, W., Sur les décompositions de nombres rationnels en fractions primaires.
>   Mathesis (1956), 16--32.

*Quoted from [FormalConjectures/ErdosProblems/242.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/242.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/242](https://www.erdosproblems.com/242).

The file states 2 research or textbook statements: 2 open.

## `Erdos242.erdos_242`

Open: stated without proof.

> For every $n>2$ there exist distinct integers $1 ≤ x < y < z$
> such that $\frac 4 n = \frac 1 x + \frac 1 y + \frac 1 z$.

```lean
theorem erdos_242 (n : ℕ) (hn : 2 < n) :
    ∃ x y z : ℕ, 1 ≤ x ∧ x < y ∧ y < z ∧
      (4 / n : ℚ) = 1 / x + 1 / y + 1 / z
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/242.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/242.lean#L40).

## `Erdos242.erdos_242.variants.schinzel_generalization`

Open: stated without proof.

> Schinzel conjectured (see [Si56]) the generalisation that, for any fixed $a$, if $n$ is sufficiently
> large in terms of $a$ then there exist distinct integers $1\leq x < y < z$ such that
> $\frac{a}{n} = \frac{1}{x}+\frac{1}{y}+\frac{1}{z}.$

```lean
theorem erdos_242.variants.schinzel_generalization
    (a : ℕ) (ha : 0 < a) :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∃ x y z : ℕ, 1 ≤ x ∧ x < y ∧ y < z ∧
      (a / n : ℚ) = 1 / x + 1 / y + 1 / z
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/242.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/242.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/242.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/242.lean)
- [erdosproblems.com/242](https://www.erdosproblems.com/242)
