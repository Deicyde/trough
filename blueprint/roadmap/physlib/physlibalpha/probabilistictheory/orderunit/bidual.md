---
declaration: module
origin: cited
lean: Bidual.coe_one, Bidual.ofE_one, Bidual.exists_bound_one, Bidual.instOrderUnitSpace, Bidual.instArchimedeanOrderUnitSpace, Bidual.apply_le_of_le_one, Bidual.instOrderUnitLattice
statement: formalized
proof: formalized
---

# The bidual of a system

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Bidual`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean): 8 declarations (1 instance with no name), 4 with a docstring.

> The bidual of a system is an Archimedean order-unit space, and a lattice for classical systems.

## i. Overview

> An element of the bidual of a system assigns to every positive functional a value, additively and
> positively homogeneously, dominated by some observable. With the unit `φ ↦ φ 1`, the total weight,
> the bidual is again an Archimedean order-unit space: a system whose observables contain those of
> the original one. When the system is classical, so that the positive functionals form a lattice,
> the observables of the bidual form a lattice.

## ii. Key results

> - `Bidual.instOrderUnitSpace` : the bidual of a system, with the total weight as unit.
> - `Bidual.instArchimedeanOrderUnitSpace` : the bidual is Archimedean.
> - `Bidual.instOrderUnitLattice` : the bidual of a classical system is an order-unit lattice.

## iv. References

> * None.

## A. The unit of the bidual

**An instance with no name**, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L51).

> The unit of the bidual: the total weight of a positive functional.

```lean
instance : One (Bidual E)
```

**`Bidual.coe_one`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L53).

```lean
lemma coe_one (φ : E →ₚ[ℝ] ℝ) : (1 : Bidual E) φ = φ 1
```

**`Bidual.ofE_one`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L55).

```lean
lemma ofE_one : ofE (1 : E) = 1
```

**`Bidual.exists_bound_one`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L58).

> An element of the bidual is bounded by a multiple of the total weight.

```lean
lemma exists_bound_one (x : Bidual E) : ∃ n : ℕ, ∀ φ, |x φ| ≤ n * φ 1
```

**`Bidual.instOrderUnitSpace`**, an instance, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L65).

```lean
instance instOrderUnitSpace : OrderUnitSpace (Bidual E)
```

**`Bidual.instArchimedeanOrderUnitSpace`**, an instance, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L74).

```lean
instance instArchimedeanOrderUnitSpace : ArchimedeanOrderUnitSpace (Bidual E)
```

**`Bidual.apply_le_of_le_one`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L85).

> A positive functional's value on an element of the bidual below the unit is at most its total
> weight.

```lean
lemma apply_le_of_le_one {x : Bidual E} (hx : x ≤ 1) (φ : E →ₚ[ℝ] ℝ) : x φ ≤ φ 1
```

## B. The bidual of a classical system

**`Bidual.instOrderUnitLattice`**, an instance, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean#L91).

> The bidual of a classical system is an order-unit lattice.

```lean
noncomputable instance instOrderUnitLattice [Fact (HasLatticeDualCone E)] :
    OrderUnitLattice (Bidual E)
```

## Depends on

- [The bidual as a lattice](../../mathematics/part-02/order/positivedual-biduallattice.md)
- [Lattice-ordered observables](lattice.md)
- [The unit of an order-unit space as an order unit](positivedual.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Bidual.lean)
