---
declaration: theorem
origin: cited
lean: TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing
statement: formalized
proof: formalized
---

# In characteristic `p`, perfectoid means perfect (Scholze, *Étale cohomology of diamonds*, Proposition 3.5)

a complete Hausdorff Tate ring of characteristic `p` is a perfectoid Tate ring
exactly when it is a perfect ring.

```lean
TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing.{u_1} {p : ℕ} [Fact (Nat.Prime p)]
  {R : Type u_1} [CommRing R] [UniformSpace R] [IsUniformAddGroup R] [IsTopologicalRing R]
  [TauCeti.Huber.IsTateRing R] [CompleteSpace R] [T2Space R] [CharP R p] :
  TauCeti.Perfectoid.IsPerfectoidTateRing p R ↔ PerfectRing R p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius surjectivity criterion](../../part-02/other-results/part-01/the-frobenius-surjectivity-criterion.md)
- [Henkel's open mapping theorem](../../../../part-02/topology/algebra/part-01/henkels-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/PerfectRing.html#TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/PerfectRing.html#TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing)
- [Source of `TauCeti.Perfectoid.isPerfectoidTateRing_iff_perfectRing` in TauCeti/RingTheory/Perfectoid/PerfectRing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/PerfectRing.lean#L94)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
