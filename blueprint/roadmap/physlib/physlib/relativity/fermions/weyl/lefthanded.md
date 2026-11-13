---
declaration: module
origin: cited
lean: Fermion.LeftHandedWeyl, Fermion.LeftHandedWeyl.toFin2ℂFun, Fermion.LeftHandedWeyl.toFin2ℂAddEquiv, Fermion.LeftHandedWeyl.toFin2ℂEquiv, Fermion.LeftHandedWeyl.toFin2ℂ, Fermion.LeftHandedWeyl.toFin2ℂ_eq_val, Fermion.LeftHandedWeyl.basis, Fermion.LeftHandedWeyl.basis_apply
statement: formalized
proof: formalized
---

# Left handed Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.LeftHanded`, [Physlib/Relativity/Fermions/Weyl/LeftHanded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean): 26 declarations (6 instances with no name), 15 with a docstring.

> Left-handed Weyl fermions and the irreducible representation of `SL(2, ℂ)` they carry.

## i. Overview

> Left-handed Weyl fermions sit in the fundamental representation of `SL(2,ℂ)`,
> and we consider them to have up indices `ψ^α` with `α = 1,2`.
>
> In this file we define the type `LeftHandedWeyl`, equip it with the structure of a
> two-dimensional complex vector space with a standard basis, define the representation `rep` of
> `SL(2, ℂ)` on it by `M ↦ M`, and show that `rep` is irreducible (C.1).

## ii. Key results

> - `LeftHandedWeyl` : the type of left-handed Weyl fermions.
> - `LeftHandedWeyl.basis` : the standard basis, indexed by `Fin 2`.
> - `LeftHandedWeyl.rep` : the representation of `SL(2, ℂ)`.
> - `LeftHandedWeyl.eq_zero_of_rep_eq_smul` : `rep` has no common eigenvector.
> - `LeftHandedWeyl.end_eq_smul_id_of_commute_rep` : Schur's lemma for `rep`.

## iv. References

> * Dreiner, Haber and Martin, Two-component spinor techniques and Feynman rules for quantum
>   field theory and supersymmetry, Phys. Rept. 494 (2010) 1-196. [ref: Dreiner:2008tw]

## A. The definition of the type

**`Fermion.LeftHandedWeyl`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L62).

> The module in which left handed fermions live. This is equivalent to `Fin 2 → ℂ`.

```lean
structure LeftHandedWeyl where
  /-- The underlying value in `Fin 2 → ℂ`. -/
  val : Fin 2 → ℂ
```

### A.1. Underlying module structure

**`Fermion.LeftHandedWeyl.toFin2ℂFun`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L79).

> The equivalence between `LeftHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂFun : LeftHandedWeyl ≃ (Fin 2 → ℂ)
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L87).

> The instance of `AddCommMonoid` on `LeftHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommMonoid LeftHandedWeyl
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L91).

> The instance of `AddCommGroup` on `LeftHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : AddCommGroup LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.toFin2ℂAddEquiv`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L94).

> The additive equivalence between `LeftHandedWeyl` and `Fin 2 → ℂ`.

```lean
def toFin2ℂAddEquiv : LeftHandedWeyl ≃+ (Fin 2 → ℂ)
```

**An instance with no name**, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L99).

> The instance of `Module` on `LeftHandedWeyl` defined via its equivalence
> with `Fin 2 → ℂ`.

```lean
instance : Module ℂ LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.toFin2ℂEquiv`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L103).

> The linear equivalence between `LeftHandedWeyl` and `(Fin 2 → ℂ)`.

```lean
def toFin2ℂEquiv : LeftHandedWeyl ≃ₗ[ℂ] (Fin 2 → ℂ)
```

**`Fermion.LeftHandedWeyl.toFin2ℂ`**, an abbrev, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L113).

> The underlying element of `Fin 2 → ℂ` of a element in `LeftHandedWeyl` defined
> through the linear equivalence `toFin2ℂEquiv`.

```lean
abbrev toFin2ℂ (ψ : LeftHandedWeyl)
```

**`Fermion.LeftHandedWeyl.toFin2ℂ_eq_val`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L115).

```lean
lemma toFin2ℂ_eq_val (ψ : LeftHandedWeyl) : ψ.toFin2ℂ = ψ.val
```

**An instance with no name**, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L117).

