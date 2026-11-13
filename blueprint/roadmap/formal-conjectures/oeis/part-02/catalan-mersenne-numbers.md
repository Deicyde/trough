---
declaration: theorem
origin: cited
lean: OeisA7013.conjecture
statement: formalized
---

# Catalan-Mersenne numbers

> Catalan-Mersenne numbers: $a(0) = 2$; for $n \ge 0$, $a(n+1) = 2^{a(n)} - 1$.
>
> *References:*
> - [A007013](https://oeis.org/A007013)

*Quoted from [FormalConjectures/OEIS/7013.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/7013.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA7013.conjecture`

Open: stated without proof.

> Catalan-Mersenne conjecture: All terms of the Catalan-Mersenne sequence are prime.

```lean
theorem conjecture (n : ℕ) : (a n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/7013.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/7013.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/7013.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/7013.lean)
- [A007013](https://oeis.org/A007013)
