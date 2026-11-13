---
declaration: theorem
origin: cited
lean: OeisA80101.conjecture
statement: formalized
---

# Number of prime powers strictly between $n$-th prime and $(n+1)$-th prime

> The sequence $a(n)$ is the number of prime powers $k$ strictly between the $n$-th prime $p_n$
> and the $(n+1)$-th prime $p_{n+1}$: $p_n < k < p_{n+1}$.
>
> *References:*
> - [A080101](https://oeis.org/A080101)

*Quoted from [FormalConjectures/OEIS/80101.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/80101.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA80101.conjecture`

Open: stated without proof.

> It is conjectured that $a(n) \le 2$ for all $n$.

```lean
theorem conjecture (n : ℕ) : a n ≤ 2
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/80101.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/80101.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/80101.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/80101.lean)
- [A080101](https://oeis.org/A080101)
