---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra, StandardModel.CovAlgebraRealization.higgsMassWeight_mul_gaugeMassWeight_le, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_le, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_eq_bot_of_lt_six, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_seven, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_six, StandardModel.CovAlgebraRealization.mul_le_sectorMassWeight_gauge_higgs, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_eight
statement: formalized
proof: formalized
---

# The mixed gauge-Higgs sector

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.GaugeHiggsSector.Basic`, [PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean): 8 declarations, 8 with a docstring.

## i. Overview

> The field-strength towers are bosonic, so they commute with every Higgs tower
> (`h.F_comm_H`, `h.F_comm_barH`); consequently the gauge algebra and the Higgs algebra
> commute (`commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra`), and so do their
> mass-weight submodules in either order (`higgsMassWeight_mul_gaugeMassWeight_le`).
> Feeding this into the abstract two-class bound `sectorMassWeight_pair_le` gives the
> mixed `{gauge, higgs}` sector's weight-`w` piece as a join, over the splittings of `w`
> into two non-zero parts, of products of the two sectors' own mass-weight submodules
> (`sectorMassWeight_gauge_higgs_le`).
>
> Both a non-zero gauge weight and a non-zero Higgs weight are even, and they are at
> least `4` and `2` respectively.  So the mixed sector vanishes below weight `6` and at
> every odd weight; at weight `6` it is exactly the underived field strength against the
> underived Higgs, and at weight `8` it is bounded by the field strength against the
> weight-four Higgs terms together with the once-derived field strength against the
> underived Higgs.

## ii. Key results

> - `commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra` : the gauge algebra and the Higgs algebra
>   commute element-wise
> - `higgsMassWeight_mul_gaugeMassWeight_le` : the Higgs and gauge mass-weight submodules commute past
>   each other
> - `sectorMassWeight_gauge_higgs_le` : the mixed gauge-Higgs sector decomposition

## iv. References

> * None.

## A. The mixed gauge-Higgs sector

**`StandardModel.CovAlgebraRealization.commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L71).

> The gauge algebra and the Higgs algebra commute element-wise.

```lean
lemma commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra {x y : B}
    (hx : x ∈ h.isGaugeSector.gaugeAlgebra) (hy : y ∈ h.isHiggsSector.higgsAlgebra) :
    Commute x y
```

**`StandardModel.CovAlgebraRealization.higgsMassWeight_mul_gaugeMassWeight_le`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L92).

> The Higgs and gauge mass-weight submodules commute past each other.

```lean
lemma higgsMassWeight_mul_gaugeMassWeight_le (a b : ℕ) :
    h.isHiggsSector.massWeightSubmodule a * h.isGaugeSector.massWeightSubmodule b
      ≤ h.isGaugeSector.massWeightSubmodule b * h.isHiggsSector.massWeightSubmodule a
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_le`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L102).

> The mixed gauge-Higgs sector decomposition.

```lean
lemma sectorMassWeight_gauge_higgs_le (w : ℕ) :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w
      ≤ ⨆ (p : ℕ × ℕ) (_ : p.1 + p.2 = w) (_ : p.1 ≠ 0) (_ : p.2 ≠ 0),
        h.isGaugeSector.massWeightSubmodule p.1 * h.isHiggsSector.massWeightSubmodule p.2
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_eq_bot_of_lt_six`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L117).

> The mixed gauge-Higgs sector vanishes below weight `6`.

```lean
lemma sectorMassWeight_gauge_higgs_eq_bot_of_lt_six {w : ℕ} (hw : w < 6) :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w = ⊥
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_seven`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L137).

> The mixed gauge-Higgs sector vanishes at weight `7`: both a gauge weight and a
> Higgs weight are even, so they cannot sum to an odd number.

```lean
lemma sectorMassWeight_gauge_higgs_seven :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} 7 = ⊥
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_six`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L159).

> **The mixed gauge-Higgs sector at weight `6`** is exactly the product of the
> underived field strength with the underived Higgs: the only surviving splitting is
> `4 + 2`.

```lean
lemma sectorMassWeight_gauge_higgs_six :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} 6
      = h.isGaugeSector.derivSubmodule 0 * h.isHiggsSector.derivSubmodule 0
```

**`StandardModel.CovAlgebraRealization.mul_le_sectorMassWeight_gauge_higgs`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L198).

> A product of a gauge-weight piece and a Higgs-weight piece lands in the mixed
> sector of the total weight.

```lean
lemma mul_le_sectorMassWeight_gauge_higgs {a b w : ℕ} {X Y : Submodule ℂ B}
    (ha : a ≠ 0) (hb : b ≠ 0) (hab : a + b = w)
    (hX : X ≤ h.isGaugeSector.massWeightSubmodule a)
    (hY : Y ≤ h.isHiggsSector.massWeightSubmodule b) :
    X * Y ≤ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_higgs_eight`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean#L216).

> **The mixed gauge-Higgs sector at weight `8`.** The surviving splittings are
> `4 + 4` and `6 + 2`, giving the field strength against the weight-four Higgs terms
> and the once-derived field strength against the underived Higgs.

```lean
lemma sectorMassWeight_gauge_higgs_eight :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} 8
      = h.isGaugeSector.derivSubmodule 0 * h.isHiggsSector.derivSubmodule 1
        ⊔ h.isGaugeSector.derivSubmodule 0 * h.isHiggsSector.derivSubmodule 0
          * h.isHiggsSector.derivSubmodule 0
        ⊔ h.isGaugeSector.derivSubmodule 1 * h.isHiggsSector.derivSubmodule 0
```

## Depends on

- [The sectors of the field algebra](covrealization-sectors.md)
- [The derivative submodules of the Higgs sector](../part-10/realization-higgscov-derivsubmodule-basic.md)

## Proof depends on

- [The mass-weight grading of the Higgs sector, in derivative submodules](../part-10/realization-higgscov-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/Basic.lean)
