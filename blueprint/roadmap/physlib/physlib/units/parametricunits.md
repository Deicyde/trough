---
declaration: module
origin: cited
lean: UnitScale, UnitScale.ratio_ne_zero, UnitScale.dimScale, UnitScale.dimScale_self, UnitScale.dimScale_one, UnitScale.dimScale_transitive, LTMCTUnitChoices.toScale
statement: formalized
proof: formalized
---

# The unit side, parametrised in the same basis

The module `Physlib.Units.ParametricUnits`, [Physlib/Units/ParametricUnits.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean): 7 declarations, 4 with a docstring.

> The dimension basis is parametric (`Dimension B`), but the *unit* side of the
> bridge is hardwired in parallel: `LTMCTUnitChoices` has five named unit fields and
> `LTMCTUnitChoices.dimScale` folds over exactly those five. This module provides the
> generic twin, parametrised in the same basis `B`.
>
> Every PhysLib base unit (`LengthUnit`, `TimeUnit`, …) is, structurally, a positive
> real (`{ val : ℝ // 0 < val }`); the typed names carry no extra algebraic content.
> So a unit choice over a basis `B` is a positive real per base dimension, and the
> scaling homomorphism folds the per-base unit ratio over `B`:
>
> * `UnitScale B` — a positive-real magnitude for each `b : B`.
> * `UnitScale.dimScale : UnitScale B → UnitScale B → Dimension B →* ℝ≥0` — the
>   `MonoidHom` `d ↦ ∏ b, (u₁ b / u₂ b) ^ d.exponent b`, generic in `B`.
>
> The current five-field `LTMCTUnitChoices.dimScale` is the `LTMCTDimensionBase` instance of this
> fold, written out by hand; `LTMCTUnitChoices.toScale` exhibits the correspondence.

**`UnitScale`**, a structure, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L40).

> A choice of unit for each base dimension of `B`: a positive-real magnitude per
> base. This is the basis-generic form of `LTMCTUnitChoices`.

```lean
structure UnitScale (B : Type) where
  /-- The positive-real magnitude of the chosen unit at each base dimension. -/
  scale : B → ℝ≥0
  /-- Each chosen unit has a positive magnitude. -/
  scale_pos : ∀ b, 0 < scale b
```

**`UnitScale.ratio_ne_zero`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L50).

```lean
lemma ratio_ne_zero (u1 u2 : UnitScale B) (b : B) : u1.scale b / u2.scale b ≠ 0
```

**`UnitScale.dimScale`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L57).

> The dimension-scaling homomorphism, generic in the basis `B`: a quantity of
> dimension `d` rescales by `∏ b, (u1 b / u2 b) ^ d.exponent b` when changing the
> unit choice from `u1` to `u2`. This is the basis-generic form of
> `LTMCTUnitChoices.dimScale`.

```lean
noncomputable def dimScale [DimensionBasis B] [Fintype B]
    (u1 u2 : UnitScale B) : Dimension B →* ℝ≥0
```

**`UnitScale.dimScale_self`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L68).

```lean
lemma dimScale_self [DimensionBasis B] [Fintype B] (u : UnitScale B) (d : Dimension B) :
    dimScale u u d = 1
```

**`UnitScale.dimScale_one`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L75).

```lean
lemma dimScale_one [DimensionBasis B] [Fintype B] (u1 u2 : UnitScale B) :
    dimScale u1 u2 1 = 1
```

**`UnitScale.dimScale_transitive`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L79).

> The scaling is transitive (a cocycle in the unit choices).

```lean
lemma dimScale_transitive [DimensionBasis B] [Fintype B]
    (u1 u2 u3 : UnitScale B) (d : Dimension B) :
    dimScale u1 u2 d * dimScale u2 u3 d = dimScale u1 u3 d
```

## The current five-field `LTMCTUnitChoices` is the `LTMCTDimensionBase` instance

> `LTMCTUnitChoices.toScale` reads the five typed units as a `UnitScale LTMCTDimensionBase`,
> exhibiting the existing bespoke `dimScale` as the `LTMCTDimensionBase` case of the generic
> fold.

**`LTMCTUnitChoices.toScale`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean#L101).

> Read a five-field `LTMCTUnitChoices` as a `UnitScale` over `LTMCTDimensionBase`.

```lean
noncomputable def toScale (u : LTMCTUnitChoices) : UnitScale LTMCTDimensionBase
```

## Depends on

- [Dimensions and unit](basic.md)

## Sources

- [Physlib/Units/ParametricUnits.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricUnits.lean)
