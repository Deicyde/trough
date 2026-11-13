---
declaration: theorem
origin: cited
lean: OeisA64313.conjecture
statement: formalized
---

# Integer part of area of a regular polygon with $n$ sides each of length 1

> The area of a regular $n$-gon with side length 1 is given by
> $\frac{n}{4} \cot(\pi / n) = \frac{n}{4 \tan(\pi / n)}$.
>
> *References:*
> - [A064313](https://oeis.org/A064313)

*Quoted from [FormalConjectures/OEIS/64313.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/64313.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA64313.conjecture`

Open: stated without proof.

> "Usually (perhaps always?) $\lfloor n^2 / (4\pi) - \pi / 12 \rfloor$ for a polygon of circumference $n$.
> Note that the area of a circle with circumference $C$ is $C^2 / (4\pi)$."

```lean
theorem conjecture (n : ℕ) (hn : 3 ≤ n) :
    a n = (Int.floor ((n : ℝ) ^ 2 / (4 * Real.pi) - Real.pi / 12)).toNat
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/OEIS/64313.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/64313.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/64313.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/64313.lean)
- [A064313](https://oeis.org/A064313)
