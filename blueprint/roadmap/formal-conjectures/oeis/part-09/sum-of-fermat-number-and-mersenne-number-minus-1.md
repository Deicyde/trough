---
declaration: theorem
origin: cited
lean: OeisA119563.conjecture
statement: formalized
---

# Sum of Fermat number and Mersenne number minus 1: $2^{2^n} + 2^n - 1$

> Define $F(n) = 2^{2^n} + 1$ (the $n$-th Fermat number) and $M(n) = 2^n - 1$ (the $n$-th Mersenne
> number). Then $a(n) = F(n) + M(n) - 1 = 2^{2^n} + 2^n - 1$.
>
> *References:*
> - [A119563](https://oeis.org/A119563)

*Quoted from [FormalConjectures/OEIS/119563.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/119563.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA119563.conjecture`

Open: stated without proof.

> The first 5 entries are primes. Are there infinitely many primes in this sequence?

```lean
theorem conjecture : Set.Infinite {n : ℕ | (a n).Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/119563.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/119563.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/119563.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/119563.lean)
- [A119563](https://oeis.org/A119563)
