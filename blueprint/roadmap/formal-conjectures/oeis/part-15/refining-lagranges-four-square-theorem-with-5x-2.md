---
declaration: theorem
origin: cited
lean: OeisA261876.conjecture_1, OeisA261876.conjecture_2, OeisA261876.conjecture_3
statement: formalized
---

# Refining Lagrange's four-square theorem with $(5x^2 + 7y^2 + 9z^2)yz$ a square

> Number of ordered ways to write $n$ as $x^2 + y^2 + z^2 + w^2$ with $(5x^2 + 7y^2 + 9z^2)yz$
> a square, where $x, y, z, w$ are nonnegative integers with $z > 0$.
>
> *References:*
> - [A261876](https://oeis.org/A261876)
> - [Refining Lagrange's four-square theorem](https://arxiv.org/abs/1604.06723)
>   by *Zhi-Wei Sun*, arXiv:1604.06723 (2016)
> - [arXiv:2608.11941](https://arxiv.org/abs/2608.11941)

*Quoted from [FormalConjectures/OEIS/261876.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261876.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA261876.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 0$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261876.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261876.lean#L78).

## `OeisA261876.conjecture_2`

Solved: stated here without proof.

> Conjecture (i): $a(n) = 1$ only for $n = 4^k m$ ($k = 0, 1, 2, \dots$ and
> $m \in \{1, 7, 23, 647, 863\}$).
>
> Disproved in [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) at $n = 69383$, where
> $(x, y, z, w) = (187, 147, 6, 113)$ is the unique representation, so $a(69383) = 1$.

```lean
theorem conjecture_2 :
    ¬ ∀ n : ℕ, (a n = 1 ↔ ∃ k : ℕ, ∃ m ∈ specialSet, n = 4 ^ k * m)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261876.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261876.lean#L89).

## `OeisA261876.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For each triple $(c_1, c_2, c_3) \in \{(1,8,20), (3,5,15), (6,14,4), (7,29,5),
> (18,38,18), (39,81,51), (42,98,14)\}$, any natural number can be written as
> $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative integers such that
> $xy(c_1 x^2 + c_2 y^2 + c_3 z^2)$ is a square.

```lean
theorem conjecture_3 (t : ℕ × ℕ × ℕ) (ht : t ∈ triples) (n : ℕ) :
    ∃ x y z w : ℕ, n = x ^ 2 + y ^ 2 + z ^ 2 + w ^ 2 ∧
      IsSquare (x * y * (t.1 * x ^ 2 + t.2.1 * y ^ 2 + t.2.2 * z ^ 2))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/261876.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261876.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/261876.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/261876.lean)
- [A261876](https://oeis.org/A261876)
