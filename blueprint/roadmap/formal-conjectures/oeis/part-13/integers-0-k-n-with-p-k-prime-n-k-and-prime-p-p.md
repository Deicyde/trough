---
declaration: theorem
origin: cited
lean: OeisA234694.conjecture_1, OeisA234694.conjecture_2, OeisA234694.conjecture_3, OeisA234694.conjecture_4, OeisA234694.conjecture_5, OeisA234694.conjecture_6
statement: formalized
---

# Integers $0 < k < n$ with $p = k + \mathrm{prime}(n - k)$ and $\mathrm{prime}(p) - p + 1$ prime

> Let $\mathrm{prime}(m)$ denote the $m$-th prime number. The sequence $a(n)$ counts the integers
> $0 < k < n$ such that $p = k + \mathrm{prime}(n - k)$ and $\mathrm{prime}(p) - p + 1$ are both
> prime.
>
> *References:*
> - [A234694](https://oeis.org/A234694)

*Quoted from [FormalConjectures/OEIS/234694.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 open. It also has 5 test statements, counted here but not shown.

## `OeisA234694.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 9$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 9 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234694.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean#L86).

## `OeisA234694.conjecture_2`

Open: stated without proof.

> Conjecture (i): For any integer $n > 51$ there is a positive integer $k < n$ such that
> $p = k + \mathrm{prime}(n - k)$ and $\mathrm{prime}(p) + p + 1$ are both prime.

```lean
theorem conjecture_2 (n : ℕ) (hn : 51 < n) :
    ∃ k, 0 < k ∧ k < n ∧
      let p := k + Nat.nth Nat.Prime (n - k - 1)
      p.Prime ∧ Nat.Prime (Nat.nth Nat.Prime (p - 1) + p + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234694.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean#L94).

## `OeisA234694.conjecture_3`

Open: stated without proof.

> Conjecture (ii): If $n > 9$, then there is a positive integer $k < n$ such that
> $m - 1$ and $\mathrm{prime}(m) + m$ are both prime, where $m = k + \mathrm{prime}(n - k)$.

```lean
theorem conjecture_3 (n : ℕ) (hn : 9 < n) :
    ∃ k, 0 < k ∧ k < n ∧
      let m := k + Nat.nth Nat.Prime (n - k - 1)
      Nat.Prime (m - 1) ∧ Nat.Prime (Nat.nth Nat.Prime (m - 1) + m)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234694.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean#L105).

## `OeisA234694.conjecture_4`

Open: stated without proof.

> Conjecture (ii): If $n > 21$, then there is a positive integer $k < n$ such that
> $m - 1$ and $\mathrm{prime}(m) - m$ are both prime, where $m = k + \mathrm{prime}(n - k)$.

```lean
theorem conjecture_4 (n : ℕ) (hn : 21 < n) :
    ∃ k, 0 < k ∧ k < n ∧
      let m := k + Nat.nth Nat.Prime (n - k - 1)
      Nat.Prime (m - 1) ∧ Nat.Prime (Nat.nth Nat.Prime (m - 1) - m)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234694.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean#L116).

## `OeisA234694.conjecture_5`

Open: stated without proof.

> Conjecture (iii): If $n > 483$, then for some $0 < k < n$ both $\mathrm{prime}(m) + m$
> and $\mathrm{prime}(m) - m$ are prime, where $m = k + \mathrm{prime}(n - k)$.

```lean
theorem conjecture_5 (n : ℕ) (hn : 483 < n) :
    ∃ k, 0 < k ∧ k < n ∧
      let m := k + Nat.nth Nat.Prime (n - k - 1)
      Nat.Prime (Nat.nth Nat.Prime (m - 1) + m) ∧
      Nat.Prime (Nat.nth Nat.Prime (m - 1) - m)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234694.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean#L127).

## `OeisA234694.conjecture_6`

Open: stated without proof.

> Conjecture (iv): If $n > 3$, then there is a positive integer $k < n$ such that
> $\mathrm{prime}(k + \mathrm{prime}(n - k)) + 2$ is prime.

```lean
theorem conjecture_6 (n : ℕ) (hn : 3 < n) :
    ∃ k, 0 < k ∧ k < n ∧
      let m := k + Nat.nth Nat.Prime (n - k - 1)
      Nat.Prime (Nat.nth Nat.Prime (m - 1) + 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234694.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/234694.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234694.lean)
- [A234694](https://oeis.org/A234694)
