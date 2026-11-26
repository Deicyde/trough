---
declaration: module
origin: cited
lean: suTensor.pairMatrix, suTensor.pairMatrix_tmul, suTensor.pairMatrix_map, suTensor.adjToPair, suTensor.pairMatrix_adjToPair, suTensor.adjToPair_adjRep, suTensor.adjContract, suTensor.adjContract_tmul
statement: formalized
proof: formalized
---

# The generator tensor of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.Generator`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean): 24 declarations, 21 with a docstring.

> Up to scale, the generators `(Tᵃ)_i^j = (λ_a)_{ij} / 2` form the only invariant tensor with an
> adjoint, a fundamental and an anti-fundamental index.

## i. Overview

> An element of `ℂᴺ ⊗ ℂᴺ`, with the fundamental and the anti-fundamental representation, is a
> matrix of components moved by `g` to `g X g⁻¹` (`pairMatrix`). Writing the matrix of an element
> of the complexified Lie algebra in this way is an equivariant map `adjToPair` from the adjoint
> representation (A).
>
> An element `x` of `adj ⊗ U`, for any representation `U`, is a linear map `adj → U` once its first
> index is contracted against the argument with the trace form (`adjContract`). This identifies
> `adj ⊗ U` with the linear maps, and an invariant `x` gives an equivariant map (B).
>
> An equivariant linear map `Φ` from the adjoint representation to the matrices is a multiple of
> the matrix of the argument (C). Its trace is an invariant linear form, which by the trace form
> is an invariant of the adjoint representation and so vanishes. Then `Φ` lands in the traceless
> matrices, that is in the complexified Lie algebra, and commutes with the adjoint action, so it is
> scalar.
>
> The generator tensor `generatorVal N` is the unit `∑ b_a ⊗ bᵃ` of the adjoint color with its
> second factor written as a matrix, in `adj ⊗ (ℂᴺ ⊗ ℂᴺ)`, and it is invariant (D). As a linear map
> `adj → ℂᴺ ⊗ ℂᴺ` it is `adjToPair`. So an invariant `x` gives a map which, written as matrices, is
> equivariant and hence a multiple of the matrix of the argument, and `x` is that multiple of the
> generator tensor (E). The tensor `generator N`, with an adjoint, a fundamental and an
> anti-fundamental index, has the components `(λ_a)_{ij} / 2` (F).

## ii. Key results

> - `suTensor.pairMatrix` : the components of an element of `ℂᴺ ⊗ ℂᴺ` as a matrix.
> - `suTensor.exists_eq_smul_adjMat_of_equivariant` : an equivariant map from the adjoint
>   representation to the matrices is a multiple of the matrix of the argument.
> - `suTensor.generatorVal` : the generator tensor.
> - `suTensor.invariants_tprod_eq_span_generatorVal` : the invariants of
>   `adj ⊗ (ℂᴺ ⊗ ℂᴺ)` are the line through the generator tensor.
> - `suTensor.generator` : the generator tensor with an adjoint, a fundamental and an
>   anti-fundamental index.
> - `suTensor.invariants_adj_fund_antiFund_eq_span_generator` : the invariant tensors with these
>   indices are the line through it.
> - `suTensor.basis_repr_generator` : its components are the entries of `λ_a / 2`.

## iv. References

> * None.

## A. A fundamental and an anti-fundamental index as a matrix

**`suTensor.pairMatrix`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L84).

> The components of an element of `ℂᴺ ⊗ ℂᴺ` as a matrix, `v ⊗ w ↦ v wᵀ`.

```lean
noncomputable def pairMatrix : (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ) ≃ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ
```

**`suTensor.pairMatrix_tmul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L90).

```lean
lemma pairMatrix_tmul (v w : Fin N → ℂ) : pairMatrix N (v ⊗ₜ w) = vecMulVec v w
```

**`suTensor.pairMatrix_map`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L98).

> The fundamental and the anti-fundamental representation move the matrix of components by
> conjugation.

```lean
lemma pairMatrix_map (g : SU N) (x : (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ)) :
    pairMatrix N (TensorProduct.map (fundRep N g) (antiFundRep N g) x)
      = g.1 * pairMatrix N x * (g⁻¹).1
