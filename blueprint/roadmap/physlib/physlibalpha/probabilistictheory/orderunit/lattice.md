---
declaration: module
origin: cited
lean: ProbabilisticTheory.OrderUnitLattice, ProbabilisticTheory.OrderUnitLattice.map_sup_of_map_inf
statement: formalized
proof: formalized
---

# Lattice-ordered observables

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Lattice`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Lattice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Lattice.lean): 2 declarations, 2 with a docstring.

> Order-unit lattices: Archimedean order-unit spaces whose order is a lattice.

## i. Overview

> An order-unit lattice is a space of observables in which any two observables have a least upper
> bound. Classical observables form such a lattice, with the pointwise maximum. Quantum observables do
> not: two self-adjoint matrices usually have no least upper bound.
>
> An order-unit lattice is a vector lattice in which the unit is a strong unit, so the order theory
> of vector lattices applies to it: an observable below a sum of two positive observables splits into
> two pieces, one below each summand, and every observable is close to a step function.

## ii. Key results

> - `OrderUnitLattice E` is an Archimedean order-unit space whose order is a lattice.
> - `OrderUnitLattice.map_sup_of_map_inf` : a positive functional preserving minima preserves maxima.

## iv. References

> * None.

## A. Order-unit lattices

**`ProbabilisticTheory.OrderUnitLattice`**, a class, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Lattice.lean#L54).

> An Archimedean order-unit space whose order is a lattice.

```lean
class OrderUnitLattice (E : Type*) extends ArchimedeanOrderUnitSpace E, Lattice E
```

**`ProbabilisticTheory.OrderUnitLattice.map_sup_of_map_inf`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Lattice.lean#L61).

> A positive functional preserves suprema whenever it preserves infima.

```lean
lemma map_sup_of_map_inf {ω : E →ₚ[ℝ] ℝ} (h : ∀ f g, ω (f ⊓ g) = min (ω f) (ω g)) (f g : E) :
    ω (f ⊔ g) = max (ω f) (ω g)
```

## Depends on

- [Archimedean order-unit spaces](../../../physlib/probabilistictheory/orderunit/archimedean.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Lattice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Lattice.lean)
