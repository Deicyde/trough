---
declaration: theorem
origin: cited
lean: Erdos951.erdos_951, Erdos951.erdos_951.variants.beurling
statement: formalized
---

# Erdős Problem 951

> *References:*
>  - [erdosproblems.com/951](https://www.erdosproblems.com/951)
>  - [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III. Number theory day (Proc. Conf., Rockefeller Univ.,
>     New York, 1976) (1977), 43-72.

*Quoted from [FormalConjectures/ErdosProblems/951.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/951.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/951](https://www.erdosproblems.com/951).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos951.erdos_951`

Open: stated without proof.

> If `1 < a 0 < ...` has property `Erdos951Prop`, is it true that `#{a i ≤ x} ≤ π x`?

```lean
theorem erdos_951 :
    ∀ a : ℕ → ℝ, 1 < a 0 → StrictMono a → Erdos951Prop a →
      ∀ᶠ (x : ℝ) in Filter.atTop, {i : ℕ | a i ≤ x}.ncard ≤ π ⌊x⌋₊
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/951.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/951.lean#L62).

## `Erdos951.erdos_951.variants.beurling`

Solved: stated here without proof.

> Beurling conjectured that if `1 < a 0 < a 1 < ⋯` has property `Erdos951Prop` and the number
> of reals in $[1, x]$ of the form $\prod_i a_i^{k_i}$ is $x + o(\log x)$, then `a` must be the
> sequence of primes. Property `Erdos951Prop` makes distinct exponent vectors give distinct
> Beurling integers, so counting the set `BeurlingIntegers a` counts the generalised integers.

```lean
theorem erdos_951.variants.beurling :
    ∀ a : ℕ → ℝ, IsBeurlingPrimes a → Erdos951Prop a →
    ((fun x => (BeurlingIntegers a ∩ .Iic x).ncard - x) =o[atTop] Real.log) →
    a = Nat.cast ∘ Nat.nth Nat.Prime
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/951.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/951.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/951.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/951.lean)
- [erdosproblems.com/951](https://www.erdosproblems.com/951)
