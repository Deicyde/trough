---
declaration: theorem
origin: cited
lean: TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator
statement: formalized
proof: formalized
---

# Representation-finiteness is the existence of an additive generator (Auslander)

a left
Artinian ring `A`, for instance an Artin algebra, is representation-finite exactly when
`mod A = FGModuleCat A` has an additive generator.

```lean
TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator.{w, v} {A : Type v} [Ring A]
  [IsArtinianRing A] : TauCeti.IsRepresentationFinite A ↔ ∃ G, TauCeti.IsAdditiveGenerator G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A Krull-Schmidt category](a-krull-schmidt-category.md)
- [Fitting's lemma, categorically](../../part-02/category/fittings-lemma-categorically.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/RepresentationFinite.html#TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator).

## Sources

- [Tau Ceti documentation: `TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/RepresentationFinite.html#TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator)
- [Source of `TauCeti.isRepresentationFinite_iff_exists_isAdditiveGenerator` in TauCeti/Algebra/Category/FGModuleCat/RepresentationFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/FGModuleCat/RepresentationFinite.lean#L109)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
