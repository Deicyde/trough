---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsInNucleus, ProbabilisticTheory.nuclear_slip_left, ProbabilisticTheory.nuclear_slip_mid, ProbabilisticTheory.nuclear_slip_last, ProbabilisticTheory.nuclear_slip_last_right, ProbabilisticTheory.IsNuclearInvolution, ProbabilisticTheory.isNuclear_add_star, ProbabilisticTheory.assoc_star_first
statement: formalized
proof: formalized
---

# Nuclear involutions

The module `PhyslibAlpha.ProbabilisticTheory.Algebra.NuclearInvolution`, [PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean): 11 declarations, 2 with a docstring.

> Nuclear elements and nuclear involutions of alternative algebras, and their associators.

## i. Overview

> An element of an algebra is in the nucleus when it associates with all elements. A nuclear
> involution is an involution whose symmetric elements are in the nucleus, as for the octonions.
> Nuclear elements pass through associators, and the associator changes sign under the involution.

## ii. Key results

> - `IsInNucleus`, `IsNuclearInvolution` : nuclear elements and nuclear involutions.
> - `nuclear_comm_associator` : nuclear elements commute with associators.

## iv. References

> * None.

## A. Nuclear elements

**`ProbabilisticTheory.IsInNucleus`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L54).

> An element associating trivially in every slot.

```lean
def IsInNucleus (x : D) : Prop
```

**`ProbabilisticTheory.nuclear_slip_left`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L58).

```lean
lemma nuclear_slip_left {n : D} (hn : IsInNucleus n) (x y z : D) :
    associator (n * x) y z = n * associator x y z
```

**`ProbabilisticTheory.nuclear_slip_mid`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L64).

```lean
lemma nuclear_slip_mid {n : D} (hn : IsInNucleus n) (x y z : D) :
    associator x (n * y) z = n * associator x y z
```

**`ProbabilisticTheory.nuclear_slip_last`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L69).

```lean
lemma nuclear_slip_last {n : D} (hn : IsInNucleus n) (x y z : D) :
    associator x y (n * z) = n * associator x y z
```

**`ProbabilisticTheory.nuclear_slip_last_right`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L75).

```lean
lemma nuclear_slip_last_right {n : D} (hn : IsInNucleus n) (x y z : D) :
    associator x y (z * n) = associator x y z * n
```

## B. Nuclear involutions

**`ProbabilisticTheory.IsNuclearInvolution`**, a class, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L90).

> A star involution whose symmetric elements are nuclear.

```lean
class IsNuclearInvolution (D : Type*) [NonUnitalNonAssocRing D] [IsAlternative D]
    [StarAddMonoid D] : Prop where
  isNuclear_of_star_eq : ∀ x : D, star x = x → IsInNucleus x
  isNuclear_comm : ∀ n x : D, IsInNucleus n → IsInNucleus (n * x - x * n)
```

**`ProbabilisticTheory.isNuclear_add_star`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L97).

```lean
lemma isNuclear_add_star (x : D) : IsInNucleus (x + star x)
```

**`ProbabilisticTheory.assoc_star_first`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L101).

```lean
lemma assoc_star_first (x y z : D) : associator (star x) y z = -associator x y z
```

**`ProbabilisticTheory.assoc_star_mid`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L107).

```lean
lemma assoc_star_mid (x y z : D) : associator x (star y) z = -associator x y z
```

**`ProbabilisticTheory.assoc_star_last`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L113).

```lean
lemma assoc_star_last (x y z : D) : associator x y (star z) = -associator x y z
```

**`ProbabilisticTheory.nuclear_comm_associator`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean#L119).

```lean
lemma nuclear_comm_associator {n : D} (hn : IsInNucleus n) (x y z : D) :
    n * associator x y z = associator x y z * n
```

## Depends on

- [Alternative algebras](alternative.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/NuclearInvolution.lean)
