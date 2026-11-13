---
declaration: theorem
origin: cited
lean: HyperbolicGroupsResiduallyFinite.hyperbolic_residuallyFinite, HyperbolicGroupsResiduallyFinite.hyperbolic_exists_finiteIndex_ne_top, HyperbolicGroupsResiduallyFinite.hyperbolic_residuallyFinite_iff_exists_finiteIndex_ne_top
statement: formalized
---

# Residual finiteness of hyperbolic groups

> Is every hyperbolic group residually finite? Kapovich and Wise [KaWi00] proved that this question
> is equivalent to asking whether every nontrivial hyperbolic group has a proper subgroup of finite
> index. Both questions were answered negatively by an internal OpenAI model in September 2026
> [OAI26a].
>
> *References:*
> - [BMS] G. Baumslag, A. G. Myasnikov and V. Shpilrain, *Open problems in combinatorial group
>   theory*, Problem (H1),
>   [online](https://shpilrain.ccny.cuny.edu/gworld/problems/probhyp.html).
> - [Be04] M. Bestvina, *Questions in geometric group theory*, updated July 2004, Q 1.15,
>   [pdf](https://www.math.utah.edu/~bestvina/eprints/questions-updated.pdf).
> - [KaWi00] I. Kapovich and D. T. Wise, *The equivalence of some residual properties of
>   word-hyperbolic groups*, J. Algebra 223 (2000), 562–583,
>   [doi:10.1006/jabr.1999.8104](https://doi.org/10.1006/jabr.1999.8104).
> - [OAI26a] OpenAI, *A torsion-free hyperbolic group that is not residually finite*. OpenAI Math
>   Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `HyperbolicGroupsResiduallyFinite.hyperbolic_residuallyFinite`

Solved: stated here without proof.

> Is every hyperbolic group residually finite?
>
> This is Problem (H1)(a) in [BMS] and Q 1.15 in [Be04].
>
> No. This was disproved by an internal OpenAI model in September 2026 [OAI26a], which constructs
> a torsion-free hyperbolic group that is not residually finite. The
> [Lean proof](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/Hyperbolic/Main.lean#L7)
> of [OAI26a] defines hyperbolicity by uniformly thin geodesic triangles in a Cayley graph. That
> definition is equivalent to `Group.IsHyperbolic`, but the equivalence is not part of the Lean
> proof.

```lean
theorem hyperbolic_residuallyFinite :
    ¬ ∀ (G : Type) [Group G] [Group.IsHyperbolic G], Group.ResiduallyFinite G
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean#L59).

## `HyperbolicGroupsResiduallyFinite.hyperbolic_exists_finiteIndex_ne_top`

Solved: stated here without proof.

> Does every nontrivial hyperbolic group have a proper subgroup of finite index?
>
> This is Problem (H1)(b) in [BMS]. The trivial group has no proper subgroup, so we assume that
> $G$ is nontrivial.
>
> No. By [KaWi00] (see `hyperbolic_residuallyFinite_iff_exists_finiteIndex_ne_top`), this problem
> is equivalent to `hyperbolic_residuallyFinite`, which was disproved in [OAI26a].

```lean
theorem hyperbolic_exists_finiteIndex_ne_top :
    ¬ ∀ (G : Type) [Group G] [Group.IsHyperbolic G] [Nontrivial G],
      ∃ H : Subgroup G, H ≠ ⊤ ∧ H.FiniteIndex
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean#L73).

## `HyperbolicGroupsResiduallyFinite.hyperbolic_residuallyFinite_iff_exists_finiteIndex_ne_top`

Solved: stated here without proof.

> Every hyperbolic group is residually finite if and only if every nontrivial hyperbolic group has a
> proper subgroup of finite index.
>
> This is the theorem of [KaWi00] that Problems (H1)(a) and (H1)(b) are equivalent.

```lean
theorem hyperbolic_residuallyFinite_iff_exists_finiteIndex_ne_top :
    (∀ (G : Type) [Group G] [Group.IsHyperbolic G], Group.ResiduallyFinite G) ↔
      ∀ (G : Type) [Group G] [Group.IsHyperbolic G] [Nontrivial G],
        ∃ H : Subgroup G, H ≠ ⊤ ∧ H.FiniteIndex
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean)
- [online](https://shpilrain.ccny.cuny.edu/gworld/problems/probhyp.html)
