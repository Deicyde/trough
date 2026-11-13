---
declaration: theorem
origin: cited
lean: OeisA260194.conjecture
statement: formalized
---

# A GCD-Driven Sequence with Universal Jumps

> OEIS A260194 begins with three ones and then adds the greatest common divisor of the current term
> and the term two places earlier. The open question asks whether every positive integer occurs as
> an adjacent difference.
>
> *References:*
> - [OEIS A260194](https://oeis.org/A260194)

*Quoted from [FormalConjectures/OEIS/260194.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/260194.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 10 test statements, counted here but not shown.

## `OeisA260194.conjecture`

Open: stated without proof.

> Does every positive integer occur as a difference in this sequence?

```lean
theorem conjecture :
    ∀ d > 0, ∃ n, a (n + 1) = a n + d
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/260194.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/260194.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/260194.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/260194.lean)
- [OEIS A260194](https://oeis.org/A260194)
