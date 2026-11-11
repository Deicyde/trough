---
declaration: theorem
origin: cited
lean: TauCeti.chainsDesc_pathClassIntegral_mextDeriv, TauCeti.SmoothSimplex.integral_mextDeriv, TauCeti.d_comp_integrationCochain, TauCeti.d_comp_integrationCochain_assoc
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

- [TauCeti.SmoothSimplex.integral](../../../part-01/differential-geometry-forms-stokes-flows-de-rham/tauceti-smoothsimplex-integral.md)
- [TauCeti.smoothSingularSubcomplex](../../../part-01/differential-geometry-forms-stokes-flows-de-rham/tauceti-smoothsingularsubcomplex.md)

## Proof depends on

- [The fundamental theorem of calculus for path classes](../part-01/the-fundamental-theorem-of-calculus-for-path-cla.md)
- [The Poincaré lemma on manifolds](../part-02/the-poincare-lemma-on-manifolds.md)
- [Stokes' theorem on the standard simplex](../../../../analysis/part-02/calculus/part-02/stokes-theorem-on-the-standard-simplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.chainsDesc_pathClassIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.html#TauCeti.chainsDesc_pathClassIntegral_mextDeriv).

## Other forms

**Stokes' theorem for a smooth singular simplex.** Formalized in Tau Ceti as [`TauCeti.SmoothSimplex.integral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv).

```lean
TauCeti.SmoothSimplex.integral_mextDeriv.{u, u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ℕ} [IsManifold I 2 M] [CompleteSpace F]
  (σ : TauCeti.SmoothSimplex I M (p + 1)) {φ : TauCeti.RoughForm I M F p}
  (hφ : TauCeti.IsSmoothForm I 1 φ) :
  σ.integral (TauCeti.mextDeriv φ) =
    ∑ i,
      (-1) ^ ↑i •
        TauCeti.SmoothSimplex.integral
          ((CategoryTheory.ConcreteCategory.hom
              (CategoryTheory.SimplicialObject.δ (TauCeti.smoothSingularSubcomplex I M).toSSet i))
            σ)
          φ
```

**Stokes' theorem for smooth singular chains.** Formalized in Tau Ceti as [`TauCeti.d_comp_integrationCochain`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.d_comp_integrationCochain).

```lean
TauCeti.d_comp_integrationCochain.{u_1, u_2} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {p : ℕ} {M : Type}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M] {F : Type} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] {φ : TauCeti.RoughForm I M F p}
  (hφ : TauCeti.IsSmoothForm I 1 φ) :
  CategoryTheory.CategoryStruct.comp
      (((TauCeti.smoothSingularSubcomplex I M).toSSet.chainComplex ↧ℝ).d (p + 1) p)
      (TauCeti.integrationCochain φ) =
    TauCeti.integrationCochain (TauCeti.mextDeriv φ)
```

**Stokes' theorem for smooth singular chains.** Formalized in Tau Ceti as [`TauCeti.d_comp_integrationCochain_assoc`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.d_comp_integrationCochain_assoc).

```lean
TauCeti.d_comp_integrationCochain_assoc.{u_1, u_2} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {p : ℕ}
  {M : Type} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M] {F : Type}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {φ : TauCeti.RoughForm I M F p}
  (hφ : TauCeti.IsSmoothForm I 1 φ) {Z : ModuleCat ℝ} (h : ↧F ⟶ Z) :
  CategoryTheory.CategoryStruct.comp
      (((TauCeti.smoothSingularSubcomplex I M).toSSet.chainComplex ↧ℝ).d (p + 1) p)
      (CategoryTheory.CategoryStruct.comp (TauCeti.integrationCochain φ) h) =
    CategoryTheory.CategoryStruct.comp (TauCeti.integrationCochain (TauCeti.mextDeriv φ)) h
```

## Sources

- [Tau Ceti documentation: `TauCeti.chainsDesc_pathClassIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.html#TauCeti.chainsDesc_pathClassIntegral_mextDeriv)
- [Source of `TauCeti.chainsDesc_pathClassIntegral_mextDeriv` in TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DeRham/HomologyPeriod.lean#L188)
