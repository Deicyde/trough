---
declaration: def
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv
statement: formalized
---

# TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv

Over a commutative rational algebra `R : Type`, the canonical Lie inclusion identifies
the Lie algebra with the primitive submodule of its enveloping algebra. No freeness or flatness
hypothesis is needed.

```lean
TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv.{v} (R : Type) (L : Type v) [CommRing R]
  [Algebra ℚ R] [LieRing L] [LieAlgebra R L] : L ≃ₗ[R] ↥(Coalgebra.skewPrimitive R 1 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Primitive.html#TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Primitive.html#TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.primitiveEquiv` in TauCeti/Algebra/Lie/UniversalEnveloping/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/UniversalEnveloping/Primitive.lean#L84)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
