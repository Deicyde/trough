---
declaration: def
origin: cited
lean: ContRepresentation.HasAlmostInvariantVectors
statement: formalized
---

# ContRepresentation.HasAlmostInvariantVectors

Every finite set of group elements admits an arbitrarily nearly fixed unit vector.
No topology on the acting monoid is required; in particular this is the discrete-group notion.

```lean
ContRepresentation.HasAlmostInvariantVectors.{u_1, u_2, u_3} {R : Type u_1} {G : Type u_2}
  {V : Type u_3} [Ring R] [Monoid G] [NormedAddCommGroup V] [_root_.Module R V]
  (ρ : ContRepresentation R G V) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.HasAlmostInvariantVectors`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/AlmostInvariant.html#ContRepresentation.HasAlmostInvariantVectors).

## Sources

- [Tau Ceti documentation: `ContRepresentation.HasAlmostInvariantVectors`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/AlmostInvariant.html#ContRepresentation.HasAlmostInvariantVectors)
- [Source of `ContRepresentation.HasAlmostInvariantVectors` in TauCeti/RepresentationTheory/Continuous/AlmostInvariant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Continuous/AlmostInvariant.lean#L37)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FactorRigidity/STATUS.md)
