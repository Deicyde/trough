---
declaration: theorem
origin: cited
lean: OeisA181082.conjecture
statement: formalized
---

# Hanna's exponential series for $\binom{n}{k}^{n+k}$

> The sequence lists the coefficients of
>
> $$\exp\Bigl(\sum_{n \ge 1} \Bigl[\sum_{k=0}^{n} \binom{n}{k}^{n+k} x^k\Bigr]
>   \frac{x^n}{n}\Bigr).$$
>
> *References:*
> - [A181082](https://oeis.org/A181082), Paul D. Hanna, 2010.

*Quoted from [FormalConjectures/OEIS/181082.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/181082.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA181082.conjecture`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-17-000018](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-17-000018).

> "Conjecture: this sequence consists entirely of integers."
> - Paul D. Hanna, Oct 02 2010.
>
> Proved in Lean in
> [the-omega-institute/trureturing](https://github.com/the-omega-institute/trureturing/blob/2e8b76c4b53d11278d187422006387f7e948ba89/D5/S1/Recurrence/Algebraic/HannaA181082Integrality.lean)
> on November 13, 2026. The linked formal proof is an independent proof by Wentao Li, with AI
> assistance.

```lean
theorem conjecture (m : ℕ) : ∃ z : ℤ, a m = z
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/OEIS/181082.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/181082.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/181082.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/181082.lean)
- [A181082](https://oeis.org/A181082)
