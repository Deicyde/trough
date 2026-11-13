---
declaration: module
origin: cited
lean: BoundedMeasurable.eq_sum_indicator, BoundedMeasurable.sum_indicator_singleton, ProbabilisticTheory.UnitalPositiveLinearMap.exists_le_add_smul_one, ProbabilisticTheory.UnitalPositiveLinearMap.isNormal_of_fintype, ProbabilisticTheory.Measurement.atomsChannel, ProbabilisticTheory.Measurement.ofAtoms, ProbabilisticTheory.Measurement.ofAtoms_toChannel_apply, ProbabilisticTheory.Measurement.coe_ofAtoms_apply
statement: formalized
proof: formalized
---

# Measurements with finitely many outcomes

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Finite`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean): 12 declarations, 9 with a docstring.

> Measurements with finitely many outcomes are the families of effects summing to `1`.

## i. Overview

> On a finite discrete outcome space, every observable of the outcome is a combination of the
> indicators of single outcomes. A measurement is therefore determined by the effects of its single
> outcomes, and these add up to `1`. Conversely, a family of effects adding up to `1` is a
> measurement: send the observable `f` to `∑ x, f x • a x`. Normality is automatic, since an
> increasing sequence of functions on finitely many points converges uniformly; this uses that the
> system is Archimedean.

## ii. Key results

> - `BoundedMeasurable.eq_sum_indicator` : an observable of a finite classical system is a combination
>   of point indicators.
> - `UnitalPositiveLinearMap.isNormal_of_fintype` : a channel from a finite classical system into an
>   Archimedean system is normal.
> - `Measurement.ofAtoms` : the measurement of a family of effects adding up to `1`.
> - `Measurement.eq_ofAtoms` : a measurement with finitely many outcomes is determined by the effects
>   of its outcomes.

## iv. References

> * None.

## A. Observables of a finite classical system

**`BoundedMeasurable.eq_sum_indicator`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L64).

> An observable of a finite classical system is a combination of point indicators.

```lean
lemma eq_sum_indicator (f : BoundedMeasurable Ω) :
    f = ∑ x, f x • indicator {x} (measurableSet_singleton x)
```

**`BoundedMeasurable.sum_indicator_singleton`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L71).

> The point indicators add up to the unit.

```lean
lemma sum_indicator_singleton :
    ∑ x, indicator {x} (measurableSet_singleton x) = (1 : BoundedMeasurable Ω)
```

## B. Normality is automatic

**`ProbabilisticTheory.UnitalPositiveLinearMap.exists_le_add_smul_one`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L91).

> An increasing sequence of functions on a finite set comes uniformly close to its least upper
> bound.

```lean
lemma exists_le_add_smul_one {f : ℕ → BoundedMeasurable Ω} (hf : Monotone f)
    {g : BoundedMeasurable Ω} (hg : IsLUB (Set.range f) g) {ε : ℝ} (hε : 0 < ε) :
    ∃ n, g ≤ f n + ε • 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isNormal_of_fintype`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L106).

> A channel from a finite classical system into an Archimedean system is normal.

```lean
lemma isNormal_of_fintype (Φ : Channel (BoundedMeasurable Ω) E) : Φ.IsNormal
```

## C. Measurements from their outcome effects

**`ProbabilisticTheory.Measurement.atomsChannel`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L128).

> The channel `f ↦ ∑ x, f x • a x` of a family of effects adding up to `1`.

```lean
noncomputable def atomsChannel (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1) :
    Channel (BoundedMeasurable Ω) E
```

**`ProbabilisticTheory.Measurement.ofAtoms`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L139).

> The measurement of a family of effects adding up to `1`: the outcome `x` has effect `a x`.

```lean
noncomputable def ofAtoms (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1) : Measurement Ω E
```

**`ProbabilisticTheory.Measurement.ofAtoms_toChannel_apply`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L144).

```lean
lemma ofAtoms_toChannel_apply (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1)
    (f : BoundedMeasurable Ω) : (ofAtoms a ha).toChannel f = ∑ x, f x • (a x : E)
```

**`ProbabilisticTheory.Measurement.coe_ofAtoms_apply`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L149).

```lean
lemma coe_ofAtoms_apply (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1) (s : Set Ω)
    (hs : MeasurableSet s) : (ofAtoms a ha s hs : E) = ∑ x, if x ∈ s then (a x : E) else 0
```

**`ProbabilisticTheory.Measurement.coe_ofAtoms_singleton`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L156).

```lean
lemma coe_ofAtoms_singleton (a : Ω → Effect E) (ha : ∑ x, (a x : E) = 1) (x : Ω)
    (hx : MeasurableSet {x}) : (ofAtoms a ha {x} hx : E) = a x
```

**`ProbabilisticTheory.Measurement.sum_singleton`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L163).

> The effects of the outcomes of a measurement add up to `1`.

```lean
lemma sum_singleton (M : Measurement Ω E) :
    ∑ x, (M {x} (measurableSet_singleton x) : E) = 1
```

**`ProbabilisticTheory.Measurement.eq_ofAtoms`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L168).

> A measurement with finitely many outcomes is the measurement of its outcome effects.

```lean
lemma eq_ofAtoms (M : Measurement Ω E) :
    M = ofAtoms (fun x => M {x} (measurableSet_singleton x)) M.sum_singleton
```

**`ProbabilisticTheory.Measurement.ext_of_singleton`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean#L175).

> Two measurements with finitely many outcomes agree when their outcome effects agree.

```lean
lemma ext_of_singleton {M N : Measurement Ω E}
    (h : ∀ x, M {x} (measurableSet_singleton x) = N {x} (measurableSet_singleton x)) :
    M = N
```

## Depends on

- [Measurements](basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Finite.lean)
