---
declaration: theorem
origin: cited
lean: OeisA219791.conjecture_1, OeisA219791.conjecture_2
statement: formalized
---

# Partitions of $n$ into $x + y$ with $(xy)^2 + 1$ prime

> Number of ways to write $n = x + y$ ($0 < x \le y$) with $(xy)^2 + 1$ prime.
>
> *References:*
> - [A219791](https://oeis.org/A219791)

*Quoted from [FormalConjectures/OEIS/219791.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219791.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA219791.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ if $n$ is different from $1, 6, 16, 24$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 0) (h1 : n ≠ 1) (h6 : n ≠ 6) (h16 : n ≠ 16) (h24 : n ≠ 24) :
    a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219791.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219791.lean#L56).

## `OeisA219791.conjecture_2`

Open: stated without proof.

> Conjecture: For any positive integer $k$, each
> sufficiently large integer $n$ can be written as $x + y$ ($x > 0, y > 0$) with $(xy)^{2^k} + 1$
> prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (k : ℕ) (hk : 0 < k) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
      ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧ Nat.Prime ((x * y) ^ (2 ^ k) + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219791.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219791.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/219791.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219791.lean)
- [A219791](https://oeis.org/A219791)
