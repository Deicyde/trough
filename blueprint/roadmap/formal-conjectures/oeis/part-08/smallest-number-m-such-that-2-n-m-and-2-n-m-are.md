---
declaration: theorem
origin: cited
lean: OeisA113213.conjecture
statement: formalized
---

# Smallest number $m$ such that $2^n - m$ and $2^n + m$ are primes

> *References:*
> - [A113213](https://oeis.org/A113213)

*Quoted from [FormalConjectures/OEIS/113213.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113213.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA113213.conjecture`

Open: stated without proof.

> Conjecture: $a(n) = O(n^3)$.
>
> The source defines $a(n)$ as the least $m$ with $2^n - m$ and $2^n + m$ prime, so it
> implicitly asserts that such an $m$ exists. Since `a n = 0` when no such $m$ exists, the
> existence of a prime pair is stated explicitly for all sufficiently large $n$.

```lean
theorem conjecture :
    (∀ᶠ n : ℕ in Filter.atTop, ∃ m, (2 ^ n - m).Prime ∧ (2 ^ n + m).Prime) ∧
    (fun n : ℕ => (a n : ℝ)) =O[Filter.atTop] (fun n : ℕ => (n ^ 3 : ℝ))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113213.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113213.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113213.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113213.lean)
- [A113213](https://oeis.org/A113213)
