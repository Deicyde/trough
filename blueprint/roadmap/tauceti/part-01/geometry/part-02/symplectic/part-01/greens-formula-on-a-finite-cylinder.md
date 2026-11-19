---
declaration: theorem
origin: cited
lean: TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic, TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport, TauCeti.SymplecticForm.integral_apply_floerLinearization_eq_integral_floerLinearizationAdjoint_apply, TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport_right, TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_add
statement: formalized
proof: formalized
---

# Green's formula on a finite cylinder

Under the hypotheses of
`Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_add` on `[a, b] × [0, 1]`,
let `ξ` and `η` take equal values on the slices `t = 0` and `t = 1`, and at each point of the
slices `s = a` and `s = b` let `ξ` or `η` vanish. Then `∫∫ g(D ξ, η) = ∫∫ g(ξ, D† η)` over
`[a, b] × [0, 1]`.

```lean
TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] {J : ℝ → TauCeti.AlmostComplexStructure V}
  {S : ℝ → V →L[ℝ] V} {ξ η : ℝ × ℝ → V} [FiniteDimensional ℝ V] {ω : TauCeti.SymplecticForm V}
  (hJ : ∀ (t : ℝ), ω.Invariant (J t)) (hJc : Continuous fun p => (J p.1).toLinearMap p.2)
  (hS :
    ∀ (t : ℝ) (v w : V),
      (fun v w => (ω.toBilinForm v) w) ((S t) v) w + (fun v w => (ω.toBilinForm v) w) v ((S t) w) =
        0)
  (hSc : Continuous S) {a b : ℝ} (hξ : ∀ z ∈ Set.Icc a b ×ˢ Set.Icc 0 1, ContDiffAt ℝ 1 ξ z)
  (hη : ∀ z ∈ Set.Icc a b ×ˢ Set.Icc 0 1, ContDiffAt ℝ 1 η z)
  (hξp : ∀ s ∈ Set.Icc a b, ξ (s, 1) = ξ (s, 0)) (hηp : ∀ s ∈ Set.Icc a b, η (s, 1) = η (s, 0))
  (ha : ∀ t ∈ Set.Icc 0 1, ξ (a, t) = 0 ∨ η (a, t) = 0)
  (hb : ∀ t ∈ Set.Icc 0 1, ξ (b, t) = 0 ∨ η (b, t) = 0) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b ×ˢ Set.Icc 0 1,
      ((ω.associatedBilinForm (J z.2)) (TauCeti.Floer.stationaryCylinderOperator J S ξ z)) (η z) =
    ∫ (z : ℝ × ℝ) in Set.Icc a b ×ˢ Set.Icc 0 1,
      ((ω.associatedBilinForm (J z.2)) (ξ z)) (TauCeti.Floer.stationaryCylinderAdjoint J S η z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus in the first coordinate](../../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-in-the-first.md)
- [The fundamental theorem of calculus in the second coordinate](../../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-in-the-secon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.html#TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic).

## Other forms

**Green's formula for compactly supported maps.** Formalized in Tau Ceti as [`TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.html#TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport).

```lean
TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] {J : ℝ → TauCeti.AlmostComplexStructure V}
  {S : ℝ → V →L[ℝ] V} {ξ η : ℝ × ℝ → V} [FiniteDimensional ℝ V] {ω : TauCeti.SymplecticForm V}
  (hJ : ∀ (t : ℝ), ω.Invariant (J t)) (hJc : Continuous fun p => (J p.1).toLinearMap p.2)
  (hS :
    ∀ (t : ℝ) (v w : V),
      (fun v w => (ω.toBilinForm v) w) ((S t) v) w + (fun v w => (ω.toBilinForm v) w) v ((S t) w) =
        0)
  (hSc : Continuous S) (hξ : ContDiff ℝ 1 ξ) (hξc : HasCompactSupport ξ)
  (hη : ∀ z ∈ tsupport ξ, ContDiffAt ℝ 1 η z) :
  ∫ (z : ℝ × ℝ),
      ((ω.associatedBilinForm (J z.2)) (TauCeti.Floer.stationaryCylinderOperator J S ξ z)) (η z) =
    ∫ (z : ℝ × ℝ),
      ((ω.associatedBilinForm (J z.2)) (ξ z)) (TauCeti.Floer.stationaryCylinderAdjoint J S η z)
```

**Green's formula for compactly supported maps.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_apply_floerLinearization_eq_integral_floerLinearizationAdjoint_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Linearization/Adjoint.html#TauCeti.SymplecticForm.integral_apply_floerLinearization_eq_integral_floerLinearizationAdjoint_apply).

