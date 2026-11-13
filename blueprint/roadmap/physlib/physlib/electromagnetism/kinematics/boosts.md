---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.electricField_apply_x_boost_zero, Electromagnetism.ElectromagneticPotential.electricField_apply_x_boost_succ, Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_apply_x_boost_zero_succ, Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_apply_x_boost_succ_succ
statement: formalized
proof: formalized
---

# Boosts on the electric and magnetic fields

The module `Physlib.Electromagnetism.Kinematics.Boosts`, [Physlib/Electromagnetism/Kinematics/Boosts.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/Boosts.lean): 4 declarations, 0 with a docstring.

## i. Overview

> We find the transformations of the electric and magnetic field matrix under
> boosts in the 'x' direction. We do this in full-generality for `d+1` space dimensions.

## ii. Key results

> - `electricField_apply_x_boost_zero` : The transformation of the x-component of the electric
>   field under a boost in the 'x' direction.
> - `electricField_apply_x_boost_succ` : The transformation of the other components of the electric
>   field under a boost in the 'x' direction.
> - `magneticFieldMatrix_apply_x_boost_zero_succ` : The transformation of the 'x-components' of the
>   magnetic field matrix under a boost in the 'x' direction
> - `magneticFieldMatrix_apply_x_boost_succ_succ` : The transformation of the other components of the
>   magnetic field matrix under a boost in the 'x' direction.

## iv. References

> * https://en.wikipedia.org/wiki/Classical\_electromagnetism\_and\_special\_relativity.
>   [ref: wiki\_classical\_em\_and\_sr]

## A. Boost of the electric field

### A.1. Boost of the x-component of the electric field

**`Electromagnetism.ElectromagneticPotential.electricField_apply_x_boost_zero`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/Boosts.lean#L66).

```lean
lemma electricField_apply_x_boost_zero {d : ℕ} {c : SpeedOfLight} (β : ℝ) (hβ : |β| < 1)
    (A : ElectromagneticPotential d.succ) (hA : Differentiable ℝ A) (t : Time) (x : Space d.succ) :
    let Λ := LorentzGroup.boost (d := d.succ) 0 β hβ
    let t' : Time := γ β * (t.val + β /c * x 0)
    let x' : Space d.succ := ⟨fun
      | 0 => γ β * (x 0 + c * β * t.val)
      | ⟨Nat.succ n, ih⟩ => x ⟨Nat.succ n, ih⟩⟩
    electricField c (Λ • A) t x 0 =
    A.electricField c t' x' 0
```

### A.2. Boost of other components of the electric field

**`Electromagnetism.ElectromagneticPotential.electricField_apply_x_boost_succ`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/Boosts.lean#L101).

```lean
lemma electricField_apply_x_boost_succ {d : ℕ} {c : SpeedOfLight} (β : ℝ) (hβ : |β| < 1)
    (A : ElectromagneticPotential d.succ) (hA : Differentiable ℝ A) (t : Time) (x : Space d.succ)
    (i : Fin d) :
    let Λ := LorentzGroup.boost (d := d.succ) 0 β hβ
    let t' : Time := γ β * (t.val + β /c * x 0)
    let x' : Space d.succ := ⟨fun
      | 0 => γ β * (x 0 + c * β * t.val)
      | ⟨Nat.succ n, ih⟩ => x ⟨Nat.succ n, ih⟩⟩
    electricField c (Λ • A) t x i.succ =
    γ β * (A.electricField c t' x' i.succ + c * β * A.magneticFieldMatrix c t' x' (0, i.succ))
```

## B. Boost of the magnetic field

### B.1. Boost of the 'x-components' of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_apply_x_boost_zero_succ`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/Boosts.lean#L137).

```lean
lemma magneticFieldMatrix_apply_x_boost_zero_succ {d : ℕ} {c : SpeedOfLight} (β : ℝ) (hβ : |β| < 1)
    (A : ElectromagneticPotential d.succ) (hA : Differentiable ℝ A) (t : Time) (x : Space d.succ)
    (i : Fin d) :
    let Λ := LorentzGroup.boost (d := d.succ) 0 β hβ
    let t' : Time := γ β * (t.val + β /c * x 0)
    let x' : Space d.succ := ⟨fun
      | 0 => γ β * (x 0 + c * β * t.val)
      | ⟨Nat.succ n, ih⟩ => x ⟨Nat.succ n, ih⟩⟩
    magneticFieldMatrix c (Λ • A) t x (0, i.succ) =
    γ β * (A.magneticFieldMatrix c t' x' (0, i.succ) + β / c * A.electricField c t' x' i.succ)
```

### B.2. Boost of the other components of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_apply_x_boost_succ_succ`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/Boosts.lean#L165).

```lean
lemma magneticFieldMatrix_apply_x_boost_succ_succ {d : ℕ} {c : SpeedOfLight} (β : ℝ) (hβ : |β| < 1)
    (A : ElectromagneticPotential d.succ) (hA : Differentiable ℝ A) (t : Time) (x : Space d.succ)
    (i j : Fin d) :
    let Λ := LorentzGroup.boost (d := d.succ) 0 β hβ
    let t' : Time := γ β * (t.val + β /c * x 0)
    let x' : Space d.succ := ⟨fun
      | 0 => γ β * (x 0 + c * β * t.val)
      | ⟨Nat.succ n, ih⟩ => x ⟨Nat.succ n, ih⟩⟩
    magneticFieldMatrix c (Λ • A) t x (i.succ, j.succ) =
    A.magneticFieldMatrix c t' x' (i.succ, j.succ)
```

## Depends on

- [The Magnetic Field](magneticfield.md)
- [Boosts in the Lorentz group](../../relativity/lorentzgroup/boosts-basic.md)

## Proof depends on

- [Boosts of space time](../../spaceandtime/spacetime/boosts.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/Boosts.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/Boosts.lean)
