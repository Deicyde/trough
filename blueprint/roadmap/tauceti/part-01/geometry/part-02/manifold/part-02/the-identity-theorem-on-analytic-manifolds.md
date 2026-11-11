---
declaration: theorem
origin: cited
lean: ContMDiff.eq_of_eventuallyEq, TauCeti.eqOn_of_preconnected_of_eventuallyEq_of_contMDiffAt
statement: formalized
proof: formalized
---

# The identity theorem on analytic manifolds

On a preconnected `C^ω` manifold modelled
without boundary on a locally connected space, two `C^ω` functions with values in a normed space
that agree on a neighbourhood of a point are equal.

```lean
ContMDiff.eq_of_eventuallyEq.{u_1, u_2, u_3, u_4, u_8} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} [I.Boundaryless] {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {F : Type u_8} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [LocallyConnectedSpace E] [IsManifold I ⊤ M] [PreconnectedSpace M] {f g : M → F}
  (hf : ContMDiff I (modelWithCornersSelf 𝕜 F) ⊤ f)
  (hg : ContMDiff I (modelWithCornersSelf 𝕜 F) ⊤ g) {x₀ : M} (hfg : f =ᶠ[nhds x₀] g) : f = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContMDiff.eq_of_eventuallyEq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiff/Analytic.html#ContMDiff.eq_of_eventuallyEq).

## Other forms

**The identity theorem on analytic manifolds.** Formalized in Tau Ceti as [`TauCeti.eqOn_of_preconnected_of_eventuallyEq_of_contMDiffAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiff/Analytic.html#TauCeti.eqOn_of_preconnected_of_eventuallyEq_of_contMDiffAt).

```lean
TauCeti.eqOn_of_preconnected_of_eventuallyEq_of_contMDiffAt.{u_1, u_2, u_3, u_4, u_8} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} [I.Boundaryless] {M : Type u_4}
  [TopologicalSpace M] [ChartedSpace H M] {F : Type u_8} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [LocallyConnectedSpace E] [IsManifold I ⊤ M] {f g : M → F} {U : Set M}
  (hf : ∀ x ∈ U, ContMDiffAt I (modelWithCornersSelf 𝕜 F) ⊤ f x)
  (hg : ∀ x ∈ U, ContMDiffAt I (modelWithCornersSelf 𝕜 F) ⊤ g x) (hU : IsPreconnected U) {x₀ : M}
  (h₀ : x₀ ∈ U) (hfg : f =ᶠ[nhds x₀] g) : Set.EqOn f g U
```

## Sources

- [Tau Ceti documentation: `ContMDiff.eq_of_eventuallyEq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiff/Analytic.html#ContMDiff.eq_of_eventuallyEq)
- [Source of `ContMDiff.eq_of_eventuallyEq` in TauCeti/Geometry/Manifold/ContMDiff/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/ContMDiff/Analytic.lean#L283)
