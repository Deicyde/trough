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
- [Source of `TauCeti.UniversalEnvelopingAlgebra.pbwAssociatedGradedMap_injective` in TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Injective.lean#L201)
