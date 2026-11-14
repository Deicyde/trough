---
declaration: module
origin: cited
lean: Fermion.LeftHandedWeyl.contrBi, Fermion.LeftHandedWeyl.contr, Fermion.LeftHandedWeyl.contr_tmul, Fermion.LeftHandedWeyl.contr_basis, Fermion.LeftHandedWeyl.contr_tmul_basis, Fermion.DualLeftHandedWeyl.contrBi, Fermion.DualLeftHandedWeyl.contr, Fermion.DualLeftHandedWeyl.contr_tmul
statement: formalized
proof: formalized
---

# Contraction of Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.Contraction`, [Physlib/Relativity/Fermions/Weyl/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean): 34 declarations, 22 with a docstring.

> The `SL(2, ℂ)`-invariant contractions of Weyl fermions with their duals, unique up to scale.

## i. Overview

> A left-handed Weyl fermion `ψ^a` and a dual-left-handed Weyl fermion `φ_a` contract to the
> number `ψ^a φ_a`, the dot product of their components in the standard bases. It is invariant
> under `SL(2, ℂ)` because `M` acts on `ψ` by `M` and on `φ` by `(M⁻¹)ᵀ`. Likewise a right-handed
> fermion `ψ^{dot a}`, acted on by the complex conjugate of `M`, contracts with a
> dual-right-handed fermion `φ_{dot a}`, acted on by `(M⁻¹)^†`.

## ii. Key results

> - `LeftHandedWeyl.contr` : the contraction `ψ^a φ_a`.
> - `DualLeftHandedWeyl.contr` : the contraction `φ_a ψ^a`.
> - `RightHandedWeyl.contr` : the contraction `ψ^{dot a} φ_{dot a}`.
> - `DualRightHandedWeyl.contr` : the contraction `φ_{dot a} ψ^{dot a}`.
> - `LeftHandedWeyl.eq_smul_contr` : every invariant pairing of left-handed with dual-left-handed
>   Weyl fermions is a multiple of `LeftHandedWeyl.contr`; likewise
>   `DualLeftHandedWeyl.eq_smul_contr`, `RightHandedWeyl.eq_smul_contr` and
>   `DualRightHandedWeyl.eq_smul_contr`.

## iv. References

> * Dreiner, Haber and Martin, Two-component spinor techniques and Feynman rules for quantum
>   field theory and supersymmetry, Phys. Rept. 494 (2010) 1-196. [ref: Dreiner:2008tw]

## A. Contractions of left-handed Weyl fermions

### A.1. The contraction `ψ^a φ_a`

**`Fermion.LeftHandedWeyl.contrBi`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L89).

> The bilinear map `(ψ, φ) ↦ ψ^a φ_a` underlying `LeftHandedWeyl.contr`.

```lean
def LeftHandedWeyl.contrBi : LeftHandedWeyl →ₗ[ℂ] DualLeftHandedWeyl →ₗ[ℂ] ℂ
```

**`Fermion.LeftHandedWeyl.contr`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L113).

> The contraction `ψ^a φ_a` of a left-handed with a dual-left-handed Weyl fermion, the dot
> product of their components, as an intertwining map to the trivial representation.

```lean
def LeftHandedWeyl.contr : (LeftHandedWeyl.rep.tprod DualLeftHandedWeyl.rep).IntertwiningMap
    (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

#### A.1.1. Basic properties

**`Fermion.LeftHandedWeyl.contr_tmul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L127).

```lean
lemma LeftHandedWeyl.contr_tmul (ψ : LeftHandedWeyl)
    (φ : DualLeftHandedWeyl) :
    LeftHandedWeyl.contr (ψ ⊗ₜ φ) = ψ.toFin2ℂ ⬝ᵥ φ.toFin2ℂ
```

**`Fermion.LeftHandedWeyl.contr_basis`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L132).

```lean
lemma LeftHandedWeyl.contr_basis (i j : Fin 2) :
    LeftHandedWeyl.contr (LeftHandedWeyl.basis i ⊗ₜ DualLeftHandedWeyl.basis j) =
      if i.1 = j.1 then (1 : ℂ) else 0
```

**`Fermion.LeftHandedWeyl.contr_tmul_basis`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L144).

> Contracting with the `j`-th basis vector picks out the `j`-th component of `ψ`.

```lean
lemma LeftHandedWeyl.contr_tmul_basis (ψ : LeftHandedWeyl) (j : Fin 2) :
    LeftHandedWeyl.contr (ψ ⊗ₜ DualLeftHandedWeyl.basis j) = ψ.val j
```

### A.2. The contraction `φ_a ψ^a`

**`Fermion.DualLeftHandedWeyl.contrBi`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L157).

