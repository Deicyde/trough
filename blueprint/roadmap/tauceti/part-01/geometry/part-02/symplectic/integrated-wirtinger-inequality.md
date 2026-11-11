---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy, TauCeti.SmoothTwoForm.Compatible.lintegral_twoForm_le_stdComplexLineEnergy, TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineArea
statement: formalized
proof: formalized
---

# Integrated Wirtinger inequality

For a compatible pair, the integral of the positive
symplectic area density is at most the energy.

```lean
TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy.{u_1, u_2} {X : Type u_1}
  {V : Type u_2} [MeasurableSpace X] [AddCommGroup V] [_root_.Module ℝ V]
  {J : TauCeti.AlmostComplexStructure V} {ω : TauCeti.SymplecticForm V}
  {μ : MeasureTheory.Measure X} {du : X → ℝ × ℝ →ₗ[ℝ] V} (hcompat : ω.Compatible J) :
  ∫⁻ (x : X),
      ENNReal.ofReal
        ((fun v w => (ω.toBilinForm v) w) ((du x) TauCeti.stdComplexLineReal)
          ((du x) TauCeti.stdComplexLineImag)) ∂μ ≤
    ω.stdComplexLineEnergy J du μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wirtinger inequality](wirtinger-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Integral.html#TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy).

## Other forms

**Integrated Wirtinger inequality on manifolds.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.Compatible.lintegral_twoForm_le_stdComplexLineEnergy`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Energy.html#TauCeti.SmoothTwoForm.Compatible.lintegral_twoForm_le_stdComplexLineEnergy).

```lean
TauCeti.SmoothTwoForm.Compatible.lintegral_twoForm_le_stdComplexLineEnergy.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {form : TauCeti.SmoothTwoForm I M}
  {J : TauCeti.SmoothAlmostComplexStructure I M} (hcompat : form.Compatible J) (u : ℝ × ℝ → M)
  (du : (z : ℝ × ℝ) → ℝ × ℝ →ₗ[ℝ] TangentSpace I (u z)) (μ : MeasureTheory.Measure (ℝ × ℝ)) :
  ∫⁻ (z : ℝ × ℝ),
      ENNReal.ofReal
        (TauCeti.SmoothBundleForm.eval₂ form (u z) ((du z) TauCeti.stdComplexLineReal)
          ((du z) TauCeti.stdComplexLineImag)) ∂μ ≤
    form.stdComplexLineEnergy J u du μ
```

**Integrated Wirtinger inequality, area form.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineArea`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Area.html#TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineArea).

```lean
TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineArea.{u_1, u_2} {X : Type u_1}
  {V : Type u_2} [MeasurableSpace X] [AddCommGroup V] [_root_.Module ℝ V]
  {J : TauCeti.AlmostComplexStructure V} {ω : TauCeti.SymplecticForm V}
  {μ : MeasureTheory.Measure X} {du : X → ℝ × ℝ →ₗ[ℝ] V} (hcompat : ω.Compatible J) :
  ∫⁻ (x : X),
      ENNReal.ofReal
        ((fun v w => (ω.toBilinForm v) w) ((du x) TauCeti.stdComplexLineReal)
          ((du x) TauCeti.stdComplexLineImag)) ∂μ ≤
    ω.stdComplexLineArea J du μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Integral.html#TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy)
- [Source of `TauCeti.SymplecticForm.lintegral_symplecticForm_le_stdComplexLineEnergy` in TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Integral.lean#L180)
