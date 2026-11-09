---
declaration: theorem
origin: cited
lean: OeisA219838.conjecture_1, OeisA219838.conjecture_2, OeisA219838.conjecture_3
statement: formalized
---

# Partitions of $n$ into $x + y$ with $(xy)^2 + xy + 1$ prime

> Number of ways to write $n$ as $x + y$ with $0 < x \le y$ and $(xy)^2 + xy + 1$ prime.
>
> *References:*
> - [A219838](https://oeis.org/A219838)

*Quoted from [FormalConjectures/OEIS/219838.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219838.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 6 test statements, counted here but not shown.

## `OeisA219838.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 1) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219838.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219838.lean#L62).

## `OeisA219838.conjecture_2`

Open: stated without proof.

> The author also guesses that any integer $n > 1157$ can be written as $x + y$ with $x$ and $y$
> positive integers, and $(xy)^2 + xy + 1$ and $(xy)^2 + xy - 1$ twin primes.

```lean
theorem conjecture_2 (n : ℕ) (hn : n > 1157) :
    ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      Nat.Prime ((x * y) ^ 2 + x * y - 1) ∧ Nat.Prime ((x * y) ^ 2 + x * y + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219838.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219838.lean#L70).

## `OeisA219838.conjecture_3`

Open: stated without proof.

> Conjecture: For each prime $p$, any sufficiently
> large integer $n$ can be written as $x + y$, where $x$ and $y$ are positive integers with
> $\frac{(xy)^p - 1}{xy - 1}$ prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3 (p : ℕ) (hp : p.Prime) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
      ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
        Nat.Prime (((x * y) ^ p - 1) / (x * y - 1))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219838.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219838.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/219838.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/219838.lean)
- [A219838](https://oeis.org/A219838)
