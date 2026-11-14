---
declaration: module
origin: cited
lean: Fermion.DualLeftHandedWeyl, Fermion.DualLeftHandedWeyl.toFin2ℂFun, Fermion.DualLeftHandedWeyl.toFin2ℂAddEquiv, Fermion.DualLeftHandedWeyl.toFin2ℂEquiv, Fermion.DualLeftHandedWeyl.toFin2ℂ, Fermion.DualLeftHandedWeyl.toFin2ℂ_eq_val, Fermion.DualLeftHandedWeyl.basis, Fermion.DualLeftHandedWeyl.basis_apply
statement: formalized
proof: formalized
---

# Dual left handed Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.DualLeftHanded`, [Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean): 26 declarations (6 instances with no name), 15 with a docstring.

> Dual left-handed Weyl fermions and the irreducible representation of `SL(2, ℂ)` they carry.

## i. Overview

> Dual left-handed Weyl fermions sit in the dual of the fundamental representation of `SL(2,ℂ)`,
> and we consider them to have down indices `ψ_α` with `α = 1,2`.
>
> In this file we define the type `DualLeftHandedWeyl`, equip it with the structure of a
> two-dimensional complex vector space with a standard basis, define the representation `rep` of
> `SL(2, ℂ)` on it by `M ↦ (M⁻¹)ᵀ`, and show that `rep` is irreducible (C.1).

## ii. Key results

> - `DualLeftHandedWeyl` : the type of dual left-handed Weyl fermions.
> - `DualLeftHandedWeyl.basis` : the standard basis, indexed by `Fin 2`.
> - `DualLeftHandedWeyl.rep` : the representation of `SL(2, ℂ)`.
> - `DualLeftHandedWeyl.eq_zero_of_rep_eq_smul` : `rep` has no common eigenvector.
> - `DualLeftHandedWeyl.end_eq_smul_id_of_commute_rep` : Schur's lemma for `rep`.

## iv. References

> * A good reference for the material in this file, although it uses a different
>   index convention: https://particle.physics.ucdavis.edu/modernsusy/slides/slideimages/spinorfeynrules.pdf. [ref: ucdavis\_spinorfeynrules]

## A. The definition of the type

**`Fermion.DualLeftHandedWeyl`**, a structure, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L61).

> The module in which dual-left handed fermions live. This is equivalent to `Fin 2 → ℂ`.

```lean
structure DualLeftHandedWeyl where
  /-- The underlying value in `Fin 2 → ℂ`. -/
  val : Fin 2 → ℂ
```

### A.1. Underlying module structure

**`Fermion.DualLeftHandedWeyl.toFin2ℂFun`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L78).

> The equivalence between `DualLeftHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂFun : DualLeftHandedWeyl ≃ (Fin 2 → ℂ)
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L86).

> The instance of `AddCommMonoid` on `DualLeftHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommMonoid DualLeftHandedWeyl
```

**An instance with no name**, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L90).

> The instance of `AddCommGroup` on `DualLeftHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommGroup DualLeftHandedWeyl
```

**`Fermion.DualLeftHandedWeyl.toFin2ℂAddEquiv`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L93).

> The additive equivalence between `DualLeftHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂAddEquiv : DualLeftHandedWeyl ≃+ (Fin 2 → ℂ)
```

**An instance with no name**, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L98).

> The instance of `Module` on `DualLeftHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : Module ℂ DualLeftHandedWeyl
```

**`Fermion.DualLeftHandedWeyl.toFin2ℂEquiv`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L102).

> The linear equivalence between `DualLeftHandedWeyl` and `(Fin 2 → ℂ)`.

```lean
def toFin2ℂEquiv : DualLeftHandedWeyl ≃ₗ[ℂ] (Fin 2 → ℂ)
```

**`Fermion.DualLeftHandedWeyl.toFin2ℂ`**, an abbrev, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L112).

> The underlying element of `Fin 2 → ℂ` of a element in `DualLeftHandedWeyl` defined
> through the linear equivalence `toFin2ℂEquiv`.

```lean
abbrev toFin2ℂ (ψ : DualLeftHandedWeyl)
```

**`Fermion.DualLeftHandedWeyl.toFin2ℂ_eq_val`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L114).

```lean
lemma toFin2ℂ_eq_val (ψ : DualLeftHandedWeyl) : ψ.toFin2ℂ = ψ.val
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L116).

```lean
instance : Nontrivial DualLeftHandedWeyl
```

## B. Basis

**`Fermion.DualLeftHandedWeyl.basis`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L125).

> The standard basis on dual-left-handed Weyl fermions.

