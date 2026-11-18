---
declaration: module
origin: cited
lean: ChargeUnit, ChargeUnit.coulombs, ChargeUnit.elementaryCharge
statement: formalized
proof: formalized
---

# The units of charge

The module `Physlib.Electromagnetism.Charge.ChargeUnit`, [Physlib/Electromagnetism/Charge/ChargeUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Charge/ChargeUnit.lean): 4 declarations (1 instance with no name), 3 with a docstring.

> A unit of charge corresponding to a choice of translationally-invariant
> metric on the charge manifold (to be defined diffeomorphic to `ℝ`).
> Such a choice is (non-canonically) equivalent to a
> choice of positive real number. We define the type `ChargeUnit` to be equivalent to the
> positive reals.
>
> We assume that the charge manifold is already defined with an orientation, with the
> electron being in the negative direction.
>
> On `ChargeUnit` there is an instance of division giving a real number, corresponding to the
> ratio of the two scales of temperature unit.
>
> To define specific charge units, we first state the existence of a
> a given charge unit, and then construct all other charge units from it.
> We choose to state the
> existence of the charge unit of the coulomb, and construct all other charge units from that.

**`ChargeUnit`**, a structure, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Charge/ChargeUnit.lean#L39).

> The choices of translationally-invariant metrics on the charge-manifold.
> Such a choice corresponds to a choice of units for charge.
> This assumes that an orientation has already being picked on the charge manifold.

```lean
structure ChargeUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Charge/ChargeUnit.lean#L44).

```lean
instance : PositiveRealUnitCore ChargeUnit
```

## Specific choices of charge units

> We define specific choices of charge units.
> We first define the notion of a columb to correspond to the charge unit with underlying value
> equal to `1`. This is really down to a choice in the isomorphism between the set of metrics
> on the charge manifold and the positive reals.

**`ChargeUnit.coulombs`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Charge/ChargeUnit.lean#L68).

> The definition of a charge unit of coulomb.

```lean
def coulombs : ChargeUnit
```

**`ChargeUnit.elementaryCharge`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Charge/ChargeUnit.lean#L71).

> The charge unit of a elementryCharge (1.602176634×10−19 coulomb).

```lean
noncomputable def elementaryCharge : ChargeUnit
```

## Depends on

- [A. Shared arithmetic for positive-real unit types](../../units/positiverealunit.md)

## Sources

- [Physlib/Electromagnetism/Charge/ChargeUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Charge/ChargeUnit.lean)
