---
declaration: theorem
origin: cited
lean: OeisA183128.conjecture
statement: formalized
---

# Hanna's exponential series for $\binom{n+k-1}{k}^{k^2+1}$

> The sequence lists the coefficients of
>
> $$\exp\Bigl(\sum_{n \ge 1} \Bigl[\sum_{k \ge 0} \binom{n+k-1}{k}^{k^2+1} x^k\Bigr]
>   \frac{x^n}{n}\Bigr).$$
>
> *References:*
> - [A183128](https://oeis.org/A183128), Paul D. Hanna, 2010.

*Quoted from [FormalConjectures/OEIS/183128.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/183128.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA183128.conjecture`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-17-000018](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-17-000018).

> "Conjecture: this sequence consists entirely of integers."
> - Paul D. Hanna, Dec 25 2010.
>
> Proved by Wentao Li, with AI assistance, by checking Dold's integrality congruences along
> the rays $(n, k) \to (pn, pk)$. This pairing of terms is from trureturing issues
> [#22220](https://github.com/the-omega-institute/trureturing/issues/22220),
> [#22221](https://github.com/the-omega-institute/trureturing/issues/22221) and
> [#22222](https://github.com/the-omega-institute/trureturing/issues/22222).

```lean
theorem conjecture (m : ℕ) : ∃ z : ℤ, a m = z
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/OEIS/183128.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/183128.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/183128.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/183128.lean)
- [A183128](https://oeis.org/A183128)