```lean
def basis : Basis (Fin 2) ℂ DualLeftHandedWeyl
```

**`Fermion.DualLeftHandedWeyl.basis_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L128).

```lean
lemma basis_apply (i j : Fin 2) : (basis i).1 j = if j = i then 1 else 0
```

**`Fermion.DualLeftHandedWeyl.eq_sum_basis`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L135).

```lean
lemma eq_sum_basis (ψ : DualLeftHandedWeyl) : ψ = ∑ i, ψ.1 i • basis i
```

**`Fermion.DualLeftHandedWeyl.basis_val`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L139).

```lean
lemma basis_val (i : Fin 2) : (basis i).val = Pi.single i 1
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L143).

```lean
instance : FiniteDimensional ℂ DualLeftHandedWeyl
```

**`Fermion.DualLeftHandedWeyl.finrank_eq_two`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L147).

> Dual left-handed Weyl fermions form a two-dimensional complex vector space.

```lean
lemma finrank_eq_two : Module.finrank ℂ DualLeftHandedWeyl = 2
```

## C. Representation

**`Fermion.DualLeftHandedWeyl.rep`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L158).

> The vector space ℂ^2 carrying the representation of SL(2,C) given by
> M → (M⁻¹)ᵀ. In index notation corresponds to a left-handed Weyl fermion with indices ψ\_a.

```lean
def rep : Representation ℂ SL(2,ℂ) DualLeftHandedWeyl
```

**`Fermion.DualLeftHandedWeyl.rep_apply`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L179).

```lean
lemma rep_apply (M : SL(2,ℂ)) (ψ : DualLeftHandedWeyl) : rep M ψ = ⟨(M.1⁻¹)ᵀ *ᵥ ψ.1⟩
```

**`Fermion.DualLeftHandedWeyl.rep_apply_eq_sum_basis`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L181).

```lean
lemma rep_apply_eq_sum_basis (M : SL(2,ℂ)) (ψ : DualLeftHandedWeyl) :
    rep M ψ = ∑ i, (∑ j, M.1⁻¹ j i * ψ.1 j) • basis i
```

**`Fermion.DualLeftHandedWeyl.rep_apply_basis`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L186).

```lean
lemma rep_apply_basis (M : SL(2,ℂ)) (i : Fin 2) :
    rep M (basis i) = ∑ j, M.1⁻¹ i j • basis j
```

**`Fermion.DualLeftHandedWeyl.rep_toMatrix`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L193).

```lean
lemma rep_toMatrix (M : SL(2,ℂ)) : (LinearMap.toMatrix basis basis) (rep M) = (M.1⁻¹)ᵀ
```

**`Fermion.DualLeftHandedWeyl.rep_apply_basis_repr`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L200).

```lean
lemma rep_apply_basis_repr (M : SL(2,ℂ)) (i j : Fin 2) :
    basis.repr (rep M (basis i)) j = M.1⁻¹ i j
```

### C.1. Irreducibility

**`Fermion.DualLeftHandedWeyl.eq_zero_of_rep_eq_smul`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L214).

> The representation `rep` has no common eigenvector.

```lean
lemma eq_zero_of_rep_eq_smul (ψ : DualLeftHandedWeyl)
    (h : ∀ M : SL(2,ℂ), ∃ c : ℂ, rep M ψ = c • ψ) : ψ = 0
```

**`Fermion.DualLeftHandedWeyl.eq_bot_or_eq_top_of_rep_mem`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L234).

> A submodule of `DualLeftHandedWeyl` stable under `rep` is either `⊥` or everything.

```lean
lemma eq_bot_or_eq_top_of_rep_mem (p : Submodule ℂ DualLeftHandedWeyl)
    (h : ∀ (M : SL(2,ℂ)) (ψ : DualLeftHandedWeyl), ψ ∈ p → rep M ψ ∈ p) :
    p = ⊥ ∨ p = ⊤
```

**An instance with no name**, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L248).

> The representation `rep` of `SL(2, ℂ)` is irreducible.

```lean
instance : rep.IsIrreducible
```

**`Fermion.DualLeftHandedWeyl.end_eq_smul_id_of_commute_rep`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean#L257).

> Schur's lemma for dual left-handed Weyl fermions.

```lean
lemma end_eq_smul_id_of_commute_rep {T : Module.End ℂ DualLeftHandedWeyl}
    (hT : ∀ M : SL(2,ℂ), T ∘ₗ rep M = rep M ∘ₗ T) : ∃ μ : ℂ, T = μ • LinearMap.id
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/DualLeftHanded.lean)
