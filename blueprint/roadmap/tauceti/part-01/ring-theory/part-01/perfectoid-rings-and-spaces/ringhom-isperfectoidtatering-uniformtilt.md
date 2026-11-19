---
declaration: theorem
origin: cited
lean: RingHom.isPerfectoidTateRing_uniformTilt
statement: formalized
proof: formalized
---

# RingHom.isPerfectoidTateRing_uniformTilt

The tilt of a complete uniform Tate ring receiving a continuous homomorphism from a
perfectoid Tate ring is perfectoid. The target ring itself need not be perfectoid, and may
be zero.

```lean
RingHom.isPerfectoidTateRing_uniformTilt.{u_1, u_2} {p : ℕ} [Fact (Nat.Prime p)] {A : Type u_1}
  {B : Type u_2} [CommRing A] [UniformSpace A] [IsUniformAddGroup A] [IsTopologicalRing A]
  [TauCeti.Huber.IsTateRing A] [CompleteSpace A] [T2Space A]
  [TauCeti.Perfectoid.IsPerfectoidTateRing p A] [CommRing B] [UniformSpace B] [IsUniformAddGroup B]
  [IsTopologicalRing B] [TauCeti.Huber.IsTateRing B] [CompleteSpace B] [T2Space B]
  [TauCeti.Huber.IsUniform B] [Fact (IsTopologicallyNilpotent ↑p)] (f : A →+* B)
  (hf : Continuous ⇑f) :
  TauCeti.Perfectoid.IsPerfectoidTateRing p (TauCeti.Perfectoid.uniformTilt p B)
```

## Depends on

- [TauCeti.Perfectoid.uniformTilt](tauceti-perfectoid-uniformtilt.md)

## Proof depends on

- [Every perfectoid Tate ring has a pseudouniformiser with compatible `p`-power roots (Scholze, *Étale cohomology of diamonds*, Lemma 3.10)](every-perfectoid-tate-ring-has-a-pseudouniformis.md)
- [Henkel's open mapping theorem](../../../../part-02/topology/algebra/part-01/henkels-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`RingHom.isPerfectoidTateRing_uniformTilt`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/UniformTilt/OfHom.html#RingHom.isPerfectoidTateRing_uniformTilt).

## Sources

- [Tau Ceti documentation: `RingHom.isPerfectoidTateRing_uniformTilt`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/UniformTilt/OfHom.html#RingHom.isPerfectoidTateRing_uniformTilt)
- [Source of `RingHom.isPerfectoidTateRing_uniformTilt` in TauCeti/RingTheory/Perfectoid/UniformTilt/OfHom.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/UniformTilt/OfHom.lean#L60)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
