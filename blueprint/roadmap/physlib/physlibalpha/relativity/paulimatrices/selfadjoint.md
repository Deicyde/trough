---
declaration: module
origin: cited
lean: PauliMatrix.pauliLower, PauliMatrix.pauliBasis'_coe, PauliMatrix.pauliLower_eq_smul, PauliMatrix.sum_pauliLower_mul_pauliLower
statement: formalized
proof: formalized
---

# The covariant Pauli matrices as plain matrices

The module `PhyslibAlpha.Relativity.PauliMatrices.SelfAdjoint`, [PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean): 4 declarations, 4 with a docstring.

> The Pauli matrices with the vector index lowered, and their completeness relation.

## i. Overview

> `Physlib.Relativity.PauliMatrices.SelfAdjoint` carries the Pauli matrices as self-adjoint
> matrices and as the basis `pauliBasis'` of the self-adjoint `2 × 2` matrices. Contracting
> them against tensor components needs them as plain matrices, which is `pauliLower μ`, the
> matrix underlying `pauliSelfAdjoint' μ`; `pauliBasis'_coe` identifies it with the basis vector
> and `pauliLower_eq_smul` with `η_{μμ} σ^μ`. The Fierz completeness relation
> `sum_pauliLower_mul_pauliLower` then says that these four matrices span the `2 × 2` matrices,
> with the trace pairing as the duality and normalisation `2`; it is the relation which turns a
> sum over a Lorentz index into a pair of Kronecker deltas on the spinor indices.

## ii. Key results

> - `PauliMatrix.pauliLower` : the covariant Pauli matrices as plain matrices.
> - `PauliMatrix.pauliBasis'_coe` : they underlie the basis `pauliBasis'`.
> - `PauliMatrix.pauliLower_eq_smul` : lowering the index multiplies by the metric entry.
> - `PauliMatrix.sum_pauliLower_mul_pauliLower` : the Fierz completeness relation.

## iv. References

> The self-adjoint Pauli matrices and the basis `pauliBasis'` are in
> `Physlib.Relativity.PauliMatrices.SelfAdjoint`.

## A. The covariant Pauli matrices as plain matrices

**`PauliMatrix.pauliLower`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean#L59).

> The Pauli matrices with the vector index lowered by the Minkowski metric,
> `σ_μ = η_{μμ} σ^μ`, as plain matrices: the underlying matrices of `pauliSelfAdjoint'`.

```lean
def pauliLower (μ : Fin 1 ⊕ Fin 3) : Matrix (Fin 2) (Fin 2) ℂ
```

**`PauliMatrix.pauliBasis'_coe`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean#L62).

> The covariant Pauli matrices are the underlying matrices of the basis `pauliBasis'`.

```lean
lemma pauliBasis'_coe (μ : Fin 1 ⊕ Fin 3) : (pauliBasis' μ).1 = pauliLower μ
```

**`PauliMatrix.pauliLower_eq_smul`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean#L66).

> Lowering the vector index multiplies by the diagonal entry of the metric.

```lean
lemma pauliLower_eq_smul (μ : Fin 1 ⊕ Fin 3) :
    pauliLower μ = ((minkowskiMatrixZ μ μ : ℤ) : ℂ) • pauliMatrix μ
```

**`PauliMatrix.sum_pauliLower_mul_pauliLower`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean#L72).

> The Fierz completeness relation: the covariant Pauli matrices span the `2 × 2` matrices,
> with the trace pairing as the duality and normalisation `2`.

```lean
lemma sum_pauliLower_mul_pauliLower (α α' β β' : Fin 2) :
    ∑ ρ : Fin 1 ⊕ Fin 3, pauliLower ρ β' β * pauliLower ρ α α'
      = 2 * ((if α = β then 1 else 0) * (if α' = β' then 1 else 0))
```

## Depends on

- [Physlib.Relativity.PauliMatrices.SelfAdjoint](../../../physlib/relativity/paulimatrices/selfadjoint.md)
- [The Minkowski matrix over the integers](../minkowskimatrix.md)

## Sources

- [PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/SelfAdjoint.lean)
