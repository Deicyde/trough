---
declaration: theorem
origin: cited
lean: Bunyakovsky.bunyakovsky_conjecture
statement: formalized
---

# Bunyakovsky conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Bunyakovsky_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Bunyakovsky.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Bunyakovsky.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

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

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Bunyakovsky.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Bunyakovsky.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Bunyakovsky.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Bunyakovsky.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Bunyakovsky_conjecture)
