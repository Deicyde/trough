---
declaration: def
origin: cited
lean: TauCeti.ApproximatelyUnitarilyEquivalent
statement: formalized
---

# TauCeti.ApproximatelyUnitarilyEquivalent

Approximate unitary equivalence, implemented by unitaries of the unital target itself.
The source and the two maps need not be unital.

```lean
TauCeti.ApproximatelyUnitarilyEquivalent.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [NonUnitalCStarAlgebra A] [CStarAlgebra B] (φ ψ : A →⋆ₙₐ[ℂ] B) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ApproximatelyUnitarilyEquivalent`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Basic.html#TauCeti.ApproximatelyUnitarilyEquivalent).

## Sources

- [Tau Ceti documentation: `TauCeti.ApproximatelyUnitarilyEquivalent`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Basic.html#TauCeti.ApproximatelyUnitarilyEquivalent)
- [Source of `TauCeti.ApproximatelyUnitarilyEquivalent` in TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Basic.lean#L33)
- [Tau Ceti roadmap status: Classification of AF and purely infinite simple C*-algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CStarClassification/STATUS.md)