```

**`suTensor.adjToPair`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L110).

> The matrix of an element of the complexified Lie algebra, as an element of `ℂᴺ ⊗ ℂᴺ`.

```lean
noncomputable def adjToPair : SUAlgebraComplexified N →ₗ[ℂ] (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ)
```

**`suTensor.pairMatrix_adjToPair`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L114).

```lean
lemma pairMatrix_adjToPair (A : SUAlgebraComplexified N) :
    pairMatrix N (adjToPair N A) = adjMat N A
```

**`suTensor.adjToPair_adjRep`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L120).

> Writing the matrix of an element of the complexified Lie algebra in `ℂᴺ ⊗ ℂᴺ` is
> equivariant.

```lean
lemma adjToPair_adjRep (g : SU N) (A : SUAlgebraComplexified N) :
    adjToPair N (adjRep N g A)
      = TensorProduct.map (fundRep N g) (antiFundRep N g) (adjToPair N A)
```

## B. Contracting an adjoint index

**`suTensor.adjContract`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L139).

> An element of `adj ⊗ U` as the linear map `adj → U` contracting its first index against the
> argument with the trace form, `A₀ ⊗ u ↦ (A ↦ tr (A₀ A) u)`.

```lean
noncomputable def adjContract :
    SUAlgebraComplexified N ⊗[ℂ] U ≃ₗ[ℂ] (SUAlgebraComplexified N →ₗ[ℂ] U)
```

**`suTensor.adjContract_tmul`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L145).

```lean
lemma adjContract_tmul (A₀ : SUAlgebraComplexified N) (u : U) (A : SUAlgebraComplexified N) :
    adjContract N U (A₀ ⊗ₜ u) A = traceForm N A₀ A • u
```

**`suTensor.traceForm_adjRep`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L150).

> The trace form is invariant under the adjoint action.

```lean
lemma traceForm_adjRep (g : SU N) (A B : SUAlgebraComplexified N) :
    traceForm N (adjRep N g A) (adjRep N g B) = traceForm N A B
```

**`suTensor.adjContract_map`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L155).

> Transforming both factors of `x` conjugates the map `adjContract x`.

```lean
lemma adjContract_map (σ : Representation ℂ (SU N) U) (g : SU N)
    (x : SUAlgebraComplexified N ⊗[ℂ] U) (A : SUAlgebraComplexified N) :
    adjContract N U (TensorProduct.map (adjRep N g) (σ g) x) (adjRep N g A)
      = σ g (adjContract N U x A)
```

**`suTensor.adjContract_lTensor`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L165).

> Applying a linear map to the second factor of `x` composes `adjContract x` with it.

```lean
lemma adjContract_lTensor {U' : Type*} [AddCommGroup U'] [Module ℂ U'] (ι : U →ₗ[ℂ] U')
    (x : SUAlgebraComplexified N ⊗[ℂ] U) (A : SUAlgebraComplexified N) :
    adjContract N U' (TensorProduct.map LinearMap.id ι x) A = ι (adjContract N U x A)
```

**`suTensor.adjContract_adjUnitVal`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L173).

> The unit of the adjoint color, as a linear map, is the identity.

```lean
lemma adjContract_adjUnitVal (A : SUAlgebraComplexified N) :
    adjContract N _ (adjUnitVal N) A = A
```

## C. Equivariant maps from the adjoint representation to the matrices

**`suTensor.eq_zero_of_adjRep_invariant`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L194).

> An invariant linear form on the complexified Lie algebra vanishes. By the trace form it is
> the pairing with an invariant element, which is zero.

```lean
lemma eq_zero_of_adjRep_invariant {ℓ : Module.Dual ℂ (SUAlgebraComplexified N)}
    (hℓ : ∀ (g : SU N) (A : SUAlgebraComplexified N), ℓ (adjRep N g A) = ℓ A) : ℓ = 0
