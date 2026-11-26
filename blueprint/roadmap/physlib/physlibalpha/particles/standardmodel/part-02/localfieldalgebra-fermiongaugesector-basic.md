---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra, StandardModel.LocalCovFieldAlgebra.fermionMassWeight_mul_gaugeMassWeight_le, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_le, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_eight, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_seven
statement: formalized
proof: formalized
---

# The mixed gauge-fermion sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionGaugeSector.Basic`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean): 6 declarations, 6 with a docstring.

> The gauge-fermion sector of the Standard Model's covariant field algebra, as a join of products.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> The field-strength towers are bosonic, so they commute with every fermion tower
> (`LocalCovFieldAlgebra.F_comm_d`, `LocalCovFieldAlgebra.F_comm_bard`, ...,
> `LocalCovFieldAlgebra.F_comm_bare`). Consequently the gauge algebra
> and the fermion algebra commute (`commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra`),
> and so do their mass-weight submodules in either order
> (`fermionMassWeight_mul_gaugeMassWeight_le`). Feeding this into the abstract two-class
> sector bound `sectorMassWeight_pair_le` gives the mixed `{gauge, fermion}` sector's
> weight-`w` piece as (the join over splittings of `w` into non-zero parts of) products
> of the gauge and fermion sectors' own mass-weight submodules
> (`sectorMassWeight_gauge_fermion_le`).
>
> Since a non-zero gauge weight is at least `4` and a non-zero fermion weight is at
> least `3`, the mixed sector vanishes below weight `7`
> (`sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven`) and at weight `8`
> (`sectorMassWeight_gauge_fermion_eight`), and at weight `7` is exactly the product of
> the underived field-strength submodule with the underived fermion submodule
> (`sectorMassWeight_gauge_fermion_seven`).

## ii. Key results

> - `commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra` : the gauge algebra and the fermion algebra
>   commute element-wise.
> - `sectorMassWeight_gauge_fermion_le` : the mixed gauge-fermion sector as a join of products.
> - `sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven`, `sectorMassWeight_gauge_fermion_eight` :
>   the mixed sector vanishes below weight `7` and at weight `8`.
> - `sectorMassWeight_gauge_fermion_seven` : the mixed sector at weight `7` is exactly the product
>   of the underived field strength with the underived fermion towers.

## iv. References

> * None.

## A. The gauge and fermion algebras commute

**`StandardModel.LocalCovFieldAlgebra.commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean#L79).

> The gauge algebra and the fermion algebra commute element-wise. Every generator of
> the gauge algebra commutes with every generator of the fermion algebra by the
> commutation rules `LocalCovFieldAlgebra.F_comm_d`, ..., `LocalCovFieldAlgebra.F_comm_bare`,
> and commutation extends from generators to the algebras they generate.

```lean
lemma commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra {x y : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ GaugeSector.gaugeAlgebra) (hy : y ∈ FermionSector.fermionAlgebra) :
    Commute x y
```

**`StandardModel.LocalCovFieldAlgebra.fermionMassWeight_mul_gaugeMassWeight_le`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean#L120).

> The fermion sector's mass-weight submodules and the gauge sector's mass-weight
> submodules commute past each other, in the order needed by
> `sectorMassWeight_pair_le`.

```lean
lemma fermionMassWeight_mul_gaugeMassWeight_le (a b : ℕ) :
    FermionSector.massWeightSubmodule a * GaugeSector.massWeightSubmodule b
      ≤ GaugeSector.massWeightSubmodule b * FermionSector.massWeightSubmodule a
```

## B. The mixed gauge-fermion sector

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_le`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean#L139).

> The mixed gauge-fermion sector decomposition. The weight-`w` piece of the
> `{gauge, fermion}` sector lies in the join, over the splittings of `w` into two
> non-zero parts, of the products of the gauge and fermion sectors' own mass-weight
> submodules.

```lean
lemma sectorMassWeight_gauge_fermion_le (w : ℕ) :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} w
      ≤ ⨆ (p : ℕ × ℕ) (_ : p.1 + p.2 = w) (_ : p.1 ≠ 0) (_ : p.2 ≠ 0),
        GaugeSector.massWeightSubmodule p.1 * FermionSector.massWeightSubmodule p.2
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean#L158).

> The mixed gauge-fermion sector vanishes below weight `7`. A non-zero gauge
> weight is at least `4` and a non-zero fermion weight is at least `3`, so no
> splitting of a weight below `7` into two non-zero parts can supply both.

```lean
lemma sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven {w : ℕ} (hw : w < 7) :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} w = ⊥
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_eight`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean#L181).

> The mixed gauge-fermion sector vanishes at weight `8`. The only splittings of
> `8` into two non-zero parts with a non-zero gauge weight and a non-zero fermion
> weight would need the gauge part to be `4` or `6` (with fermion part `4` or `2`), but
> the fermion sector vanishes at both `4` and `2`.

```lean
lemma sectorMassWeight_gauge_fermion_eight :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} 8 = ⊥
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_gauge_fermion_seven`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean#L205).

> The mixed gauge-fermion sector at weight `7` is exactly the product of the
> underived field-strength submodule with the underived fermion submodule, the only
> splitting of `7` into a non-zero gauge weight and a non-zero fermion weight that
> survives is `4 + 3`.

```lean
lemma sectorMassWeight_gauge_fermion_seven :
    fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} 7
      = GaugeSector.derivSubmodule 0 * FermionSector.derivSubmodule 0
```

## Depends on

- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [The mass-weight grading of the fermion sector](../part-03/localfieldalgebra-fermionsector-massweight-basic.md)
- [The mass-weight grading of the gauge sector](../part-04/localfieldalgebra-gaugesector-massweight-basic.md)

## Proof depends on

- [The one-kind sectors of the Standard Model](../part-05/localfieldalgebra-localcovfieldalgebra-sectors.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/Basic.lean)
