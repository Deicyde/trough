---
declaration: theorem
origin: cited
lean: BingBorsuk.bing_borsuk_conjecture
statement: formalized
---

# The Bing-Borsuk Conjecture

> The Bing-Borsuk conjecture states that every $n$-dimensional homogeneous absolute neighborhood
> retract is a topological $n$-manifold.
>
> The conjecture has been verified in dimensions $1$ and $2$ but remains open in higher dimensions.
> A notable consequence is that if the $3$-dimensional case is true, it implies the Poincaré
> conjecture.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Bing%E2%80%93Borsuk_conjecture)
>  - [HR2008] Halverson, Denise M., and Dušan Repovš. "The Bing-Borsuk and the Busemann
>    conjectures." Mathematical Communications 13.2 (2008): 163-184.
>    https://arxiv.org/abs/0811.0886

*Quoted from [FormalConjectures/Wikipedia/BingBorsuk.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BingBorsuk.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `BingBorsuk.bing_borsuk_conjecture`

Open: stated without proof.

> The Bing-Borsuk Conjecture: every $n$-dimensional homogeneous absolute neighborhood retract
> is a topological $n$-manifold. A topological space $X$ is an $n$-dimensional manifold
> when `T2Space X ∧ Nonempty (ChartedSpace (Fin n → ℝ) X)`. The hypothesis `[MetrizableSpace X]`
> implies `T2Space X` so this does not appear in the conclusion.

```lean
theorem bing_borsuk_conjecture : ∀ n : ℕ, ∀ (X : Type) [TopologicalSpace X] [MetrizableSpace X] [HomogeneousSpace X] [IsAbsoluteNeighborhoodRetract X],
    HasLebesgueCoveringDimensionEq X n → Nonempty (ChartedSpace (Fin n → ℝ) X)
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Wikipedia/BingBorsuk.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BingBorsuk.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BingBorsuk.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BingBorsuk.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Bing%E2%80%93Borsuk_conjecture)
