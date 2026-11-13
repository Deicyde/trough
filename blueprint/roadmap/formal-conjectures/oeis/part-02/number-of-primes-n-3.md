---
declaration: theorem
origin: cited
lean: OeisA38098.conjecture1, OeisA38098.conjecture2
statement: formalized
---

# Number of primes $< n^3$

> Number of primes strictly less than $n^3$.
>
> *References:*
> - [A038098](https://oeis.org/A038098)

*Quoted from [FormalConjectures/OEIS/38098.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38098.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA38098.conjecture1`

Open: stated without proof.

> Conjecture (i): for any integer $k > 2$, the sequence $\pi(n^k)/n^k$ ($n = 2, 3, \ldots$) is strictly
> decreasing, where $\pi(x)$ denotes the number of primes not exceeding $x$.
> - Zhi-Wei Sun, Oct 17 2015

```lean
theorem conjecture1 (k : ℕ) (hk : 2 < k) (n : ℕ) (hn : 2 ≤ n) :
    (Nat.primeCounting ((n + 1) ^ k) : ℚ) / ((n + 1) ^ k : ℚ) <
    (Nat.primeCounting (n ^ k) : ℚ) / (n ^ k : ℚ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38098.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38098.lean#L67).

## `OeisA38098.conjecture2`

Open: stated without proof.

> Conjecture (ii): all the numbers $\pi(n^2)/n^2$ ($n = 1, 2, 3, \ldots$) are pairwise distinct.
> Moreover, we have $\pi(n^2)/n^2 > \pi((n+1)^2)/(n+1)^2$ for all $n > 15646$.
> - Zhi-Wei Sun, Oct 17 2015

```lean
theorem conjecture2 :
    (∀ m n : ℕ, 1 ≤ m → 1 ≤ n →
      (Nat.primeCounting (m ^ 2) : ℚ) / (m ^ 2 : ℚ) =
      (Nat.primeCounting (n ^ 2) : ℚ) / (n ^ 2 : ℚ) → m = n) ∧
    (∀ n : ℕ, 15646 < n →
      (Nat.primeCounting ((n + 1) ^ 2) : ℚ) / ((n + 1) ^ 2 : ℚ) <
      (Nat.primeCounting (n ^ 2) : ℚ) / (n ^ 2 : ℚ))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38098.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38098.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/38098.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38098.lean)
- [A038098](https://oeis.org/A038098)
