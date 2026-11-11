---
declaration: theorem
origin: cited
lean: TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt
statement: formalized
proof: formalized
---

# The linear local model at a fixed point

Let a finite group `G` act continuously on a
finite-dimensional real manifold without boundary, fixing `y`, by maps that are `C¹` at `y`.
Inside any neighbourhood `s` of `y` there is a chart `e` sending `y` to `0` whose domain is
`G`-invariant and preconnected and whose target is a positive strict sublevel set of a
`σ`-invariant inner product, in which `G` acts linearly through a continuous representation `σ`.
Every element of `G` is retained, including those acting trivially: `g` acts as the identity near
`y`, that is, lies in the germ kernel at `y`, exactly when `σ g = 1`, and exactly when `g` fixes
every point of the domain of `e`.

```lean
TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt.{u_1, u_2,
    u_3, u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {G : Type u_4} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] [Group G] [Fintype G] [MulAction G M]
  [ContinuousConstSMul G M] {y : M} (hsmooth : ∀ (g : G), ContMDiffAt I I 1 (fun x => g • x) y)
  (hy : ∀ (g : G), g • y = y) {s : Set M} (hs : s ∈ nhds y) :
  ∃ σ e c,
    0 < c ∧
      y ∈ e.source ∧
        ↑e y = 0 ∧
          e.source ⊆ s ∧
            e.target =
                (ContRepresentation.toRepresentation ℝ G E σ).sumOfConjugatesInnerSublevel c ∧
              IsPreconnected e.source ∧
                (∀ (g : G), ∀ z ∈ e.source, g • z ∈ e.source ∧ ↑e (g • z) = (σ g) (↑e z)) ∧
                  ∀ (g : G),
                    (σ g = 1 ↔ g ∈ TauCeti.MulAction.germKernel G y) ∧
                      (σ g = 1 ↔ ∀ z ∈ e.source, g • z = z)
```

## Depends on

- [TauCeti.MulAction.germKernel](tauceti-mulaction-germkernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/GermKernel.html#TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/GermKernel.html#TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt)
- [Source of `TauCeti.exists_equivariant_chart_target_eq_sumOfConjugatesInnerSublevel_of_contMDiffAt` in TauCeti/Geometry/Manifold/GroupAction/GermKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/GroupAction/GermKernel.lean#L335)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Orbifolds/STATUS.md)
