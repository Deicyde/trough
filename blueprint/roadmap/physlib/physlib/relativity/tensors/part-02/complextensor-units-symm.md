---
declaration: module
origin: cited
lean: complexLorentzTensor.coContrUnit_symm, complexLorentzTensor.contrCoUnit_symm, complexLorentzTensor.dualLeftLeftUnit_symm, complexLorentzTensor.leftDualLeftUnit_symm, complexLorentzTensor.dualRightRightUnit_symm, complexLorentzTensor.rightDualRightUnit_symm
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Units.Symm

The module `Physlib.Relativity.Tensors.ComplexTensor.Units.Symm`, [Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean): 6 declarations, 6 with a docstring.

## Symmetry lemmas relating to units

## Symmetry properties

**`complexLorentzTensor.coContrUnit_symm`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean#L30).

> Swapping indices of `coContrUnit` returns `contrCoUnit`: `{δ' | μ ν = δ | ν μ}ᵀ`.

```lean
lemma coContrUnit_symm : {δ' | μ ν = δ | ν μ}ᵀ
```

**`complexLorentzTensor.contrCoUnit_symm`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean#L35).

> Swapping indices of `contrCoUnit` returns `coContrUnit`: `{δ | μ ν = δ' | ν μ}ᵀ`.

```lean
lemma contrCoUnit_symm : {δ | μ ν = δ' | ν μ}ᵀ
```

**`complexLorentzTensor.dualLeftLeftUnit_symm`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean#L41).

> Swapping indices of `dualLeftLeftUnit` returns
> `leftDualLeftUnit`: `{δL' | α α' = δL | α' α}ᵀ`.

```lean
lemma dualLeftLeftUnit_symm : {δL' | α α' = δL | α' α}ᵀ
```

**`complexLorentzTensor.leftDualLeftUnit_symm`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean#L47).

> Swapping indices of `leftDualLeftUnit` returns
> `dualLeftLeftUnit`: `{δL | α α' = δL' | α' α}ᵀ`.

```lean
lemma leftDualLeftUnit_symm : {δL | α α' = δL' | α' α}ᵀ
```

**`complexLorentzTensor.dualRightRightUnit_symm`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean#L54).

> Swapping indices of `dualRightRightUnit` returns `rightDualRightUnit`:
> `{δR' | β β' = δR | β' β}ᵀ`.

```lean
lemma dualRightRightUnit_symm : {δR' | β β' = δR | β' β}ᵀ
```

**`complexLorentzTensor.rightDualRightUnit_symm`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean#L61).

> Swapping indices of `rightDualRightUnit` returns `dualRightRightUnit`:
> `{δR | β β' = δR' | β' β}ᵀ`.

```lean
lemma rightDualRightUnit_symm : {δR | β β' = δR' | β' β}ᵀ
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Units.Basic](../part-01/complextensor-units-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Symm.lean)
