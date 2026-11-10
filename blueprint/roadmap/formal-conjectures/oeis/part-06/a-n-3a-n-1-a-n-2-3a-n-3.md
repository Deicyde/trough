---
declaration: theorem
origin: cited
lean: OeisA103425.conjecture, OeisA103425.conjecture.variants.nonconstant, OeisA103425.conjecture.variants.nonconstant_distinct_coeffs
statement: formalized
---

# $a(n) = 3a(n-1) + a(n-2) - 3a(n-3)$

> *References:*
> - [A103425](https://oeis.org/A103425)

*Quoted from [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103425.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 5 test statements, counted here but not shown.

## `OeisA103425.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a103425-prime-free/blob/b04b155/lean/OeisA103425FC.lean#L13-L35](https://github.com/KitaKen1/oeis-a103425-prime-free/blob/b04b155/lean/OeisA103425FC.lean#L13-L35).

> The current sequence contains primes, including $3, 5, 41, 21523361$.
> Is there an $(a, b, c)$ weighted tribonacci sequence with $a, b, c$ relatively prime
> which is prime-free?
>
> Yes: take $(a, b, c) = (1, 1, -1)$ and the constant sequence $x(n) = 4$.
> The linked Lean proof is by Kenta Kitamura.

```lean
theorem conjecture :
    ∃ (a b c : ℤ) (x : ℕ → ℤ),
      Nat.gcd (Int.gcd a b) c.natAbs = 1 ∧
      IsWeightedTribonacci a b c x ∧
      ∀ n, ¬ (x n).natAbs.Prime
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103425.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103425.lean#L74).

## `OeisA103425.conjecture.variants.nonconstant`

Proved here.

> Is there a non-constant $(a, b, c)$ weighted tribonacci sequence with $a, b, c$ relatively
> prime which is prime-free?
>
> Yes: take $(a, b, c) = (1, 1, -1)$ and $x(n) = 4(n + 1)$.

```lean
theorem conjecture.variants.nonconstant :
    ∃ (a b c : ℤ) (x : ℕ → ℤ),
      Nat.gcd (Int.gcd a b) c.natAbs = 1 ∧
      IsWeightedTribonacci a b c x ∧
      (∃ m n, x m ≠ x n) ∧
      ∀ n, ¬ (x n).natAbs.Prime
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103425.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103425.lean#L88).

## `OeisA103425.conjecture.variants.nonconstant_distinct_coeffs`

Proved here.

> Is there a non-constant $(a, b, c)$ weighted tribonacci sequence with $a, b, c$ relatively
> prime and pairwise distinct which is prime-free?
>
> Yes: take $(a, b, c) = (3, -3, 1)$ and $x(n) = (n + 2)^2$.

```lean
theorem conjecture.variants.nonconstant_distinct_coeffs :
    ∃ (a b c : ℤ) (x : ℕ → ℤ),
      Nat.gcd (Int.gcd a b) c.natAbs = 1 ∧
      a ≠ b ∧ a ≠ c ∧ b ≠ c ∧
      IsWeightedTribonacci a b c x ∧
      (∃ m n, x m ≠ x n) ∧
      ∀ n, ¬ (x n).natAbs.Prime
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103425.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103425.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/103425.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103425.lean)
- [A103425](https://oeis.org/A103425)
