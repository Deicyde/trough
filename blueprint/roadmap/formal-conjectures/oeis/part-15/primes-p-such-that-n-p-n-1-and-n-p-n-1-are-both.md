---
declaration: theorem
origin: cited
lean: OeisA261627.conjecture_1, OeisA261627.conjecture_2
statement: formalized
---

# Primes $p$ such that $n - (p n' - 1)$ and $n + (p n' - 1)$ are both prime

> Number of primes $p$ such that $n - (p n' - 1)$ and $n + (p n' - 1)$ are both prime,
> where $n'$ is $1$ or $2$ according as $n$ is odd or even.
>
> *References:*
> - [A261627](https://oeis.org/A261627)
> - [Conjectures involving primes and quadratic forms](https://arxiv.org/abs/1211.1588)
>   by *Zhi-Wei Sun*, arXiv:1211.1588 (2012-2015)

*Quoted from [FormalConjectures/OEIS/261627.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261627.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 6 test statements, counted here but not shown.

## `OeisA261627.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 6$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 6 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261627.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261627.lean#L73).

## `OeisA261627.conjecture_2`

Open: stated without proof.

> Conjecture: $a(n) = 1$ only for
> $n = 5, 7, 10, 11, 12, 19, 22, 30, 34, 44, 46, 72, 142$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n ∈ singletons
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261627.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261627.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/261627.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261627.lean)
- [A261627](https://oeis.org/A261627)
