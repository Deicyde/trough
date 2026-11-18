---
declaration: module
origin: cited
lean: LorentzGroup.exists_boost_mul_rotation, LorentzGroup.toVelocity, LorentzGroup.toVelocity_val, LorentzGroup.toVelocity_continuous, LorentzGroup.toRotation, LorentzGroup.toRotation_continuous, LorentzGroup.toBoostRotation
statement: formalized
proof: formalized
---

# The construction of an element of the Lorentz group from a boost and a rotation

The module `Physlib.Relativity.LorentzGroup.Restricted.FromBoostRotation`, [Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean): 7 declarations, 4 with a docstring, 1 listed as significant.

> The main result of this module is the homeomorphism `toBoostRotation`
> from the restricted Lorentz group to the product of Lorentz velocities and rotations.
>
> The inverse of this homeomorphism writes elements of the restricted Lorentz group
> as a product of a generalized boost and a rotation.

**`LorentzGroup.toVelocity`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L32).

> The Lorentz velocity obtained from `toVector Λ` where `Λ` is an element
> of the restricted Lorentz group.

```lean
def toVelocity {d} (Λ : LorentzGroup.restricted d) : Lorentz.Velocity d
```

**`LorentzGroup.toVelocity_val`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L39).

```lean
lemma toVelocity_val {d} (Λ : LorentzGroup.restricted d) :
    (toVelocity Λ).1 = toVector Λ
```

**`LorentzGroup.toVelocity_continuous`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L43).

```lean
lemma toVelocity_continuous {d} :
    Continuous (toVelocity : LorentzGroup.restricted d → Lorentz.Velocity d)
```

**`LorentzGroup.toRotation`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L49).

> A map from the restricted Lorentz group to rotations.

```lean
def toRotation {d} (Λ : LorentzGroup.restricted d) : Rotations d
```

**`LorentzGroup.toRotation_continuous`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L62).

```lean
lemma toRotation_continuous {d} :
    Continuous (toRotation : LorentzGroup.restricted d → Rotations d)
```

**`LorentzGroup.toBoostRotation`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L72).

> The homeomorphism from the restricted Lorentz group to the product of
> `Lorentz.Velocity d` and `Matrix.specialOrthogonalGroup (Fin d) ℝ`. The
> inverse of this map writes an element of the restricted Lorentz group
> as a product of a boost and a rotation.

```lean
def toBoostRotation {d} : LorentzGroup.restricted d ≃ₜ Lorentz.Velocity d ×
    Matrix.specialOrthogonalGroup (Fin d) ℝ
```

**`LorentzGroup.exists_boost_mul_rotation`**, a theorem, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean#L110). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every element of the restricted Lorentz group can be written as a product of a
> generalized boost and a rotation.

```lean
theorem exists_boost_mul_rotation {d} (Λ : LorentzGroup.restricted d) :
    ∃ (v : Lorentz.Velocity d) (R : Rotations d),
      (Λ : LorentzGroup d) = generalizedBoost 0 v * (R : LorentzGroup d)
```

## Depends on

- [Generalized Boosts](boosts-generalized.md)
- [Rotations](rotations.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted/FromBoostRotation.lean)
