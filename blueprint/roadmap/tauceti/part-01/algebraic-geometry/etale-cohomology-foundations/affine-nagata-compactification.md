---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_denseCompactification_of_isAffine
statement: formalized
proof: formalized
---

# Affine Nagata compactification

A morphism of finite type between affine schemes has a
dense compactification.

```lean
TauCeti.nonempty_denseCompactification_of_isAffine.{u} {X S : AlgebraicGeometry.Scheme} (f : X ⟶ S)
  [AlgebraicGeometry.IsAffine X] [AlgebraicGeometry.IsAffine S]
  [AlgebraicGeometry.LocallyOfFiniteType f] : Nonempty (TauCeti.DenseCompactification f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The projective closure of an affine scheme of finite type](the-projective-closure-of-an-affine-scheme-of-fi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_denseCompactification_of_isAffine`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.html#TauCeti.nonempty_denseCompactification_of_isAffine).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_denseCompactification_of_isAffine`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.html#TauCeti.nonempty_denseCompactification_of_isAffine)
- [Source of `TauCeti.nonempty_denseCompactification_of_isAffine` in TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.lean#L114)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
