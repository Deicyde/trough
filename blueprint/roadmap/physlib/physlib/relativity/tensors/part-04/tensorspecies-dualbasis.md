---
declaration: module
origin: cited
lean: TensorSpecies.IsContrDualMatching, TensorSpecies.IsContrDualMatching.unique, TensorSpecies.HasContrDualBases, TensorSpecies.HasContrDualBases.contrDualIdxEquiv, TensorSpecies.HasContrDualBases.contr_basis_eq_ite, TensorSpecies.HasContrDualBases.contrDualIdxEquiv_eq_of_isContrDualMatching, TensorSpecies.HasContrDualBases.dualIdxEquiv, TensorSpecies.HasContrDualBases.dualIdxEquiv_apply
statement: formalized
proof: formalized
---

# Species whose bases at dual colors are dual bases

The module `Physlib.Relativity.Tensors.TensorSpecies.DualBasis`, [Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean): 11 declarations, 10 with a docstring.

## i. Overview

> This file defines `HasContrDualBases`: species whose basis at `S.τ c` is dual to the basis at `c`
> under the pairing `S.contr c`.
>
> A matching `e : basisIdx (S.τ c) ≃ basisIdx c` satisfies the δ law (`IsContrDualMatching`) if
> `S.contr c (b c x₁ ⊗ₜ b (S.τ c) x₂) = if x₁ = e x₂ then 1 else 0`. The class asks for one such
> matching at every color, so the label types need only be in bijection.
>
> Over a nontrivial ring the matching is unique (`IsContrDualMatching.unique`). Hence
> `contrDualIdxEquiv`, although picked by choice, is the only matching, so nothing depends on the
> choice. A concrete species identifies it through `contrDualIdxEquiv_eq_of_isContrDualMatching`,
> and the double-dual law `contrDualIdxEquiv_tau` is a theorem.
>
> The contraction functionals are the dual basis of `b c` (`contr_tmul_basis_eq_dualBasis`).
> Contracted basis vectors have δ coefficients (`Pure.contrPCoeff_basisVector`), and components of a
> contraction are single sums (`contrT_basis_repr_apply_eq_sum_dual`).

## ii. Key results

> - `TensorSpecies.IsContrDualMatching.unique` : the δ law determines the matching.
> - `TensorSpecies.HasContrDualBases` : the class.
> - `TensorSpecies.HasContrDualBases.contrDualIdxEquiv` : the matching of the labels at `S.τ c`
>     with those at `c`.
> - `TensorSpecies.HasContrDualBases.contr_basis_eq_ite` : the δ law for `contrDualIdxEquiv`.
> - `TensorSpecies.HasContrDualBases.contrDualIdxEquiv_eq_of_isContrDualMatching` : any matching
>     satisfying the δ law is `contrDualIdxEquiv`.
> - `TensorSpecies.HasContrDualBases.dualIdxEquiv` : the equivalence between labels of dual
>     indices.
> - `TensorSpecies.HasContrDualBases.contrDualIdxEquiv_tau` : the matching at `S.τ c` is the
>     inverse of the one at `c`, through `S.τ (S.τ c) = c`.
> - `TensorSpecies.HasContrDualBases.dualIdxEquiv_symm` : the inverse of `dualIdxEquiv` from `c1`
>     to `c2` is `dualIdxEquiv` from `c2` to `c1`.
> - `TensorSpecies.HasContrDualBases.contr_tmul_basis_eq_dualBasis` : contracting with a basis vector
>     at `S.τ c` is an element of `Module.Basis.dualBasis`.

## iv. References

> There are no known references for the material in this module.

## A. Matchings satisfying the δ law

**`TensorSpecies.IsContrDualMatching`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L84).

> A matching `e` of the basis labels at `S.τ c` with those at `c` satisfies the δ law:
> contracting a basis vector at `c` with one at `S.τ c` gives `1` if `e` matches their labels and
> `0` otherwise.

```lean
def IsContrDualMatching (S : TensorSpecies k C G V basisIdx rep b) (c : C)
    (e : basisIdx (S.τ c) ≃ basisIdx c) : Prop
```

**`TensorSpecies.IsContrDualMatching.unique`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L90).

> Over a nontrivial ring the δ law determines the matching: the label matched with `x₂` is the
> one whose basis vector pairs with `b (S.τ c) x₂` to `1`.

```lean
lemma IsContrDualMatching.unique [Nontrivial k] {S : TensorSpecies k C G V basisIdx rep b}
    {c : C} {e e' : basisIdx (S.τ c) ≃ basisIdx c}
    (he : IsContrDualMatching S c e) (he' : IsContrDualMatching S c e') : e = e'
```

