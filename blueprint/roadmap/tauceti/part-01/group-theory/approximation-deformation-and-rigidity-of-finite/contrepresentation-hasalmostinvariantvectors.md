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
- [Source of `ContRepresentation.HasAlmostInvariantVectors` in TauCeti/RepresentationTheory/Continuous/AlmostInvariant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Continuous/AlmostInvariant.lean#L41)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FactorRigidity/STATUS.md)