```

**`suTensor.exists_eq_smul_adjMat_of_equivariant`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L206).

> An equivariant linear map from the complexified Lie algebra to the matrices, moved by
> conjugation, is a multiple of the matrix of the argument.

```lean
lemma exists_eq_smul_adjMat_of_equivariant
    {Φ : SUAlgebraComplexified N →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ}
    (hΦ : ∀ (g : SU N) (A : SUAlgebraComplexified N), Φ (adjRep N g A) = g.1 * Φ A * (g⁻¹).1) :
    ∃ μ : ℂ, Φ = μ • adjMat N
```

## D. The generator tensor

**`suTensor.generatorVal`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L239).

> The generator tensor, the unit `∑ b_a ⊗ bᵃ` of the adjoint color with its second factor
> written as a matrix, in `adj ⊗ (ℂᴺ ⊗ ℂᴺ)`. Its components are the entries of `λ_a / 2`.

```lean
noncomputable def generatorVal :
    SUAlgebraComplexified N ⊗[ℂ] ((Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ))
```

**`suTensor.adjContract_generatorVal`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L245).

> As a linear map from the complexified Lie algebra, the generator tensor writes the matrix of
> the argument in `ℂᴺ ⊗ ℂᴺ`.

```lean
lemma adjContract_generatorVal (A : SUAlgebraComplexified N) :
    adjContract N _ (generatorVal N) A = adjToPair N A
```

**`suTensor.generatorVal_mem_invariants`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L250).

> The generator tensor is invariant.

```lean
lemma generatorVal_mem_invariants :
    generatorVal N ∈ ((adjRep N).tprod ((fundRep N).tprod (antiFundRep N))).invariants
```

## E. The generator tensor is the unique invariant

**`suTensor.invariants_tprod_eq_span_generatorVal`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L276).

> The invariants of `adj ⊗ (ℂᴺ ⊗ ℂᴺ)`, with the adjoint, the fundamental and the
> anti-fundamental representation, are the line through the generator tensor.

```lean
lemma invariants_tprod_eq_span_generatorVal :
    ((adjRep N).tprod ((fundRep N).tprod (antiFundRep N))).invariants = ℂ ∙ generatorVal N
```

## F. The generator tensor with three indices

**`suTensor.generator`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L302).

> The generator tensor `(Tᵃ)_i^j` with an adjoint, a fundamental and an anti-fundamental
> index.

```lean
noncomputable def generator : SuT[N, .adj, .fund, .antiFund]
```

**`suTensor.generator_invariant`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L306).

> The generator tensor is invariant.

```lean
lemma generator_invariant (g : SU N) : g • generator N = generator N
```

**`suTensor.invariants_adj_fund_antiFund_eq_span_generator`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L312).

> The invariant tensors with an adjoint, a fundamental and an anti-fundamental index are the
> line through the generator tensor.

```lean
lemma invariants_adj_fund_antiFund_eq_span_generator :
    ((suTensor N).tensorRep ![.adj, .fund, .antiFund]).invariants = ℂ ∙ generator N
```

**`suTensor.dualBasis_adjBasis`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L317).

> The dual basis of the Gell-Mann basis under the trace form is half of it.

```lean
lemma dualBasis_adjBasis (a : GellMann.Index N) :
    (traceForm N).dualBasis (traceForm_nondegenerate N) (adjBasis N) a
      = (1 / 2 : ℂ) • adjBasis N a
```

**`suTensor.generatorVal_eq_sum`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L332).

> The generator tensor as a sum over the Gell-Mann basis, with the matrices `λ_a / 2` in its
> second factor.

```lean
lemma generatorVal_eq_sum : generatorVal N
    = ∑ a, adjBasis N a ⊗ₜ adjToPair N ((1 / 2 : ℂ) • adjBasis N a)
```

**`suTensor.basis_repr_generator`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean#L338).

> The components of the generator tensor are the entries of the generators `λ_a / 2`.

```lean
lemma basis_repr_generator (a : GellMann.Index N) (i j : Fin N) :
    (Tensor.basis _).repr (generator N) (fun | 0 => a | 1 => i | 2 => j)
      = GellMann.matrix a i j / 2
```

## Depends on

- [The complex tensor species of `SU(N)`](globalgaugegroup-su-tensorspecies.md)

## Proof depends on

- [What commutes with the adjoint action of `SU(N)`, and the Reynolds element of its tensors](globalgaugegroup-su-invariants-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Generator.lean)
