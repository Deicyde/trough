---
declaration: module
origin: cited
lean: Fermion.DualRightHandedWeyl, Fermion.DualRightHandedWeyl.toFin2ℂFun, Fermion.DualRightHandedWeyl.toFin2ℂAddEquiv, Fermion.DualRightHandedWeyl.toFin2ℂEquiv, Fermion.DualRightHandedWeyl.toFin2ℂ, Fermion.DualRightHandedWeyl.toFin2ℂ_eq_val, Fermion.DualRightHandedWeyl.basis, Fermion.DualRightHandedWeyl.basis_apply
statement: formalized
proof: formalized
---

# Dual right handed Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.DualRightHanded`, [Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean): 26 declarations (6 instances with no name), 15 with a docstring.

> Dual right-handed Weyl fermions and the irreducible representation of `SL(2, ℂ)` they carry.

## i. Overview

> Dual right-handed Weyl fermions sit in the dual-conjugate representation of `SL(2,ℂ)`,
> and we consider them to have down indices `ψ_{dot α}` with `α = 1,2`.
>
> In this file we define the type `DualRightHandedWeyl`, equip it with the structure of a
> two-dimensional complex vector space with a standard basis, define the representation `rep` of
> `SL(2, ℂ)` on it by `M ↦ (M⁻¹)^†`, and show that `rep` is irreducible (C.1).

## ii. Key results

> - `DualRightHandedWeyl` : the type of dual right-handed Weyl fermions.
> - `DualRightHandedWeyl.basis` : the standard basis, indexed by `Fin 2`.
> - `DualRightHandedWeyl.rep` : the representation of `SL(2, ℂ)`.
> - `DualRightHandedWeyl.eq_zero_of_rep_eq_smul` : `rep` has no common eigenvector.
> - `DualRightHandedWeyl.end_eq_smul_id_of_commute_rep` : Schur's lemma for `rep`.

## iv. References

> * Dreiner, Haber and Martin, Two-component spinor techniques and Feynman rules for quantum
>   field theory and supersymmetry, Phys. Rept. 494 (2010) 1-196. [ref: Dreiner:2008tw]

## A. The definition of the type

**`Fermion.DualRightHandedWeyl`**, a structure, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L61).

> The module in which dual-right handed fermions live. This is equivalent to `Fin 2 → ℂ`.

```lean
structure DualRightHandedWeyl where
  /-- The underlying value in `Fin 2 → ℂ`. -/
  val : Fin 2 → ℂ
```

### A.1. Underlying module structure

**`Fermion.DualRightHandedWeyl.toFin2ℂFun`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L78).

> The equivalence between `DualRightHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂFun : DualRightHandedWeyl ≃ (Fin 2 → ℂ)
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L86).

> The instance of `AddCommMonoid` on `DualRightHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommMonoid DualRightHandedWeyl
```

**An instance with no name**, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L90).

> The instance of `AddCommGroup` on `DualRightHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommGroup DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.toFin2ℂAddEquiv`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L93).

> The additive equivalence between `DualRightHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂAddEquiv : DualRightHandedWeyl ≃+ (Fin 2 → ℂ)
```

**An instance with no name**, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L98).

> The instance of `Module` on `DualRightHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : Module ℂ DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.toFin2ℂEquiv`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L102).

> The linear equivalence between `DualRightHandedWeyl` and `(Fin 2 → ℂ)`.

```lean
def toFin2ℂEquiv : DualRightHandedWeyl ≃ₗ[ℂ] (Fin 2 → ℂ)
```

**`Fermion.DualRightHandedWeyl.toFin2ℂ`**, an abbrev, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L112).

> The underlying element of `Fin 2 → ℂ` of a element in `DualRightHandedWeyl` defined
> through the linear equivalence `toFin2ℂEquiv`.

```lean
abbrev toFin2ℂ (ψ : DualRightHandedWeyl)
```

**`Fermion.DualRightHandedWeyl.toFin2ℂ_eq_val`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L114).

```lean
lemma toFin2ℂ_eq_val (ψ : DualRightHandedWeyl) : ψ.toFin2ℂ = ψ.val
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L116).

```lean
instance : Nontrivial DualRightHandedWeyl
```

## B. Basis

**`Fermion.DualRightHandedWeyl.basis`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L125).

> The standard basis on dual-right-handed Weyl fermions.