```lean
TauCeti.SymplecticForm.integral_apply_floerLinearization_eq_integral_floerLinearizationAdjoint_apply.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {ω : TauCeti.SymplecticForm V} {J : ℝ × ℝ → V → V →L[ℝ] V} {Ks Kt : ℝ × ℝ → V → ℝ}
  {u ξ : ℝ × ℝ → V} {η : ℝ × ℝ → V →L[ℝ] ℝ} (hξ : ContDiff ℝ 1 ξ) (hξc : HasCompactSupport ξ)
  (hJ : ∀ z ∈ tsupport ξ, ContDiffAt ℝ 1 (Function.uncurry J) (z, u z))
  (hKs : ∀ z ∈ tsupport ξ, ContDiffAt ℝ 2 (Function.uncurry Ks) (z, u z))
  (hKt : ∀ z ∈ tsupport ξ, ContDiffAt ℝ 2 (Function.uncurry Kt) (z, u z))
  (hu : ∀ z ∈ tsupport ξ, ContDiffAt ℝ 1 u z) (hη : ∀ z ∈ tsupport ξ, ContDiffAt ℝ 1 η z) :
  ∫ (z : ℝ × ℝ), (η z) (ω.floerLinearization J Ks Kt u ξ z) =
    ∫ (z : ℝ × ℝ), (ω.floerLinearizationAdjoint J Ks Kt u η z) (ξ z)
```

**Green's formula for compactly supported maps, tested on the right.** Formalized in Tau Ceti as [`TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport_right`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.html#TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport_right).

```lean
TauCeti.Floer.integral_associatedBilinForm_stationaryCylinderOperator_eq_of_hasCompactSupport_right.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] {J : ℝ → TauCeti.AlmostComplexStructure V}
  {S : ℝ → V →L[ℝ] V} {ξ η : ℝ × ℝ → V} [FiniteDimensional ℝ V] {ω : TauCeti.SymplecticForm V}
  (hJ : ∀ (t : ℝ), ω.Invariant (J t)) (hJc : Continuous fun p => (J p.1).toLinearMap p.2)
  (hS :
    ∀ (t : ℝ) (v w : V),
      (fun v w => (ω.toBilinForm v) w) ((S t) v) w + (fun v w => (ω.toBilinForm v) w) v ((S t) w) =
        0)
  (hSc : Continuous S) (hη : ContDiff ℝ 1 η) (hηc : HasCompactSupport η)
  (hξ : ∀ z ∈ tsupport η, ContDiffAt ℝ 1 ξ z) :
  ∫ (z : ℝ × ℝ),
      ((ω.associatedBilinForm (J z.2)) (TauCeti.Floer.stationaryCylinderOperator J S ξ z)) (η z) =
    ∫ (z : ℝ × ℝ),
      ((ω.associatedBilinForm (J z.2)) (ξ z)) (TauCeti.Floer.stationaryCylinderAdjoint J S η z)
```

**Green's formula for the stationary cylinder operator.** Formalized in Tau Ceti as [`TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.html#TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_add).

```lean
TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_add.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] {J : ℝ → TauCeti.AlmostComplexStructure V}
  {S : ℝ → V →L[ℝ] V} {ξ η : ℝ × ℝ → V} [FiniteDimensional ℝ V] {ω : TauCeti.SymplecticForm V}
  (hJ : ∀ (t : ℝ), ω.Invariant (J t)) (hJc : Continuous fun p => (J p.1).toLinearMap p.2)
  (hS :
    ∀ (t : ℝ) (v w : V),
      (fun v w => (ω.toBilinForm v) w) ((S t) v) w + (fun v w => (ω.toBilinForm v) w) v ((S t) w) =
        0)
  (hSc : Continuous S) {a₁ b₁ a₂ b₂ : ℝ} (h₁ : a₁ ≤ b₁) (h₂ : a₂ ≤ b₂)
  (hξ : ∀ z ∈ Set.Icc a₁ b₁ ×ˢ Set.Icc a₂ b₂, ContDiffAt ℝ 1 ξ z)
  (hη : ∀ z ∈ Set.Icc a₁ b₁ ×ˢ Set.Icc a₂ b₂, ContDiffAt ℝ 1 η z) :
  ∫ (z : ℝ × ℝ) in Set.Icc a₁ b₁ ×ˢ Set.Icc a₂ b₂,
      ((ω.associatedBilinForm (J z.2)) (TauCeti.Floer.stationaryCylinderOperator J S ξ z)) (η z) =
    ((∫ (z : ℝ × ℝ) in Set.Icc a₁ b₁ ×ˢ Set.Icc a₂ b₂,
          ((ω.associatedBilinForm (J z.2)) (ξ z))
            (TauCeti.Floer.stationaryCylinderAdjoint J S η z)) +
        ∫ (t : ℝ) in Set.Icc a₂ b₂,
          ((ω.associatedBilinForm (J t)) (ξ (b₁, t))) (η (b₁, t)) -
            ((ω.associatedBilinForm (J t)) (ξ (a₁, t))) (η (a₁, t))) +
      ∫ (s : ℝ) in Set.Icc a₁ b₁,
        (fun v w => (ω.toBilinForm v) w) (ξ (s, b₂)) (η (s, b₂)) -
          (fun v w => (ω.toBilinForm v) w) (ξ (s, a₂)) (η (s, a₂))
```

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.html#TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic)
- [Source of `TauCeti.Floer.setIntegral_associatedBilinForm_stationaryCylinderOperator_eq_of_periodic` in TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/AsymptoticOperator/Adjoint.lean#L350)
