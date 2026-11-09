---
declaration: theorem
origin: cited
lean: Erdos859.erdos_859.variants.erdos_upper_lower_bounds, Erdos859.erdos_859, Erdos859.erdos_859.variants.trivial_case, Erdos859.erdos_859.variants.positive_density
statement: formalized
---

# Erdős Problem 859

> *Reference:* [erdosproblems.com/859](https://www.erdosproblems.com/859)

*Quoted from [FormalConjectures/ErdosProblems/859.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/859.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/859](https://www.erdosproblems.com/859).

The file states 4 research or textbook statements: 1 open, 1 solved and 2 textbook results.

## `Erdos859.erdos_859.variants.erdos_upper_lower_bounds`

Solved: stated here without proof.

> A weaker version of the problem proved by Erdos:
> The density `dₜ` of `DivisorSumSet (t : ℕ)` is bounded from below by `1 / log (t) ^ c₃` and
> from above by `1 / log (t) ^ c₄` for some positive constants `c₃` and `c₄`.

```lean
theorem erdos_859.variants.erdos_upper_lower_bounds : ∃ᵉ (c₃ > (0 : ℝ)) (c₄ > (0 : ℝ)) (t₀ : ℕ),
    ∀ᶠ t in atTop, ∃ dₜ : ℝ, (DivisorSumSet t).HasDensity dₜ ∧
    1 / Real.log t ^ c₃ < dₜ ∧ dₜ < 1 / Real.log t ^ c₄
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/859.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/859.lean#L43).

## `Erdos859.erdos_859`

Open: stated without proof.

> The density of the divisor sum set is asymptotically equivalent to $c_1 / \log(t)^{c_2}$.

```lean
theorem erdos_859 :
    ∃ c₁ > 0, ∃ c₂ > (0 : ℝ), ∃ d : ℕ → ℝ, (∀ t > 0, (DivisorSumSet t).HasDensity (d t)) ∧
      (fun (t : ℕ) ↦ d t) ~[atTop] (fun t ↦ c₁ / Real.log t ^ c₂)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/859.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/859.lean#L56).

## `Erdos859.erdos_859.variants.trivial_case`

Textbook result, proved here.

> A case where we can easily calculate the density of `DivisorSumSet t` is that of `t=0`.

```lean
lemma erdos_859.variants.trivial_case : DivisorSumSet 0 = Set.univ
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/859.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/859.lean#L65).

## `Erdos859.erdos_859.variants.positive_density`

Textbook result, stated without proof.

> An easy sanity check is to prove that for every natural number `t` the density `dₜ` is
> a positive number.
> Hint: investigate some multiplicative structure of `DivisorSumSet t`.

```lean
lemma erdos_859.variants.positive_density (t : ℕ) :
    (DivisorSumSet t).HasPosDensity
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/859.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/859.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/859.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/859.lean)
- [erdosproblems.com/859](https://www.erdosproblems.com/859)
