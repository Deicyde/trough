---
declaration: theorem
origin: cited
lean: OeisA248123.conjecture
statement: formalized
---

# Least $m > 0$ coprime to $n$ such that $mn \mid C(m+n)$

> The sequence $a(n)$ is the least positive integer $m$ such that $\gcd(m, n) = 1$ and
> $m \cdot n \mid C(m+n)$, where $C(k) = \frac{1}{k+1} \binom{2k}{k}$ is the $k$-th Catalan number.
>
> *References:*
> - [A248123](https://oeis.org/A248123)

*Quoted from [FormalConjectures/OEIS/248123.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/248123.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA248123.conjecture`

Open: stated without proof.

> Conjecture: $a(n)$ exists for all $n > 0$.
> Since $a(n)$ is defined as the infimum of a set of positive integers, existence is equivalent
> to $0 < a(n)$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/248123.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/248123.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/248123.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/248123.lean)
- [A248123](https://oeis.org/A248123)