> The bilinear map `(φ, ψ) ↦ φ_a ψ^a` underlying `DualLeftHandedWeyl.contr`.

```lean
def DualLeftHandedWeyl.contrBi : DualLeftHandedWeyl →ₗ[ℂ] LeftHandedWeyl →ₗ[ℂ] ℂ
```

**`Fermion.DualLeftHandedWeyl.contr`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L180).

> The contraction `φ_a ψ^a` of a dual-left-handed with a left-handed Weyl fermion, the dot
> product of their components, as an intertwining map to the trivial representation.

```lean
def DualLeftHandedWeyl.contr : (DualLeftHandedWeyl.rep.tprod LeftHandedWeyl.rep).IntertwiningMap
    (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

#### A.2.1. Basic properties

**`Fermion.DualLeftHandedWeyl.contr_tmul`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L194).

```lean
lemma DualLeftHandedWeyl.contr_tmul (φ : DualLeftHandedWeyl) (ψ : LeftHandedWeyl) :
    DualLeftHandedWeyl.contr (φ ⊗ₜ ψ) = φ.toFin2ℂ ⬝ᵥ ψ.toFin2ℂ
```

**`Fermion.DualLeftHandedWeyl.contr_basis`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L198).

```lean
lemma DualLeftHandedWeyl.contr_basis (i j : Fin 2) :
    DualLeftHandedWeyl.contr (DualLeftHandedWeyl.basis i ⊗ₜ LeftHandedWeyl.basis j) =
      if i.1 = j.1 then (1 : ℂ) else 0
```

### A.3. Symmetry

**`Fermion.LeftHandedWeyl.contr_tmul_symm`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L215).

```lean
lemma LeftHandedWeyl.contr_tmul_symm (ψ : LeftHandedWeyl) (φ : DualLeftHandedWeyl) :
    LeftHandedWeyl.contr (ψ ⊗ₜ[ℂ] φ) = DualLeftHandedWeyl.contr (φ ⊗ₜ[ℂ] ψ)
```

**`Fermion.DualLeftHandedWeyl.contr_tmul_symm`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L219).

```lean
lemma DualLeftHandedWeyl.contr_tmul_symm (φ : DualLeftHandedWeyl) (ψ : LeftHandedWeyl) :
    DualLeftHandedWeyl.contr (φ ⊗ₜ[ℂ] ψ) = LeftHandedWeyl.contr (ψ ⊗ₜ[ℂ] φ)
```

### A.4. Nondegeneracy

**`Fermion.LeftHandedWeyl.eq_zero_of_contr_tmul_eq_zero`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L230).

> The contraction is nondegenerate: if `ψ^a φ_a = 0` for every `φ` then `ψ = 0`.

```lean
lemma LeftHandedWeyl.eq_zero_of_contr_tmul_eq_zero (ψ : LeftHandedWeyl)
    (h : ∀ φ, LeftHandedWeyl.contr (ψ ⊗ₜ φ) = 0) : ψ = 0
```

**`Fermion.DualLeftHandedWeyl.eq_zero_of_contr_tmul_eq_zero`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L237).

> The contraction is nondegenerate: if `φ_a ψ^a = 0` for every `ψ` then `φ = 0`.

```lean
lemma DualLeftHandedWeyl.eq_zero_of_contr_tmul_eq_zero (φ : DualLeftHandedWeyl)
    (h : ∀ ψ, DualLeftHandedWeyl.contr (φ ⊗ₜ ψ) = 0) : φ = 0
```

### A.5. Perfect pairing

**`Fermion.LeftHandedWeyl.contrBi_isPerfPair`**, an instance, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L251).

> The pairing `(ψ, φ) ↦ ψ^a φ_a` is perfect. It identifies dual-left-handed Weyl fermions with
> the dual of left-handed Weyl fermions, and vice versa.

```lean
instance LeftHandedWeyl.contrBi_isPerfPair : LeftHandedWeyl.contrBi.IsPerfPair
```

**`Fermion.DualLeftHandedWeyl.contrBi_isPerfPair`**, an instance, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L262).

> The pairing `(φ, ψ) ↦ φ_a ψ^a` is perfect. It identifies left-handed Weyl fermions with the
> dual of dual-left-handed Weyl fermions, and vice versa.

```lean
instance DualLeftHandedWeyl.contrBi_isPerfPair : DualLeftHandedWeyl.contrBi.IsPerfPair
```

### A.6. Uniqueness up to scale

**`Fermion.LeftHandedWeyl.eq_smul_contr`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L279).

> Every `SL(2,ℂ)`-invariant pairing of left-handed with dual-left-handed Weyl fermions is a
> multiple of `LeftHandedWeyl.contr`.

```lean
lemma LeftHandedWeyl.eq_smul_contr
    (B : (LeftHandedWeyl.rep.tprod DualLeftHandedWeyl.rep).IntertwiningMap
      (Representation.trivial ℂ SL(2,ℂ) ℂ)) :
    ∃ z : ℂ, B = z • LeftHandedWeyl.contr
