---
declaration: theorem
origin: cited
lean: TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule
statement: formalized
proof: formalized
---

# The cyclic quotient of the preprojective algebra of an orientation of `E₈` vanishes in positive degrees when `2`, `3` and `5` are units

every homogeneous piece of positive path
degree lies in the commutator submodule.

```lean
TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule.{u_1} (k : Type u_1) [CommRing k]
  (o : TauCeti.DoubledQuiver.Orientation TauCeti.zigzagE8Graph) (h2 : IsUnit 2) (h3 : IsUnit 3)
  (h5 : IsUnit 5) {d : ℕ} (hd : 0 < d) :
  TauCeti.preprojectiveGrade k (TauCeti.DoubledQuiver.OrientedQuiver TauCeti.zigzagE8Graph o) d ≤
    TauCeti.commutatorSubmodule k
      (TauCeti.preprojectiveAlgebra k
        (TauCeti.DoubledQuiver.OrientedQuiver TauCeti.zigzagE8Graph o))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/TypeE/CyclicQuotient.html#TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule).

## Sources

- [Tau Ceti documentation: `TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/TypeE/CyclicQuotient.html#TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule)
- [Source of `TauCeti.preprojectiveGrade_E8_le_commutatorSubmodule` in TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/TypeE/CyclicQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/TypeE/CyclicQuotient.lean#L496)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
