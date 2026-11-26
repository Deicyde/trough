---
declaration: module
origin: cited
lean: GlobalGaugeGroup.realSpecialOrthogonalGroup, GlobalGaugeGroup.isClosedEmbedding_ofReal_mapMatrix, GlobalGaugeGroup.star_ofReal_mapMatrix, GlobalGaugeGroup.mem_realSpecialOrthogonalGroup_iff, GlobalGaugeGroup.ofReal_mem_realSpecialOrthogonalGroup_iff, GlobalGaugeGroup.isClosed_realSpecialOrthogonalGroup, GlobalGaugeGroup.star_mem_realSpecialOrthogonalGroup, GlobalGaugeGroup.SO
statement: formalized
proof: formalized
---

# The global gauge group SO(n)

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SO`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean): 9 declarations, 9 with a docstring.

> The special orthogonal group, as a global gauge group.

## i. Overview

> The special orthogonal group `SO(n)` is the group of real orthogonal `n × n` matrices of
> determinant one, the rotations of `ℝⁿ`. It appears as a gauge group in grand unified
> theories, such as `SO(10)`. A global gauge group sits inside `GL(n, ℂ)`, and there `SO(n)`
> is the group of real matrices in `SU(n)`. A real matrix `B` is unitary exactly when
> `Bᵀ B = 1`, and has determinant one as a complex matrix exactly when it does as a real one.
>
> The real matrices are the image of the entrywise embedding `ℝ → ℂ`. This embedding has the
> entrywise real part as a continuous left inverse, so its image is closed, and the real
> matrices in `SU(n)` form a closed submonoid. The conjugate transpose of a real matrix is its
> transpose, again real, so the submonoid is closed under the conjugate transpose.

## ii. Key results

> - `GlobalGaugeGroup.realSpecialOrthogonalGroup` : the real special orthogonal matrices, as
>   complex matrices.
> - `GlobalGaugeGroup.ofReal_mem_realSpecialOrthogonalGroup_iff` : a real matrix lies in it
>   exactly when it is orthogonal of determinant one.
> - `GlobalGaugeGroup.SO` : the global gauge group `SO(n)`.
> - `GlobalGaugeGroup.mem_SO_iff` : an invertible matrix lies in `SO(n)` exactly when it is a
>   real orthogonal matrix of determinant one.

## iv. References

> * None.

## A. The real special orthogonal matrices

**`GlobalGaugeGroup.realSpecialOrthogonalGroup`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L64).

> The real orthogonal `n × n` matrices of determinant one, as complex matrices, the real
> matrices in `SU(n)`.

```lean
def realSpecialOrthogonalGroup (n : ℕ) : Submonoid (Matrix (Fin n) (Fin n) ℂ)
```

## B. Real matrices

**`GlobalGaugeGroup.isClosedEmbedding_ofReal_mapMatrix`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L76).

> The entrywise embedding of real matrices into complex matrices is a closed embedding.
> The entrywise real part is a continuous left inverse.

```lean
lemma isClosedEmbedding_ofReal_mapMatrix (n : ℕ) :
    IsClosedEmbedding (Complex.ofRealHom.mapMatrix : Matrix (Fin n) (Fin n) ℝ →+* _)
```

**`GlobalGaugeGroup.star_ofReal_mapMatrix`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L84).

> The conjugate transpose of a real matrix is its transpose.

```lean
lemma star_ofReal_mapMatrix {n : ℕ} (B : Matrix (Fin n) (Fin n) ℝ) :
    star (Complex.ofRealHom.mapMatrix B) = Complex.ofRealHom.mapMatrix Bᵀ
```

## C. Membership in the real special orthogonal matrices

**`GlobalGaugeGroup.mem_realSpecialOrthogonalGroup_iff`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L97).

> A complex matrix is a real special orthogonal matrix exactly when it is special unitary and
> the entrywise embedding of a real matrix.

```lean
lemma mem_realSpecialOrthogonalGroup_iff {n : ℕ} {A : Matrix (Fin n) (Fin n) ℂ} :
    A ∈ realSpecialOrthogonalGroup n ↔
      A ∈ specialUnitaryGroup (Fin n) ℂ ∧ ∃ B : Matrix (Fin n) (Fin n) ℝ,
        Complex.ofRealHom.mapMatrix B = A
```

**`GlobalGaugeGroup.ofReal_mem_realSpecialOrthogonalGroup_iff`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L105).

> A real matrix lies in the real special orthogonal matrices exactly when it is
> orthogonal, `Bᵀ B = 1`, of determinant one.

```lean
lemma ofReal_mem_realSpecialOrthogonalGroup_iff {n : ℕ} (B : Matrix (Fin n) (Fin n) ℝ) :
    Complex.ofRealHom.mapMatrix B ∈ realSpecialOrthogonalGroup n ↔
      Bᵀ * B = 1 ∧ B.det = 1
```

**`GlobalGaugeGroup.isClosed_realSpecialOrthogonalGroup`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L116).

> The real special orthogonal matrices form a closed set.

```lean
lemma isClosed_realSpecialOrthogonalGroup (n : ℕ) :
    IsClosed (realSpecialOrthogonalGroup n : Set (Matrix (Fin n) (Fin n) ℂ))
```

**`GlobalGaugeGroup.star_mem_realSpecialOrthogonalGroup`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L124).

> The conjugate transpose of a real special orthogonal matrix is real special
> orthogonal.

```lean
lemma star_mem_realSpecialOrthogonalGroup {n : ℕ} {A : Matrix (Fin n) (Fin n) ℂ}
    (hA : A ∈ realSpecialOrthogonalGroup n) : star A ∈ realSpecialOrthogonalGroup n
```

## D. The group SO(n)

**`GlobalGaugeGroup.SO`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L138).

> The global gauge group `SO(n)`, the real orthogonal `n × n` matrices of determinant one,
> as complex matrices.

```lean
def SO (n : ℕ) : GlobalGaugeGroup (Fin n)
```

**`GlobalGaugeGroup.mem_SO_iff`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean#L143).

> An invertible matrix lies in `SO(n)` exactly when it is a real orthogonal matrix of
> determinant one.

```lean
lemma mem_SO_iff {n : ℕ} {g : GeneralLinearGroup (Fin n) ℂ} :
    g ∈ (SO n).group ↔ ∃ B : Matrix (Fin n) (Fin n) ℝ,
      Bᵀ * B = 1 ∧ B.det = 1 ∧ Complex.ofRealHom.mapMatrix B = g
```

## Depends on

- [Global gauge groups](globalgaugegroup-basic.md)

## Proof depends on

- [The global gauge group SU(n)](globalgaugegroup-su.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SO.lean)
