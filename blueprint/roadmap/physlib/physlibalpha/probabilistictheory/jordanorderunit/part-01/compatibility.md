---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.IsJordanCompatible, ProbabilisticTheory.JordanAlgebra.isJordanCompatible_self, ProbabilisticTheory.JordanAlgebra.isJordanCompatible_comm, ProbabilisticTheory.JordanAlgebra.mulLeft_one_eq_id, ProbabilisticTheory.JordanAlgebra.isJordanCompatible_one_left, ProbabilisticTheory.JordanAlgebra.isJordanCompatible_one_right
statement: formalized
proof: formalized
---

# Compatible observables

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Compatibility`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean): 6 declarations, 3 with a docstring.

> Jordan compatibility of observables: their Jordan multiplication operators commute.

## i. Overview

> Two observables of a Jordan algebra are compatible when their multiplication operators commute, `L\_a
> L\_b = L\_b L\_a`. This needs no commutator, which the Jordan structure does not have. Commuting
> observables of a C⋆-algebra are compatible.

## ii. Key results

> - `JordanAlgebra.IsJordanCompatible` : compatible observables.
> - `JordanAlgebra.isJordanCompatible_comm` : compatibility is symmetric.
> - `JordanAlgebra.isJordanCompatible_one_left` : the unit is compatible with everything.
> - `JordanAlgebra.isJordanCompatible_self` : every observable is compatible with itself.
> - `JordanAlgebra.isJordanCompatible_one_right` : everything is compatible with the unit.

## iv. References

> * None.

## A. The compatibility predicate

**`ProbabilisticTheory.JordanAlgebra.IsJordanCompatible`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean#L55).

> `a` and `b` are Jordan-compatible: their multiplication operators commute,
> `L_a \circ L_b = L_b \circ L_a`. The Jordan-intrinsic substitute for "`a` and `b` commute", not
> needing an associative product to state.

```lean
def IsJordanCompatible (a b : E) : Prop
```

**`ProbabilisticTheory.JordanAlgebra.isJordanCompatible_self`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean#L57).

```lean
lemma isJordanCompatible_self (a : E) : IsJordanCompatible a a
```

**`ProbabilisticTheory.JordanAlgebra.isJordanCompatible_comm`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean#L59).

```lean
lemma isJordanCompatible_comm {a b : E} (h : IsJordanCompatible a b) :
    IsJordanCompatible b a
```

**`ProbabilisticTheory.JordanAlgebra.mulLeft_one_eq_id`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean#L63).

> `L_1` is the identity.

```lean
lemma mulLeft_one_eq_id : (L (1 : E) : E →ₗ[ℝ] E) = LinearMap.id
```

**`ProbabilisticTheory.JordanAlgebra.isJordanCompatible_one_left`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean#L67).

> The order unit is Jordan-compatible with everything: `L_1 = id` commutes with any operator.

```lean
lemma isJordanCompatible_one_left (a : E) : IsJordanCompatible 1 a
```

**`ProbabilisticTheory.JordanAlgebra.isJordanCompatible_one_right`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean#L72).

```lean
lemma isJordanCompatible_one_right (a : E) : IsJordanCompatible a 1
```

## Depends on

- [Powers, multiplication operators and the quadratic representation](operator.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Compatibility.lean)
