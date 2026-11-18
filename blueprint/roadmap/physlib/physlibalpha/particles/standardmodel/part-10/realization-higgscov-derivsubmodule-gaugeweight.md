---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight, StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_supp
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the Higgs sector

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.DerivSubmodule.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/GaugeWeight.lean): 2 declarations, 2 with a docstring.

## i. Overview

> The Higgs and conjugate-Higgs submodules carrying `n` derivatives each come with a gauge
> weight decomposition, and the two join to one of `derivSubmodule n`.  The weights that
> occur are the two Higgs weights `(0, 0, ∓1, -3)` and the two conjugate-Higgs weights
> `(0, 0, ±1, 3)`; they do not depend on the number of derivatives.

## ii. Key results

> - `derivSubmoduleGaugeWeight`
> - `derivSubmoduleGaugeWeight_supp` : the gauge weights occurring in the Higgs derivative submodules:
>   the two Higgs weights `(0, 0, ∓1, -3)` and the two conjugate-Higgs weights `(0, 0, ±1, 3)`

## iv. References

> * None.

## A. The gauge weight decomposition

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight`**, an instance, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/GaugeWeight.lean#L64).

> **The gauge weight decomposition of the Higgs derivative submodules**: the join of
> the decompositions of the Higgs and conjugate-Higgs submodules, whose weights are
> `(0, 0, ∓1, -3)` and `(0, 0, ±1, 3)` respectively.
>
> This is an instance: its statement mentions `h`, so unification against the goal
> recovers the sector and with it the rest of the structure's implicit data.

```lean
noncomputable instance derivSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition rep (h.derivSubmodule n)
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_supp`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/GaugeWeight.lean#L73).

> The gauge weights occurring in the Higgs derivative submodules: the two Higgs
> weights `(0, 0, ∓1, -3)` and the two conjugate-Higgs weights `(0, 0, ±1, 3)`.

```lean
lemma derivSubmoduleGaugeWeight_supp (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).supp
      = {((0, 0, -1, -3) : GaugeWeight), (0, 0, 1, -3), (0, 0, 1, 3), (0, 0, -1, 3)}
```

## Depends on

- [The derivative submodules of the Higgs sector](realization-higgscov-derivsubmodule-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/GaugeWeight.lean)
