---
declaration: module
origin: cited
lean: LocalGaugeData.MatrixRep.kronecker_one_map, LocalGaugeData.MatrixRep.one_kronecker_map, LocalGaugeData.MatrixRep.kronecker_map_of_mul, LocalGaugeData.MatrixRep.neg_kronecker, LocalGaugeData.MatrixRep.kronecker_neg, LocalGaugeData.MatrixRep.trivial, LocalGaugeData.MatrixRep.kron, LocalGaugeData.MatrixRep.foldl_pderiv_star
statement: formalized
proof: formalized
---

# Constructions of matrix representations

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Constructions`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean): 9 declarations, 4 with a docstring.

## i. Overview

> The matrix representations of a jet gauge group are closed under the operations by which
> a model-building table combines the representations of the factors of the gauge group:
> the trivial (singlet) representation, the Kronecker (tensor) product of two
> representations, and the conjugate of a representation. This file provides these three
> constructions; the representations of the individual factors are built in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Factors`.

## ii. Key results

> - `MatrixRep.trivial` : the singlet representation on `Fin 1`.
> - `MatrixRep.kron` : the Kronecker product of two matrix representations.
> - `MatrixRep.conj` : the conjugate of a matrix representation.

## iv. References

> * None.

## A. Matrices with an identity factor

> Entrywise maps that send `0` to `0` pass through a Kronecker product with an identity
> factor, whether or not they are multiplicative.

**`LocalGaugeData.MatrixRep.kronecker_one_map`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L66).

```lean
lemma kronecker_one_map [MulZeroOneClass α] [MulZeroOneClass β] (φ : α → β) (h0 : φ 0 = 0)
    (A : Matrix ι₁ ι₁ α) :
    (A ⊗ₖ (1 : Matrix ι₂ ι₂ α)).map φ = (A.map φ) ⊗ₖ (1 : Matrix ι₂ ι₂ β)
```

**`LocalGaugeData.MatrixRep.one_kronecker_map`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L74).

```lean
lemma one_kronecker_map [MulZeroOneClass α] [MulZeroOneClass β] (φ : α → β) (h0 : φ 0 = 0)
    (B : Matrix ι₂ ι₂ α) :
    ((1 : Matrix ι₁ ι₁ α) ⊗ₖ B).map φ = (1 : Matrix ι₁ ι₁ β) ⊗ₖ (B.map φ)
```

**`LocalGaugeData.MatrixRep.kronecker_map_of_mul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L82).

```lean
lemma kronecker_map_of_mul [Mul α] [Mul β] (φ : α → β) (hφ : ∀ a b, φ (a * b) = φ a * φ b)
    (A : Matrix ι₁ ι₁ α) (B : Matrix ι₂ ι₂ α) :
    (A ⊗ₖ B).map φ = (A.map φ) ⊗ₖ (B.map φ)
```

**`LocalGaugeData.MatrixRep.neg_kronecker`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L89).

```lean
lemma neg_kronecker [Mul α] [HasDistribNeg α] (A : Matrix ι₁ ι₁ α) (B : Matrix ι₂ ι₂ α) :
    (-A) ⊗ₖ B = -(A ⊗ₖ B)
```

**`LocalGaugeData.MatrixRep.kronecker_neg`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L95).

```lean
lemma kronecker_neg [Mul α] [HasDistribNeg α] (A : Matrix ι₁ ι₁ α) (B : Matrix ι₂ ι₂ α) :
    A ⊗ₖ (-B) = -(A ⊗ₖ B)
```

## B. The trivial representation

**`LocalGaugeData.MatrixRep.trivial`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L110).

> **The trivial representation**: the one-dimensional singlet, on which every gauge jet
> acts as the identity and the gauge algebra by zero.

```lean
noncomputable def trivial : MatrixRep jets (Fin 1)
```

## C. The Kronecker product

**`LocalGaugeData.MatrixRep.kron`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L135).

> **The Kronecker product** of two matrix representations: the gauge jets act by the
> Kronecker product of the two matrices of jets, the gauge algebra by the Kronecker sum
> of the two action matrices.

```lean
noncomputable def kron (R₁ : MatrixRep jets ι₁) (R₂ : MatrixRep jets ι₂) :
    MatrixRep jets (ι₁ × ι₂)
```

## D. The conjugate representation

**`LocalGaugeData.MatrixRep.foldl_pderiv_star`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L186).

> The iterated formal derivative commutes with conjugation.

```lean
lemma foldl_pderiv_star (x : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) :
    x.foldl (fun h ρ => pderiv ρ h) (star f) = star (x.foldl (fun h ρ => pderiv ρ h) f)
```

**`LocalGaugeData.MatrixRep.conj`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean#L194).

> **The conjugate representation**: the gauge jets act by the entrywise conjugate matrix
> of jets, the gauge algebra by the entrywise conjugate action matrix.

```lean
noncomputable def conj (R : MatrixRep jets ι) : MatrixRep jets ι
```

## Depends on

- [Matrix representations of a jet gauge group](matterfield-matrixrep-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Constructions.lean)
