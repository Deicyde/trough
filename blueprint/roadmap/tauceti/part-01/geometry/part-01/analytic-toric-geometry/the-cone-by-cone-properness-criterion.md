---
declaration: theorem
origin: cited
lean: TauCeti.Toric.FanHom.isProperMap_analyticMap_iff
statement: formalized
proof: formalized
---

# The cone-by-cone properness criterion

The analytic map of a morphism of regular fans
with nonempty source is proper exactly when, for every target cone `τ`, the inverse image of `τ`
under the real-linear map is the union of the source cones mapped into `τ`. The nonemptiness
hypothesis is necessary: the inclusion of the empty subfan is proper, but `0` lies in the inverse
image of every cone and in no cone of the empty fan. See
`TauCeti.Toric.FanHom.isProperMap_analyticMap_iff_isEmpty_or` for the form without it.

```lean
TauCeti.Toric.FanHom.isProperMap_analyticMap_iff.{u} {N N' V V' : Type u} [AddCommGroup N]
  [AddCommGroup N'] [AddCommGroup V] [AddCommGroup V'] [_root_.Module ℝ V] [_root_.Module ℝ V']
  {i : N →+ V} {i' : N' →+ V'} {Φ : TauCeti.Toric.Fan i} {Ψ : TauCeti.Toric.Fan i'}
  (f : TauCeti.Toric.FanHom Φ Ψ) (hΦ : Φ.IsRegular) (hΨ : Ψ.IsRegular) (hΦ0 : Nonempty ↑Φ.cones) :
  IsProperMap ⇑(CategoryTheory.ConcreteCategory.hom (f.analyticMap hΦ hΨ)) ↔
    ∀ (τ : ↑Ψ.cones), ⇑f.realMap ⁻¹' ↑↑τ = ⋃ σ, ⋃ (_ : PointedCone.map f.realMap ↑σ ≤ ↑τ), ↑↑σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma](../../part-02/other-results/gordans-lemma.md)
- [Hoffman's error bound for a polyhedral cone](../../part-02/convex/hoffmans-error-bound-for-a-polyhedral-cone.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.FanHom.isProperMap_analyticMap_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Map/Proper.html#TauCeti.Toric.FanHom.isProperMap_analyticMap_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.FanHom.isProperMap_analyticMap_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Map/Proper.html#TauCeti.Toric.FanHom.isProperMap_analyticMap_iff)
- [Source of `TauCeti.Toric.FanHom.isProperMap_analyticMap_iff` in TauCeti/Geometry/Toric/Analytic/Fan/Map/Proper.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Analytic/Fan/Map/Proper.lean#L226)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AnalyticToricGeometry/STATUS.md)
