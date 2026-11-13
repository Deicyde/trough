---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.vectorPotential, Electromagnetism.ElectromagneticPotential.ofScalarPotential_vectorPotential, Electromagnetism.ElectromagneticPotential.ofStaticScalarPotential_vectorPotential, Electromagnetism.ElectromagneticPotential.ofVectorPotential_vectorPotential, Electromagnetism.ElectromagneticPotential.ofStaticVectorPotential_vectorPotential, Electromagnetism.ElectromagneticPotential.ofPotentials_vectorPotential, Electromagnetism.ElectromagneticPotential.ofStaticPotentials_vectorPotential, Electromagnetism.ElectromagneticPotential.ofElectromagneticField_vectorPotential
statement: formalized
proof: formalized
---

# The vector Potential (Kinematics/VectorPotential)

The module `Physlib.Electromagnetism.Kinematics.VectorPotential`, [Physlib/Electromagnetism/Kinematics/VectorPotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean): 19 declarations, 2 with a docstring.

## i. Overview

> The electromagnetic potential is given by
> `A = (1/c φ, \vec A)`
> where `φ` is the scalar potential and `\vec A` is the vector potential.
>
> In this module we define the vector potential, and prove lemmas about it.
>
> Since `A` is relativistic it is a function of `SpaceTime d`, whilst
> the vector potential is non-relativistic and is therefore a function of `Time` and `Space d`.

## ii. Key results

> - `ElectromagneticPotential.vectorPotential` : The vector potential from an
>   electromagnetic potential.

## iv. References

> * None.

## A. Definition of the Vector Potential

**`Electromagnetism.ElectromagneticPotential.vectorPotential`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L64).

> The vector potential from the electromagnetic potential.

```lean
noncomputable def vectorPotential {d} (c : SpeedOfLight := 1) (A : ElectromagneticPotential d) :
    Time → Space d → EuclideanSpace ℝ (Fin d)
```

## B. Relation to constructors

**`Electromagnetism.ElectromagneticPotential.ofScalarPotential_vectorPotential`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L75).

```lean
lemma ofScalarPotential_vectorPotential {d} (c : SpeedOfLight)
    (φ : Time → Space d → ℝ) : (ofScalarPotential c φ).vectorPotential c = 0
```

**`Electromagnetism.ElectromagneticPotential.ofStaticScalarPotential_vectorPotential`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L81).

```lean
lemma ofStaticScalarPotential_vectorPotential {d} (c : SpeedOfLight)
    (φ : Space d → ℝ) : (ofStaticScalarPotential c φ).vectorPotential c = 0
```

**`Electromagnetism.ElectromagneticPotential.ofVectorPotential_vectorPotential`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L86).

```lean
lemma ofVectorPotential_vectorPotential {d} (c : SpeedOfLight)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    (ofVectorPotential c A).vectorPotential c = A
```

**`Electromagnetism.ElectromagneticPotential.ofStaticVectorPotential_vectorPotential`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L93).

```lean
lemma ofStaticVectorPotential_vectorPotential {d} (c : SpeedOfLight)
    (A : Space d → EuclideanSpace ℝ (Fin d)) :
    (ofStaticVectorPotential c A).vectorPotential c = fun _ => A
```

**`Electromagnetism.ElectromagneticPotential.ofPotentials_vectorPotential`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L99).

```lean
lemma ofPotentials_vectorPotential {d} (c : SpeedOfLight) (φ : Time → Space d → ℝ)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    (ofPotentials c φ A).vectorPotential c = A
```

**`Electromagnetism.ElectromagneticPotential.ofStaticPotentials_vectorPotential`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L106).

```lean
lemma ofStaticPotentials_vectorPotential {d} (c : SpeedOfLight) (φ : Space d → ℝ)
    (A : Space d → EuclideanSpace ℝ (Fin d)) :
    (ofStaticPotentials c φ A).vectorPotential c = fun _ => A
```

