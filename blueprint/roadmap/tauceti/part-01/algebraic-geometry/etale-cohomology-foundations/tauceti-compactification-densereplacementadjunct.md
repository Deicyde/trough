---
declaration: def
origin: cited
lean: TauCeti.Compactification.denseReplacementAdjunction
statement: formalized
---

# TauCeti.Compactification.denseReplacementAdjunction

Dense replacement is right adjoint to the inclusion of dense compactifications; the counit
is the canonical map `denseReplacementMap`.

```lean
TauCeti.Compactification.denseReplacementAdjunction.{u} {X S : AlgebraicGeometry.Scheme}
  (f : X ⟶ S) :
  (TauCeti.denseCompactificationProperty f).ι ⊣ TauCeti.Compactification.denseReplacementFunctor f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Compactification.denseReplacementAdjunction`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.html#TauCeti.Compactification.denseReplacementAdjunction).

## Sources

- [Tau Ceti documentation: `TauCeti.Compactification.denseReplacementAdjunction`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.html#TauCeti.Compactification.denseReplacementAdjunction)
- [Source of `TauCeti.Compactification.denseReplacementAdjunction` in TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.lean#L158)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
