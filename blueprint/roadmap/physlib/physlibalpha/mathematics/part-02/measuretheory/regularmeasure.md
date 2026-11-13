---
declaration: module
origin: cited
lean: MeasureTheory.Measure.InnerRegular.of_le, MeasureTheory.Measure.Regular.of_innerRegular, MeasureTheory.Measure.Regular.of_le, MeasureTheory.Measure.Regular.map_of_continuous, MeasureTheory.Measure.InnerRegular.comap_subtype
statement: formalized
proof: formalized
---

# Regular measures

The module `PhyslibAlpha.Mathematics.MeasureTheory.RegularMeasure`, [PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean): 5 declarations, 5 with a docstring.

> Inner regularity and regularity pass to smaller measures, continuous images and subsets.

## i. Overview

> A measure is regular when the measure of a set is approximated by compact sets from inside and by
> open sets from outside. For finite measures on a Hausdorff space the inner approximation is enough.
> Inner regularity passes to smaller measures, along continuous maps and to measurable subsets, and so
> regularity does too.

## ii. Key results

> - `MeasureTheory.Measure.InnerRegular.of_le` proves that a measure below a finite inner regular
>   measure is inner regular.
> - `MeasureTheory.Measure.Regular.of_innerRegular` proves that a finite inner regular measure is
>   regular.
> - `MeasureTheory.Measure.Regular.map_of_continuous` proves that regularity passes along continuous
>   maps.
> - `MeasureTheory.Measure.InnerRegular.comap_subtype` proves that inner regularity passes to
>   measurable subsets.

## iv. References

> * None.

## A. Measures below inner regular measures

**`MeasureTheory.Measure.InnerRegular.of_le`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean#L60).

> A measure below a finite inner regular measure is inner regular.

```lean
lemma InnerRegular.of_le [OpensMeasurableSpace α] [T2Space α] [IsFiniteMeasure μ]
    [InnerRegular μ] (h : ν ≤ μ) : InnerRegular ν
```

## B. Regularity from inner regularity

**`MeasureTheory.Measure.Regular.of_innerRegular`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean#L76).

> A finite inner regular measure on a Hausdorff space is regular.

```lean
lemma Regular.of_innerRegular [T2Space α] [BorelSpace α] [IsFiniteMeasure μ] [InnerRegular μ] :
    Regular μ
```

**`MeasureTheory.Measure.Regular.of_le`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean#L83).

> A measure below a finite inner regular measure on a Hausdorff space is regular.

```lean
lemma Regular.of_le [T2Space α] [BorelSpace α] [IsFiniteMeasure μ] [InnerRegular μ] (h : ν ≤ μ) :
    Regular ν
```

**`MeasureTheory.Measure.Regular.map_of_continuous`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean#L91).

> A finite regular measure pushes forward to a regular measure along a continuous map into a
> Hausdorff space.

```lean
lemma Regular.map_of_continuous {β : Type*} [TopologicalSpace β] [MeasurableSpace β]
    [BorelSpace β] [T2Space β] [BorelSpace α] [IsFiniteMeasure μ] [Regular μ] {f : α → β}
    (hf : Continuous f) : Regular (μ.map f)
```

**`MeasureTheory.Measure.InnerRegular.comap_subtype`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean#L98).

> An inner regular measure stays inner regular on a measurable subset.

```lean
lemma InnerRegular.comap_subtype [InnerRegular μ] {s : Set α} (hs : MeasurableSet s) :
    InnerRegular (μ.comap ((↑) : s → α))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RegularMeasure.lean)
