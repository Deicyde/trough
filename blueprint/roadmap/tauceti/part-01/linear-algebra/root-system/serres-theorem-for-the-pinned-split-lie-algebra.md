---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.serreLift_injective
statement: formalized
proof: formalized
---

# Serre's theorem for the pinned split Lie algebra

the comparison map from the Lie algebra
presented by Serre's relations for the pinned Cartan matrix is injective.

```lean
TauCeti.DynkinType.serreLift_injective (t : TauCeti.DynkinType) (ht : t.Valid) :
  Function.Injective ⇑(t.serreLift ht)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's theorem (`TauCeti.serreLift_injective_of_base`)](../../algebra/part-02/lie/part-02/serres-theorem-tauceti-serrelift-injective-of-ba.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.serreLift_injective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/SerrePresentation.html#TauCeti.DynkinType.serreLift_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.serreLift_injective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/SerrePresentation.html#TauCeti.DynkinType.serreLift_injective)
- [Source of `TauCeti.DynkinType.serreLift_injective` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/SerrePresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/SerrePresentation.lean#L222)
