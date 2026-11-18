---
declaration: module
origin: cited
lean: Weight, Weight.IsFaithful, Weight.IsFinite, Weight.IsSemifinite, Weight.monotone, Weight.IsFinite.isSemifinite, Weight.IsFinite.toReal_map_add, Weight.toReal_map_nnreal_smul
statement: formalized
proof: formalized
---

# Weights (Physlib)

The module `Physlib.ProbabilisticTheory.Weight.Basic`, [Physlib/ProbabilisticTheory/Weight/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean): 14 declarations, 13 with a docstring.

## i. Overview

> A state assigns each positive observable a nonnegative expectation value, normalized so the
> certain outcome reads exactly `1`. A *weight* generalizes this by dropping the normalization and
> letting the values be extended nonnegative reals, possibly `+∞`. This matters especially in
> infinite dimensions: the trace on `B(H)` is only finite on the trace-class operators and genuinely
> diverges to `+∞` elsewhere. A state is then the special case that happens to be finite everywhere
> and normalized.

## ii. Key results

> - `Weight.monotone` : weights are monotone on the positive cone.
> - `Weight.IsFinite.isSemifinite` : a finite weight is automatically semifinite.
> - `Weight.IsFinite.normalize_isState` : rescaling a finite weight that's nonzero at the order unit
>   turns it into a state.

## iv. References

> - G. Ludwig, *Foundations of Quantum Mechanics I*, Springer, 1983.
>   <https://link.springer.com/book/10.1007/978-3-642-86751-4>

## A. Weights

**`Weight`**, an abbrev, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L54).

> An extended nonnegative linear functional on the positive cone.

```lean
abbrev Weight (E : Type*) [OrderedVectorSpace E]
```

**`Weight.IsFaithful`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L63).

> Only the zero positive element has weight zero.

```lean
def IsFaithful (w : Weight E) : Prop
```

**`Weight.IsFinite`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L66).

> A weight has no infinite values.

```lean
def IsFinite (w : Weight E) : Prop
```

**`Weight.IsSemifinite`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L69).

> A weight is the supremum of its finite values below each positive element.

```lean
def IsSemifinite (w : Weight E) : Prop
```

**`Weight.monotone`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L73).

> Weights are monotone on the positive cone.

```lean
lemma monotone (w : Weight E) : Monotone w
```

**`Weight.IsFinite.isSemifinite`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L81).

> A finite weight is semifinite.

```lean
lemma IsFinite.isSemifinite {w : Weight E} (hw : w.IsFinite) : w.IsSemifinite
```

**`Weight.IsFinite.toReal_map_add`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L85).

> A finite weight's real value is additive.

```lean
lemma IsFinite.toReal_map_add {w : Weight E} (hw : w.IsFinite) (A B : PosCone E) :
    (w (A + B)).toReal = (w A).toReal + (w B).toReal
```

**`Weight.toReal_map_nnreal_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L90).

> A weight's real value scales linearly under nonnegative real scaling.

```lean
lemma toReal_map_nnreal_smul (w : Weight E) (k : ℝ≥0) (A : PosCone E) :
    (w (k • A)).toReal = k * (w A).toReal
```

**`Weight.IsNormal`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L96).

> A weight is normal when it preserves least upper bounds of increasing sequences in the
> positive cone.

```lean
def IsNormal (w : Weight E) : Prop
```

## B. States as weights

**`Weight.IsState`**, a structure, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L112).

> A weight that's finite everywhere and gives the certain outcome weight exactly `1`.

```lean
structure IsState (w : Weight E) : Prop where
  /-- A state is finite everywhere. -/
  finite : w.IsFinite
  /-- A state gives the certain outcome weight exactly `1`. -/
  normalized : w 1 = 1
```

**`Weight.normalize`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L119).

> Rescale a weight by the inverse of its value at the order unit.

```lean
noncomputable def normalize (w : Weight E) : Weight E
```

**`Weight.normalize_apply`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L124).

```lean
lemma normalize_apply (w : Weight E) (A : PosCone E) :
    normalize w A = (w 1)⁻¹ * w A
```

**`Weight.IsFinite.normalize_isFinite`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L128).

> Normalizing a finite weight that's nonzero at the order unit keeps it finite.

```lean
lemma IsFinite.normalize_isFinite {w : Weight E} (hw : w.IsFinite) (h : w 1 ≠ 0) :
    (normalize w).IsFinite
```

**`Weight.IsFinite.normalize_isState`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean#L134).

> Normalizing a finite weight that's nonzero at the order unit makes it a state: the order unit
> is scaled to weight exactly `1`.

```lean
lemma IsFinite.normalize_isState {w : Weight E} (hw : w.IsFinite) (h : w 1 ≠ 0) :
    (normalize w).IsState
```

## Depends on

- [Ordered positive cones](../orderunit/cone.md)

## Sources

- [Physlib/ProbabilisticTheory/Weight/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Basic.lean)
