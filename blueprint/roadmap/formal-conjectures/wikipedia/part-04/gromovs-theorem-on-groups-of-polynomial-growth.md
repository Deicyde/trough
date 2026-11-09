---
declaration: theorem
origin: cited
lean: GromovPolynomialGrowth.GromovPolynomialGrowthTheorem
statement: formalized
---

# Gromov's theorem on groups of polynomial growth

> *Reference:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Gromov%27s_theorem_on_groups_of_polynomial_growth)

*Quoted from [FormalConjectures/Wikipedia/GromovPolynomialGrowth.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GromovPolynomialGrowth.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `GromovPolynomialGrowth.GromovPolynomialGrowthTheorem`

Solved: stated here without proof.

> **Gromov's Polynomial Growth Theorem** : A finitely generated group has
> polynomial growth if and only if it is virtually nilpotent.

```lean
theorem GromovPolynomialGrowthTheorem [Group.FG G] :
    HasPolynomialGrowth G ↔ Group.IsVirtuallyNilpotent G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/GromovPolynomialGrowth.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GromovPolynomialGrowth.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GromovPolynomialGrowth.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GromovPolynomialGrowth.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Gromov%27s_theorem_on_groups_of_polynomial_growth)
