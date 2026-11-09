---
declaration: structure
origin: cited
lean: Finset.IsSquarefreeBasis
statement: formalized
---

# Finset.IsSquarefreeBasis

`B` is a squarefree basis of the finite family `F` of polynomials over `D`: its members
are primitive, squarefree, of positive degree and pairwise relatively prime, and every member
of `F` is a constant times a product of powers of members of `B`.

```lean
Finset.IsSquarefreeBasis.{u_1} {D : Type u_1} [CommRing D] (F B : Finset (Polynomial D)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.IsSquarefreeBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/SquarefreeBasis.html#Finset.IsSquarefreeBasis).

## Sources

- [Tau Ceti documentation: `Finset.IsSquarefreeBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/SquarefreeBasis.html#Finset.IsSquarefreeBasis)
- [Source of `Finset.IsSquarefreeBasis` in TauCeti/RingTheory/Polynomial/SquarefreeBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Polynomial/SquarefreeBasis.lean#L85)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
