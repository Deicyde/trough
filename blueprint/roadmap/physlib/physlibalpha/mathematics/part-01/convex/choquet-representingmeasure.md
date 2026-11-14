---
declaration: module
origin: cited
lean: Choquet.IsRepresentingMeasure, Choquet.representingMeasures, Choquet.restrictCLM, Choquet.isClosed_representingMeasures, Choquet.ChoquetLE, Choquet.ChoquetLE.refl, Choquet.ChoquetLE.trans, Choquet.isClosed_setOf_choquetLE
statement: formalized
proof: formalized
---

# Representing measures and the Choquet order

The module `PhyslibAlpha.Mathematics.Convex.Choquet.RepresentingMeasure`, [PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean): 14 declarations, 9 with a docstring.

> Representing measures of points of a convex set, the Choquet order, and maximal measures.

## i. Overview

> A probability measure on a convex set `S` represents a point `x` when `x` is its average: every
> continuous linear functional takes at `x` its average value under the measure. For states, a
> representing measure is a way to prepare the state as a random mixture.
>
> A point has many representing measures, the Dirac measure at the point being the trivial one. One
> measure is higher than another in the Choquet order when it gives every continuous convex function a
> larger average. Higher measures push their weight further out, towards the extreme points. On a
> compact set every point has a representing measure that is maximal in this order.

## ii. Key results

> - `Choquet.IsRepresentingMeasure` states that a probability measure represents a point.
> - `Choquet.ChoquetLE` is the Choquet order.
> - `Choquet.ChoquetLE.isRepresentingMeasure` proves that a higher measure represents the same point.
> - `Choquet.exists_isChoquetMaximalAt` proves that every point has a maximal representing measure.

## iv. References

> * None.

## A. Representing measures

**`Choquet.IsRepresentingMeasure`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L64).

> A probability measure represents `x` when every continuous linear functional has the same
> value at `x` as its integral.

```lean
def IsRepresentingMeasure (x : S) (μ : ProbabilityMeasure S) : Prop
```

**`Choquet.representingMeasures`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L68).

> The probability measures representing `x`.

```lean
def representingMeasures (x : S) : Set (ProbabilityMeasure S)
```

**`Choquet.restrictCLM`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L72).

> A continuous linear functional, as a continuous function on `S`.

```lean
def restrictCLM (ℓ : V →L[ℝ] ℝ) : C(S, ℝ)
```

**`Choquet.isClosed_representingMeasures`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L75).

```lean
lemma isClosed_representingMeasures (x : S) : IsClosed (representingMeasures x)
```

## B. The Choquet order

**`Choquet.ChoquetLE`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L88).

> The Choquet order: `ν` gives every continuous convex function at least the integral `μ`
> gives it.

```lean
def ChoquetLE (μ ν : ProbabilityMeasure S) : Prop
```

**`Choquet.ChoquetLE.refl`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L92).

```lean
lemma ChoquetLE.refl (μ : ProbabilityMeasure S) : ChoquetLE hS μ μ
```

**`Choquet.ChoquetLE.trans`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L95).

```lean
lemma ChoquetLE.trans {μ ν ρ : ProbabilityMeasure S} (hμν : ChoquetLE hS μ ν)
    (hνρ : ChoquetLE hS ν ρ) : ChoquetLE hS μ ρ
```

**`Choquet.isClosed_setOf_choquetLE`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L99).

```lean
lemma isClosed_setOf_choquetLE (μ : ProbabilityMeasure S) :
    IsClosed {ν : ProbabilityMeasure S | ChoquetLE hS μ ν}
```

**`Choquet.ChoquetLE.isRepresentingMeasure`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L107).

> Moving up the Choquet order keeps the represented point.

```lean
lemma ChoquetLE.isRepresentingMeasure {x : S} {μ ν : ProbabilityMeasure S}
    (hμ : IsRepresentingMeasure x μ) (hμν : ChoquetLE hS μ ν) : IsRepresentingMeasure x ν
```

## C. Maximal representing measures

**`Choquet.representingMeasures_nonempty`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L121).

```lean
lemma representingMeasures_nonempty (x : S) : (representingMeasures x).Nonempty
```

**`Choquet.IsChoquetMaximalAt`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L125).

> `μ` represents `x` and is maximal in the Choquet order among the measures representing `x`.

```lean
def IsChoquetMaximalAt (x : S) (μ : ProbabilityMeasure S) : Prop
```

**`Choquet.directed_choquetUpperSets`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L130).

> The representing measures above the members of a chain form a directed family.

```lean
lemma directed_choquetUpperSets (x : S) {c : Set (representingMeasures x)}
    (hc : IsChain (fun a b : representingMeasures x => ChoquetLE hS a.1 b.1) c) :
    Directed (· ⊇ ·) fun i : c => representingMeasures x ∩ {ν | ChoquetLE hS i.1.1 ν}
```

**`Choquet.exists_choquetLE_of_isChain`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L141).

> A nonempty chain of measures representing `x` has an upper bound among them.

```lean
lemma exists_choquetLE_of_isChain (x : S) {c : Set (representingMeasures x)}
    (hc : IsChain (fun a b : representingMeasures x => ChoquetLE hS a.1 b.1) c)
    (hcne : c.Nonempty) : ∃ ub : representingMeasures x, ∀ a ∈ c, ChoquetLE hS a.1 ub.1
```

**`Choquet.exists_isChoquetMaximalAt`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean#L154).

> Every point has a Choquet-maximal representing measure.

```lean
lemma exists_isChoquetMaximalAt (x : S) :
    ∃ μ : ProbabilityMeasure S, IsChoquetMaximalAt hS x μ
```

## Depends on

- [Mixtures in a convex set](choquet-mixture.md)

## Sources

- [PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/RepresentingMeasure.lean)
