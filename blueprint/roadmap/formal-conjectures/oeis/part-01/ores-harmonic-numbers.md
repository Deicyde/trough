---
declaration: theorem
origin: cited
lean: OeisA1599.eq_one_of_odd_of_a
statement: formalized
---

# Ore's harmonic numbers

> A001599 lists the positive integers whose positive divisors have an integral harmonic mean.
> Equivalently, $n$ belongs to the sequence when
> $\sigma_1(n) \mid n\sigma_0(n)$, where $\sigma_1(n)$ is the sum of the divisors of $n$ and
> $\sigma_0(n)$ is their number.
>
> *References:*
> - [A001599](https://oeis.org/A001599)

*Quoted from [FormalConjectures/OEIS/1599.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1599.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `OeisA1599.eq_one_of_odd_of_a`

Open: stated without proof.

> "Ore conjectured that 1 is the only odd harmonic number."
>
> *Reference:* [A001599](https://oeis.org/A001599)

```lean
theorem eq_one_of_odd_of_a {n : ℕ} (hn : A n) (hodd : Odd n) : n = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/1599.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1599.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/1599.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1599.lean)
- [A001599](https://oeis.org/A001599)
