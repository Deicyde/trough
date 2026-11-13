---
declaration: theorem
origin: cited
lean: OeisA238568.conjecture_1, OeisA238568.conjecture_2, OeisA238568.conjecture_3, OeisA238568.conjecture_4, OeisA238568.conjecture_5
statement: formalized
---

# Number of positive integers $k < n$ such that $n^2 - \pi(k n)$ is prime

> The sequence $a(n)$ counts the number of positive integers $k < n$ such that
> $n^2 - \pi(k n)$ is prime, where $\pi(x)$ is the prime counting function:
>
> $$a(n) = |\{0 < k < n : n^2 - \pi(k n) \text{ is prime}\}|$$
>
> *References:*
> - [A238568](https://oeis.org/A238568)
> - [Problems on combinatorial properties of primes](https://arxiv.org/abs/1402.6641)
>   by *Zhi-Wei Sun* (2014)

*Quoted from [FormalConjectures/OEIS/238568.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 5 test statements, counted here but not shown.

## `OeisA238568.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238568.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean#L67).

## `OeisA238568.conjecture_2`

Open: stated without proof.

> Conjecture (i): $a(n) = 1$ only for $n \in \{2, 3, 4, 8, 10, 24, 41\}$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n ∈ ({2, 3, 4, 8, 10, 24, 41} : Set ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238568.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean#L74).

## `OeisA238568.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For any integer $n > 6$, there is a positive integer $k < n$ with
> $n^2 + \pi(k n) - 1$ prime.

```lean
theorem conjecture_3 (n : ℕ) (hn : 6 < n) :
    ∃ k : ℕ, 0 < k ∧ k < n ∧ Nat.Prime (n ^ 2 + Nat.primeCounting (k * n) - 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238568.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean#L83).

## `OeisA238568.conjecture_4`

Open: stated without proof.

> Conjecture (iii), part 1: If $n > 2$, then $\pi(n^2) - \pi(k n)$ is prime for some $0 < k < n$.

```lean
theorem conjecture_4 (n : ℕ) (hn : 2 < n) :
    ∃ k : ℕ, 0 < k ∧ k < n ∧
      Nat.Prime (Nat.primeCounting (n ^ 2) - Nat.primeCounting (k * n))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238568.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean#L91).

## `OeisA238568.conjecture_5`

Open: stated without proof.

> Conjecture (iii), part 2: If $n > 1$, then $\pi(n^2) + \pi(k n) - 1$ is prime for some $0 < k < n$.

```lean
theorem conjecture_5 (n : ℕ) (hn : 1 < n) :
    ∃ k : ℕ, 0 < k ∧ k < n ∧
      Nat.Prime (Nat.primeCounting (n ^ 2) + Nat.primeCounting (k * n) - 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238568.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/238568.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238568.lean)
- [A238568](https://oeis.org/A238568)
