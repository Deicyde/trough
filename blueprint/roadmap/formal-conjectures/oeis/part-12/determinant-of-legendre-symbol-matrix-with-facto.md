---
declaration: theorem
origin: cited
lean: OeisA226163.conjecture
statement: formalized
---

# Determinant of Legendre symbol matrix with factorial shifts

> Determinant of the $(p_n-1)/2$-by-$(p_n-1)/2$ matrix with $(i,j)$-entry being the Legendre symbol
>
> $$\left(\frac{i^2 - \left(\frac{p_n-1}{2}\right)! j}{p_n}\right),$$
>
> where $p_n$ is the $n$-th prime ($n \ge 2$).
>
> *References:*
> - [A226163](https://oeis.org/A226163)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/226163.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/226163.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA226163.conjecture`

Solved: stated here without proof.

> Conjecture: $a(n) = 0$ if and only if $p_n \equiv 3 \pmod 4$.
> - _Zhi-Wei Sun_, Aug 13 2013
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture (n : ℕ) (hn : 2 ≤ n) :
    a n = 0 ↔ Nat.nth Nat.Prime (n - 1) % 4 = 3
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/226163.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/226163.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/226163.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/226163.lean)
- [A226163](https://oeis.org/A226163)
