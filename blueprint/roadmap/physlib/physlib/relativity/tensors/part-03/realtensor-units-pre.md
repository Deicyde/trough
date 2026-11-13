---
declaration: module
origin: cited
lean: Lorentz.CoMod.unitVal, Lorentz.CoMod.unitVal_expand_tmul, Lorentz.CoMod.unit, Lorentz.CoMod.unit_apply_one, Lorentz.ContrMod.unitVal, Lorentz.ContrMod.unitVal_expand_tmul, Lorentz.ContrMod.unit, Lorentz.ContrMod.unit_apply_one
statement: formalized
proof: formalized
---

# Unit for complex Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Units.Pre`, [Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean): 12 declarations, 8 with a docstring.

**`Lorentz.CoMod.unitVal`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L24).

> The contra-co unit for complex lorentz vectors. Usually denoted `δⁱᵢ`.

```lean
def CoMod.unitVal (d : ℕ := 3) : ContrMod d ⊗[ℝ] CoMod d
```

**`Lorentz.CoMod.unitVal_expand_tmul`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L28).

> Expansion of `CoMod.unitVal` into basis.

```lean
lemma CoMod.unitVal_expand_tmul {d : ℕ} : CoMod.unitVal d =
    ∑ i, contrBasis d i ⊗ₜ[ℝ] coBasis d i
```

**`Lorentz.CoMod.unit`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L49).

> The contra-co unit for complex lorentz vectors as a morphism
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ complexContr ⊗ complexCo`, manifesting the invariance under
> the `SL(2, ℂ)` action.

```lean
def CoMod.unit (d : ℕ := 3) :
  (Representation.trivial ℝ (LorentzGroup d) ℝ).IntertwiningMap
    ((ContrMod.rep).tprod (CoMod.rep))
```

**`Lorentz.CoMod.unit_apply_one`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L70).

```lean
lemma CoMod.unit_apply_one {d : ℕ} : (CoMod.unit d) (1 : ℝ) = CoMod.unitVal d
```

**`Lorentz.ContrMod.unitVal`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L75).

> The co-contra unit for complex lorentz vectors. Usually denoted `δᵢⁱ`.

```lean
def ContrMod.unitVal (d : ℕ := 3) : CoMod d ⊗[ℝ] ContrMod d
```

**`Lorentz.ContrMod.unitVal_expand_tmul`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L79).

> Expansion of `ContrMod.unitVal` into basis.

```lean
lemma ContrMod.unitVal_expand_tmul {d : ℕ} : ContrMod.unitVal d =
    ∑ i, coBasis d i ⊗ₜ[ℝ] contrBasis d i
```

**`Lorentz.ContrMod.unit`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L100).

> The co-contra unit for complex lorentz vectors as a morphism
> `𝟙_ (Rep ℝ (LorentzGroup d)) ⟶ CoMod.rep ⊗ ContrMod.rep`, manifesting the invariance under
> the `LorentzGroup d` action.

```lean
def ContrMod.unit (d : ℕ) : (Representation.trivial ℝ (LorentzGroup d) ℝ).IntertwiningMap
    ((CoMod.rep).tprod (ContrMod.rep))
```

**`Lorentz.ContrMod.unit_apply_one`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L122).

```lean
lemma ContrMod.unit_apply_one {d : ℕ} : (ContrMod.unit d) (1 : ℝ) = ContrMod.unitVal d
```

## Contraction of the units

**`Lorentz.CoMod.contr_unit`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L133).

> Contraction on the right with `CoMod.unit` does nothing.

```lean
lemma CoMod.contr_unit {d : ℕ} (x : CoMod d) :
    (TensorProduct.lid ℝ _ <|
    CoMod.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℝ (CoMod d) (ContrMod d) (CoMod d)).symm <|
    x ⊗ₜ[ℝ] (CoMod.unit d (1 : ℝ))) = x
```

**`Lorentz.ContrMod.contr_unit`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L167).

> Contraction on the right with `ContrMod.unit` does nothing.

```lean
lemma ContrMod.contr_unit {d : ℕ} (x : ContrMod d) :
    (TensorProduct.lid ℝ _ <|
    ContrMod.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℝ (ContrMod d) (CoMod d) (ContrMod d)).symm <|
    x ⊗ₜ[ℝ] (ContrMod.unit d (1 : ℝ))) = x
```

## Symmetry properties of the units

**`Lorentz.CoMod.unit_symm`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L207).

```lean
lemma CoMod.unit_symm {d : ℕ} :
    (CoMod.unit d) (1 : ℝ) = LinearMap.lTensor _ (LinearEquiv.cast (by rfl)).toLinearMap
      (TensorProduct.comm ℝ _ _ ((ContrMod.unit d) (1 : ℝ)))
```

**`Lorentz.ContrMod.unit_symm`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean#L214).

```lean
lemma ContrMod.unit_symm {d : ℕ} :
    (ContrMod.unit d) (1 : ℝ) = LinearMap.lTensor _ (LinearEquiv.cast (by simp)).toLinearMap
    (TensorProduct.comm ℝ _ _ ((CoMod.unit d) (1 : ℝ)))
```

## Depends on

- [Tensor products of two real Lorentz vectors](realtensor-matrix-pre.md)
- [Contraction of Real Lorentz vectors](../part-04/realtensor-vector-pre-contraction.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Pre.lean)