## B. The class

**`TensorSpecies.HasContrDualBases`**, a class, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L106).

> A tensor species whose basis at `S.τ c` is dual to its basis at `c` under the pairing
> `S.contr c`: for every color some matching of the labels satisfies the δ law.

```lean
class HasContrDualBases (S : TensorSpecies k C G V basisIdx rep b) : Prop where
  /-- At every color, some matching of the labels at `S.τ c` with those at `c` satisfies the δ
    law. -/
  exists_matching : ∀ c, ∃ e, IsContrDualMatching S c e
```

## C. The matching

**`TensorSpecies.HasContrDualBases.contrDualIdxEquiv`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L125).

> A matching of the basis labels at `S.τ c` with those at `c` satisfying the δ law, chosen by
> `Classical.choose`. Over a nontrivial ring it is the only one
> (`contrDualIdxEquiv_eq_of_isContrDualMatching`).

```lean
noncomputable def contrDualIdxEquiv (c : C) : basisIdx (S.τ c) ≃ basisIdx c
```

**`TensorSpecies.HasContrDualBases.contr_basis_eq_ite`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L129).

> The δ law for `contrDualIdxEquiv`.

```lean
lemma contr_basis_eq_ite (c : C) (x₁ : basisIdx c) (x₂ : basisIdx (S.τ c)) :
    S.contr c (b c x₁ ⊗ₜ[k] b (S.τ c) x₂) =
      if x₁ = contrDualIdxEquiv S c x₂ then 1 else 0
```

**`TensorSpecies.HasContrDualBases.contrDualIdxEquiv_eq_of_isContrDualMatching`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L136).

> Any matching satisfying the δ law is `contrDualIdxEquiv`. This is how a concrete species
> identifies its matching.

```lean
lemma contrDualIdxEquiv_eq_of_isContrDualMatching [Nontrivial k] {c : C}
    {e : basisIdx (S.τ c) ≃ basisIdx c} (he : IsContrDualMatching S c e) :
    contrDualIdxEquiv S c = e
```

**`TensorSpecies.HasContrDualBases.dualIdxEquiv`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L143).

> The equivalence between labels of dual indices: a label at `c1` carried across the variance
> dual by `contrDualIdxEquiv`, then along `h`.

```lean
noncomputable def dualIdxEquiv {c1 c2 : C} (h : S.τ c1 = c2) : basisIdx c1 ≃ basisIdx c2
```

**`TensorSpecies.HasContrDualBases.dualIdxEquiv_apply`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L147).

```lean
lemma dualIdxEquiv_apply {c1 c2 : C} (h : S.τ c1 = c2) (x : basisIdx c1) :
    dualIdxEquiv h x = basisIdxCongr h ((contrDualIdxEquiv S c1).symm x)
```

## D. The double dual

**`TensorSpecies.HasContrDualBases.contrDualIdxEquiv_tau`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L159).

> The matching at `S.τ c` is the inverse of the one at `c`, once `S.τ (S.τ c)` is identified
> with `c` by `S.τ_τ_apply`. The inverse matching satisfies the δ law at `S.τ c` by
> `contr_tmul_symm`, so uniqueness identifies the two.

```lean
lemma contrDualIdxEquiv_tau [Nontrivial k] (c : C) (x : basisIdx (S.τ (S.τ c))) :
    contrDualIdxEquiv S (S.τ c) x =
      (contrDualIdxEquiv S c).symm (basisIdxCongr (S.τ_τ_apply c) x)
```

**`TensorSpecies.HasContrDualBases.dualIdxEquiv_symm`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L174).

> The inverse of `dualIdxEquiv` from `c1` to `c2` is `dualIdxEquiv` from `c2` to `c1`.

```lean
lemma dualIdxEquiv_symm [Nontrivial k] {c1 c2 : C} (h : S.τ c1 = c2) (h' : S.τ c2 = c1) :
    (dualIdxEquiv h).symm = dualIdxEquiv h'
```

## E. The dual basis

**`TensorSpecies.HasContrDualBases.contr_tmul_basis_eq_dualBasis`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean#L189).

> The functional `v ↦ S.contr c (v ⊗ₜ b (S.τ c) x)` is the element of `(b c).dualBasis` at the
> label matched with `x`.

```lean
lemma contr_tmul_basis_eq_dualBasis (c : C) (x : basisIdx (S.τ c)) (v : V c) :
    S.contr c (v ⊗ₜ[k] b (S.τ c) x) = (b c).dualBasis (contrDualIdxEquiv S c x) v
```

## Depends on

- [Tensor species (Basic)](tensorspecies-basic.md)

## Sources

- [Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/DualBasis.lean)
