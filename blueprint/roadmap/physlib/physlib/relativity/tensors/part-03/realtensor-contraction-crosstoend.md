---
declaration: module
origin: cited
lean: realLorentzTensor.crossToEnd_basis_repr_apply_eq_fin
statement: formalized
proof: formalized
---

# Components of real Lorentz cross contractions

The module `Physlib.Relativity.Tensors.RealTensor.Contraction.CrossToEnd`, [Physlib/Relativity/Tensors/RealTensor/Contraction/CrossToEnd.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Contraction/CrossToEnd.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This file gives the standard-basis component formula for `crossToEnd` on real Lorentz tensors.
> The contraction pairing of the standard covariant and contravariant bases reduces the generic
> component expansion to one finite sum.

## ii. Key results

> - `realLorentzTensor.crossToEnd_basis_repr_apply_eq_fin` expresses each component of a cross
>   contraction as a sum over the contracted Lorentz index.

## iv. References

> * None.

## A. Basis components

**`realLorentzTensor.crossToEnd_basis_repr_apply_eq_fin`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Contraction/CrossToEnd.lean#L49).

> For real Lorentz tensors, the component formula for `crossToEnd` collapses to one sum because
> the standard contravariant and covariant bases are dual under contraction.

```lean
lemma crossToEnd_basis_repr_apply_eq_fin {d nA nB : ℕ} {cA : Fin (nA + 1) → Color}
    {cB : Fin (nB + 1) → Color} (i : Fin (nA + 1)) (j : Fin (nB + 1))
    (hc : (realLorentzTensor d).τ (cA i) = cB j) (t : ℝT(d, cA)) (M : ℝT(d, cB))
    (φ : ComponentIdx (S := realLorentzTensor d)
      (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))) :
    (Tensor.basis _).repr (crossToEnd i j hc t M) φ =
      ∑ x : Fin 1 ⊕ Fin d,
        (Tensor.basis cA).repr t (i.insertNth x (fun m => φ (Fin.castAdd nB m))) *
          (Tensor.basis cB).repr M (j.insertNth x (fun m => φ (Fin.natAdd nA m)))
```

## Depends on

- [Physlib.Relativity.Tensors.RealTensor.Basic](realtensor-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Contraction/CrossToEnd.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Contraction/CrossToEnd.lean)
