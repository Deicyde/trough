---
declaration: theorem
origin: cited
lean: OeisA119591.conjecture
statement: formalized
---

# Least $k \ge 1$ such that $2 \cdot n^k - 1$ is prime

> $a(n) = \min \{k \ge 1 \mid \text{Prime}(2 \cdot n^k - 1)\}$ for $n \ge 2$.
>
> *References:*
> - [A119591](https://oeis.org/A119591)

*Quoted from [FormalConjectures/OEIS/119591.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/119591.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 test statements, counted here but not shown.

## `OeisA119591.conjecture`

Open: stated without proof.

> Is $a(n)$ defined for all $n \ge 2$?
> That is, does there exist $k > 0$ such that $2 \cdot n^k - 1$ is prime?

```lean
theorem conjecture (n : ℕ) (hn : 2 ≤ n) : ∃ k > 0, (2 * n ^ k - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/119591.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/119591.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/119591.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/119591.lean)
- [A119591](https://oeis.org/A119591)
