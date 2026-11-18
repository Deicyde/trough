---
declaration: module
origin: cited
lean: StandardModel.UnbrokenGaugeGroupI, StandardModel.UnbrokenGaugeGroupI.incl, StandardModel.UnbrokenGaugeGroupI.incl_toSU3, StandardModel.UnbrokenGaugeGroupI.incl_toSU2, StandardModel.UnbrokenGaugeGroupI.incl_toU1
statement: formalized
proof: formalized
---

# The unbroken gauge group

The module `Physlib.Particles.StandardModel.GaugeGroup.Unbroken`, [Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean): 5 declarations, 2 with a docstring.

> We define the gauge group `SU(3) × U(1)_EM` left unbroken by the Higgs vacuum.

## i. Overview

> A non-zero Higgs vacuum breaks `SU(3) × SU(2) × U(1)` down to color and electromagnetism,
> `SU(3) × U(1)_EM`. This file defines that group and its inclusion into `GaugeGroupI`.

## ii. Key results

> - `UnbrokenGaugeGroupI`: The group `SU(3) × U(1)_EM`.
> - `UnbrokenGaugeGroupI.incl`: Its inclusion `(h, u) ↦ (h, diag(u³, ū³), u)` into `GaugeGroupI`.

## iv. References

> * Peskin & Schroeder, An Introduction to QFT, chapter 20. [ref: peskin\_schroeder\_qft]

## A. The unbroken gauge group

**`StandardModel.UnbrokenGaugeGroupI`**, an abbrev, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean#L49).

> The gauge group `SU(3) × U(1)_EM` left unbroken by the Higgs vacuum. As for `GaugeGroupI`,
> the `I` indicates that no discrete quotient is taken.

```lean
abbrev UnbrokenGaugeGroupI : Type
```

**`StandardModel.UnbrokenGaugeGroupI.incl`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean#L54).

> The inclusion `(h, u) ↦ (h, diag(u³, ū³), u)` of `SU(3) × U(1)_EM` into `GaugeGroupI`.

```lean
noncomputable def incl : UnbrokenGaugeGroupI →* GaugeGroupI
```

**`StandardModel.UnbrokenGaugeGroupI.incl_toSU3`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean#L61).

```lean
lemma incl_toSU3 (p : UnbrokenGaugeGroupI) : GaugeGroupI.toSU3 (incl p) = p.1
```

**`StandardModel.UnbrokenGaugeGroupI.incl_toSU2`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean#L64).

```lean
lemma incl_toSU2 (p : UnbrokenGaugeGroupI) :
    GaugeGroupI.toSU2 (incl p) = GaugeGroupI.diagSU2 (p.2 ^ 3)
```

**`StandardModel.UnbrokenGaugeGroupI.incl_toU1`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean#L68).

```lean
lemma incl_toU1 (p : UnbrokenGaugeGroupI) : GaugeGroupI.toU1 (incl p) = p.2
```

## Depends on

- [The Standard Model Gauge Group](basic.md)

## Sources

- [Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Unbroken.lean)
