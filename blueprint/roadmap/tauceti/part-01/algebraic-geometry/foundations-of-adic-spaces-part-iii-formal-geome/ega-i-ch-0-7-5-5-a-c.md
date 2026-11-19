---
declaration: theorem
origin: cited
lean: TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff
statement: formalized
proof: formalized
---

# EGA I, Ch. 0, 7.5.5, (a) ⇔ (c)

Over a noetherian ring `A` with the `I`-adic topology, a
topological `A`-algebra `B` is strictly topologically of finite type exactly when `B` is
noetherian, `I·B`-adic, `I·B`-adically separated and complete, and `B ⧸ I·B` is a finitely
generated `A ⧸ I`-algebra. Noetherianity of `B` follows from the other three conditions.

```lean
TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff.{u_1, u_2} {A : Type u_1}
  [CommRing A] [TopologicalSpace A] [NonarchimedeanRing A] {I : Ideal A} {B : Type u_2} [CommRing B]
  [TopologicalSpace B] [Algebra A B] [IsNoetherianRing A] (hI : IsAdic I) :
  TauCeti.Huber.IsStrictlyTopologicallyFiniteType (algebraMap A B) ↔
    IsNoetherianRing B ∧
      IsAdic (Ideal.map (algebraMap A B) I) ∧
        IsAdicComplete (Ideal.map (algebraMap A B) I) B ∧
          Algebra.FiniteType (A ⧸ I) (B ⧸ Ideal.map (algebraMap A B) I)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TopologicallyFiniteType/Adic.html#TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TopologicallyFiniteType/Adic.html#TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff)
- [Source of `TauCeti.Huber.isStrictlyTopologicallyFiniteType_algebraMap_iff` in TauCeti/RingTheory/Huber/TopologicallyFiniteType/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/TopologicallyFiniteType/Adic.lean#L240)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
