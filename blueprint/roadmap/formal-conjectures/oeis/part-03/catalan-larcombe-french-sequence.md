---
declaration: theorem
origin: cited
lean: OeisA53175.conjecture
statement: formalized
---

# Catalan-Larcombe-French sequence

> The Catalan-Larcombe-French sequence defined by $a(0)=1$, $a(1)=8$, and
>
> $$n^2 a(n) = 8(3n^2 - 3n + 1) a(n-1) - 128(n-1)^2 a(n-2)$$
>
> for $n \ge 2$.
>
> *References:*
> - [A053175](https://oeis.org/A053175)
> - [ZS18] [Zhu, B.-X., Sun, Z.-W., *Hankel-type determinants for some combinatorial sequences*,
>   Int. J. Number Theory **14** (2018), 1265-1277](https://arxiv.org/abs/1609.06810)

*Quoted from [FormalConjectures/OEIS/53175.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/53175.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA53175.conjecture`

Solved: stated here without proof.

> Conjecture: let $P(n)$ be the $(n+1) \times (n+1)$ Hankel-type determinant with $(i,j)$-entry
> equal to $a(i+j)$ for all $i,j = 0, \ldots, n$. Then $P(n)/2^{n(n+3)}$ is a positive odd integer.
> - Zhi-Wei Sun, Aug 14 2013
>
> Proved by [ZS18], Theorem 1.2: $2^{-n(n+3)} |P_{i+j}|_{0 \le i,j \le n}$ is a positive odd
> integer for every $n \in \mathbb{N}$, where $P_n$ are the Catalan-Larcombe-French numbers.

```lean
theorem conjecture (n : ℕ) :
    let detP := (hankelMatrix n).det
    let pow2 := (2 : ℤ) ^ (n * (n + 3))
    pow2 ∣ detP ∧ 0 < detP / pow2 ∧ (detP / pow2) % 2 = 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/53175.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/53175.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/53175.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/53175.lean)
- [A053175](https://oeis.org/A053175)
