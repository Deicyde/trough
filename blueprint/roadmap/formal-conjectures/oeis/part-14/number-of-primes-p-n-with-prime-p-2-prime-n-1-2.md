---
declaration: theorem
origin: cited
lean: OeisA238585.conjecture_1, OeisA238585.conjecture_2, OeisA238585.conjecture_3, OeisA238585.conjecture_4, OeisA238585.conjecture_5
statement: formalized
---

# Number of primes $p < n$ with $\text{prime}(p)^2 + (\text{prime}(n) - 1)^2$ prime

> The sequence $a(n)$ counts the number of primes $p < n$ such that
> $\text{prime}(p)^2 + (\text{prime}(n) - 1)^2$ is prime, where $\text{prime}(i)$ denotes the
> $i$-th prime number (1-indexed).
>
> *References:*
> - [A238585](https://oeis.org/A238585)
> - [Problems on combinatorial properties of primes](https://arxiv.org/abs/1402.6641)
>   by *Zhi-Wei Sun* (2014)

*Quoted from [FormalConjectures/OEIS/238585.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 6 test statements, counted here but not shown.

## `OeisA238585.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ unless $n$ divides $6$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) :
    0 < a n ↔ ¬(n ∣ 6)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238585.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean#L95).

## `OeisA238585.conjecture_2`

Open: stated without proof.

> Conjecture (i): $a(n) = 1$ only for
> $n \in \{4, 5, 7, 10, 11, 12, 19, 21, 22, 31, 42, 44\}$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 0 < n) :
    a n = 1 ↔ n ∈ ({4, 5, 7, 10, 11, 12, 19, 21, 22, 31, 42, 44} : Set ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238585.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean#L104).

## `OeisA238585.conjecture_3`

Open: stated without proof.

> Conjecture (ii): If $n > 2$ is not equal to $9$, then
> $\text{prime}(n)^2 + (\text{prime}(p) - 1)^2$ is prime for some prime $p < n$.

```lean
theorem conjecture_3 (n : ℕ) (hn : 2 < n) (hn9 : n ≠ 9) :
    ∃ p : ℕ, p < n ∧ p.Prime ∧
      Nat.Prime (Nat.nth Nat.Prime (n - 1) ^ 2 + (Nat.nth Nat.Prime (p - 1) - 1) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238585.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean#L113).

## `OeisA238585.conjecture_4`

Open: stated without proof.

> Conjecture (iii), part 1: For $n > 3$, there is a prime $p < n$ with
> $\text{prime}(p) + \text{prime}(n) + 1$ prime.

```lean
theorem conjecture_4 (n : ℕ) (hn : 3 < n) :
    ∃ p : ℕ, p < n ∧ p.Prime ∧
      Nat.Prime (Nat.nth Nat.Prime (p - 1) + Nat.nth Nat.Prime (n - 1) + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238585.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean#L123).

## `OeisA238585.conjecture_5`

Open: stated without proof.

> Conjecture (iii), part 2: If $n > 9$ is not equal to $18$, then
> $\text{prime}(p)^2 + \text{prime}(n)^2 - 1$ is prime for some prime $p < n$.

```lean
theorem conjecture_5 (n : ℕ) (hn : 9 < n) (hn18 : n ≠ 18) :
    ∃ p : ℕ, p < n ∧ p.Prime ∧
      Nat.Prime (Nat.nth Nat.Prime (p - 1) ^ 2 + Nat.nth Nat.Prime (n - 1) ^ 2 - 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238585.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean#L133).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/238585.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/238585.lean)
- [A238585](https://oeis.org/A238585)
