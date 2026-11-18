---
declaration: module
origin: cited
lean: LorentzGroup.toVector, LorentzGroup.toVector_mul, LorentzGroup.toVector_neg, LorentzGroup.toVector_apply, LorentzGroup.toVector_eq_fun, LorentzGroup.toVector_continuous, LorentzGroup.toVector_timeComponent, LorentzGroup.toVector_minkowskiProduct_self
statement: formalized
proof: formalized
---

# Vectors from Lorentz group elements

The module `Physlib.Relativity.LorentzGroup.ToVector`, [Physlib/Relativity/LorentzGroup/ToVector.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean): 11 declarations, 1 with a docstring.

> Every element of the Lorentz group defines a Lorentz vector, but it's first column.

**`LorentzGroup.toVector`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L25).

> The Lorentz vector obtained by acting the Lorentz group element `Λ` on `basis (Sum.inl 0)`.

```lean
def toVector {d : ℕ} (Λ : LorentzGroup d) : Lorentz.Vector d
```

**`LorentzGroup.toVector_mul`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L27).

```lean
lemma toVector_mul {d : ℕ} (Λ₁ Λ₂ : LorentzGroup d) :
    toVector (Λ₁ * Λ₂) = Λ₁ • toVector Λ₂
```

**`LorentzGroup.toVector_neg`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L31).

```lean
lemma toVector_neg {d : ℕ} (Λ : LorentzGroup d) :
    toVector (-Λ) = -toVector Λ
```

**`LorentzGroup.toVector_apply`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L36).

```lean
lemma toVector_apply {d : ℕ} (Λ : LorentzGroup d)
    (i : Fin 1 ⊕ Fin d) : (toVector Λ) i = Λ.1 i (Sum.inl 0)
```

**`LorentzGroup.toVector_eq_fun`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L40).

```lean
lemma toVector_eq_fun {d : ℕ} (Λ : LorentzGroup d) :
    toVector Λ = (fun i => Λ.1 i (Sum.inl 0))
```

**`LorentzGroup.toVector_continuous`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L46).

```lean
lemma toVector_continuous {d : ℕ} : Continuous (toVector (d := d))
```

**`LorentzGroup.toVector_timeComponent`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L56).

```lean
lemma toVector_timeComponent {d : ℕ} (Λ : LorentzGroup d) :
    (toVector Λ).timeComponent = Λ.1 (Sum.inl 0) (Sum.inl 0)
```

**`LorentzGroup.toVector_minkowskiProduct_self`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L61).

```lean
lemma toVector_minkowskiProduct_self {d : ℕ} (Λ : LorentzGroup d) :
    ⟪toVector Λ, toVector Λ⟫ₘ = 1
```

**`LorentzGroup.one_le_abs_timeComponent`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L65).

```lean
lemma one_le_abs_timeComponent {d : ℕ} (Λ : LorentzGroup d) :
    1 ≤ |Λ.1 (Sum.inl 0) (Sum.inl 0)|
```

**`LorentzGroup.toVector_eq_basis_iff_timeComponent_eq_one`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L70).

```lean
lemma toVector_eq_basis_iff_timeComponent_eq_one {d : ℕ} (Λ : LorentzGroup d) :
    toVector Λ = basis (Sum.inl 0) ↔ Λ.1 (Sum.inl 0) (Sum.inl 0) = 1
```

**`LorentzGroup.smul_timeComponent_eq_toVector_minkowskiProduct`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean#L93).

```lean
lemma smul_timeComponent_eq_toVector_minkowskiProduct {d : ℕ} (Λ : LorentzGroup d)
    (v : Lorentz.Vector d) :
    (Λ • v).timeComponent = ⟪toVector Λ⁻¹, v⟫ₘ
```

## Depends on

- [Minkowski product on Lorentz vectors](../tensors/part-03/realtensor-vector-minkowskiproduct.md)

## Sources

- [Physlib/Relativity/LorentzGroup/ToVector.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/ToVector.lean)
