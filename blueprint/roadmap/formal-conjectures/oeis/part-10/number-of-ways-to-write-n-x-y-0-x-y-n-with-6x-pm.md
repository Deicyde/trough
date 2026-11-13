---
declaration: theorem
origin: cited
lean: OeisA187759.conjecture
statement: formalized
---

# Number of ways to write $n = x + y$ ($0 < x < y < n$) with $6x \pm 1$ and $6y \pm 1$ prime

> The sequence $a(n)$ counts the number of ways to write $n = x + y$ with $0 < x < y < n$ such that
> $6x - 1$, $6x + 1$, $6y - 1$, and $6y + 1$ are all prime numbers.
>
> *References:*
> - [A187759](https://oeis.org/A187759)
> - [Conjectures involving primes and quadratic forms](https://arxiv.org/abs/1211.1588)
>   by *Zhi-Wei Sun*, arXiv:1211.1588 (2012)

*Quoted from [FormalConjectures/OEIS/187759.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/187759.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA187759.conjecture`

Open: stated without proof.

> Conjecture: If $n > 200$ is not among $211, 226, 541, 701$, then $a(n) > 0$.
> - _Zhi-Wei Sun_, Jan 03 2013

```lean
theorem conjecture (n : ℕ) (hn : 200 < n) (hnot : n ∉ ({211, 226, 541, 701} : Finset ℕ)) :
    0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/187759.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/187759.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/187759.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/187759.lean)
- [A187759](https://oeis.org/A187759)
