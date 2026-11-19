---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective
statement: formalized
proof: formalized
---

# TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective

Every conjugate class is produced by an embedding of the field of definition.

```lean
TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective.{u_1} {k : Type u_1}
  [Field k] [CharZero k] [Normal ℚ k] {K : IntermediateField ℚ k}
  {c : TauCeti.AlgebraicBelyiPair.IsoClass k}
  (hc : TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver (↥K) c) :
  Function.Surjective hc.embeddingToOrbit
```

## Depends on

- [The Galois action on isomorphism classes](the-galois-action-on-isomorphism-classes.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Embeddings.html#TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Embeddings.html#TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective)
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver.embeddingToOrbit_surjective` in TauCeti/FieldTheory/FunctionField/Belyi/Embeddings.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/Belyi/Embeddings.lean#L46)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BelyiMaps/STATUS.md)
