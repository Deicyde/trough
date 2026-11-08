---
declaration: def
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv
statement: formalized
---

# The Poincaré--Birkhoff--Witt theorem

For a Lie algebra that is free as a module, the
symmetric algebra is isomorphic to the associated graded of the PBW filtration of the enveloping
algebra, by the algebra map sending `x ∈ L` to the degree-one class of `ι(x)`.

```lean
TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv.{u, v} (R : Type u) (L : Type v)
  [CommRing R] [LieRing L] [LieAlgebra R L] [Module.Free R L] :
  SymmetricAlgebra R L ≃ₐ[R] TauCeti.UniversalEnvelopingAlgebra.PBWAssociatedGraded R L
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](the-linear-independence-half-of-the-poincare-bir.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.html#TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.html#TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedEquiv` in TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.lean#L210)
