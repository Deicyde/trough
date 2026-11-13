---
declaration: theorem
origin: cited
lean: OeisA53000.conjecture
statement: formalized
---

# $a(n) = (\text{smallest prime} > n^2) - n^2$

> The difference between the smallest prime strictly greater than $n^2$ and $n^2$.
>
> *References:*
> - [A053000](https://oeis.org/A053000)

*Quoted from [FormalConjectures/OEIS/53000.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/53000.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA53000.conjecture`

Open: stated without proof.

> Conjecture: $a(n) \le 1 + \phi(n)$ for $n > 0$. This improves on Oppermann's conjecture, which says
> $a(n) < n$.
> - Thomas Ordowski, Dec 17 2014

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : a n ≤ 1 + n.totient
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/53000.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/53000.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/53000.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/53000.lean)
- [A053000](https://oeis.org/A053000)
