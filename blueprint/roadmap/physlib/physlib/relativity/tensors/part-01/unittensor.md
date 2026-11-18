---
declaration: module
origin: cited
lean: TensorSpecies.unitTensor, TensorSpecies.unitTensor_basis_repr, TensorSpecies.unitTensor_congr, TensorSpecies.unitTensor_eq_permT_dual, TensorSpecies.dual_unitTensor_eq_permT_unitTensor, TensorSpecies.unit_fromSingleTContrFromPairT_eq_fromSingleT, TensorSpecies.contrT_single_unitTensor, TensorSpecies.contrT_unitTensor_dual_single
statement: formalized
proof: formalized
---

# The unit tensors

The module `Physlib.Relativity.Tensors.UnitTensor`, [Physlib/Relativity/Tensors/UnitTensor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean): 15 declarations, 10 with a docstring.

**`TensorSpecies.unitTensor`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L31).

> The unit tensor associated with a color `c`.

```lean
noncomputable def unitTensor (c : C) : S.Tensor ![S.τ c, c]
```

**`TensorSpecies.unitTensor_basis_repr`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L36).

> A component of the unit tensor is the corresponding component of the unit intertwiner in the
> tensor-product basis.

```lean
lemma unitTensor_basis_repr (c : C) (φ : ComponentIdx (S := S) ![S.τ c, c]) :
    (Tensor.basis _).repr (unitTensor (S := S) c) φ =
      (Module.Basis.tensorProduct (b (S.τ c)) (b c)).repr ((S.unit c) (1 : k))
        (φ 0, φ 1)
```

**`TensorSpecies.unitTensor_congr`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L42).

```lean
lemma unitTensor_congr {c c1 : C} (h : c = c1) :
    unitTensor c = permT id (by simp [h]) (unitTensor (S := S) c1)
```

**`TensorSpecies.unitTensor_eq_permT_dual`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L49).

> The unit tensor is symmetric on dualing the color.

```lean
lemma unitTensor_eq_permT_dual (c : C) :
    S.unitTensor c = permT ![1, 0] (And.intro (by decide) (fun i => by fin_cases i <;> simp))
    (unitTensor (S.τ c))
```

**`TensorSpecies.dual_unitTensor_eq_permT_unitTensor`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L76).

```lean
lemma dual_unitTensor_eq_permT_unitTensor (c : C) :
    S.unitTensor (S.τ c) = permT ![1, 0] (And.intro (by decide) (fun i => by fin_cases i <;> simp))
      (unitTensor c)
```

**`TensorSpecies.unit_fromSingleTContrFromPairT_eq_fromSingleT`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L83).

```lean
lemma unit_fromSingleTContrFromPairT_eq_fromSingleT {c : C} (x : V c) :
    fromSingleTContrFromPairT x ((S.unit c) (1 : k)) =
    fromSingleT x
```

**`TensorSpecies.contrT_single_unitTensor`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L91).

> This lemma represents the de-categorification of `S.contr_unit`.

```lean
lemma contrT_single_unitTensor {c : C} (x : Tensor S ![c]) :
    contrT 1 0 1 (by simp; rfl) (prodT x (unitTensor c)) =
    permT id (by simp; rfl) x
```

**`TensorSpecies.contrT_unitTensor_dual_single`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L100).

```lean
lemma contrT_unitTensor_dual_single {c : C} (x : Tensor S ![S.τ c]) :
    contrT 1 1 2 (by simp; rfl) (prodT (unitTensor c) x) =
    permT id (by simp; rfl) x
```

**`TensorSpecies.unitTensor_invariant`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L124).

```lean
lemma unitTensor_invariant {c : C} (g : G) :
    g • S.unitTensor c = S.unitTensor c
```

**`TensorSpecies.unitTensor_pair_basis_repr`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L130).

> For a species with dual bases at dual colours, the unit tensor's components are a Kronecker δ,
> the first label carried across the variance dual by `contrDualIdxEquiv`.

