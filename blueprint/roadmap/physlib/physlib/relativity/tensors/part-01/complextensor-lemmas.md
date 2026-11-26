---
declaration: module
origin: cited
lean: complexLorentzTensor.antiSymm_contr_symm
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Lemmas

The module `Physlib.Relativity.Tensors.ComplexTensor.Lemmas`, [Physlib/Relativity/Tensors/ComplexTensor/Lemmas.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Relativity/Tensors/ComplexTensor/Lemmas.lean): 1 declaration, none with a docstring.

## Lemmas related to complex Lorentz tensors.

**`complexLorentzTensor.antiSymm_contr_symm`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Relativity/Tensors/ComplexTensor/Lemmas.lean#L28).

```lean
lemma antiSymm_contr_symm {A : ℂT[.up, .up]} {S : ℂT[.down, .down]}
    (hA : {A | μ ν = - (A | ν μ)}ᵀ) (hs : {S | μ ν = S | ν μ}ᵀ) :
    {A | μ ν ⊗ S | μ ν = - A | μ ν ⊗ S | μ ν}ᵀ
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](complextensor-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Lemmas.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Relativity/Tensors/ComplexTensor/Lemmas.lean)
