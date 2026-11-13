---
declaration: theorem
origin: cited
lean: OeisA111114.conjecture
statement: formalized
---

# Integer part of $\mathrm{prime}(n)/\pi(n)$

> Here $\mathrm{prime}(n)$ is the $n$-th prime number, and $\pi(n)$ is the prime-counting function.
>
> *References:*
> - [A111114](https://oeis.org/A111114)

*Quoted from [FormalConjectures/OEIS/111114.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111114.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA111114.conjecture`

Open: stated without proof.

> Conjecture: As $n \rightarrow \infty$, there are infinitely many n's such that
> $a(n)$ is greater than $a(n+1)$.

```lean
theorem conjecture : ∃ᶠ n in atTop, a n > a (n + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/111114.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111114.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/111114.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/111114.lean)
- [A111114](https://oeis.org/A111114)
