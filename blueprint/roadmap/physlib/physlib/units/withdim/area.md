---
declaration: module
origin: cited
lean: DimArea, DimArea.squareMeter, DimArea.squareFoot, DimArea.squareMile, DimArea.are, DimArea.hectare, DimArea.acre, DimArea.squareMeter_in_SI
statement: formalized
proof: formalized
---

# Area

The module `Physlib.Units.WithDim.Area`, [Physlib/Units/WithDim/Area.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean): 14 declarations, 8 with a docstring.

> In this module we define the dimensionful type corresponding to an area.
> We define specific instances of areas, such as square meters, square feet, etc.

**`DimArea`**, an abbrev, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L24).

> The type of areas in the absence of a choice of unit.

```lean
abbrev DimArea : Type
```

## Basic areas

**`DimArea.squareMeter`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L39).

> The dimensional area corresponding to 1 square meter.

```lean
noncomputable def squareMeter : DimArea
```

**`DimArea.squareFoot`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L42).

> The dimensional area corresponding to 1 square foot.

```lean
noncomputable def squareFoot : DimArea
```

**`DimArea.squareMile`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L46).

> The dimensional area corresponding to 1 square mile.

```lean
noncomputable def squareMile : DimArea
```

**`DimArea.are`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L50).

> The dimensional area corresponding to 1 are (100 square meters).

```lean
noncomputable def are : DimArea
```

**`DimArea.hectare`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L53).

> The dimensional area corresponding to 1 hectare (10,000 square meters).

```lean
noncomputable def hectare : DimArea
```

**`DimArea.acre`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L56).

> The dimensional area corresponding to 1 acre (1/640 square miles).

```lean
noncomputable def acre : DimArea
```

## Area in SI units

**`DimArea.squareMeter_in_SI`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L66).

```lean
lemma squareMeter_in_SI : squareMeter.1 SI = ⟨1⟩
```

**`DimArea.squareFoot_in_SI`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L71).

```lean
lemma squareFoot_in_SI : squareFoot.1 SI = ⟨0.09290304⟩
```

**`DimArea.squareMile_in_SI`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L79).

```lean
lemma squareMile_in_SI : squareMile.1 SI = ⟨2589988.110336⟩
```

**`DimArea.are_in_SI`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L86).

```lean
lemma are_in_SI : are.1 SI = ⟨100⟩
```

**`DimArea.hectare_in_SI`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L90).

```lean
lemma hectare_in_SI : hectare.1 SI = ⟨10000⟩
```

**`DimArea.acre_in_SI`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L95).

```lean
lemma acre_in_SI : acre.1 SI = ⟨4046.8564224⟩
```

> ## Relations between areas

**`DimArea.acre_eq_mul_squareFeet`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean#L109).

> One acre is exactly `43560` square feet.

```lean
lemma acre_eq_mul_squareFeet : acre = (43560 : ℝ≥0) • squareFoot
```

## Depends on

- [Physlib.Units.WithDim.Basic](basic.md)

## Sources

- [Physlib/Units/WithDim/Area.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Area.lean)
