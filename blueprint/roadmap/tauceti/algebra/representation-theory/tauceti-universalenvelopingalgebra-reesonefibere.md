---
declaration: def
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv
statement: formalized
---

# TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv

Tensor base change of the PBW Rees algebra at one is the enveloping algebra.
The polynomial parameter acts on the left tensor factor by evaluation at one.

```lean
TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv.{u, v} (R : Type u) (L : Type v) [CommRing R]
  [LieRing L] [LieAlgebra R L] :
  TensorProduct (Polynomial R) R ↥(TauCeti.UniversalEnvelopingAlgebra.reesAlgebra R L) ≃ₐ[R]
    UniversalEnvelopingAlgebra R L
```

## Depends on

- [TauCeti.UniversalEnvelopingAlgebra.reesAlgebra](tauceti-universalenvelopingalgebra-reesalgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/OneFiber.html#TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/OneFiber.html#TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.reesOneFiberEquiv` in TauCeti/Algebra/Lie/UniversalEnveloping/Rees/OneFiber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/OneFiber.lean#L63)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
