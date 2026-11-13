---
declaration: theorem
origin: cited
lean: Mathoverflow1973.mathoverflow_1973
statement: formalized
---

# Mathoverflow 1973

> Does the 6-sphere $S^6$ admit the structure of a complex manifold?
>
> *References:*
> - [mathoverflow/1973](https://mathoverflow.net/questions/1973/),
>   asked by user [*Fetchinson0234*](https://mathoverflow.net/users/41312/victor-ramos).
> - [Al26] L. Alpöge, [*A compact complex threefold fibred by tori over the projective line, and the six-sphere*](https://alpo.ge/s6.pdf) (2026),
>   originally [shared on X](https://x.com/__alpoge__/status/2091639597193368014).

*Quoted from [FormalConjectures/Mathoverflow/1973.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/1973.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Mathoverflow1973.mathoverflow_1973`

Solved: stated here; a Lean proof is at [https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/Solution.lean](https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/Solution.lean).

> Does the 6-sphere admit a complex structure, i.e. an atlas of holomorphically compatible charts
> relating it to `EuclideanSpace ℂ (Fin 3)`? This is known as the Hopf Problem.
>
> The answer is yes, see [Al26].
> Formalisation of the proof by Boris Alexeev.

```lean
theorem mathoverflow_1973 :
    ∃ atlas : ChartedSpace (EuclideanSpace ℂ (Fin 3)) (unitSphere 6),
      IsManifold 𝓘(ℂ, EuclideanSpace ℂ (Fin 3)) 1 (unitSphere 6)
```

Category `research solved`; AMS [32 Several complex variables and analytic spaces](../by-subject/part-01/32-several-complex-variables-and-analytic-spaces/README.md). Declared in [FormalConjectures/Mathoverflow/1973.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/1973.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/1973.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/1973.lean)
- [mathoverflow/1973](https://mathoverflow.net/questions/1973/)
