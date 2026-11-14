---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.Pure.dropPair_basisVector, TensorSpecies.Tensor.Pure.contrPCoeff_basisVector, TensorSpecies.Tensor.contrT_basis_repr_apply, TensorSpecies.Tensor.contrT_basis_repr_apply_eq_sum_fin, TensorSpecies.Tensor.contrT_basis_repr_apply_eq_sum_dual, TensorSpecies.Tensor.contrT_basis
statement: formalized
proof: formalized
---

# Contractions on basis tensors

The module `Physlib.Relativity.Tensors.Contraction.Basis`, [Physlib/Relativity/Tensors/Contraction/Basis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean): 6 declarations, 2 with a docstring.

**`TensorSpecies.Tensor.Pure.dropPair_basisVector`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean#L33).

```lean
lemma Pure.dropPair_basisVector {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx c) :
    Pure.dropPair i j hij (basisVector c b) =
    basisVector (S := S) (c ∘ Fin.succSuccAbove i j) fun m => b (Fin.succSuccAbove i j m)
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_basisVector`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean#L43).

> For a species with dual bases (`HasContrDualBases`), the contraction coefficient of a basis
> vector is the Kronecker δ of its labels at `i` and `j`, the label at `j` read as a label at the
> color `c i`. The per-species `contrPCoeff_basis` lemmas follow from it.

```lean
lemma Pure.contrPCoeff_basisVector [HasContrDualBases S] {n : ℕ} {c : Fin n → C} (i j : Fin n)
    (hij : i ≠ j ∧ S.τ (c i) = c j) (φ : ComponentIdx (S := S) c) :
    Pure.contrPCoeff i j hij (Pure.basisVector c φ) =
      if φ i = HasContrDualBases.contrDualIdxEquiv S (c i) (basisIdxCongr hij.2.symm (φ j)) then 1
      else 0
```

**`TensorSpecies.Tensor.contrT_basis_repr_apply`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean#L53).

```lean
lemma contrT_basis_repr_apply {n : ℕ} {c : Fin (n + 1 + 1) → C} {i j : Fin (n + 1 + 1)}
    (h : i ≠ j ∧ S.τ (c i) = c j) (t : Tensor S c)
    (φ : ComponentIdx (c ∘ Fin.succSuccAbove i j)) :
    (basis (c ∘ Fin.succSuccAbove i j)).repr (contrT n i j h t) φ =
    ∑ (b' : DropPairSection φ), (basis c).repr t b'.1 *
      (S.contr (c i) (b (c i) (b'.1 i) ⊗ₜ[k] b (S.τ (c i))
      (basisIdxCongr (by rw [h.2]) (b'.1 j))))
```

**`TensorSpecies.Tensor.contrT_basis_repr_apply_eq_sum_fin`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean#L91).

```lean
lemma contrT_basis_repr_apply_eq_sum_fin {n : ℕ} {c : Fin (n + 1 + 1) → C} {i j : Fin (n + 1 + 1)}
    (h : i ≠ j ∧ S.τ (c i) = c j) (t : Tensor S c)
    (φ : ComponentIdx (c ∘ Fin.succSuccAbove i j)) :
    (basis (c ∘ Fin.succSuccAbove i j)).repr (contrT n i j h t) φ =
    ∑ (x1 : basisIdx (c i)), ∑ (x2 : basisIdx (c j)),
    (basis c).repr t (DropPairSection.ofFinEquiv h.1 φ (x1, x2)).1 *
    ((S.contr (c i))
    (b (c i) x1 ⊗ₜ[k] b (S.τ (c i)) (basisIdxCongr (by rw [h.2]) x2)))
```

**`TensorSpecies.Tensor.contrT_basis_repr_apply_eq_sum_dual`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean#L107).

> For a species with dual bases (`HasContrDualBases`), a component of a contraction is a single
> sum over the labels at the first contracted index: the δ law
> (`HasContrDualBases.contr_basis_eq_ite`) fixes the label at the second. This collapses the double
> sum of `contrT_basis_repr_apply_eq_sum_fin`.

```lean
lemma contrT_basis_repr_apply_eq_sum_dual [HasContrDualBases S] {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (h : i ≠ j ∧ S.τ (c i) = c j) (t : Tensor S c)
    (φ : ComponentIdx (c ∘ Fin.succSuccAbove i j)) :
    (basis (c ∘ Fin.succSuccAbove i j)).repr (contrT n i j h t) φ =
    ∑ x : basisIdx (c i), (basis c).repr t
      (DropPairSection.ofFinEquiv h.1 φ
        (x, basisIdxCongr h.2 ((HasContrDualBases.contrDualIdxEquiv S (c i)).symm x))).1
```

**`TensorSpecies.Tensor.contrT_basis`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean#L118).

```lean
lemma contrT_basis {n : ℕ} {c : Fin (n + 1 + 1) → C} {i j : Fin (n + 1 + 1)}
    (h : i ≠ j ∧ S.τ (c i) = c j) (b : ComponentIdx (S := S) c) :
    contrT n i j h (basis c b) =
    Pure.contrPCoeff i j h (Pure.basisVector c b) •
      basis (c ∘ Fin.succSuccAbove i j) (b.dropPair i j)
```

## Depends on

- [Contractions of component indices](componentidx-contraction.md)
- [Contractions on tensors](contraction-basic.md)
- [Species whose bases at dual colors are dual bases](../part-04/tensorspecies-dualbasis.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/Basis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basis.lean)
