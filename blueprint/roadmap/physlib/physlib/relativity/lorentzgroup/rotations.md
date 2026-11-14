---
declaration: module
origin: cited
lean: LorentzGroup.Rotations, LorentzGroup.mem_rotations_iff, LorentzGroup.transpose_mem_rotations, LorentzGroup.ofSpecialOrthogonal, LorentzGroup.ofSpecialOrthogonal_continuous, LorentzGroup.ofSpecialOrthogonal_symm_continuous, LorentzGroup.rotations_subset_restricted, LorentzGroup.toVector_rotation
statement: formalized
proof: formalized
---

# Rotations

The module `Physlib.Relativity.LorentzGroup.Rotations`, [Physlib/Relativity/LorentzGroup/Rotations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean): 8 declarations, 2 with a docstring.

> In this module we define rotations of in the Lorentz group.

**`LorentzGroup.Rotations`**, a def, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L23).

> The subgroup of rotations of the Lorentz group.

```lean
def Rotations (d) : Subgroup (LorentzGroup d)
```

**`LorentzGroup.mem_rotations_iff`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L51).

```lean
lemma mem_rotations_iff {d} (Λ : LorentzGroup d) :
    Λ ∈ Rotations d ↔ Λ.1 (Sum.inl 0) (Sum.inl 0) = 1 ∧ IsProper Λ
```

**`LorentzGroup.transpose_mem_rotations`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L56).

```lean
lemma transpose_mem_rotations {d} (Λ : LorentzGroup d) :
    transpose Λ ∈ Rotations d ↔ Λ ∈ Rotations d
```

**`LorentzGroup.ofSpecialOrthogonal`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L62).

> The group homomorphism from the special orthogonal group to the Lorentz group.

```lean
def ofSpecialOrthogonal {d} :
    Matrix.specialOrthogonalGroup (Fin d) ℝ ≃* Rotations d
```

**`LorentzGroup.ofSpecialOrthogonal_continuous`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L167).

```lean
lemma ofSpecialOrthogonal_continuous {d} :
    Continuous (ofSpecialOrthogonal : Matrix.specialOrthogonalGroup (Fin d) ℝ → Rotations d)
```

**`LorentzGroup.ofSpecialOrthogonal_symm_continuous`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L173).

```lean
lemma ofSpecialOrthogonal_symm_continuous {d} :
    Continuous (ofSpecialOrthogonal.symm :
      Rotations d → Matrix.specialOrthogonalGroup (Fin d) ℝ)
```

**`LorentzGroup.rotations_subset_restricted`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L181).

```lean
lemma rotations_subset_restricted (d) : Rotations d ≤ LorentzGroup.restricted d
```

**`LorentzGroup.toVector_rotation`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean#L189).

```lean
lemma toVector_rotation {d} (Λ : Rotations d) :
    LorentzGroup.toVector Λ.1= Lorentz.Vector.basis (Sum.inl 0)
```

## Depends on

- [The Restricted Lorentz Group](restricted-basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Rotations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Rotations.lean)