```

**`Fermion.DualLeftHandedWeyl.eq_smul_contr`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L303).

> Every `SL(2,ℂ)`-invariant pairing of dual-left-handed with left-handed Weyl fermions is a
> multiple of `DualLeftHandedWeyl.contr`.

```lean
lemma DualLeftHandedWeyl.eq_smul_contr
    (B : (DualLeftHandedWeyl.rep.tprod LeftHandedWeyl.rep).IntertwiningMap
      (Representation.trivial ℂ SL(2,ℂ) ℂ)) :
    ∃ z : ℂ, B = z • DualLeftHandedWeyl.contr
```

## B. Contractions of right-handed Weyl fermions

### B.1. The contraction `ψ^{dot a} φ_{dot a}`

**`Fermion.RightHandedWeyl.contrBi`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L327).

> The bilinear map `(ψ, φ) ↦ ψ^{dot a} φ_{dot a}` underlying `RightHandedWeyl.contr`.

```lean
def RightHandedWeyl.contrBi : RightHandedWeyl →ₗ[ℂ] DualRightHandedWeyl →ₗ[ℂ] ℂ
```

**`Fermion.RightHandedWeyl.contr`**, a def, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L352).

> The contraction `ψ^{dot a} φ_{dot a}` of a right-handed with a dual-right-handed Weyl
> fermion, the dot product of their components, as an intertwining map to the trivial
> representation.

```lean
def RightHandedWeyl.contr : (RightHandedWeyl.rep.tprod DualRightHandedWeyl.rep).IntertwiningMap
    (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

#### B.1.1. Basic properties

**`Fermion.RightHandedWeyl.contr_tmul`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L377).

```lean
lemma RightHandedWeyl.contr_tmul (ψ : RightHandedWeyl)
    (φ : DualRightHandedWeyl) :
    RightHandedWeyl.contr (ψ ⊗ₜ φ) = ψ.toFin2ℂ ⬝ᵥ φ.toFin2ℂ
```

**`Fermion.RightHandedWeyl.contr_basis`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L382).

```lean
lemma RightHandedWeyl.contr_basis (i j : Fin 2) :
    RightHandedWeyl.contr (RightHandedWeyl.basis i ⊗ₜ DualRightHandedWeyl.basis j) =
    if i.1 = j.1 then (1 : ℂ) else 0
```

**`Fermion.RightHandedWeyl.contr_tmul_basis`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L394).

> Contracting with the `j`-th basis vector picks out the `j`-th component.

```lean
lemma RightHandedWeyl.contr_tmul_basis (ψ : RightHandedWeyl) (j : Fin 2) :
    RightHandedWeyl.contr (ψ ⊗ₜ DualRightHandedWeyl.basis j) = ψ.val j
```

### B.2. The contraction `φ_{dot a} ψ^{dot a}`

**`Fermion.DualRightHandedWeyl.contrBi`**, a def, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L407).

> The bilinear map `(φ, ψ) ↦ φ_{dot a} ψ^{dot a}` underlying `DualRightHandedWeyl.contr`.

```lean
def DualRightHandedWeyl.contrBi : DualRightHandedWeyl →ₗ[ℂ] RightHandedWeyl →ₗ[ℂ] ℂ
```

**`Fermion.DualRightHandedWeyl.contr`**, a def, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L431).

> The contraction `φ_{dot a} ψ^{dot a}` of a dual-right-handed with a right-handed Weyl
> fermion, the dot product of their components, as an intertwining map to the trivial
> representation.

```lean
def DualRightHandedWeyl.contr : (DualRightHandedWeyl.rep.tprod RightHandedWeyl.rep).IntertwiningMap
    (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

#### B.2.1. Basic properties

**`Fermion.DualRightHandedWeyl.contr_tmul`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L456).

```lean
lemma DualRightHandedWeyl.contr_tmul (φ : DualRightHandedWeyl)
    (ψ : RightHandedWeyl) :
    DualRightHandedWeyl.contr (φ ⊗ₜ ψ) = φ.toFin2ℂ ⬝ᵥ ψ.toFin2ℂ
```

**`Fermion.DualRightHandedWeyl.contr_basis`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L461).

```lean
lemma DualRightHandedWeyl.contr_basis (i j : Fin 2) :
    DualRightHandedWeyl.contr (DualRightHandedWeyl.basis i ⊗ₜ RightHandedWeyl.basis j) =
    if i.1 = j.1 then (1 : ℂ) else 0
