---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity, TauCeti.SymplecticForm.Compatible.apply_le_wedgeNorm, TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity
statement: formalized
proof: formalized
---

# Wirtinger inequality

For a compatible pair `(ω, J)` and any real-linear map out of the
standard complex line, twice the symplectic area density of the ordered coordinate pair is at
most the standard energy density: the local form of `E(u) ≥ ∫ u^*ω`.

```lean
TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity.{u_1} {V : Type u_1}
  [AddCommGroup V] [_root_.Module ℝ V] {J : TauCeti.AlmostComplexStructure V}
  {ω : TauCeti.SymplecticForm V} (hcompat : ω.Compatible J) (F : ℝ × ℝ →ₗ[ℝ] V) :
  2 *
      (fun v w => (ω.toBilinForm v) w) (F TauCeti.stdComplexLineReal)
        (F TauCeti.stdComplexLineImag) ≤
    ω.stdComplexLineEnergyDensity J F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy--Schwarz along a complex line](cauchy-schwarz-along-a-complex-line.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Basic.html#TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity).

## Other forms

**The Wirtinger inequality.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.Compatible.apply_le_wedgeNorm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Wirtinger.html#TauCeti.SymplecticForm.Compatible.apply_le_wedgeNorm).

```lean
TauCeti.SymplecticForm.Compatible.apply_le_wedgeNorm.{u_1} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℝ V] {ω : TauCeti.SymplecticForm V} {J : TauCeti.AlmostComplexStructure V}
  (h : ω.Compatible J) (v w : V) : (fun v w => (ω.toBilinForm v) w) v w ≤ ω.wedgeNorm J v w
```

**Wirtinger inequality on manifolds.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Energy.html#TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity).

```lean
TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {form : TauCeti.SmoothTwoForm I M}
  {J : TauCeti.SmoothAlmostComplexStructure I M} (hcompat : form.Compatible J) (x : M)
  (F : ℝ × ℝ →ₗ[ℝ] TangentSpace I x) :
  2 *
      TauCeti.SmoothBundleForm.eval₂ form x (F TauCeti.stdComplexLineReal)
        (F TauCeti.stdComplexLineImag) ≤
    form.stdComplexLineEnergyDensity J x F
```

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Basic.html#TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity)
- [Source of `TauCeti.SymplecticForm.two_mul_symplecticForm_le_stdComplexLineEnergyDensity` in TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/JHolomorphic/Energy/Basic.lean#L413)
