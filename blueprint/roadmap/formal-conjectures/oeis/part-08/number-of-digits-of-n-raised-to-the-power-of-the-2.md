---
declaration: theorem
origin: cited
lean: OeisA113019.conjecture
statement: formalized
proof: formalized
---

# Number of digits of n raised to the power of the digital root of n

> *References:*
> - [A113019](https://oeis.org/A113019)

*Quoted from [FormalConjectures/OEIS/113019.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113019.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA113019.conjecture`

Proved here.

> $n=1$ and $32$ are fixed points. Are there any others?
>
> Yes: 9^9 = 387420489 is also a fixed point. - [Kenta Kitamura](https://oeis.org/wiki/User:Kenta_Kitamura), Aug 14 2026

```lean
theorem conjecture : ¬ ∀ n : ℕ, a n = n → n = 1 ∨ n = 32
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113019.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113019.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113019.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113019.lean)
- [A113019](https://oeis.org/A113019)
