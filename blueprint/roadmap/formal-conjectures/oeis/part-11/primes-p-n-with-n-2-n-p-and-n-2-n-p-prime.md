---
declaration: theorem
origin: cited
lean: OeisA219023.conjecture_1, OeisA219023.conjecture_2, OeisA219023.conjecture_3, OeisA219023.conjecture_4
statement: formalized
---

# Primes $p < n$ with $n^2 - n + p$ and $n^2 + n - p$ prime

> For $n \ge 1$, $a(n)$ is the number of primes $p < n$ such that $n^2 - n + p$ and $n^2 + n - p$
> are both prime.
>
> *References:*
> - [A219023](https://oeis.org/A219023)

*Quoted from [FormalConjectures/OEIS/219023.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219023.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA219023.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 2732$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 2732 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219023.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219023.lean#L59).

## `OeisA219023.conjecture_2`

Open: stated without proof.

> Conjecture: For $n > 3512$, there is a prime $p \in (n, 2n)$
> such that both $n^2 - n + p$ and $n^2 + n - p$ are prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (n : ℕ) (hn : 3512 < n) :
    ∃ p : ℕ, p.Prime ∧ n < p ∧ p < 2 * n ∧
      Nat.Prime (n ^ 2 - n + p) ∧ Nat.Prime (n ^ 2 + n - p)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219023.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219023.lean#L68).

## `OeisA219023.conjecture_3`

Open: stated without proof.

> Conjecture: For $n > 1828$, there is a prime $p < n$ such that
> both $n^2 - n - p$ and $n^2 + n + p$ are prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3 (n : ℕ) (hn : 1828 < n) :
    ∃ p : ℕ, p.Prime ∧ p < n ∧
      Nat.Prime (n ^ 2 - n - p) ∧ Nat.Prime (n ^ 2 + n + p)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219023.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219023.lean#L79).

## `OeisA219023.conjecture_4`

Open: stated without proof.

> Conjecture: For $n > 4517$, there is a prime $p \in (n, 2n)$
> such that both $n^2 - n - p$ and $n^2 + n + p$ are prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_4 (n : ℕ) (hn : 4517 < n) :
    ∃ p : ℕ, p.Prime ∧ n < p ∧ p < 2 * n ∧
      Nat.Prime (n ^ 2 - n - p) ∧ Nat.Prime (n ^ 2 + n + p)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219023.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219023.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/219023.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219023.lean)
- [A219023](https://oeis.org/A219023)
