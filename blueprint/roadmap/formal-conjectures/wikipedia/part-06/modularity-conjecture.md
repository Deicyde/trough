---
declaration: theorem
origin: cited
lean: ModularityConjecture.modularity_conjecture
statement: formalized
---

# Modularity conjecture

> The **Modularity conjecture** (also known as the Shimura-Taniyama-Weil conjecture) states that
> every rational elliptic curve is modular, meaning that it can be
> associated with a modular form. We state the `a_p` version of the conjecture, which relates the
> coefficients of the modular form to the number of points on the elliptic curve over finite fields.
>
> Since we don't have the conductor of the elliptic curve, our definition of `a_p(E)` differs from
> that in the literature at primes of bad reduction. For this reason, we state the conjecture with the
> assumption that `p ∤ N`, in order to give an equivalent statement.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Modularity_theorem)
> - [F. Diamond and J. Shurman, *A First Course in Modular Forms*](https://doi.org/10.1007/978-0-387-27226-9)

*Quoted from [FormalConjectures/Wikipedia/ModularityConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ModularityConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `ModularityConjecture.modularity_conjecture`

Solved: stated here without proof.

> The Modularity Theorem (formerly Shimura-Taniyama-Weil conjecture): every elliptic curve
> over $\mathbb{Q}$ is modular.

```lean
theorem modularity_conjecture (E : WeierstrassCurve ℚ) [E.IsElliptic] : modularityConjecture E
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ModularityConjecture.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ModularityConjecture.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ModularityConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ModularityConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Modularity_theorem)
