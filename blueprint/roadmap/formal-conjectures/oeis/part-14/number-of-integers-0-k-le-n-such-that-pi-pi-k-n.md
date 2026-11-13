---
declaration: theorem
origin: cited
lean: OeisA238902.conjecture_1, OeisA238902.conjecture_2
statement: formalized
---

# Number of integers $0 < k \le n$ such that $\pi(\pi(k n))$ is a square

> The sequence $a(n)$ counts the number of integers $k \in \{1, \dots, n\}$ such that
> $\pi(\pi(k n))$ is a square, where $\pi(x)$ is the prime counting function:
>
> $$a(n) = |\{0 < k \le n : \pi(\pi(k n)) \text{ is a square}\}|$$
>
> *References:*
> - [A238902](https://oeis.org/A238902)
> - [Problems on combinatorial properties of primes](https://arxiv.org/abs/1402.6641)
>   by *Zhi-Wei Sun* (2014)

*Quoted from [FormalConjectures/OEIS/238902.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238902.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA238902.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 0$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238902.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238902.lean#L69).

## `OeisA238902.conjecture_2`

Open: stated without proof.

> Conjecture (ii): For every $n = 1, 2, 3, \dots$, there exists a positive integer
> $k \le (n + 1) / 2$ such that $\pi(\pi(k n))$ is a triangular number.

```lean
theorem conjecture_2 (n : ℕ) (hn : 0 < n) :
    ∃ k : ℕ, 0 < k ∧ k ≤ (n + 1) / 2 ∧
      (Nat.primeCounting (Nat.primeCounting (k * n))).IsTriangular
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238902.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238902.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/238902.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238902.lean)
- [A238902](https://oeis.org/A238902)
