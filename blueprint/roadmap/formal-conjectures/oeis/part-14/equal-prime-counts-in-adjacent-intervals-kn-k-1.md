---
declaration: theorem
origin: cited
lean: OeisA238281.conjecture_1, OeisA238281.conjecture_2, OeisA238281.conjecture_3
statement: formalized
---

# Equal prime counts in adjacent intervals $(kn, (k+1)n)$ and $((k+1)n, (k+2)n)$

> Let $\pi$ denote the prime counting function. The sequence $a(n)$ counts the number of integers
> $0 < k < n$ such that the intervals $(kn, (k+1)n)$ and $((k+1)n, (k+2)n)$ contain the same number
> of primes.
>
> *References:*
> - [A238281](https://oeis.org/A238281)

*Quoted from [FormalConjectures/OEIS/238281.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238281.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA238281.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238281.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238281.lean#L61).

## `OeisA238281.conjecture_2`

Open: stated without proof.

> Conjecture: Moreover, if $n > 1$ is not equal to $8$, then there is a positive integer $k < n$ with
> $2k + 1$ prime such that the two intervals $((k-1)n, kn]$ and $(kn, (k+1)n]$ contain the same
> number of primes.
>
> OEIS states open intervals, but for $n = 2$ the only candidate is $k = 1$, where the open
> interval $(0, 2)$ contains 0 primes while $(2, 4)$ contains 1 prime. Half-open intervals
> $((k-1)n, kn]$ match Sun's Mathematica formula `PrimePi[k*n] - PrimePi[(k-1)*n]` and hold for
> $n = 2$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 1 < n) (h8 : n ≠ 8) :
    ∃ k : ℕ, 0 < k ∧ k < n ∧ (2 * k + 1).Prime ∧
      Nat.primeCounting (k * n) - Nat.primeCounting ((k - 1) * n) =
      Nat.primeCounting ((k + 1) * n) - Nat.primeCounting (k * n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238281.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238281.lean#L75).

## `OeisA238281.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For any integer $n > 4$, there is a positive integer $k < p_n$ such that all the
> three intervals $(kn, (k+1)n)$, $((k+1)n, (k+2)n)$, $((k+2)n, (k+3)n)$ contain the same number of
> primes, i.e., $\pi(kn)$, $\pi((k+1)n)$, $\pi((k+2)n)$, $\pi((k+3)n)$ form a $4$-term arithmetic
> progression.

```lean
theorem conjecture_3 (n : ℕ) (hn : 4 < n) :
    ∃ k : ℕ, 0 < k ∧ k < Nat.nth Nat.Prime (n - 1) ∧
      Nat.primeCounting ((k + 1) * n) - Nat.primeCounting (k * n) =
      Nat.primeCounting ((k + 2) * n) - Nat.primeCounting ((k + 1) * n) ∧
      Nat.primeCounting ((k + 2) * n) - Nat.primeCounting ((k + 1) * n) =
      Nat.primeCounting ((k + 3) * n) - Nat.primeCounting ((k + 2) * n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238281.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238281.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/238281.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238281.lean)
- [A238281](https://oeis.org/A238281)
