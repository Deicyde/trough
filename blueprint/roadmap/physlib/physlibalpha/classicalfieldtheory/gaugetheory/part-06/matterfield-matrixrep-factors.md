---
declaration: module
origin: cited
lean: MatterField.pderiv_chargePow, LocalGaugeData.U1Factor.pderiv_chargePow_u, LocalGaugeData.U1Factor.charge, LocalGaugeData.SUFactor.fund
statement: formalized
proof: formalized
---

# The factors of a gauge group as matrix representations

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Factors`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean): 4 declarations, 4 with a docstring.

## i. Overview

> A model-building table assigns to each field one charge per factor of the gauge group: a
> rational charge under a `U(1)` factor, a representation label under an `SU(n)` factor.
> The factors themselves, `LocalGaugeData.U1Factor` and `LocalGaugeData.SUFactor`, are part
> of the gauge data (`PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Factor`). This
> file builds the representations they name: `U1Factor.charge n R` twists a matrix
> representation `R` by the charge-`n` power of the unitary jet, and `SUFactor.fund` is the
> fundamental representation. Together with `MatrixRep.trivial`, `MatrixRep.kron` and
> `MatrixRep.conj`, every representation named in a table is assembled from these.

## ii. Key results

> - `U1Factor.charge` : the charge twist of a matrix representation by a `U(1)` factor.
> - `MatterField.pderiv_chargePow` : the derivative of a power of a unitary jet.
> - `SUFactor.fund` : the fundamental representation of an `SU(n)` factor.

## iv. References

> * None.

## A. Powers of a unitary jet

**`MatterField.pderiv_chargePow`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean#L57).

> **The derivative of a power of a unitary jet**: `∂_μ (u ^ n) = n · u ^ n · (u⁻¹ ∂_μ u)`,
> for every integer `n`.

```lean
lemma pderiv_chargePow (n : ℤ) (w : unitary SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3) :
    pderiv μ (chargePow n w)
      = (n : ℂ) •
          (chargePow n w * (star (w : SpaceTimeAlgebra) * pderiv μ (w : SpaceTimeAlgebra)))
```

## B. The charge twist of a `U(1)` factor

**`LocalGaugeData.U1Factor.pderiv_chargePow_u`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean#L105).

> The derivative of the charge-`n` power of the unitary jet of a gauge jet, in terms of
> the Maurer–Cartan form: `∂_μ (u ^ n) = -(i n) φJ (ω_μ U) · u ^ n`.

```lean
lemma pderiv_chargePow_u (n : ℤ) (U : GJ) (μ : Fin 1 ⊕ Fin 3) :
    pderiv μ (chargePow n (F.u U))
      = -(((Complex.I * n) • F.φJ (jets.maurerCartan U μ)) * chargePow n (F.u U))
```

**`LocalGaugeData.U1Factor.charge`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean#L119).

> **The charge twist**: a matrix representation twisted by the charge-`n` power of the
> unitary jet of the `U(1)` factor. The gauge algebra acts by the original action plus
> `i n` times the `u(1)` component.

```lean
noncomputable def charge (n : ℤ) (R : MatrixRep jets ι) : MatrixRep jets ι
```

## C. The fundamental representation of an `SU(n)` factor

**`LocalGaugeData.SUFactor.fund`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean#L194).

> **The fundamental representation** of an `SU(n)` factor: the gauge jets act by their
> unitary matrices of jets, the gauge algebra by `i` times its matrix component.

```lean
noncomputable def fund : MatrixRep jets n
```

## Depends on

- [The factors of a gauge group](../part-04/localgaugedata-factor.md)
- [Charged matter fields under `U(1)` jets](../part-05/matterfield-charge.md)
- [Matrix representations of a jet gauge group](matterfield-matrixrep-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Factors.lean)
