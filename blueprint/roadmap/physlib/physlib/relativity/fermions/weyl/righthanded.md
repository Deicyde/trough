---
declaration: module
origin: cited
lean: Fermion.RightHandedWeyl, Fermion.RightHandedWeyl.toFin2ℂFun, Fermion.RightHandedWeyl.toFin2ℂAddEquiv, Fermion.RightHandedWeyl.toFin2ℂEquiv, Fermion.RightHandedWeyl.toFin2ℂ, Fermion.RightHandedWeyl.toFin2ℂ_eq_val, Fermion.RightHandedWeyl.basis, Fermion.RightHandedWeyl.basis_apply
statement: formalized
proof: formalized
---

# Right handed Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.RightHanded`, [Physlib/Relativity/Fermions/Weyl/RightHanded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean): 26 declarations (6 instances with no name), 15 with a docstring.

> Right-handed Weyl fermions and the irreducible representation of `SL(2, ℂ)` they carry.

## i. Overview

> Right-handed Weyl fermions sit in the conjugate representation of `SL(2,ℂ)`,
> and we consider them to have up indices `ψ^{dot α}` with `α = 1,2`.
>
> In this file we define the type `RightHandedWeyl`, equip it with the structure of a
> two-dimensional complex vector space with a standard basis, define the representation `rep` of
> `SL(2, ℂ)` on it by `M ↦ M̅`, and show that `rep` is irreducible (C.1).

## ii. Key results

> - `RightHandedWeyl` : the type of right-handed Weyl fermions.
> - `RightHandedWeyl.basis` : the standard basis, indexed by `Fin 2`.
> - `RightHandedWeyl.rep` : the representation of `SL(2, ℂ)`.
> - `RightHandedWeyl.eq_zero_of_rep_eq_smul` : `rep` has no common eigenvector.
> - `RightHandedWeyl.end_eq_smul_id_of_commute_rep` : Schur's lemma for `rep`.

## iv. References

> * Dreiner, Haber and Martin, Two-component spinor techniques and Feynman rules for quantum
>   field theory and supersymmetry, Phys. Rept. 494 (2010) 1-196. [ref: Dreiner:2008tw]

## A. The definition of the type

**`Fermion.RightHandedWeyl`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L60).

> The module in which right handed fermions live. This is equivalent to `Fin 2 → ℂ`.

```lean
structure RightHandedWeyl where
  /-- The underlying value in `Fin 2 → ℂ`. -/
  val : Fin 2 → ℂ
```

### A.1. Underlying module structure

**`Fermion.RightHandedWeyl.toFin2ℂFun`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L77).

> The equivalence between `RightHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂFun : RightHandedWeyl ≃ (Fin 2 → ℂ)
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L85).

> The instance of `AddCommMonoid` on `RightHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommMonoid RightHandedWeyl
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L89).

> The instance of `AddCommGroup` on `RightHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommGroup RightHandedWeyl
```

**`Fermion.RightHandedWeyl.toFin2ℂAddEquiv`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L92).

> The additive equivalence between `RightHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂAddEquiv : RightHandedWeyl ≃+ (Fin 2 → ℂ)
```

**An instance with no name**, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L97).

> The instance of `Module` on `RightHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : Module ℂ RightHandedWeyl
```

**`Fermion.RightHandedWeyl.toFin2ℂEquiv`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L101).

> The linear equivalence between `RightHandedWeyl` and `(Fin 2 → ℂ)`.

```lean
def toFin2ℂEquiv : RightHandedWeyl ≃ₗ[ℂ] (Fin 2 → ℂ)
```

**`Fermion.RightHandedWeyl.toFin2ℂ`**, an abbrev, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L111).

> The underlying element of `Fin 2 → ℂ` of a element in `RightHandedWeyl` defined
> through the linear equivalence `toFin2ℂEquiv`.

```lean
abbrev toFin2ℂ (ψ : RightHandedWeyl)
```

**`Fermion.RightHandedWeyl.toFin2ℂ_eq_val`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L113).

```lean
lemma toFin2ℂ_eq_val (ψ : RightHandedWeyl) : ψ.toFin2ℂ = ψ.val
```

**An instance with no name**, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L115).

```lean
instance : Nontrivial RightHandedWeyl
```

## B. Basis

**`Fermion.RightHandedWeyl.basis`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L124).

> The standard basis on right-handed Weyl fermions.

