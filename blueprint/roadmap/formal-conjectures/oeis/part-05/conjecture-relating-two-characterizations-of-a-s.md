---
declaration: theorem
origin: cited
lean: OeisA80170.gcdCondition_iff_primePowerCondition
statement: formalized
---

# Conjecture relating two characterizations of a set of integers.

> Informal Statement:
> For an integer $k \ge 2$, the following are equivalent:
>
> 1. The greatest common divisor of the binomial coefficients
>     $\binom{2k}{k}, \binom{3k}{k}, \dots, \binom{(k+1)k}{k} = 1$.
>
> 2. Writing prime factorization of $k$ as
>     $k = \prod p_i^{e_i}$, and let
>     $P = \max_i p_i^{e_i}$,
>     one has $k / P > P$.
>
> This conjecture asserts that the sequence defined by 1. is obtained by
> taking 1 off each number in the sequence defined by 2.
>
> *References:*
> - [A80170](https://oeis.org/A80170)
> - [A51283](https://oeis.org/A51283)

*Quoted from [FormalConjectures/OEIS/80170.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/80170.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA80170.gcdCondition_iff_primePowerCondition`

Solved: stated here; a Lean proof is at [https://github.com/guodk/formal-conjectures/blob/0720658844d76a50d48e4baa152eef14d4462907/FormalConjectures/OEIS/80170.lean#L1823](https://github.com/guodk/formal-conjectures/blob/0720658844d76a50d48e4baa152eef14d4462907/FormalConjectures/OEIS/80170.lean#L1823).

> Conjecture: The gcd condition is equivalent to the prime power condition.
> This has been conjectured by Ralf Stephan.
>
> Both the natural-language proof and its Lean 4 formalization were carried out
> by the KLMM MechMath Agent Team; see the `formal_proof` attribute.
>
> *References:*
> - [Ralf Stephan, *Prove or Disprove. 100 Conjectures from the OEIS*, 2004, Conjecture 17 (arXiv:math/0409509)](https://arxiv.org/abs/math/0409509)
> - [Dakai Guo et al., *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, 2026 (arXiv:2606.22997)](https://arxiv.org/abs/2606.22997)

```lean
theorem gcdCondition_iff_primePowerCondition (k : ℕ) (hk : 2 ≤ k) :
    A k ↔ B (k + 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/80170.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/80170.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/80170.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/80170.lean)
- [A80170](https://oeis.org/A80170)
