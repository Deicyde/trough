---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsClassical, ProbabilisticTheory.OrderUnitLattice.isClassical
statement: formalized
proof: formalized
---

# Classical systems

The module `PhyslibAlpha.ProbabilisticTheory.Classical.Basic`, [PhyslibAlpha/ProbabilisticTheory/Classical/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Basic.lean): 2 declarations, 2 with a docstring.

> Classical systems: those whose positive functionals have least upper bounds.

## i. Overview

> A system is classical when every state decomposes in exactly one way into pure states: a state is
> then nothing but a probability distribution over the pure states. In the language of convex
> geometry the state space is a Choquet simplex. By the Choquet–Meyer theorem this is the same as
> asking that any two positive functionals have a least upper bound, which is how it is stated here.
>
> Classicality is characterized operationally by the absence of incompatibility (Kuramochi's theorem)
> and by the uniqueness of composites (the Namioka–Phelps theorem). It is weaker than asking that the
> observables themselves form a lattice, as they do for the functions on a sample space.

## ii. Key results

> - `IsClassical E` : the system `E` is classical.
> - `OrderUnitLattice.isClassical` : a system whose observables form a lattice is classical.

## iv. References

> * None.

## A. Classical systems

**`ProbabilisticTheory.IsClassical`**, an abbrev, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Basic.lean#L49).

> A system is **classical** when every state decomposes uniquely into pure states: its state
> space is a Choquet simplex, i.e. any two positive functionals have a least upper bound.

```lean
abbrev IsClassical (E : Type*) [OrderUnitSpace E] : Prop
```

**`ProbabilisticTheory.OrderUnitLattice.isClassical`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Basic.lean#L52).

> A system whose observables form a lattice is classical.

```lean
lemma OrderUnitLattice.isClassical (E : Type*) [OrderUnitLattice E] : IsClassical E
```

## Depends on

- [The Riesz–Kantorovich formula](../../mathematics/part-02/order/positivedual-rieszkantorovich.md)
- [Lattice-ordered observables](../orderunit/lattice.md)
- [The unit of an order-unit space as an order unit](../orderunit/positivedual.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Basic.lean)
