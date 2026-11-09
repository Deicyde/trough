---
declaration: theorem
origin: cited
lean: OeisA157225.conjecture
statement: formalized
---

# Representations as $p + 2^x + 7 \cdot 2^y$ with $p \equiv 5 \pmod 6$

> Number of ways to write the $n$-th positive odd integer in the form $p + 2^x + 7 \cdot 2^y$
> with $p$ a prime congruent to $5 \bmod 6$ and $x, y$ positive integers.
>
> $$a(n) = \left|\left\{(p, x, y) : p + 2^x + 7 \cdot 2^y = 2n - 1 \text{ with } p \text{ prime},
> p \equiv 5 \pmod 6, x, y \in \mathbb{Z}^+\right\}\right|.$$
>
> *References:*
> - [A157225](https://oeis.org/A157225)
> - Z.-W. Sun, "Mixed sums of primes and other terms", arXiv preprint
>   [arXiv:0901.3075](https://arxiv.org/abs/0901.3075) [math.NT], 2009.

*Quoted from [FormalConjectures/OEIS/157225.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/157225.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA157225.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/main/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_157225_conjecture_0/Submission/Spec.lean](https://github.com/epoch-research/LeanOpenProblems-results/blob/main/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_157225_conjecture_0/Submission/Spec.lean).

> On Feb. 24, 2009, Zhi-Wei Sun conjectured that $a(n) = 0$ if and only if $n < 11$ or
> $n \in \{13, 16, 992\}$; in other words, except for $25, 31, 1983$, any odd integer greater
> than $20$ can be written as the sum of a prime congruent to $5 \bmod 6$, a positive power of $2$
> and seven times a positive power of $2$.
>
> Answer: false, for n = 716993899 we have a(n) = 0.
> See T. Adamczewski, OEIS Open: How many conjectures can language models turn into theorems?,
> [arxiv/2608.11941](https://arxiv.org/pdf/2608.11941).

```lean
theorem conjecture :
    ¬ ∀ n : ℕ, 0 < n → (a n = 0 ↔ n < 11 ∨ n = 13 ∨ n = 16 ∨ n = 992)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/157225.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/157225.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/157225.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/157225.lean)
- [A157225](https://oeis.org/A157225)
