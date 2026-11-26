---
declaration: module
origin: cited
lean: GlobalGaugeGroup.compactSymplecticGroup, GlobalGaugeGroup.Sp, GlobalGaugeGroup.mem_compactSymplecticGroup_iff, GlobalGaugeGroup.star_mem_compactSymplecticGroup, GlobalGaugeGroup.mem_Sp_iff
statement: formalized
proof: formalized
---

# The global gauge group Sp(n)

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.Sp`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean): 5 declarations, 5 with a docstring.

> The compact symplectic group, as a global gauge group.

## i. Overview

> The compact symplectic group `Sp(n)`, also written `USp(2n)`, is the group of unitary
> `2n × 2n` complex matrices `A` which preserve the standard symplectic form `J`,
> `A J Aᵀ = J`. It is the compact real form of the complex symplectic group, and it appears as
> a gauge group in grand unified and supersymmetric theories. Here `Sp(1)` is `SU(2)`.
>
> Unitarity and the symplectic condition are both closed, so the compact symplectic matrices
> form a closed submonoid of matrices. The conjugate transpose of a unitary matrix is its
> inverse, and the inverse of a symplectic matrix is symplectic, so the submonoid is closed
> under the conjugate transpose. An invertible matrix therefore lies in the global gauge
> group `Sp(n)` exactly when it is unitary and symplectic.

## ii. Key results

> - `GlobalGaugeGroup.compactSymplecticGroup` : the unitary symplectic matrices.
> - `GlobalGaugeGroup.Sp` : the global gauge group `Sp(n)`.
> - `GlobalGaugeGroup.mem_Sp_iff` : an invertible matrix lies in `Sp(n)` exactly when it is
>   unitary and symplectic.

## iv. References

> * None.

## A. The group Sp(n)

**`GlobalGaugeGroup.compactSymplecticGroup`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean#L60).

> The unitary `2n × 2n` complex matrices `A` preserving the symplectic form,
> `A J Aᵀ = J`.

```lean
def compactSymplecticGroup (n : ℕ) : Submonoid (Matrix (Fin n ⊕ Fin n) (Fin n ⊕ Fin n) ℂ)
```

**`GlobalGaugeGroup.Sp`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean#L65).

> The global gauge group `Sp(n)`, the unitary `2n × 2n` complex matrices preserving the
> symplectic form. Unitarity and the symplectic condition are both closed conditions.

```lean
def Sp (n : ℕ) : GlobalGaugeGroup (Fin n ⊕ Fin n)
```

## B. Membership

**`GlobalGaugeGroup.mem_compactSymplecticGroup_iff`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean#L80).

> A matrix lies in the unitary symplectic matrices exactly when it is unitary and
> symplectic.

```lean
lemma mem_compactSymplecticGroup_iff {n : ℕ} {A : Matrix (Fin n ⊕ Fin n) (Fin n ⊕ Fin n) ℂ} :
    A ∈ compactSymplecticGroup n ↔
      A ∈ unitaryGroup (Fin n ⊕ Fin n) ℂ ∧ A ∈ symplecticGroup (Fin n) ℂ
```

**`GlobalGaugeGroup.star_mem_compactSymplecticGroup`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean#L87).

> The conjugate transpose of a unitary symplectic matrix is unitary symplectic, being its
> inverse.

```lean
lemma star_mem_compactSymplecticGroup {n : ℕ} {A : Matrix (Fin n ⊕ Fin n) (Fin n ⊕ Fin n) ℂ}
    (hA : A ∈ compactSymplecticGroup n) : star A ∈ compactSymplecticGroup n
```

**`GlobalGaugeGroup.mem_Sp_iff`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean#L95).

> An invertible matrix lies in `Sp(n)` exactly when it is unitary and symplectic.

```lean
lemma mem_Sp_iff {n : ℕ} {g : GeneralLinearGroup (Fin n ⊕ Fin n) ℂ} :
    g ∈ (Sp n).group ↔ (g : Matrix (Fin n ⊕ Fin n) (Fin n ⊕ Fin n) ℂ) ∈ compactSymplecticGroup n
```

## Depends on

- [Global gauge groups](globalgaugegroup-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Sp.lean)
