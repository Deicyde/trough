---
declaration: module
origin: cited
lean: ProbabilisticTheory.JBWAlgebra, ProbabilisticTheory.JBWAlgebra.eq_of_forall_normal_state_eq, ProbabilisticTheory.JBWAlgebra.exists_isLUB_range_and_normal_state_image, ProbabilisticTheory.JBWAlgebra.isLUB_rangeSup_normal_state_image, ProbabilisticTheory.JBWAlgebra.exists_normal_finite_weight_ne_zero
statement: formalized
proof: formalized
---

# JBW-algebras

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JBW.Basic`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean): 5 declarations, 5 with a docstring.

> JBW-algebras: monotone-complete JB-algebras whose normal states separate points.

## i. Overview

> A JBW-algebra is a monotone-complete JB-algebra whose normal states separate points.

## ii. Key results

> - `JBWAlgebra` : JBW-algebras.
> - `JBWAlgebra.eq_of_forall_normal_state_eq` : normal states separate points.

## iv. References

> * None.

## A. JBW-algebras

**`ProbabilisticTheory.JBWAlgebra`**, a class, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean#L46).

> A JBW-algebra, presented as a monotone-complete JB-algebra with enough normal states.
> The ordinary JB, order-unit, and scalar-order data stay in their existing canonical classes.

```lean
class JBWAlgebra (E : Type*) [IsJBOrderUnit E] : Prop
    extends MonotoneCompleteOrder E where
  /-- Normal states separate a nonzero observable from zero. -/
  exists_normal_state_ne_zero : ∀ {x : E}, x ≠ 0 →
    ∃ ω : 𝓢[ℝ, E], ω.IsNormal ∧ ω x ≠ 0
```

## B. Separation and monotone convergence

**`ProbabilisticTheory.JBWAlgebra.eq_of_forall_normal_state_eq`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean#L59).

> Equality of observables is detected by all normal states.

```lean
lemma eq_of_forall_normal_state_eq {x y : E}
    (h : ∀ ω : 𝓢[ℝ, E], ω.IsNormal → ω x = ω y) : x = y
```

**`ProbabilisticTheory.JBWAlgebra.exists_isLUB_range_and_normal_state_image`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean#L68).

> A bounded increasing sequence has a supremum, and a normal state maps it to the supremum of the
> values.

```lean
lemma exists_isLUB_range_and_normal_state_image (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal)
    (x : ℕ → E) (hx : Monotone x) (hbounded : BddAbove (Set.range x)) :
    ∃ a : E, IsLUB (Set.range x) a ∧
      IsLUB (Set.range fun n => ω (x n)) (ω a)
```

**`ProbabilisticTheory.JBWAlgebra.isLUB_rangeSup_normal_state_image`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean#L78).

> The same monotone-convergence statement using the canonical chosen sequence supremum from
> `MonotoneCompleteOrder`.

```lean
lemma isLUB_rangeSup_normal_state_image (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal)
    (x : ℕ → E) (hx : Monotone x) (hbounded : BddAbove (Set.range x)) :
    IsLUB (Set.range fun n => ω (x n))
      (ω (MonotoneCompleteOrder.rangeSup x hx hbounded))
```

**`ProbabilisticTheory.JBWAlgebra.exists_normal_finite_weight_ne_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean#L88).

> A nonzero positive observable is detected by a normal finite weight.  This is the canonical
> state-to-weight direction: normal-state separation supplies the state, and the established
> state/weight conversion transports its normality to the positive cone.

```lean
lemma exists_normal_finite_weight_ne_zero {x : E} (hx : 0 ≤ x) (hxne : x ≠ 0) :
    ∃ w : Weight E, w.IsNormal ∧ w.IsFinite ∧ w ⟨x, hx⟩ ≠ 0
```

## Depends on

- [Normal channels](../../channel/normal.md)
- [Normed Jordan algebras and JB-algebras](../part-01/jb-basic.md)
- [Monotone-complete ordered spaces](../../orderunit/monotonecomplete.md)
- [Weights](../../weight/basic.md)

## Proof depends on

- [Normal states give normal weights](../../state/normalequivalence.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/Basic.lean)
