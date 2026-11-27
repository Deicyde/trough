---
declaration: theorem
origin: cited
lean: OeisA158110.conjecture
statement: formalized
---

# Exponentials of $\sum_{n \ge 1} q^{n^m} x^n / n$

> The sequence lists the coefficients of $\exp\left(\sum_{n \ge 1} 2^{n^3} x^n / n\right)$.
> Paul D. Hanna conjectured that $\exp\left(\sum_{n \ge 1} q^{n^m} x^n / n\right)$ has integer
> coefficients for all nonnegative integers $q$ and $m$. Sela Fried proved this [Fr25].
>
> *References:*
> - [A158110](https://oeis.org/A158110), Paul D. Hanna, 2009.
> - [Fr25] Sela Fried, [Proof of a conjecture stated in A158110](https://oeis.org/A158110/a158110.pdf),
>   2025.
> - [Fr26] Sela Fried, [Further proofs of conjectures from the OEIS](https://arxiv.org/abs/2607.24832),
>   arXiv:2607.24832, 2026.

*Quoted from [FormalConjectures/OEIS/158110.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/158110.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 3 test statements, counted here but not shown.

## `OeisA158110.conjecture`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-14-000003](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-14-000003).

> "Conjecture: given q and m are nonnegative integers, then exp( Sum_{n>=1} q^(n^m)*x^n/n ) is a
> power series in x with integer coefficients."
> - Paul D. Hanna, Mar 19 2009.
>
> Proved by Sela Fried [Fr25]. The case $m = 0$ gives $(1 - x)^{-q}$, and $q = 0$ gives $1$.

```lean
theorem conjecture (q m n : ℕ) : ∃ z : ℤ, coeff n (subst (logSeries q m) (exp ℚ)) = z
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/158110.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/158110.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/158110.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/158110.lean)
- [A158110](https://oeis.org/A158110)