```lean
lemma unitTensor_pair_basis_repr [HasContrDualBases S] (c : C) (J y : basisIdx c) :
    (basis ![S.τ c, c]).repr (unitTensor c)
        (ComponentIdx.pair.symm ((HasContrDualBases.contrDualIdxEquiv S c).symm J, y)) =
      if J = y then 1 else 0
```

**`TensorSpecies.unitTensor_basis_repr_eq_ite`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L159).

> `unitTensor_pair_basis_repr` at an arbitrary component index.

```lean
lemma unitTensor_basis_repr_eq_ite [HasContrDualBases S] (c : C)
    (φ : ComponentIdx (S := S) ![S.τ c, c]) :
    (basis ![S.τ c, c]).repr (unitTensor c) φ =
      if HasContrDualBases.contrDualIdxEquiv S c (φ 0) = φ 1 then 1 else 0
```

**`TensorSpecies.Tensor.toMatrix_permT_unitTensor`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L175).

> The component matrix of a unit tensor recoloured without moving its slots is the identity, with
> the labels transported back to the unit tensor's colours.

```lean
lemma toMatrix_permT_unitTensor [HasContrDualBases S] (c : C) {cs : Fin 2 → C}
    {σ : Fin 2 → Fin 2} (hσ : ∀ i, σ i = i) (hperm : IsReindexing ![S.τ c, c] cs σ) :
    toMatrix (permT σ hperm (unitTensor (S := S) c)) =
      (1 : Matrix (basisIdx c) (basisIdx c) k).submatrix
        (fun x => HasContrDualBases.contrDualIdxEquiv S c
          (basisIdxCongr (by rw [← hperm.2 0, hσ]; rfl) x))
        (fun y => basisIdxCongr (by rw [← hperm.2 1, hσ]; rfl) y)
```

**`TensorSpecies.Tensor.toMatrix_unitTensor`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L189).

> The unit tensor's component matrix is the identity, carried along `contrDualIdxEquiv`.

```lean
lemma toMatrix_unitTensor [HasContrDualBases S] (c : C) :
    toMatrix (unitTensor (S := S) c) =
      (1 : Matrix (basisIdx c) (basisIdx c) k).submatrix
        ⇑(HasContrDualBases.contrDualIdxEquiv S c) id
```

**`TensorSpecies.Tensor.IsReindexing.unitTensor_of_tau_eq`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L198).

> If `τ e = a`, the identity is a reindexing from `![τ e, e]` to `![a, e]`, so `permT` renames the
> colours of `unitTensor e` to `![a, e]`.

```lean
lemma IsReindexing.unitTensor_of_tau_eq {a e : C} (h : S.τ e = a) :
    IsReindexing (![S.τ e, e] : Fin 2 → C) ![a, e] (id : Fin 2 → Fin 2)
```

**`TensorSpecies.Tensor.toMatrix_permT_unitTensor_of_tau_eq`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean#L205).

> The matrix of `unitTensor e`, with its colours renamed to `![a, e]`, is the identity matrix with
> its rows relabelled by `dualIdxEquiv h`.

```lean
lemma toMatrix_permT_unitTensor_of_tau_eq [HasContrDualBases S] {a e : C} (h : S.τ e = a) :
    toMatrix (permT id (IsReindexing.unitTensor_of_tau_eq h) (unitTensor (S := S) e)) =
      (1 : Matrix (basisIdx e) (basisIdx e) k).submatrix (dualIdxEquiv h).symm id
```

## Depends on

- [Constructors of tensors.](constructors.md)
- [Species whose bases at dual colors are dual bases](../part-04/tensorspecies-dualbasis.md)

## Proof depends on

- [Component indices for one-index tensors](../part-02/componentidx-single.md)
- [Contractions on basis tensors](../part-02/contraction-basis.md)

## Sources

- [Physlib/Relativity/Tensors/UnitTensor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/UnitTensor.lean)
