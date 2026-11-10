---
declaration: theorem
origin: cited
lean: OeisA237348.conjecture_1, OeisA237348.conjecture_2
statement: formalized
---

# Ordered ways to write $n = k + m$ with $p_k + 4$ and $p_{p_m} + 4$ both prime

> Let $p_j$ denote the $j$-th prime number. The sequence $a(n)$ counts the number of ordered ways to
> write $n = k + m$ with $k > 0$ and $m > 0$ such that $p_k + 4$ and $p_{p_m} + 4$ are both prime.
>
> *References:*
> - [A237348](https://oeis.org/A237348)

*Quoted from [FormalConjectures/OEIS/237348.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237348.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA237348.conjecture_1`

Open: stated without proof.

> Conjecture: For each $d = 1, 2, 3, \dots$ there is a positive integer $N(d)$ for which any integer
> $n > N(d)$ can be written as $k + m$ with $k > 0$ and $m > 0$ such that
> $p_k + 2d$ and $p_{p_m} + 2d$ are both prime.

```lean
theorem conjecture_1 (d : ℕ) (hd : 1 ≤ d) :
    ∃ N : ℕ, 0 < N ∧ ∀ n : ℕ, N < n →
      ∃ k m : ℕ, 0 < k ∧ 0 < m ∧ n = k + m ∧
        (Nat.nth Nat.Prime (k - 1) + 2 * d).Prime ∧
        (Nat.nth Nat.Prime (Nat.nth Nat.Prime (m - 1) - 1) + 2 * d).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237348.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237348.lean#L83).

## `OeisA237348.conjecture_2`

Open: stated without proof.

> In particular, we may take $(N(1), N(2), \dots, N(10)) = (2, 11, 4, 15, 31, 4, 2, 77, 4, 7)$
> in the conjecture.

```lean
theorem conjecture_2 (d : Fin 10) (n : ℕ)
    (hn : ![2, 11, 4, 15, 31, 4, 2, 77, 4, 7] d < n) :
    ∃ k m : ℕ, 0 < k ∧ 0 < m ∧ n = k + m ∧
      (Nat.nth Nat.Prime (k - 1) + 2 * (d.val + 1)).Prime ∧
      (Nat.nth Nat.Prime (Nat.nth Nat.Prime (m - 1) - 1) + 2 * (d.val + 1)).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237348.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237348.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/237348.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237348.lean)
- [A237348](https://oeis.org/A237348)
