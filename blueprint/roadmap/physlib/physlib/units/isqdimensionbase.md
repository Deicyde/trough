---
declaration: module
origin: cited
lean: ISQDimensionBase, ISQDimensionBase.card_eq_seven, ISQDimensionBase.charge, ISQDimensionBase.charge_exponent_current, ISQDimensionBase.charge_exponent_time, ISQDimensionBase.charge_exponent_mass, ISQDimensionBase.single_amount_ne_one, ISQDimensionBase.single_luminousIntensity_ne_one
statement: formalized
proof: formalized
---

# The ISQ base quantities

The module `Physlib.Units.ISQDimensionBase`, [Physlib/Units/ISQDimensionBase.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean): 10 declarations (2 instances with no name), 8 with a docstring.

> The International System of Quantities (ISQ), specified in ISO/IEC 80000-1 and
> described in the International Vocabulary of Metrology (VIM, 3rd edition,
> JCGM 200:2012), fixes seven mutually independent *base quantities*: length, mass,
> time, electric current, thermodynamic temperature, amount of substance, and
> luminous intensity.
>
> `ISQDimensionBase` is that seven-element basis, realised as an instantiation
> `Dimension ISQDimensionBase` of the parametric dimensional algebra. It differs from
> PhysLib's default `LTMCTDimensionBase` in two ways:
>
> * the electromagnetic base quantity is *electric current*, so electric charge is a
>   *derived* dimension (`Q = I · T`, `ISQDimensionBase.charge`); and
> * *amount of substance* and *luminous intensity* are additional independent base
>   quantities.

## References

> * ISO/IEC 80000-1:2009, Quantities and units — Part 1: General. [ref: iso\_80000\_1\_2009]
> * JCGM 200:2012, International vocabulary of metrology — Basic and general concepts and associated
>   terms (VIM, 3rd edition). [ref: jcgm\_200\_2012]

**`ISQDimensionBase`**, an inductive, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L44).

> The seven ISQ base quantities (ISO/IEC 80000-1; VIM 3rd edition). Unlike
> `LTMCTDimensionBase`, electric current is the electromagnetic base quantity (so
> charge is derived), and amount of substance and luminous intensity are further
> base quantities.

```lean
inductive ISQDimensionBase where
  /-- The length base quantity. -/
  | length
  /-- The mass base quantity. -/
  | mass
  /-- The time base quantity. -/
  | time
  /-- The electric-current base quantity. -/
  | current
  /-- The thermodynamic-temperature base quantity. -/
  | temperature
  /-- The amount-of-substance base quantity. -/
  | amount
  /-- The luminous-intensity base quantity. -/
  | luminousIntensity
```

**An instance with no name**, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L61).

```lean
instance : Fintype ISQDimensionBase
```

**An instance with no name**, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L65).

```lean
instance : DimensionBasis ISQDimensionBase
```

**`ISQDimensionBase.card_eq_seven`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L70).

> The ISQ has seven base quantities.

```lean
lemma card_eq_seven : Fintype.card ISQDimensionBase = 7
```

**`ISQDimensionBase.charge`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L73).

> Electric charge is a *derived* dimension in the ISQ: `Q = I · T`.

```lean
def charge : Dimension ISQDimensionBase
```

**`ISQDimensionBase.charge_exponent_current`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L76).

> The derived charge dimension has electric-current exponent `1`.

```lean
lemma charge_exponent_current : charge.exponent .current = 1
```

**`ISQDimensionBase.charge_exponent_time`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L80).

> The derived charge dimension has time exponent `1`.

```lean
lemma charge_exponent_time : charge.exponent .time = 1
```

**`ISQDimensionBase.charge_exponent_mass`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L84).

> The derived charge dimension has mass exponent `0`.

```lean
lemma charge_exponent_mass : charge.exponent .mass = 0
```

**`ISQDimensionBase.single_amount_ne_one`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L89).

> Amount of substance is an independent base dimension (absent from
> `LTMCTDimensionBase`).

```lean
lemma single_amount_ne_one : single (.amount : ISQDimensionBase) ≠ 1
```

**`ISQDimensionBase.single_luminousIntensity_ne_one`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean#L96).

> Luminous intensity is an independent base dimension (absent from
> `LTMCTDimensionBase`).

```lean
lemma single_luminousIntensity_ne_one :
    single (.luminousIntensity : ISQDimensionBase) ≠ 1
```

## Depends on

- [Dimension](dimension.md)

## Sources

- [Physlib/Units/ISQDimensionBase.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQDimensionBase.lean)
