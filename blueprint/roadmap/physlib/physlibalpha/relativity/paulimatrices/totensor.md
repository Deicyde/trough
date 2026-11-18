---
declaration: module
origin: cited
lean: PauliMatrix.indexBasis, PauliMatrix.indexBasis_apply, PauliMatrix.toTensor_eq_sum_indexBasis
statement: formalized
proof: formalized
---

# The Pauli tensor in components

The module `PhyslibAlpha.Relativity.PauliMatrices.ToTensor`, [PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean): 3 declarations, 2 with a docstring.

> The basis of `ℂT[.up, .upL, .upR]` indexed by a Lorentz and two spinor indices.

## i. Overview

> `Physlib.Relativity.Bispinors.Pauli.ToTensor` carries the Pauli matrices as the tensor
> `σ^^^ : ℂT[.up, .upL, .upR]` and the equivalence `indexEquiv` identifying the component index
> of that tensor with a triple `(μ, α, β)`. Reindexing the tensor basis along `indexEquiv` gives
> `indexBasis`, the basis labelled by such triples, and `toTensor_eq_sum_indexBasis` expands the
> Pauli tensor in it: the coefficient of `e_μ ⊗ e_α ⊗ e_β` is the entry `σ^μ_{α β}`. This is the
> form in which the Pauli tensor enters a component computation.

## ii. Key results

> - `PauliMatrix.indexBasis` : the basis of `ℂT[.up, .upL, .upR]` indexed by `(μ, α, β)`.
> - `PauliMatrix.toTensor_eq_sum_indexBasis` : `σ^^^ = ∑ σ^μ_{α β} e_μ ⊗ e_α ⊗ e_β`.

## iv. References

> The Pauli tensor and `indexEquiv` are in `Physlib.Relativity.Bispinors.Pauli.ToTensor`.

## A. The basis indexed by a Lorentz and two spinor indices

**`PauliMatrix.indexBasis`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean#L62).

> The basis of `ℂT[.up, .upL, .upR]` indexed by `(Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2` through
> `indexEquiv`: `indexBasis (μ, α, β) = e_μ ⊗ e_α ⊗ e_β`.

```lean
noncomputable def indexBasis :
    Basis ((Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2) ℂ ℂT[.up, .upL, .upR]
```

**`PauliMatrix.indexBasis_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean#L66).

```lean
lemma indexBasis_apply (d : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2) :
    indexBasis d = Tensor.basis ![Color.up, Color.upL, Color.upR] (indexEquiv.symm d)
```

**`PauliMatrix.toTensor_eq_sum_indexBasis`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean#L72).

> The Pauli tensor as a sum over its components, `σ^^^ = ∑ σ^μ_{α β} e_μ ⊗ e_α ⊗ e_β`.

```lean
lemma toTensor_eq_sum_indexBasis : σ^^^ = ∑ d : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2,
    pauliMatrix d.1 d.2.1 d.2.2 • indexBasis d
```

## Depends on

- [Pauli matrices as a tensor](../../../physlib/relativity/bispinors/pauli-totensor.md)

## Sources

- [PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/ToTensor.lean)
