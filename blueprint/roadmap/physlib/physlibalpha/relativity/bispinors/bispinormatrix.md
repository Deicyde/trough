---
declaration: module
origin: cited
lean: Lorentz.bispinorMatrix, Lorentz.pauliTransform, Lorentz.sum_pauliLower_mul_bispinorMatrix, Lorentz.act_bispinorMatrix_pauliTransform, Lorentz.sum_pauliLower_mul_pauliLower_swap, Lorentz.pauliTransform_injective
statement: formalized
proof: formalized
---

# The action of `SL(2, ℂ)` on bispinor indices

The module `PhyslibAlpha.Relativity.Bispinors.BispinorMatrix`, [PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean): 6 declarations, 6 with a docstring.

> A bispinor index is a left-handed and a right-handed Weyl index side by side, and the Pauli
> matrices carry four-vector indices to bispinor indices.

## i. Overview

> A bispinor index `(α, α̇)` is a left-handed and a right-handed Weyl index side by side, on which
> `M ∈ SL(2, ℂ)` acts by `M_{αβ} conj(M_{α̇β̇})` (`bispinorMatrix`).
>
> The covariant Pauli matrices change a four-vector index `μ` into a bispinor index,
> `μ ↦ (σ_μ)_{αα̇}`. On every index of a coefficient tensor this is `pauliTransform`. As
> `M σ_μ Mᴴ = Σ_ν Λ_{νμ} σ_ν`, it carries the action of the Lorentz matrix `Λ` of `M` to that of
> `M` on bispinor indices, and by the trace orthogonality of the Pauli matrices it is injective (A).
> On tensors this is `complexLorentzTensor.pauliTensorMap`, in
> `PhyslibAlpha.Relativity.Bispinors.ComplexifiedAction`.

## ii. Key results

> - `Lorentz.bispinorMatrix` : the action of `SL(2, ℂ)` on one bispinor index.
> - `Lorentz.pauliTransform` : the change from four-vector indices to bispinor indices.
> - `Lorentz.act_bispinorMatrix_pauliTransform` : it intertwines the two actions.
> - `Lorentz.pauliTransform_injective` : it is injective.

## iv. References

> * None.

**`Lorentz.bispinorMatrix`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean#L54).

> The matrix by which `M ∈ SL(2, ℂ)` acts on one bispinor index `(α, α̇)`, a left-handed and a
> right-handed Weyl index, `M_{αβ} conj(M_{α̇β̇})`.

```lean
def bispinorMatrix (M : SL(2,ℂ)) : Fin 2 × Fin 2 → Fin 2 × Fin 2 → ℂ
```

## A. From four-vector indices to bispinor indices

**`Lorentz.pauliTransform`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean#L65).

> The change from a four-vector index to a bispinor index by the covariant Pauli matrices,
> `μ ↦ (σ_μ)_{αα̇}`, on every index of a coefficient tensor.

```lean
def pauliTransform {ι : Type*} [Fintype ι] [DecidableEq ι] :
    ((ι → Fin 1 ⊕ Fin 3) → ℂ) →ₗ[ℂ] ((ι → Fin 2 × Fin 2) → ℂ)
```

**`Lorentz.sum_pauliLower_mul_bispinorMatrix`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean#L71).

> The covariant Pauli matrices move as a covector, `M σ_μ Mᴴ = Σ_ν Λ_{νμ} σ_ν`, written
> entrywise against the action on a bispinor index.

```lean
lemma sum_pauliLower_mul_bispinorMatrix (M : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (q : Fin 2 × Fin 2) :
    ∑ p : Fin 2 × Fin 2, PauliMatrix.pauliLower μ p.1 p.2 * bispinorMatrix M q p
      = ∑ ν, (((SL2C.toLorentzGroup M).1 ν μ : ℝ) : ℂ) * PauliMatrix.pauliLower ν q.1 q.2
```

**`Lorentz.act_bispinorMatrix_pauliTransform`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean#L85).

> The Pauli change of indices carries the action of the Lorentz matrix of `M` on four-vector
> indices to the action of `M` on bispinor indices.

```lean
lemma act_bispinorMatrix_pauliTransform {ι : Type*} [Fintype ι] [DecidableEq ι] (M : SL(2,ℂ))
    (c : (ι → Fin 1 ⊕ Fin 3) → ℂ) :
    act (bispinorMatrix M) (pauliTransform c)
      = pauliTransform (act (fun a b => (((SL2C.toLorentzGroup M).1 a b : ℝ) : ℂ)) c)
```

**`Lorentz.sum_pauliLower_mul_pauliLower_swap`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean#L92).

> The trace orthogonality of the covariant Pauli matrices, `tr (σ_μ σ_ν) = 2 δ_{μν}`.

```lean
lemma sum_pauliLower_mul_pauliLower_swap (μ ν : Fin 1 ⊕ Fin 3) :
    ∑ p : Fin 2 × Fin 2, PauliMatrix.pauliLower μ p.1 p.2 * PauliMatrix.pauliLower ν p.2 p.1
      = 2 * if μ = ν then 1 else 0
```

**`Lorentz.pauliTransform_injective`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean#L100).

> The Pauli change of indices is injective. Half the transposed Pauli matrices undo it.

```lean
lemma pauliTransform_injective {ι : Type*} [Fintype ι] [DecidableEq ι] :
    Function.Injective (pauliTransform (ι := ι))
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../../physlib/relativity/sl2c/basic.md)
- [Matrices acting slot by slot on coefficient functions](../../mathematics/part-02/representationtheory/slotaction.md)
- [The covariant Pauli matrices as plain matrices](../paulimatrices/selfadjoint.md)

## Sources

- [PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/BispinorMatrix.lean)
