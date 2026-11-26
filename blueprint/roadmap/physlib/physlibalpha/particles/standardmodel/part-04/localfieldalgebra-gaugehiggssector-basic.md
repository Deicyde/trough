---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra, StandardModel.LocalCovFieldAlgebra.higgsMassWeight_mul_gaugeMassWeight_le, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_le, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_eq_bot_of_lt_six, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_seven, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_six, StandardModel.LocalCovFieldAlgebra.mul_le_sectorMassWeight_gauge_higgs, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_eight
statement: formalized
proof: formalized
---

# The mixed gauge-Higgs sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.GaugeHiggsSector.Basic`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean): 8 declarations, 8 with a docstring.

> The gauge-Higgs sector of the Standard Model's covariant field algebra, as a join of products.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> The field-strength towers are bosonic, so they commute with every Higgs tower
> (`LocalCovFieldAlgebra.F_comm_H`, `LocalCovFieldAlgebra.F_comm_barH`). Consequently the gauge
> algebra and the Higgs algebra commute (`commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra`), and so do
> their mass-weight submodules in either order (`higgsMassWeight_mul_gaugeMassWeight_le`). Feeding
> this into the abstract two-class bound `sectorMassWeight_pair_le` gives the mixed `{gauge, scalar}`
> sector's weight-`w` piece as a join, over the splittings of `w` into two non-zero parts, of products
> of the two sectors' own mass-weight submodules (`sectorMassWeight_gauge_higgs_le`).
>
> Both a non-zero gauge weight and a non-zero Higgs weight are even, and they are at
> least `4` and `2` respectively. So the mixed sector vanishes below weight `6` and at
> every odd weight. At weight `6` it is exactly the underived field strength against the
> underived Higgs, and at weight `8` it is bounded by the field strength against the
> weight-four Higgs terms together with the once-derived field strength against the
> underived Higgs.

## ii. Key results

> - `commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra` : the gauge algebra and the Higgs algebra
>   commute element-wise.
> - `sectorMassWeight_gauge_higgs_le` : the mixed gauge-Higgs sector as a join of products.
> - `sectorMassWeight_gauge_higgs_six`, `sectorMassWeight_gauge_higgs_eight` : the mixed sector at
>   weights six and eight.

## iv. References

> * None.

## A. The mixed gauge-Higgs sector

**`StandardModel.LocalCovFieldAlgebra.commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L71).

> The gauge algebra and the Higgs algebra commute element-wise.

```lean
lemma commute_of_mem_gaugeAlgebra_of_mem_higgsAlgebra {x y : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ GaugeSector.gaugeAlgebra) (hy : y ∈ ScalarSector.higgsAlgebra) :
    Commute x y
```

**`StandardModel.LocalCovFieldAlgebra.higgsMassWeight_mul_gaugeMassWeight_le`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L93).

> The Higgs and gauge mass-weight submodules commute past each other.

```lean
lemma higgsMassWeight_mul_gaugeMassWeight_le (a b : ℕ) :
    ScalarSector.massWeightSubmodule a * GaugeSector.massWeightSubmodule b
      ≤ GaugeSector.massWeightSubmodule b * ScalarSector.massWeightSubmodule a
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_le`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L103).

> The mixed gauge-Higgs sector decomposition.

```lean
lemma sectorMassWeight_gauge_higgs_le (w : ℕ) :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w
      ≤ ⨆ (p : ℕ × ℕ) (_ : p.1 + p.2 = w) (_ : p.1 ≠ 0) (_ : p.2 ≠ 0),
        GaugeSector.massWeightSubmodule p.1 * ScalarSector.massWeightSubmodule p.2
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_eq_bot_of_lt_six`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L120).

> The mixed gauge-Higgs sector vanishes below weight `6`.

```lean
lemma sectorMassWeight_gauge_higgs_eq_bot_of_lt_six {w : ℕ} (hw : w < 6) :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w = ⊥
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_seven`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L140).

> The mixed gauge-Higgs sector vanishes at weight `7`, since both a gauge weight and a
> Higgs weight are even, so they cannot sum to an odd number.

```lean
lemma sectorMassWeight_gauge_higgs_seven :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} 7 = ⊥
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_six`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L162).

> The mixed gauge-Higgs sector at weight `6` is exactly the product of the
> underived field strength with the underived Higgs, the only surviving splitting being
> `4 + 2`.

```lean
lemma sectorMassWeight_gauge_higgs_six :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} 6
      = GaugeSector.derivSubmodule 0 * ScalarSector.derivSubmodule 0
```

**`StandardModel.LocalCovFieldAlgebra.mul_le_sectorMassWeight_gauge_higgs`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L201).

> A product of a gauge-weight piece and a Higgs-weight piece lands in the mixed
> sector of the total weight.

```lean
lemma mul_le_sectorMassWeight_gauge_higgs {a b w : ℕ}
    {X Y : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (ha : a ≠ 0) (hb : b ≠ 0) (hab : a + b = w)
    (hX : X ≤ GaugeSector.massWeightSubmodule a)
    (hY : Y ≤ ScalarSector.massWeightSubmodule b) :
    X * Y ≤ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_higgs_eight`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean#L221).

> The mixed gauge-Higgs sector at weight `8`. The surviving splittings are
> `4 + 4` and `6 + 2`, giving the field strength against the weight-four Higgs terms
> and the once-derived field strength against the underived Higgs.

```lean
lemma sectorMassWeight_gauge_higgs_eight :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} 8
      = GaugeSector.derivSubmodule 0 * ScalarSector.derivSubmodule 1
        ⊔ GaugeSector.derivSubmodule 0 * ScalarSector.derivSubmodule 0
          * ScalarSector.derivSubmodule 0
        ⊔ GaugeSector.derivSubmodule 1 * ScalarSector.derivSubmodule 0
```

## Depends on

- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [The mass-weight grading of the gauge sector](localfieldalgebra-gaugesector-massweight-basic.md)
- [The derivative submodules of the scalar sector](../part-05/localfieldalgebra-scalarsector-derivsubmodule-ba.md)

## Proof depends on

- [The one-kind sectors of the Standard Model](../part-05/localfieldalgebra-localcovfieldalgebra-sectors.md)
- [The mass-weight grading of the scalar sector, in derivative submodules](../part-05/localfieldalgebra-scalarsector-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/Basic.lean)
