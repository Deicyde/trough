---
declaration: module
origin: cited
lean: BoundedMeasurable.indicatorEffect, BoundedMeasurable.coe_indicatorEffect, BoundedMeasurable.outcomeMeasurement
statement: formalized
proof: formalized
---

# Observables of a sample space

The module `PhyslibAlpha.ProbabilisticTheory.Classical.BoundedMeasurable`, [PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean): 6 declarations (3 instances with no name), 2 with a docstring.

> Bounded measurable functions on a sample space as a classical order-unit lattice.

## i. Overview

> The observables of a sample space `Ω` are the bounded measurable functions on `Ω`, ordered
> pointwise, with the constant function `1` as order unit. They form a classical system whose
> observables are even a lattice. For a mechanical system, `Ω` is its phase space; for a measurement,
> `Ω` is its set of outcomes. Asking whether the outcome lies in a measurable set `A` is the effect
> `1_A`; these effects form the effect-valued measure of the outcome.

## ii. Key results

> - `BoundedMeasurable Ω` is an order-unit lattice.
> - `BoundedMeasurable.indicatorEffect` : the effect testing whether the outcome lies in a set.
> - `BoundedMeasurable.outcomeMeasurement` : the effect-valued measure of the outcome.

## iv. References

> * None.

## A. The order-unit space

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean#L59).

```lean
instance : OrderUnitSpace (BoundedMeasurable Ω)
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean#L66).

```lean
instance : ArchimedeanOrderUnitSpace (BoundedMeasurable Ω)
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean#L70).

```lean
instance : OrderUnitLattice (BoundedMeasurable Ω)
```

## B. Indicator effects

**`BoundedMeasurable.indicatorEffect`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean#L88).

> The effect testing whether the outcome lies in `s`.

```lean
noncomputable def indicatorEffect (s : Set Ω) (hs : MeasurableSet s) :
    Effect (BoundedMeasurable Ω)
```

**`BoundedMeasurable.coe_indicatorEffect`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean#L92).

```lean
lemma coe_indicatorEffect (s : Set Ω) (hs : MeasurableSet s) :
    (indicatorEffect s hs : BoundedMeasurable Ω) = indicator s hs
```

**`BoundedMeasurable.outcomeMeasurement`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean#L96).

> The effect-valued measure of the outcome: the set `A` is the effect `1_A`.

```lean
noncomputable def outcomeMeasurement : EffectValuedMeasure Ω (BoundedMeasurable Ω)
```

## Depends on

- [Bounded measurable functions](../../mathematics/part-02/measuretheory/boundedmeasurable.md)
- [Effect-valued measures](../measurement/effectvaluedmeasure.md)
- [Lattice-ordered observables](../orderunit/lattice.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BoundedMeasurable.lean)
