---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.scalarPotential, Electromagnetism.ElectromagneticPotential.ofScalarPotential_scalarPotential, Electromagnetism.ElectromagneticPotential.ofStaticScalarPotential_scalarPotential, Electromagnetism.ElectromagneticPotential.ofVectorPotential_scalarPotential, Electromagnetism.ElectromagneticPotential.ofStaticVectorPotential_scalarPotential, Electromagnetism.ElectromagneticPotential.ofPotentials_scalarPotential, Electromagnetism.ElectromagneticPotential.ofStaticPotentials_scalarPotential, Electromagnetism.ElectromagneticPotential.ofElectromagneticField_scalarPotential
statement: formalized
proof: formalized
---

# The Scalar Potential

The module `Physlib.Electromagnetism.Kinematics.ScalarPotential`, [Physlib/Electromagnetism/Kinematics/ScalarPotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean): 12 declarations, 1 with a docstring.

## i. Overview

> The electromagnetic potential is given by
> `A = (1/c φ, \vec A)`
> where `φ` is the scalar potential and `\vec A` is the vector potential.
>
> In this module we define the scalar potential, and prove lemmas about it.
>
> Since `A` is relativistic it is a function of `SpaceTime d`, whilst
> the scalar potential is non-relativistic and is therefore a function of `Time` and `Space d`.

## ii. Key results

> - `ElectromagneticPotential.scalarPotential` : The scalar potential from an
>   electromagnetic potential.

## iv. References

> * None.

## A. Definition of the Scalar Potential

**`Electromagnetism.ElectromagneticPotential.scalarPotential`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L64).

> The scalar potential from the electromagnetic potential.

```lean
noncomputable def scalarPotential {d} (c : SpeedOfLight := 1) (A : ElectromagneticPotential d) :
    Time → Space d → ℝ
```

## B. Relation to constructors

**`Electromagnetism.ElectromagneticPotential.ofScalarPotential_scalarPotential`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L75).

```lean
lemma ofScalarPotential_scalarPotential {d} (c : SpeedOfLight)
    (φ : Time → Space d → ℝ) : (ofScalarPotential c φ).scalarPotential c = φ
```

**`Electromagnetism.ElectromagneticPotential.ofStaticScalarPotential_scalarPotential`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L82).

```lean
lemma ofStaticScalarPotential_scalarPotential {d} (c : SpeedOfLight)
    (φ : Space d → ℝ) : (ofStaticScalarPotential c φ).scalarPotential c = fun _ => φ
```

**`Electromagnetism.ElectromagneticPotential.ofVectorPotential_scalarPotential`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L87).

```lean
lemma ofVectorPotential_scalarPotential {d} (c : SpeedOfLight)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    (ofVectorPotential c A).scalarPotential = 0
```

**`Electromagnetism.ElectromagneticPotential.ofStaticVectorPotential_scalarPotential`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L94).

```lean
lemma ofStaticVectorPotential_scalarPotential {d} (c : SpeedOfLight)
    (A : Space d → EuclideanSpace ℝ (Fin d)) :
    (ofStaticVectorPotential c A).scalarPotential = 0
```

**`Electromagnetism.ElectromagneticPotential.ofPotentials_scalarPotential`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L100).

```lean
lemma ofPotentials_scalarPotential {d} (c : SpeedOfLight) (φ : Time → Space d → ℝ)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    (ofPotentials c φ A).scalarPotential c = φ
```

**`Electromagnetism.ElectromagneticPotential.ofStaticPotentials_scalarPotential`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L108).

```lean
lemma ofStaticPotentials_scalarPotential {d} (c : SpeedOfLight) (φ : Space d → ℝ)
    (A : Space d → EuclideanSpace ℝ (Fin d)) :
    (ofStaticPotentials c φ A).scalarPotential c = fun _ => φ
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_scalarPotential`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L114).

```lean
lemma ofElectromagneticField_scalarPotential (c : SpeedOfLight)
    (E : Time → Space → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space → EuclideanSpace ℝ (Fin 3)) :
    (ofElectromagneticField c E B).scalarPotential c = fun t x =>
    - ∫ u in (0 : ℝ)..1, ⟪E t (u • x), basis.repr x⟫_ℝ ∂(volume)
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_scalarPotential_eq_add_vectorPotential`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L122).

```lean
lemma ofElectromagneticField_scalarPotential_eq_add_vectorPotential (c : SpeedOfLight)
    (E : Time → Space → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space → EuclideanSpace ℝ (Fin 3)) (hb : ContDiff ℝ 1 ↿B) :
    (ofElectromagneticField c E B).scalarPotential c = fun t x =>
    - ∫ u in (0 : ℝ)..1, ⟪E t (u • x) +
    ∂ₜ ((ofElectromagneticField c E B).vectorPotential c ·
      (u • x)) t, basis.repr x⟫_ℝ ∂(volume)
```

## C. Smoothness of the Scalar Potential

> We prove various lemmas about the smoothness of the scalar potential.

**`Electromagnetism.ElectromagneticPotential.scalarPotential_contDiff`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L145).

```lean
lemma scalarPotential_contDiff {n} {d} (c : SpeedOfLight) (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ n A) : ContDiff ℝ n ↿(A.scalarPotential c)
```

**`Electromagnetism.ElectromagneticPotential.scalarPotential_contDiff_space_of_smooth`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L159).

```lean
lemma scalarPotential_contDiff_space_of_smooth {n : ℕ} {d} (c : SpeedOfLight)
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (t : Time) : ContDiff ℝ n (A.scalarPotential c t)
```

## d. Differentiability of the Scalar Potential

> We prove various lemmas about the differentiability of the scalar potential.

**`Electromagnetism.ElectromagneticPotential.scalarPotential_differentiable`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean#L174).

```lean
lemma scalarPotential_differentiable {d} (c : SpeedOfLight) (A : ElectromagneticPotential d)
    (hA : Differentiable ℝ A) : Differentiable ℝ ↿(A.scalarPotential c)
```

## Depends on

- [The vector Potential](vectorpotential.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/ScalarPotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ScalarPotential.lean)
