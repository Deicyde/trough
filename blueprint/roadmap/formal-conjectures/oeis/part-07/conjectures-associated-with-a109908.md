---
declaration: theorem
origin: cited
lean: OeisA109908.conjecture
statement: formalized
---

# Conjectures associated with A109908

> $a(n)$ = greatest prime of the form $k(n-k)-1$, or $0$ if no such prime exists.
>
> *References:*
> - [A109908](https://oeis.org/A109908)

*Quoted from [FormalConjectures/OEIS/109908.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/109908.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109908.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for $n > 3$.

```lean
theorem conjecture : ∀ n > 3, a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109908.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/109908.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109908.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/109908.lean)
- [A109908](https://oeis.org/A109908)
