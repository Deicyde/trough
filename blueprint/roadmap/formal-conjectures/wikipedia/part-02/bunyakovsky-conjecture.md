---
declaration: theorem
origin: cited
lean: Bunyakovsky.bunyakovsky_conjecture
statement: formalized
---

# Bunyakovsky conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Bunyakovsky_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Bunyakovsky.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bunyakovsky.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Bunyakovsky.bunyakovsky_conjecture`

Open: stated without proof.

> **Bunyakovsky conjecture**
> If a polynomial $f$ over integers satisfies both Schinzel and Bunyakovsky conditions,
> there exist infinitely many natural numbers $m$ such that $f(m)$ is prime.

```lean
theorem bunyakovsky_conjecture (f : ℤ[X]) :
    BunyakovskyCondition f ∧ SchinzelCondition {f} →
    Infinite {n : ℕ | (f.eval (n : ℤ)).natAbs.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Bunyakovsky.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bunyakovsky.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Bunyakovsky.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bunyakovsky.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Bunyakovsky_conjecture)
