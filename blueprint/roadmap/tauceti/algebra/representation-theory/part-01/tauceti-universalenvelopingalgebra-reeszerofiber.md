---
declaration: def
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv
statement: formalized
---

# TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv

The PBW zero fibre is canonically the symmetric algebra, without a choice of basis.

```lean
TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv.{u, v} (R : Type u) (L : Type v) [CommRing R]
  [LieRing L] [LieAlgebra R L] [Module.Free R L] :
  (↥(TauCeti.UniversalEnvelopingAlgebra.reesAlgebra R L) ⧸
      Ideal.span {TauCeti.UniversalEnvelopingAlgebra.reesParameter R L}) ≃ₐ[R]
    SymmetricAlgebra R L
```

## Depends on

- [The Poincaré--Birkhoff--Witt theorem](../../lie/the-poincare-birkhoff-witt-theorem.md)
- [TauCeti.UniversalEnvelopingAlgebra.reesAlgebra](tauceti-universalenvelopingalgebra-reesalgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/ZeroFiber.html#TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/ZeroFiber.html#TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.reesZeroFiberEquiv` in TauCeti/Algebra/Lie/UniversalEnveloping/Rees/ZeroFiber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/ZeroFiber.lean#L121)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
