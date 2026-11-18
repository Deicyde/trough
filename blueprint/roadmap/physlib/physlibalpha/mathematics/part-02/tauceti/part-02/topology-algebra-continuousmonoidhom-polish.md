---
declaration: module
origin: cited
lean: ContinuousMonoidHom.instPolishSpace
statement: formalized
proof: formalized
---

# Polish spaces of continuous homomorphisms

The module `PhyslibAlpha.Mathematics.TauCeti.Topology.Algebra.ContinuousMonoidHom.Polish`, [PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/ContinuousMonoidHom/Polish.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/ContinuousMonoidHom/Polish.lean): 1 declaration, 1 with a docstring.

> The compact-open space of continuous homomorphisms from a second-countable locally compact monoid to
> a Polish topological monoid is Polish.

## i. Overview

> The compact-open space of continuous homomorphisms from a second-countable locally compact
> monoid to a Polish topological monoid is Polish. In particular, this supplies the regularity
> of spaces of characters needed for uniqueness of Fourier–Stieltjes measures.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`ContinuousMonoidHom.instPolishSpace`**, an instance, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/ContinuousMonoidHom/Polish.lean#L45).

> Continuous homomorphisms from a second-countable locally compact monoid to a Polish
> topological monoid form a Polish space in the compact-open topology.

```lean
instance _root_.ContinuousMonoidHom.instPolishSpace {A B : Type*}
    [Monoid A] [TopologicalSpace A] [LocallyCompactSpace A] [SecondCountableTopology A]
    [Monoid B] [TopologicalSpace B] [ContinuousMul B] [PolishSpace B] :
    PolishSpace (A →ₜ* B)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/ContinuousMonoidHom/Polish.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Topology/Algebra/ContinuousMonoidHom/Polish.lean)
