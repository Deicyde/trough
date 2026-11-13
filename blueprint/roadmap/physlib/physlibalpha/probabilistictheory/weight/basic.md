---
declaration: module
origin: cited
lean: ProbabilisticTheory.Weight, ProbabilisticTheory.Weight.ext, ProbabilisticTheory.Weight.IsFaithful, ProbabilisticTheory.Weight.IsFinite, ProbabilisticTheory.Weight.IsSemifinite, ProbabilisticTheory.Weight.mono, ProbabilisticTheory.Weight.IsFinite.isSemifinite, ProbabilisticTheory.Weight.IsFinite.toReal_map_add
statement: formalized
proof: formalized
---

# Weights

The module `PhyslibAlpha.ProbabilisticTheory.Weight.Basic`, [PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean): 15 declarations, 13 with a docstring.

> Weights: additive, possibly infinite maps on the positive cone; states are finite normalized ones.

## i. Overview

> A state assigns each positive observable a nonnegative expectation value, normalized so the certain
> outcome reads exactly `1`. A weight drops the normalization and allows the value `+∞`. This matters
> in infinite dimensions: the trace on `B(H)` is finite only on the trace-class operators. A state is
> a weight that is finite and normalized.

## ii. Key results

> - `Weight.mono` : weights are monotone on the positive cone.
> - `Weight.IsFinite.isSemifinite` : a finite weight is automatically semifinite.
> - `Weight.IsFinite.normalize_isState` : rescaling a finite weight that's nonzero at the order unit
>   turns it into a state.

## iv. References

> - G. Ludwig, *Foundations of Quantum Mechanics I*, Springer, 1983.
>   <https://link.springer.com/book/10.1007/978-3-642-86751-4>

## A. Weights

**`ProbabilisticTheory.Weight`**, an abbrev, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L55).

> An extended nonnegative linear functional on the positive cone.

```lean
abbrev Weight (E : Type*) [OrderedVectorSpace E]
```

**`ProbabilisticTheory.Weight.ext`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L64).

```lean
lemma ext {w₁ w₂ : Weight E} (h : ∀ A, w₁ A = w₂ A) : w₁ = w₂
```

**`ProbabilisticTheory.Weight.IsFaithful`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L68).

> Only the zero positive element has weight zero.

```lean
def IsFaithful (w : Weight E) : Prop
```

**`ProbabilisticTheory.Weight.IsFinite`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L71).

> A weight has no infinite values.

```lean
def IsFinite (w : Weight E) : Prop
```

**`ProbabilisticTheory.Weight.IsSemifinite`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L74).

> A weight is the supremum of its finite values below each positive element.

```lean
def IsSemifinite (w : Weight E) : Prop
```

**`ProbabilisticTheory.Weight.mono`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L78).

> Weights are monotone on the positive cone.

```lean
lemma mono (w : Weight E) : Monotone (w : PosCone E → ℝ≥0∞)
```

**`ProbabilisticTheory.Weight.IsFinite.isSemifinite`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L87).

> A finite weight is semifinite.

```lean
lemma IsFinite.isSemifinite {w : Weight E} (hw : w.IsFinite) : w.IsSemifinite
```

**`ProbabilisticTheory.Weight.IsFinite.toReal_map_add`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L91).

> A finite weight's real value is additive.

```lean
lemma IsFinite.toReal_map_add {w : Weight E} (hw : w.IsFinite) (A B : PosCone E) :
    (w (A + B)).toReal = (w A).toReal + (w B).toReal
```

**`ProbabilisticTheory.Weight.toReal_map_nnreal_smul`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L96).

> A weight's real value scales linearly under nonnegative real scaling.

```lean
lemma toReal_map_nnreal_smul (w : Weight E) (k : ℝ≥0) (A : PosCone E) :
    (w (k • A)).toReal = k * (w A).toReal
```

**`ProbabilisticTheory.Weight.IsNormal`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L102).

> A weight is normal when it preserves least upper bounds of increasing sequences in the
> positive cone.

```lean
def IsNormal (w : Weight E) : Prop
```

## B. States as weights

**`ProbabilisticTheory.Weight.IsState`**, a structure, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L118).

> A weight that's finite everywhere and gives the certain outcome weight exactly `1`.

```lean
structure IsState (w : Weight E) : Prop where
  /-- A state is finite everywhere. -/
  finite : w.IsFinite
  /-- A state gives the certain outcome weight exactly `1`. -/
  normalized : w 1 = 1
```

**`ProbabilisticTheory.Weight.normalize`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L125).

> Rescale a weight by the inverse of its value at the order unit.

```lean
noncomputable def normalize (w : Weight E) : Weight E
```

**`ProbabilisticTheory.Weight.normalize_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L132).

```lean
lemma normalize_apply (w : Weight E) (A : PosCone E) :
    normalize w A = (w 1)⁻¹ * w A
```

**`ProbabilisticTheory.Weight.IsFinite.normalize_isFinite`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L136).

> Normalizing a finite weight that's nonzero at the order unit keeps it finite.

```lean
lemma IsFinite.normalize_isFinite {w : Weight E} (hw : w.IsFinite) (h : w 1 ≠ 0) :
    (normalize w).IsFinite
```

**`ProbabilisticTheory.Weight.IsFinite.normalize_isState`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean#L142).

> Normalizing a finite weight that's nonzero at the order unit makes it a state: the order unit
> is scaled to weight exactly `1`.

```lean
lemma IsFinite.normalize_isState {w : Weight E} (hw : w.IsFinite) (h : w 1 ≠ 0) :
    (normalize w).IsState
```

## Depends on

- [Ordered positive cones](../../../physlib/probabilistictheory/orderunit/cone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean)
