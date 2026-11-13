---
declaration: theorem
origin: cited
lean: Hilbert5.hilbert_smith_conjecture, Hilbert5.hilbert_smith_conjecture.variants.riemannian, Hilbert5.hilbert_smith_conjecture.variants.dimension_three, Hilbert5.hilbert_smith_padic_formulation, Hilbert5.hilbert_fifth_problem
statement: formalized
---

# Hilbert's Fifth Problem and the Hilbert–Smith Conjecture

> The **Hilbert–Smith conjecture** states that a locally compact topological group acting
> continuously and faithfully on a connected finite-dimensional topological manifold must be a
> Lie group. It remains open in general; Pardon proved it for 3-manifolds in 2013.
> An equivalent formulation: no p-adic integer group `ℤ_[p]` can act faithfully on any
> connected finite-dimensional topological manifold.
>
> ## Main statements
>
> - `hilbert_smith_conjecture`: the Hilbert–Smith conjecture.
> - `hilbert_smith_padic_formulation`: the equivalent formulation for `ℤ_[p]`.
> - `hilbert_smith_conjecture.variants.dimension_three`: Pardon's theorem for 3-manifolds.
> - `hilbert_smith_conjecture.variants.riemannian`: the case of isometric actions on Riemannian
>   manifolds.
> - `hilbert_fifth_problem`: Hilbert's fifth problem, solved by Gleason, Montgomery and Zippin.
>
> ## Implementation notes
>
> `AdmitsLieGroupStructure G`, defined in
> `FormalConjecturesForMathlib.Geometry.Manifold.LieGroupPresentation`, says that `G` is
> continuously isomorphic to a finite-dimensional real-analytic Lie group. Lie groups are Hausdorff
> but not assumed second countable: every discrete group is a `0`-dimensional Lie group
> (`admitsLieGroupStructure_of_discreteTopology`). This matters for the Hilbert–Smith conjecture,
> since uncountable discrete groups act continuously and faithfully on connected manifolds, for
> instance `ℝ` with the discrete topology acting on `ℝ` by translations.
>
> The acting group is not assumed Hausdorff: a topological group acting continuously and
> faithfully on a Hausdorff space is Hausdorff, because the closure of the identity acts trivially.
>
> The hypotheses on the manifold `X` are written in each theorem. A section variable
> `[ChartedSpace (EuclideanSpace ℝ (Fin n)) X]` is included only in a theorem that mentions `n`,
> so it would be dropped silently from a statement that mentions only `X`.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Hilbert%E2%80%93Smith_conjecture)
> - [Tao's blog](https://terrytao.wordpress.com/2011/08/13/the-hilbert-smith-conjecture/)
> - [Pardon 2013] J. Pardon, *The Hilbert–Smith conjecture for three-manifolds*,
>   J. Amer. Math. Soc. 26 (2013), 879–899. https://doi.org/10.1090/S0894-0347-2013-00766-3,
>   [arXiv:1112.2324](https://arxiv.org/abs/1112.2324)
> - [Myers–Steenrod 1939] S. B. Myers, N. E. Steenrod, *The group of isometries of a Riemannian
>   manifold*, Ann. of Math. 40 (1939), 400–416. https://doi.org/10.2307/1968928
> - [van den Dries–Goldbring 2015] L. van den Dries, I. Goldbring, *Hilbert's 5th problem*,
>   Enseign. Math. 61 (2015), 3–43. https://doi.org/10.4171/LEM/61-1/2-2

*Quoted from [FormalConjectures/HilbertProblems/5.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 2 test statements, counted here but not shown.

## `Hilbert5.hilbert_smith_conjecture`

Open: stated without proof.

> **Hilbert–Smith conjecture**: every locally compact topological group acting continuously
> and faithfully on a connected finite-dimensional topological manifold is a Lie group.

```lean
theorem hilbert_smith_conjecture {X : Type*}
    [TopologicalSpace X] [T2Space X] [ConnectedSpace X]
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) X]
    [IsTopologicalGroup G] [LocallyCompactSpace G]
    [MulAction G X] [ContinuousSMul G X] [FaithfulSMul G X] :
    AdmitsLieGroupStructure G
```

Category `research open`; AMS [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md), [58 Global analysis, analysis on manifolds](../by-subject/part-02/58-global-analysis-analysis-on-manifolds/README.md). Declared in [FormalConjectures/HilbertProblems/5.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean#L89).

## `Hilbert5.hilbert_smith_conjecture.variants.riemannian`

Solved: stated here without proof.

> The Hilbert–Smith conjecture holds for actions by isometries of a connected smooth Riemannian
> manifold `X`: the isometry group of `X` is a Lie group by the Myers–Steenrod theorem, so `G` has
> no small subgroups and is a Lie group by the Gleason–Montgomery–Zippin theorem.
>
> Here `X` carries its Riemannian distance (`IsRiemannianManifold`), so the metric topology of `X`
> is its manifold topology.

```lean
theorem hilbert_smith_conjecture.variants.riemannian {X : Type*} [EMetricSpace X]
    [ConnectedSpace X] [ChartedSpace (EuclideanSpace ℝ (Fin n)) X] [IsManifold (𝓡 n) ∞ X]
    [Bundle.RiemannianBundle (fun x : X ↦ TangentSpace (𝓡 n) x)]
    [IsContMDiffRiemannianBundle (𝓡 n) ∞ (EuclideanSpace ℝ (Fin n))
      (fun x : X ↦ TangentSpace (𝓡 n) x)]
    [IsRiemannianManifold (𝓡 n) X]
    [IsTopologicalGroup G] [LocallyCompactSpace G]
    [MulAction G X] [ContinuousSMul G X] [FaithfulSMul G X]
    (hiso : ∀ g : G, Isometry (g • · : X → X)) :
    AdmitsLieGroupStructure G
```

Category `research solved`; AMS [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md), [53 Differential geometry](../by-subject/part-02/53-differential-geometry/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md), [58 Global analysis, analysis on manifolds](../by-subject/part-02/58-global-analysis-analysis-on-manifolds/README.md). Declared in [FormalConjectures/HilbertProblems/5.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean#L104).

## `Hilbert5.hilbert_smith_conjecture.variants.dimension_three`

Solved: stated here without proof.

> **Pardon's theorem** (2013): the Hilbert–Smith conjecture holds for connected 3-manifolds,
> see [Pardon 2013].

```lean
theorem hilbert_smith_conjecture.variants.dimension_three {X : Type*}
    [TopologicalSpace X] [T2Space X] [ConnectedSpace X]
    [ChartedSpace (EuclideanSpace ℝ (Fin 3)) X]
    [IsTopologicalGroup G] [LocallyCompactSpace G]
    [MulAction G X] [ContinuousSMul G X] [FaithfulSMul G X] :
    AdmitsLieGroupStructure G
```

Category `research solved`; AMS [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md), [58 Global analysis, analysis on manifolds](../by-subject/part-02/58-global-analysis-analysis-on-manifolds/README.md). Declared in [FormalConjectures/HilbertProblems/5.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean#L119).

## `Hilbert5.hilbert_smith_padic_formulation`

Open: stated without proof.

> **p-adic formulation**: the p-adic integers `ℤ_[p]` cannot act continuously and faithfully
> on a connected finite-dimensional topological manifold. This is equivalent to
> `hilbert_smith_conjecture` by the Gleason–Yamabe theorem together with Newman's theorem on
> periodic transformations of manifolds.

```lean
theorem hilbert_smith_padic_formulation {X : Type*}
    [TopologicalSpace X] [T2Space X] [ConnectedSpace X]
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) X]
    (p : ℕ) [Fact p.Prime] [AddAction ℤ_[p] X] [ContinuousVAdd ℤ_[p] X] :
    ¬ FaithfulVAdd ℤ_[p] X
```

Category `research open`; AMS [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md), [58 Global analysis, analysis on manifolds](../by-subject/part-02/58-global-analysis-analysis-on-manifolds/README.md). Declared in [FormalConjectures/HilbertProblems/5.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean#L132).

## `Hilbert5.hilbert_fifth_problem`

Solved: stated here without proof.

> **Hilbert's fifth problem** (Gleason–Montgomery–Zippin, 1952): every Hausdorff topological
> group modeled on a finite-dimensional Euclidean space is continuously isomorphic to a real-analytic
> Lie group.
>
> The input `ChartedSpace` supplies only a topological atlas. The compatible analytic atlas and
> analytic group operations belong to the output `LieGroupPresentation`.

```lean
theorem hilbert_fifth_problem
    [IsTopologicalGroup G] [T2Space G]
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) G] :
    Nonempty (LieGroupPresentation G n)
```

Category `research solved`; AMS [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/HilbertProblems/5.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean#L146).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/HilbertProblems/5.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/HilbertProblems/5.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hilbert%E2%80%93Smith_conjecture)
