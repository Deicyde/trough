---
declaration: theorem
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective
statement: formalized
proof: formalized
---

# The linear-independence half of the Poincaré--Birkhoff--Witt theorem

The canonical map
`Sym(L) → gr U(L)` is injective when `L` is a free module.

```lean
TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective.{u, v} (R : Type u) (L : Type v)
  [CommRing R] [LieRing L] [LieAlgebra R L] [Module.Free R L] :
  Function.Injective ⇑(TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap R L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.html#TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.html#TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective` in TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.lean#L201)
