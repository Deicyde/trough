---
declaration: theorem
origin: cited
lean: OeisA217317.conjecture
statement: formalized
---

# Number of primes between $n^2$ and $n^2 + (\log_2 n)^2$

> For $n \ge 1$, $a(n)$ is the number of primes between $n^2$ and $n^2 + (\log_2 n)^2$ inclusive,
> given by $\pi(\lfloor n^2 + (\log_2 n)^2 \rfloor) - \pi(n^2)$.
>
> *References:*
> - [A217317](https://oeis.org/A217317)

*Quoted from [FormalConjectures/OEIS/217317.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217317.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA217317.conjecture`

Open: stated without proof.

> Conjecture: For every $n > 4765516$, $a(n) > 0$.

```lean
theorem conjecture (n : ℕ) (hn : 4765516 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/217317.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217317.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/217317.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/217317.lean)
- [A217317](https://oeis.org/A217317)
