---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsAlternative, ProbabilisticTheory.IsAlternative.associator, ProbabilisticTheory.IsAlternative.associator_add_left, ProbabilisticTheory.IsAlternative.associator_add_mid, ProbabilisticTheory.IsAlternative.associator_add_right, ProbabilisticTheory.IsAlternative.teichmuller, ProbabilisticTheory.IsAlternative.associator_self_left, ProbabilisticTheory.IsAlternative.associator_right_self
statement: formalized
proof: formalized
---

# Alternative algebras

The module `PhyslibAlpha.ProbabilisticTheory.Algebra.Alternative`, [PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean): 16 declarations (1 instance with no name), 8 with a docstring.

> Alternative algebras, the associator, the flexible law, and the left Moufang identity.

## i. Overview

> An algebra is alternative when the associator `(a, b, c) = (a b) c - a (b c)` is alternating. The
> octonions are alternative, and they coordinatize the exceptional Albert Jordan algebra. Alternative
> algebras satisfy the flexible law and the left Moufang identity.

## ii. Key results

> - `IsAlternative` : alternative algebras.
> - `associator` : the associator.
> - `IsAlternative.mul_flexible` : the flexible law.
> - `IsAlternative.moufang_left` : the left Moufang identity.
> - `IsAlternative.left_bumping` : McCrimmon's left bumping formula.

## iv. References

> * None.

## A. Alternative multiplications

**`ProbabilisticTheory.IsAlternative`**, a class, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L54).

> An alternative multiplication has associative repeated factors on either side.

```lean
class IsAlternative (A : Type*) [Mul A] : Prop where
  /-- Left alternativity. -/
  mul_alternative_left : ∀ x y : A, x * (x * y) = (x * x) * y
  /-- Right alternativity. -/
  mul_alternative_right : ∀ x y : A, (y * x) * x = y * (x * x)
```

**An instance with no name**, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L61).

> Associative algebras are alternative.

```lean
instance (priority := 100) {A : Type*} [Semigroup A] : IsAlternative A
```

## B. The associator

**`ProbabilisticTheory.IsAlternative.associator`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L76).

> The failure of associativity.

```lean
def associator (x y z : A) : A
```

**`ProbabilisticTheory.IsAlternative.associator_add_left`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L78).

```lean
lemma associator_add_left (x y z w : A) :
    associator (x + y) z w = associator x z w + associator y z w
```

**`ProbabilisticTheory.IsAlternative.associator_add_mid`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L84).

```lean
lemma associator_add_mid (x y z w : A) :
    associator x (y + z) w = associator x y w + associator x z w
```

**`ProbabilisticTheory.IsAlternative.associator_add_right`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L90).

```lean
lemma associator_add_right (x y z w : A) :
    associator x y (z + w) = associator x y z + associator x y w
```

**`ProbabilisticTheory.IsAlternative.teichmuller`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L97).

> Teichmüller's identity holds before alternativity is assumed.

```lean
lemma teichmuller (x y z w : A) :
    associator (x * y) z w - associator x (y * z) w + associator x y (z * w) =
      associator x y z * w + x * associator y z w
```

## C. Identities in alternative algebras

**`ProbabilisticTheory.IsAlternative.associator_self_left`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L112).

```lean
lemma associator_self_left (x y : A) : associator x x y = 0
```

**`ProbabilisticTheory.IsAlternative.associator_right_self`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L117).

```lean
lemma associator_right_self (x y : A) : associator y x x = 0
```

**`ProbabilisticTheory.IsAlternative.associator_swap_first`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L123).

> The associator is skew under an adjacent swap.

```lean
lemma associator_swap_first (x y z : A) : associator x y z = -associator y x z
```

**`ProbabilisticTheory.IsAlternative.associator_swap_last`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L132).

```lean
lemma associator_swap_last (x y z : A) : associator x y z = -associator x z y
```

**`ProbabilisticTheory.IsAlternative.associator_cyclic`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L141).

```lean
lemma associator_cyclic (x y z : A) : associator x y z = associator y z x
```

**`ProbabilisticTheory.IsAlternative.associator_outer_self`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L144).

```lean
lemma associator_outer_self (x y : A) : associator x y x = 0
```

**`ProbabilisticTheory.IsAlternative.mul_flexible`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L148).

> The flexible law is forced by alternativity.

```lean
lemma mul_flexible (x y : A) : x * (y * x) = (x * y) * x
```

**`ProbabilisticTheory.IsAlternative.moufang_left`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L154).

> The left Moufang identity.

```lean
lemma moufang_left (x y z : A) : (x * (z * x)) * y = x * (z * (x * y))
```

**`ProbabilisticTheory.IsAlternative.left_bumping`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean#L188).

> McCrimmon's left bumping formula, the key alternative-algebra identity for Albert matrices.

```lean
lemma left_bumping (x y z : A) : associator x y (z * x) = x * associator y z x
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Alternative.lean)
