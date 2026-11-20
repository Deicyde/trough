---
declaration: theorem
origin: cited
lean: OeisA242775.conjecture
statement: formalized
---

# Smallest $k \ge 1$ such that the concatenation of $k$ threes and $\text{prime}(n)$ is prime

> Let $b_k = 3 \dots 3$ consist of $k \ge 1$ threes in base $10$. The sequence $a(n)$ is the smallest
> $k \ge 1$ such that the decimal concatenation of $b_k$ and $\text{prime}(n)$ is prime, or
> $a(n) = 0$ if no such prime exists.
>
> *References:*
> - [A242775](https://oeis.org/A242775)

*Quoted from [FormalConjectures/OEIS/242775.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/242775.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `OeisA242775.conjecture`

Open: stated without proof.

> Conjecture: For $n \ge 4$, $a(n) > 0$.

```lean
theorem conjecture (n : ℕ) (hn : 4 ≤ n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/242775.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/242775.lean#L155).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/242775.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/242775.lean)
- [A242775](https://oeis.org/A242775)
