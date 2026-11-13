---
declaration: module
origin: cited
lean: Lorentz.CoVector.sl2Rep, Lorentz.CoVector.sl2Rep_dual_dualBasis
statement: formalized
proof: formalized
---

# The representation of `SL(2, ℂ)` on real Lorentz covectors

The module `PhyslibAlpha.Relativity.Tensors.RealTensor.CoVector.Representation`, [PhyslibAlpha/Relativity/Tensors/RealTensor/CoVector/Representation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/RealTensor/CoVector/Representation.lean): 2 declarations, 2 with a docstring.

> The covector representation pulled back along the covering map, and its dual.

## i. Overview

> `Physlib.Relativity.Tensors.RealTensor.CoVector.Representation` carries the representation of
> the Lorentz group on real Lorentz covectors. Composing it with the covering map
> `SL(2, ℂ) →* LorentzGroup 3` gives `sl2Rep`, the representation of `SL(2, ℂ)` on the same
> space, which is the form a spinor computation needs. Its dual acts on the dual basis
> contravariantly: `sl2Rep_dual_dualBasis` says that `e^μ` goes to the combination given by the
> column `μ` of the Lorentz matrix.

## ii. Key results

> - `Lorentz.CoVector.sl2Rep` : the representation of `SL(2, ℂ)` on real Lorentz covectors.
> - `Lorentz.CoVector.sl2Rep_dual_dualBasis` : dual covectors transform by the columns of the
>   Lorentz matrix.

## iv. References

> The Lorentz-group representation is in
> `Physlib.Relativity.Tensors.RealTensor.CoVector.Representation`.

## A. The representation of `SL(2, ℂ)`

**`Lorentz.CoVector.sl2Rep`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L59).

> The representation of `SL(2,ℂ)` on real Lorentz covectors, obtained from the
> representation of the Lorentz group through the covering map
> `SL(2,ℂ) →* LorentzGroup 3`.

```lean
noncomputable def sl2Rep : Representation ℝ SL(2,ℂ) Lorentz.CoVector
```

**`Lorentz.CoVector.sl2Rep_dual_dualBasis`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/RealTensor/CoVector/Representation.lean#L64).

> The dual of the covector representation on the dual basis: dual covectors
> transform contravariantly, by the columns of the Lorentz matrix.

```lean
lemma sl2Rep_dual_dualBasis (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    Lorentz.CoVector.sl2Rep.dual Λ (Lorentz.CoVector.basis.dualBasis μ) =
      ∑ j, (Lorentz.SL2C.toLorentzGroup Λ).1 j μ •
        Lorentz.CoVector.basis.dualBasis j
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../../physlib/relativity/sl2c/basic.md)
- [Representation of the Lorentz group on Lorentz vectors](../../../physlib/relativity/tensors/part-03/realtensor-covector-representation.md)

## Proof depends on

- [Dual representations on a dual basis](../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/RealTensor/CoVector/Representation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/RealTensor/CoVector/Representation.lean)
