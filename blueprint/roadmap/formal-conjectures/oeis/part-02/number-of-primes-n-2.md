---
declaration: theorem
origin: cited
lean: OeisA38107.conjecture
statement: formalized
---

# Number of primes $< n^2$

> Number of primes strictly less than $n^2$.
>
> *References:*
> - [A038107](https://oeis.org/A038107)

*Quoted from [FormalConjectures/OEIS/38107.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38107.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA38107.conjecture`

Open: stated without proof.

> Conjecture: all the numbers $\sum_{i=j}^k \frac{1}{a(i)}$ with $1 < j \le k$ have pairwise distinct
> fractional parts.
> - Zhi-Wei Sun, Sep 24 2015

```lean
theorem conjecture (j k j' k' : ℕ)
    (hj : 1 < j) (hjk : j ≤ k) (hj' : 1 < j') (hj'k' : j' ≤ k')
    (h_eq : Int.fract (∑ i ∈ Finset.Icc j k, (1 : ℝ) / (a i : ℝ)) =
            Int.fract (∑ i ∈ Finset.Icc j' k', (1 : ℝ) / (a i : ℝ))) :
    j = j' ∧ k = k'
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38107.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38107.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/38107.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38107.lean)
- [A038107](https://oeis.org/A038107)
