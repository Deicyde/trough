---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.derivSubmoduleGaugeWeight, StandardModel.ScalarSector.derivSubmoduleGaugeWeight_supp
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the scalar sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.DerivSubmodule.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/GaugeWeight.lean): 2 declarations, 2 with a docstring.

> The gauge weight decomposition of the Higgs derivative submodules and the weights that occur.

## i. Overview

> The Higgs and conjugate-Higgs submodules carrying `n` derivatives each come with a gauge
> weight decomposition, and the two join to one of `derivSubmodule n`. The weights that
> occur are the two Higgs weights `(0, 0, ∓1, -3)` and the two conjugate-Higgs weights
> `(0, 0, ±1, 3)`; they do not depend on the number of derivatives.

## ii. Key results

> - `derivSubmoduleGaugeWeight` : the gauge weight decomposition of the Higgs derivative
>   submodules.
> - `derivSubmoduleGaugeWeight_supp` : the gauge weights occurring in the Higgs derivative
>   submodules, the two Higgs weights `(0, 0, ∓1, -3)` and the two conjugate-Higgs weights
>   `(0, 0, ±1, 3)`.

## iv. References

> * None.

## A. The gauge weight decomposition

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight`**, an instance, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/GaugeWeight.lean#L58).

> The gauge weight decomposition of the Higgs derivative submodules, the join of
> the decompositions of the Higgs and conjugate-Higgs submodules, whose weights are
> `(0, 0, ∓1, -3)` and `(0, 0, ±1, 3)` respectively.

```lean
noncomputable instance derivSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition repGaugeGroupI (derivSubmodule n)
```

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_supp`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/GaugeWeight.lean#L67).

> The gauge weights occurring in the Higgs derivative submodules are the two Higgs
> weights `(0, 0, ∓1, -3)` and the two conjugate-Higgs weights `(0, 0, ±1, 3)`.

```lean
lemma derivSubmoduleGaugeWeight_supp (n : ℕ) :
    (derivSubmoduleGaugeWeight n).supp
      = {((0, 0, -1, -3) : GaugeWeight), (0, 0, 1, -3), (0, 0, 1, 3), (0, 0, -1, 3)}
```

## Depends on

- [The derivative submodules of the scalar sector](localfieldalgebra-scalarsector-derivsubmodule-ba.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/GaugeWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/GaugeWeight.lean)