```lean
def basis : Basis (Fin 2) ℂ DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.basis_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L128).

```lean
lemma basis_apply (i j : Fin 2) : (basis i).1 j = if j = i then 1 else 0
```

**`Fermion.DualRightHandedWeyl.eq_sum_basis`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L135).

```lean
lemma eq_sum_basis (ψ : DualRightHandedWeyl) : ψ = ∑ i, ψ.1 i • basis i
```

**`Fermion.DualRightHandedWeyl.basis_val`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L139).

```lean
lemma basis_val (i : Fin 2) : (basis i).val = Pi.single i 1
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L143).

```lean
instance : FiniteDimensional ℂ DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.finrank_eq_two`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L147).

> Dual right-handed Weyl fermions form a two-dimensional complex vector space.

```lean
lemma finrank_eq_two : Module.finrank ℂ DualRightHandedWeyl = 2
```

## C. Representation

**`Fermion.DualRightHandedWeyl.rep`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L159).

> The vector space ℂ^2 carrying the representation of SL(2,C) given by
> M → (M⁻¹)^†.
> In index notation this corresponds to a Weyl fermion with index `ψ_{dot a}`.

```lean
def rep : Representation ℂ SL(2,ℂ) DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.rep_apply`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L180).

```lean
lemma rep_apply (M : SL(2,ℂ)) (ψ : DualRightHandedWeyl) :
    rep M ψ = ⟨(M.1⁻¹).conjTranspose *ᵥ ψ.1⟩
```

**`Fermion.DualRightHandedWeyl.rep_apply_eq_sum_basis`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L183).

```lean
lemma rep_apply_eq_sum_basis (M : SL(2,ℂ)) (ψ : DualRightHandedWeyl) :
    rep M ψ = ∑ i, (∑ j, (M.1⁻¹).conjTranspose i j * ψ.1 j) • basis i
```

**`Fermion.DualRightHandedWeyl.rep_apply_basis`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L188).

```lean
lemma rep_apply_basis (M : SL(2,ℂ)) (i : Fin 2) :
    rep M (basis i) = ∑ j, (M.1⁻¹).conjTranspose j i • basis j
```

**`Fermion.DualRightHandedWeyl.rep_toMatrix`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L195).

```lean
lemma rep_toMatrix (M : SL(2,ℂ)) :
    (LinearMap.toMatrix basis basis) (rep M) = (M.1⁻¹).conjTranspose
```

**`Fermion.DualRightHandedWeyl.rep_apply_basis_repr`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L203).

```lean
lemma rep_apply_basis_repr (M : SL(2,ℂ)) (i j : Fin 2) :
    basis.repr (rep M (basis i)) j = star (M.1⁻¹ i j)
```

### C.1. Irreducibility

**`Fermion.DualRightHandedWeyl.eq_zero_of_rep_eq_smul`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L217).

> The representation `rep` has no common eigenvector.

```lean
lemma eq_zero_of_rep_eq_smul (ψ : DualRightHandedWeyl)
    (h : ∀ M : SL(2,ℂ), ∃ c : ℂ, rep M ψ = c • ψ) : ψ = 0
```

**`Fermion.DualRightHandedWeyl.eq_bot_or_eq_top_of_rep_mem`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L237).

> A submodule of `DualRightHandedWeyl` stable under `rep` is either `⊥` or everything.

```lean
lemma eq_bot_or_eq_top_of_rep_mem (p : Submodule ℂ DualRightHandedWeyl)
    (h : ∀ (M : SL(2,ℂ)) (ψ : DualRightHandedWeyl), ψ ∈ p → rep M ψ ∈ p) :
    p = ⊥ ∨ p = ⊤
```

**An instance with no name**, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L251).

> The representation `rep` of `SL(2, ℂ)` is irreducible.

```lean
instance : rep.IsIrreducible
```

**`Fermion.DualRightHandedWeyl.end_eq_smul_id_of_commute_rep`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean#L260).

> Schur's lemma for dual right-handed Weyl fermions.

```lean
lemma end_eq_smul_id_of_commute_rep {T : Module.End ℂ DualRightHandedWeyl}
    (hT : ∀ M : SL(2,ℂ), T ∘ₗ rep M = rep M ∘ₗ T) : ∃ μ : ℂ, T = μ • LinearMap.id
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualRightHanded.lean)
