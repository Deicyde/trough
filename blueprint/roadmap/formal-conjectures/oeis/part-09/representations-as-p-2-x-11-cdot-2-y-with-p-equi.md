---
declaration: theorem
origin: cited
lean: OeisA157237.conjecture
statement: formalized
---

# Representations as $p + 2^x + 11 \cdot 2^y$ with $p \equiv 1 \pmod 6$

> Number of ways to write the $n$-th positive odd integer in the form $p + 2^x + 11 \cdot 2^y$
> with $p$ a prime congruent to $1 \bmod 6$ and $x, y$ positive integers.
>
> $$a(n) = \left|\left\{(p, x, y) : p + 2^x + 11 \cdot 2^y = 2n - 1 \text{ with } p \text{ prime},
> p \equiv 1 \pmod 6, x, y \in \mathbb{Z}^+\right\}\right|.$$
>
> *References:*
> - [A157237](https://oeis.org/A157237)
> - Z.-W. Sun, "Mixed sums of primes and other terms", arXiv preprint
>   [arXiv:0901.3075](https://arxiv.org/abs/0901.3075) [math.NT], 2009.

*Quoted from [FormalConjectures/OEIS/157237.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/157237.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA157237.conjecture`

Open: stated without proof.

> On Feb. 24, 2009, Zhi-Wei Sun conjectured that $a(n) = 0$ if and only if $n < 16$ or
> $n \in \{18, 21, 24, 51, 84, 1011, 59586\}$; in other words, except for
> $35, 41, 47, 101, 167, 2021, 119171$, any odd integer greater than $30$ can be written as the
> sum of a prime congruent to $1 \bmod 6$, a positive power of $2$ and eleven times a positive
> power of $2$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) :
    a n = 0 ↔ n ≤ 15 ∨ n = 18 ∨ n = 21 ∨ n = 24 ∨ n = 51 ∨ n = 84 ∨ n = 1011 ∨ n = 59586
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/157237.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/157237.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/157237.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/157237.lean)
- [A157237](https://oeis.org/A157237)
