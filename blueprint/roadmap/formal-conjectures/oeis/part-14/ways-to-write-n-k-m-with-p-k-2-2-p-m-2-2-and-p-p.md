---
declaration: theorem
origin: cited
lean: OeisA237413.conjecture
statement: formalized
---

# Ways to write $n = k + m$ with $p_k^2 - 2$, $p_m^2 - 2$, and $p_{p_m}^2 - 2$ all prime

> Let $p_j$ denote the $j$-th prime number. The sequence $a(n)$ counts the number of ways to write
> $n = k + m$ with $k > 0$ and $m > 0$ such that $p_k^2 - 2$, $p_m^2 - 2$, and $p_{p_m}^2 - 2$ are all
> prime.
>
> *References:*
> - [A237413](https://oeis.org/A237413)

*Quoted from [FormalConjectures/OEIS/237413.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237413.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA237413.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237413.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237413.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/237413.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237413.lean)
- [A237413](https://oeis.org/A237413)