## B.1. ofElectromagneticField

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_vectorPotential`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L118).

```lean
lemma ofElectromagneticField_vectorPotential (c : SpeedOfLight)
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)) :
    (ofElectromagneticField c E B).vectorPotential c =
    fun t x => - ∫ u in 0..(1 : ℝ), (u • Space.basis.repr x) ⨯ₑ₃ B t (u • x) ∂volume
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_vectorPotential_apply`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L126).

```lean
lemma ofElectromagneticField_vectorPotential_apply {t x} (c : SpeedOfLight)
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)) (i : Fin 3) (hB : Continuous ↿B) :
    (ofElectromagneticField c E B).vectorPotential c t x i =
    - ∫ u in 0..(1 : ℝ), ((u • Space.basis.repr x) ⨯ₑ₃ B t (u • x)) i ∂volume
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_vectorPotential_apply_eq_expand`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L143).

```lean
lemma ofElectromagneticField_vectorPotential_apply_eq_expand {t x} {c : SpeedOfLight}
    {E : Time → Space 3 → EuclideanSpace ℝ (Fin 3)}
    {B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)} (hB : Continuous ↿B) (i : Fin 3) :
    (ofElectromagneticField c E B).vectorPotential c t x i =
    x (i + 2) * ∫ u in 0..(1 : ℝ), u * B t (u • x) (i + 1) ∂volume -
    x (i + 1) * ∫ u in 0..(1 : ℝ), u * B t (u • x) (i + 2) ∂volume
```

**`Electromagnetism.ElectromagneticPotential.contDiff_vectorPotential_ofElectromagneticField`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L169).

```lean
lemma contDiff_vectorPotential_ofElectromagneticField {n : ℕ} (c : SpeedOfLight)
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (hB : ContDiff ℝ n ↿B) : ContDiff ℝ n ↿((ofElectromagneticField c E B).vectorPotential c)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_vectorPotential_ofElectromagneticField_space`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L198).

> At a fixed time, the vector potential of `ofElectromagneticField` is `C^n` in space if the
> magnetic field is `C^n` in space at that time.

```lean
lemma contDiff_vectorPotential_ofElectromagneticField_space {n : ℕ} (c : SpeedOfLight)
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)) (t : Time) (hB : ContDiff ℝ n (B t)) :
    ContDiff ℝ n ((ofElectromagneticField c E B).vectorPotential c t)
```

**`Electromagnetism.ElectromagneticPotential.vectorPotential_inner_radial_eq_zero_ofElectromagneticField`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L213).

```lean
lemma vectorPotential_inner_radial_eq_zero_ofElectromagneticField
    {c : SpeedOfLight} {E B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)}
    {t : Time} {x : Space 3} {a : ℝ} (hB : Continuous ↿B) :
    ⟪(ofElectromagneticField c E B).vectorPotential c t (a • x), Space.basis.repr x⟫_ℝ = 0
```

**`Electromagnetism.ElectromagneticPotential.time_deriv_vectorPotential_inner_radial_eq_zero_ofElectromagneticField`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L226).

```lean
lemma time_deriv_vectorPotential_inner_radial_eq_zero_ofElectromagneticField
    {c : SpeedOfLight} {E B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)}
    {t : Time} {x : Space 3} {a : ℝ} (hB : ContDiff ℝ 1 ↿B) :
    ⟪∂ₜ ((ofElectromagneticField c E B).vectorPotential c · (a • x)) t,
      Space.basis.repr x⟫_ℝ = 0
```

## B. Smoothness of the vector potential

> We prove various lemmas about the smoothness of the vector potential from
> the smoothness of the electromagnetic potential.

**`Electromagnetism.ElectromagneticPotential.vectorPotential_contDiff`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L255).

```lean
lemma vectorPotential_contDiff {n} {d} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ n A) : ContDiff ℝ n ↿(A.vectorPotential c)
```

**`Electromagnetism.ElectromagneticPotential.vectorPotential_contDiff_of_smooth`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L267).

```lean
lemma vectorPotential_contDiff_of_smooth {n : ℕ} {d} {c : SpeedOfLight}
    (A : ElectromagneticPotential d) (hA : ContDiff ℝ ∞ A) :
    ContDiff ℝ n ↿(A.vectorPotential c)
```

**`Electromagnetism.ElectromagneticPotential.vectorPotential_apply_contDiff`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L274).

```lean
lemma vectorPotential_apply_contDiff {n} {d} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ n A) (i : Fin d) : ContDiff ℝ n ↿(fun t x => A.vectorPotential c t x i)
```

## C. Differentiablity of the vector potential

> We prove various lemmas about the differentiablity of the vector potential from
> the differentiablity of the electromagnetic potential.

**`Electromagnetism.ElectromagneticPotential.vectorPotential_differentiable`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L291).

```lean
lemma vectorPotential_differentiable {d} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : Differentiable ℝ A) : Differentiable ℝ ↿(A.vectorPotential c)
```

**`Electromagnetism.ElectromagneticPotential.vectorPotential_differentiable_time`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean#L302).

```lean
lemma vectorPotential_differentiable_time {d} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : Differentiable ℝ A) (x : Space d) : Differentiable ℝ (A.vectorPotential c · x)
```

## Depends on

- [The Electromagnetic Potential (EMPotential)](empotential.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/VectorPotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/VectorPotential.lean)