```lean
def basis : Basis (Fin 2) ℂ RightHandedWeyl
```

**`Fermion.RightHandedWeyl.basis_apply`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L127).

```lean
lemma basis_apply (i j : Fin 2) : (basis i).1 j = if j = i then 1 else 0
```

**`Fermion.RightHandedWeyl.eq_sum_basis`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L134).

```lean
lemma eq_sum_basis (ψ : RightHandedWeyl) : ψ = ∑ i, ψ.1 i • basis i
```

**`Fermion.RightHandedWeyl.basis_val`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L138).

```lean
lemma basis_val (i : Fin 2) : (basis i).val = Pi.single i 1
```

**An instance with no name**, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L142).

```lean
instance : FiniteDimensional ℂ RightHandedWeyl
```

**`Fermion.RightHandedWeyl.finrank_eq_two`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L146).

> Right-handed Weyl fermions form a two-dimensional complex vector space.

```lean
lemma finrank_eq_two : Module.finrank ℂ RightHandedWeyl = 2
```

## C. Representation

**`Fermion.RightHandedWeyl.rep`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L157).

> The vector space ℂ^2 carrying the conjugate representation of SL(2,C).
> In index notation corresponds to a Weyl fermion with indices ψ^\{dot a}.

```lean
def rep : Representation ℂ SL(2,ℂ) RightHandedWeyl
```

**`Fermion.RightHandedWeyl.rep_apply`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L175).

```lean
lemma rep_apply (M : SL(2,ℂ)) (ψ : RightHandedWeyl) : rep M ψ = ⟨M.1.map star *ᵥ ψ.1⟩
```

**`Fermion.RightHandedWeyl.rep_apply_eq_sum_basis`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L177).

```lean
lemma rep_apply_eq_sum_basis (M : SL(2,ℂ)) (ψ : RightHandedWeyl) :
    rep M ψ = ∑ i, (∑ j, M.1.map star i j * ψ.1 j) • basis i
```

**`Fermion.RightHandedWeyl.rep_apply_basis`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L182).

```lean
lemma rep_apply_basis (M : SL(2,ℂ)) (i : Fin 2) :
    rep M (basis i) = ∑ j, M.1.map star j i • basis j
```

**`Fermion.RightHandedWeyl.rep_toMatrix`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L189).

```lean
lemma rep_toMatrix (M : SL(2,ℂ)) : (LinearMap.toMatrix basis basis) (rep M) = M.1.map star
```

**`Fermion.RightHandedWeyl.rep_apply_basis_repr`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L196).

```lean
lemma rep_apply_basis_repr (M : SL(2,ℂ)) (i j : Fin 2) :
    basis.repr (rep M (basis i)) j = star (M.1 j i)
```

### C.1. Irreducibility

**`Fermion.RightHandedWeyl.eq_zero_of_rep_eq_smul`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L207).

> The representation `rep` has no common eigenvector.

```lean
lemma eq_zero_of_rep_eq_smul (ψ : RightHandedWeyl)
    (h : ∀ M : SL(2,ℂ), ∃ c : ℂ, rep M ψ = c • ψ) : ψ = 0
```

**`Fermion.RightHandedWeyl.eq_bot_or_eq_top_of_rep_mem`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L226).

> A submodule of `RightHandedWeyl` stable under `rep` is either `⊥` or everything.

```lean
lemma eq_bot_or_eq_top_of_rep_mem (p : Submodule ℂ RightHandedWeyl)
    (h : ∀ (M : SL(2,ℂ)) (ψ : RightHandedWeyl), ψ ∈ p → rep M ψ ∈ p) :
    p = ⊥ ∨ p = ⊤
```

**An instance with no name**, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L240).

> The representation `rep` of `SL(2, ℂ)` is irreducible.

```lean
instance : rep.IsIrreducible
```

**`Fermion.RightHandedWeyl.end_eq_smul_id_of_commute_rep`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean#L249).

> Schur's lemma for right-handed Weyl fermions.

```lean
lemma end_eq_smul_id_of_commute_rep {T : Module.End ℂ RightHandedWeyl}
    (hT : ∀ M : SL(2,ℂ), T ∘ₗ rep M = rep M ∘ₗ T) : ∃ μ : ℂ, T = μ • LinearMap.id
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Fermions/Weyl/RightHanded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/RightHanded.lean)
