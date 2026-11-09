---
declaration: theorem
origin: cited
lean: TauCeti.chainsDesc_pathClassIntegral_mextDeriv
statement: formalized
proof: formalized
---

# Stokes' theorem on singular `1`-chains

The integral of `dψ` along a singular `1`-chain is
the evaluation of the `0`-form `ψ` on its boundary.

```lean
TauCeti.chainsDesc_pathClassIntegral_mextDeriv.{u_1, u_2} {E : Type u_1} {H : Type u_2} {M F : Type}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M] [CompleteSpace F]
  {ψ : TauCeti.RoughForm I M F 0} (hψ : TauCeti.IsSmoothForm I 2 ψ) :
  (TauCeti.chainsDesc fun s =>
      TauCeti.pathClassIntegral (TauCeti.mextDeriv ψ)
        (Path.Homotopic.Quotient.mk (TauCeti.TopCat.path₁ s))) =
    (TauCeti.chainsDesc fun v => (ψ (TopCat.toSSetObj₀Equiv v)) 0) ∘ₗ
      ModuleCat.Hom.hom (((TauCeti.singularChains ℤ).obj ↧M).d 1 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for path classes](../part-01/the-fundamental-theorem-of-calculus-for-path-cla.md)
- [The Poincaré lemma on manifolds](../../manifold/part-02/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.chainsDesc_pathClassIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.html#TauCeti.chainsDesc_pathClassIntegral_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.chainsDesc_pathClassIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.html#TauCeti.chainsDesc_pathClassIntegral_mextDeriv)
- [Source of `TauCeti.chainsDesc_pathClassIntegral_mextDeriv` in TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.lean#L177)
