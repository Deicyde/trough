---
declaration: module
origin: cited
lean: complexLorentzTensor.ofGaussianInt, complexLorentzTensor.ofGaussianInt_basis_repr_apply, complexLorentzTensor.basis_eq_ofGaussianInt, complexLorentzTensor.contr_basis_gaussianInt, complexLorentzTensor.prodT_ofGaussianInt_ofGaussianInt, complexLorentzTensor.contrT_ofGaussianInt_eq_sum_dropPairSection, complexLorentzTensor.contrT_ofGaussianInt, complexLorentzTensor.permT_ofGaussianInt
statement: formalized
proof: formalized
---

# Complex Lorentz tensors with Gaussian integer components

The module `Physlib.Relativity.Tensors.ComplexTensor.OfGaussianInt`, [Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean): 8 declarations, 1 with a docstring.

> A complex Lorentz tensor whose components in the standard basis are Gaussian integers can be
> written as `ofGaussianInt f` for a map `f` from component indices to `GaussianInt`. The
> product, contraction and permutation of such tensors are again of this form, so identities
> between them reduce to decidable equalities of Gaussian integers.

**`complexLorentzTensor.ofGaussianInt`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L35).

> A complex Lorentz tensor from a map
> `(Π j, complexLorentzTensor.basisIdx (c j)) → GaussianInt`. All complex Lorentz tensors
> with Gaussian integer coefficients with respect to the basis are of this form.

```lean
noncomputable def ofGaussianInt {n : ℕ} {c : Fin n → complexLorentzTensor.Color} :
    ((ComponentIdx (S := complexLorentzTensor) c) → GaussianInt) →ₛₗ[GaussianInt.toComplex]
      ℂT(c)
```

**`complexLorentzTensor.ofGaussianInt_basis_repr_apply`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L51).

```lean
lemma ofGaussianInt_basis_repr_apply {n : ℕ} {c : Fin n → complexLorentzTensor.Color}
    (f : (ComponentIdx c) → GaussianInt)
    (b :(ComponentIdx c)) :
  (Tensor.basis c).repr (ofGaussianInt f) b = GaussianInt.toComplex (f b)
```

**`complexLorentzTensor.basis_eq_ofGaussianInt`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L58).

```lean
lemma basis_eq_ofGaussianInt {n : ℕ} {c : Fin n → complexLorentzTensor.Color}
    (b : (ComponentIdx c)) :
    Tensor.basis c b
    = ofGaussianInt (fun b' => if b = b' then 1 else 0)
```

**`complexLorentzTensor.contr_basis_gaussianInt`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L67).

```lean
lemma contr_basis_gaussianInt {c : complexLorentzTensor.Color}
    (i : complexLorentzTensor.basisIdx c)
    (j : complexLorentzTensor.basisIdx (complexLorentzTensor.τ c)) :
      ((complexLorentzTensor.contr c)
      (complexLorentzTensor.basis c i ⊗ₜ
      complexLorentzTensor.basis (complexLorentzTensor.τ c) j))
      = GaussianInt.toComplex (if i = basisIdxTauEquiv c j then 1 else 0)
```

**`complexLorentzTensor.prodT_ofGaussianInt_ofGaussianInt`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L81).

```lean
lemma prodT_ofGaussianInt_ofGaussianInt {n n1 : ℕ} {c : Fin n → complexLorentzTensor.Color}
    (f : (ComponentIdx c) → GaussianInt)
    {c1 : Fin n1 → complexLorentzTensor.Color}
    (f1 : (ComponentIdx c1) → GaussianInt) :
    (prodT (ofGaussianInt f) (ofGaussianInt f1)) =
    ((ofGaussianInt (fun b => f (ComponentIdx.prod b).1 *
      f1 (ComponentIdx.prod b).2)))
```

**`complexLorentzTensor.contrT_ofGaussianInt_eq_sum_dropPairSection`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L93).

```lean
lemma contrT_ofGaussianInt_eq_sum_dropPairSection {n : ℕ}
    {c : Fin (n + 1 + 1) → complexLorentzTensor.Color}
    {i j : Fin (n + 1 + 1)} {h : i ≠ j ∧ complexLorentzTensor.τ (c i) = c j }
    (f : (ComponentIdx c) → GaussianInt) :
  (contrT n i j h (ofGaussianInt f)) = ((ofGaussianInt (fun b =>
    (∑ x : ComponentIdx.DropPairSection b,
      f x.1 * if x.1 i = basisIdxTauEquiv (c i) (basisIdxCongr h.2.symm (x.1 j))
        then 1 else 0))))
```

**`complexLorentzTensor.contrT_ofGaussianInt`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L115).

```lean
lemma contrT_ofGaussianInt {n : ℕ} {c : Fin (n + 1 + 1) → complexLorentzTensor.Color}
    {i j : Fin (n + 1 + 1)} {h : i ≠ j ∧ complexLorentzTensor.τ (c i) = c j }
    (f : (ComponentIdx c) → GaussianInt) :
  (contrT n i j h (ofGaussianInt f)) = ((ofGaussianInt (fun b =>
    (∑ x : complexLorentzTensor.basisIdx (c i),
      f (DropPairSection.ofFinEquiv h.1 b
        (x, basisIdxCongr h.2 ((basisIdxTauEquiv (c i)).symm x)))))))
```

**`complexLorentzTensor.permT_ofGaussianInt`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean#L141).

```lean
lemma permT_ofGaussianInt {n m : ℕ} {c : Fin n → complexLorentzTensor.Color}
    {c1 : Fin m → complexLorentzTensor.Color}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ)
    (f : ComponentIdx c → GaussianInt) :
    (permT σ h ((ofGaussianInt f))) =
    ((ofGaussianInt (fun b => f (fun i => basisIdxCongr
      (IsReindexing.inv_perserve_color h i) (b (h.inv σ i))))))
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](complextensor-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/OfGaussianInt.lean)
