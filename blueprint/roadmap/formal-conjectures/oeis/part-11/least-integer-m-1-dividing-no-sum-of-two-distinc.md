---
declaration: theorem
origin: cited
lean: OeisA210186.conjecture_1, OeisA210186.conjecture_2
statement: formalized
---

# Least integer $m > 1$ dividing no sum of two distinct primorials up to $P_n$

> For $n \ge 1$, $a(n)$ is the least integer $m > 1$ such that $m$ divides none of $P_i + P_j$ with
> $0 < i < j \le n$, where $P_k$ is the product of the first $k$ primes.
>
> *References:*
> - [A210186](https://oeis.org/A210186)

*Quoted from [FormalConjectures/OEIS/210186.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/210186.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA210186.conjecture_1`

Open: stated without proof.

> "Conjecture: all the terms are primes."
> - _Zhi-Wei Sun_, Mar 18 2012

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 ≤ n) : (a n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/210186.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/210186.lean#L123).

## `OeisA210186.conjecture_2`

Open: stated without proof.

> "Conjecture: $a(n) < n^2$ for all $n > 1$."
> - _Zhi-Wei Sun_, Mar 18 2012

```lean
theorem conjecture_2 (n : ℕ) (hn : 1 < n) : a n < n ^ 2
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/210186.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/210186.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/210186.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/210186.lean)
- [A210186](https://oeis.org/A210186)