```lean
instance : Nontrivial LeftHandedWeyl
```

## B. Basis

**`Fermion.LeftHandedWeyl.basis`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L126).

> The standard basis on left-handed Weyl fermions.

```lean
def basis : Basis (Fin 2) ℂ LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.basis_apply`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L129).

```lean
lemma basis_apply (i j : Fin 2) : (basis i).1 j = if j = i then 1 else 0
```

**`Fermion.LeftHandedWeyl.eq_sum_basis`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L136).

```lean
lemma eq_sum_basis (ψ : LeftHandedWeyl) : ψ = ∑ i, ψ.1 i • basis i
```

**`Fermion.LeftHandedWeyl.basis_val`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L140).

```lean
lemma basis_val (i : Fin 2) : (basis i).val = Pi.single i 1
```

**An instance with no name**, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L144).

```lean
instance : FiniteDimensional ℂ LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.finrank_eq_two`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L148).

> Left-handed Weyl fermions form a two-dimensional complex vector space.

```lean
lemma finrank_eq_two : Module.finrank ℂ LeftHandedWeyl = 2
```

## C. Representation

**`Fermion.LeftHandedWeyl.rep`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L159).

> The vector space ℂ^2 carrying the fundamental representation of SL(2,C).
> In index notation corresponds to a Weyl fermion with indices ψ^a.

```lean
def rep : Representation ℂ SL(2,ℂ) LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.rep_apply`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L178).

```lean
lemma rep_apply (M : SL(2,ℂ)) (ψ : LeftHandedWeyl) : rep M ψ = ⟨M.1 *ᵥ ψ.1⟩
```

**`Fermion.LeftHandedWeyl.rep_apply_eq_sum_basis`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L180).

```lean
lemma rep_apply_eq_sum_basis (M : SL(2,ℂ)) (ψ : LeftHandedWeyl) :
    rep M ψ = ∑ i, (∑ j, M.1 i j * ψ.1 j) • basis i
```

**`Fermion.LeftHandedWeyl.rep_apply_basis`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L185).

```lean
lemma rep_apply_basis (M : SL(2,ℂ)) (i : Fin 2) :
    rep M (basis i) = ∑ j, M.1 j i • basis j
```

**`Fermion.LeftHandedWeyl.rep_toMatrix`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L192).

```lean
lemma rep_toMatrix (M : SL(2,ℂ)) : (LinearMap.toMatrix basis basis) (rep M) = M.1
```

**`Fermion.LeftHandedWeyl.rep_apply_basis_repr`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L199).

```lean
lemma rep_apply_basis_repr (M : SL(2,ℂ)) (i j : Fin 2) :
    basis.repr (rep M (basis i)) j = M.1 j i
```

### C.1. Irreducibility

**`Fermion.LeftHandedWeyl.eq_zero_of_rep_eq_smul`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L210).

> The representation `rep` has no common eigenvector.

```lean
lemma eq_zero_of_rep_eq_smul (ψ : LeftHandedWeyl)
    (h : ∀ M : SL(2,ℂ), ∃ c : ℂ, rep M ψ = c • ψ) : ψ = 0
```

**`Fermion.LeftHandedWeyl.eq_bot_or_eq_top_of_rep_mem`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L229).

> A submodule of `LeftHandedWeyl` stable under `rep` is either `⊥` or everything.

```lean
lemma eq_bot_or_eq_top_of_rep_mem (p : Submodule ℂ LeftHandedWeyl)
    (h : ∀ (M : SL(2,ℂ)) (ψ : LeftHandedWeyl), ψ ∈ p → rep M ψ ∈ p) :
    p = ⊥ ∨ p = ⊤
```

**An instance with no name**, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L243).

> The representation `rep` of `SL(2, ℂ)` is irreducible.

```lean
instance : rep.IsIrreducible
```

**`Fermion.LeftHandedWeyl.end_eq_smul_id_of_commute_rep`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean#L252).

> Schur's lemma for left-handed Weyl fermions.

```lean
lemma end_eq_smul_id_of_commute_rep {T : Module.End ℂ LeftHandedWeyl}
    (hT : ∀ M : SL(2,ℂ), T ∘ₗ rep M = rep M ∘ₗ T) : ∃ μ : ℂ, T = μ • LinearMap.id
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Fermions/Weyl/LeftHanded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/LeftHanded.lean)
