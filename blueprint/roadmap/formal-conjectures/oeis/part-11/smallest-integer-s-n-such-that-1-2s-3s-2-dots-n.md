---
declaration: theorem
origin: cited
lean: OeisA217785.conjecture_1, OeisA217785.conjecture_2, OeisA217785.conjecture_3, OeisA217785.conjecture_4
statement: formalized
---

# Smallest integer $s > n$ such that $1 + 2s + 3s^2 + \dots + n s^{n-1}$ is prime

> For $n \ge 2$, $a(n)$ is the smallest integer $s > n$ such that the sum
> $P_n(s) = \sum_{k=0}^{n-1} (k+1) s^k$ is a prime number.
>
> *References:*
> - [A217785](https://oeis.org/A217785)

*Quoted from [FormalConjectures/OEIS/217785.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217785.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA217785.conjecture_1`

Open: stated without proof.

> Conjecture: For each $n \ge 2$, there are infinitely many primes of the form
> $1 + 2s + \dots + n s^{n-1}$ where $s$ is a positive integer.

```lean
theorem conjecture_1 (n : ℕ) (hn : 2 ≤ n) :
    {s : ℕ | 0 < s ∧ Nat.Prime (polyP n s)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/217785.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217785.lean#L101).

## `OeisA217785.conjecture_2`

Open: stated without proof.

> Conjecture: For each $n \ge 2$, $a(n) < 12 n^2$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 2 ≤ n) :
    ∃ m < 12 * n ^ 2, a n = some m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/217785.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217785.lean#L109).

## `OeisA217785.conjecture_3`

Open: stated without proof.

> Conjecture: The polynomials $s_n(x) = \sum_{k=0}^n (k+1) x^k$ for
> $n \ge 1$ are all irreducible over the field of rational numbers.

```lean
theorem conjecture_3 (n : ℕ) (hn : 1 ≤ n) :
    Irreducible (Polynomial.map (Int.castRingHom ℚ) (polyS n))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/OEIS/217785.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217785.lean#L118).

## `OeisA217785.conjecture_4`

Open: stated without proof.

> Conjecture: For $n \ge 1$, the polynomial $s_n(x) = \sum_{k=0}^n (k+1) x^k$ is
> reducible modulo every prime if and only if $n$ has the form $8k(k+1)$ where $k$ is a
> positive integer.

```lean
theorem conjecture_4 (n : ℕ) (hn : 1 ≤ n) :
    (∀ p : ℕ, p.Prime → ¬ Irreducible (Polynomial.map (Int.castRingHom (ZMod p)) (polyS n))) ↔
      ∃ k : ℕ, 0 < k ∧ n = 8 * k * (k + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/OEIS/217785.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217785.lean#L128).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/217785.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217785.lean)
- [A217785](https://oeis.org/A217785)
