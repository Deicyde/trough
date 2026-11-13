---
declaration: theorem
origin: cited
lean: OeisA117027.conjecture
statement: formalized
---

# Determinants of 2 X 2 matrices of non-overlapping blocks of 4 consecutive primes

> $a(n) = p_{4n-3}p_{4n} - p_{4n-2}p_{4n-1}$ where $p_k$ is the k-th prime number (1-indexed).
>
> *References:*
> - [A117027](https://oeis.org/A117027)

*Quoted from [FormalConjectures/OEIS/117027.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/117027.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements and 7 API statements, counted here but not shown.

## `OeisA117027.conjecture`

Open: stated without proof.

> This suggests the ratio is approaching a limit close to 0.87.
>
> Formalized as: The sequence of ratios $P(N)/Neg(N)$ converges to a limit L,
> and L is in the interval (0.8, 0.9).

```lean
theorem conjecture :
  ∃ L : ℝ, Tendsto ratioSeq atTop (nhds L) ∧ 0.8 < L ∧ L < 0.9
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/117027.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/117027.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/117027.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/117027.lean)
- [A117027](https://oeis.org/A117027)
