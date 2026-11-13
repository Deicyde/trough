---
declaration: theorem
origin: cited
lean: OeisA34694.conjecture
statement: formalized
---

# Smallest prime $\equiv 1 \pmod n$

> $$a(n) = \min \{p \in \mathbb{P} \mid p \equiv 1 \pmod n\}$$
>
> *References:*
> - [A034694](https://oeis.org/A034694)

*Quoted from [FormalConjectures/OEIS/34694.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/34694.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA34694.conjecture`

Open: stated without proof.

> "Conjecture: $a(n) < n^2$ for $n > 1$. - _Thomas Ordowski_, Dec 19 2016"

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : a n < n ^ 2
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/34694.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/34694.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/34694.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/34694.lean)
- [A034694](https://oeis.org/A034694)