```

### B.3. Symmetry

**`Fermion.RightHandedWeyl.contr_tmul_symm`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L478).

```lean
lemma RightHandedWeyl.contr_tmul_symm (ψ : RightHandedWeyl) (φ : DualRightHandedWeyl) :
    RightHandedWeyl.contr (ψ ⊗ₜ[ℂ] φ) = DualRightHandedWeyl.contr (φ ⊗ₜ[ℂ] ψ)
```

**`Fermion.DualRightHandedWeyl.contr_tmul_symm`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L482).

```lean
lemma DualRightHandedWeyl.contr_tmul_symm (φ : DualRightHandedWeyl) (ψ : RightHandedWeyl) :
    DualRightHandedWeyl.contr (φ ⊗ₜ[ℂ] ψ) = RightHandedWeyl.contr (ψ ⊗ₜ[ℂ] φ)
```

### B.4. Nondegeneracy

**`Fermion.RightHandedWeyl.eq_zero_of_contr_tmul_eq_zero`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L494).

> The contraction is nondegenerate: if `ψ^{dot a} φ_{dot a} = 0` for every `φ` then
> `ψ = 0`.

```lean
lemma RightHandedWeyl.eq_zero_of_contr_tmul_eq_zero (ψ : RightHandedWeyl)
    (h : ∀ φ, RightHandedWeyl.contr (ψ ⊗ₜ φ) = 0) : ψ = 0
```

**`Fermion.DualRightHandedWeyl.eq_zero_of_contr_tmul_eq_zero`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L502).

> The contraction is nondegenerate: if `φ_{dot a} ψ^{dot a} = 0` for every `ψ` then
> `φ = 0`.

```lean
lemma DualRightHandedWeyl.eq_zero_of_contr_tmul_eq_zero (φ : DualRightHandedWeyl)
    (h : ∀ ψ, DualRightHandedWeyl.contr (φ ⊗ₜ ψ) = 0) : φ = 0
```

### B.5. Perfect pairing

**`Fermion.RightHandedWeyl.contrBi_isPerfPair`**, an instance, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L516).

> The pairing `(ψ, φ) ↦ ψ^{dot a} φ_{dot a}` is perfect. It identifies dual-right-handed Weyl
> fermions with the dual of right-handed Weyl fermions, and vice versa.

```lean
instance RightHandedWeyl.contrBi_isPerfPair : RightHandedWeyl.contrBi.IsPerfPair
```

**`Fermion.DualRightHandedWeyl.contrBi_isPerfPair`**, an instance, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L527).

> The pairing `(φ, ψ) ↦ φ_{dot a} ψ^{dot a}` is perfect. It identifies right-handed Weyl
> fermions with the dual of dual-right-handed Weyl fermions, and vice versa.

```lean
instance DualRightHandedWeyl.contrBi_isPerfPair : DualRightHandedWeyl.contrBi.IsPerfPair
```

### B.6. Uniqueness up to scale

> The argument is that of A.6.

**`Fermion.RightHandedWeyl.eq_smul_contr`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L546).

> Every `SL(2,ℂ)`-invariant pairing of right-handed with dual-right-handed Weyl fermions is a
> multiple of `RightHandedWeyl.contr`.

```lean
lemma RightHandedWeyl.eq_smul_contr
    (B : (RightHandedWeyl.rep.tprod DualRightHandedWeyl.rep).IntertwiningMap
      (Representation.trivial ℂ SL(2,ℂ) ℂ)) :
    ∃ z : ℂ, B = z • RightHandedWeyl.contr
```

**`Fermion.DualRightHandedWeyl.eq_smul_contr`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean#L570).

> Every `SL(2,ℂ)`-invariant pairing of dual-right-handed with right-handed Weyl fermions is a
> multiple of `DualRightHandedWeyl.contr`.

```lean
lemma DualRightHandedWeyl.eq_smul_contr
    (B : (DualRightHandedWeyl.rep.tprod RightHandedWeyl.rep).IntertwiningMap
      (Representation.trivial ℂ SL(2,ℂ) ℂ)) :
    ∃ z : ℂ, B = z • DualRightHandedWeyl.contr
```

## Depends on

- [Dual left handed Weyl fermions](duallefthanded.md)
- [Dual right handed Weyl fermions](dualrighthanded.md)
- [Left handed Weyl fermions](lefthanded.md)
- [Right handed Weyl fermions](righthanded.md)

## Sources

- [Physlib/Relativity/Fermions/Weyl/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Contraction.lean)
