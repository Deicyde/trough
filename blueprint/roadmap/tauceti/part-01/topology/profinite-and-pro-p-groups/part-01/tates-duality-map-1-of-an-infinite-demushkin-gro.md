---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective
statement: formalized
proof: formalized
---

# Tate's duality map `α₁` of an infinite Demushkin group with coefficients `I(χ)/pⁱ` is bijective on every finite discrete `G`-module `M` killed by `pⁱ`

`H¹(G, M) × H¹(G, Hom(M, I(χ)/pⁱ)) → H²(G, I(χ)/pⁱ)` is a perfect pairing.

```lean
TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Infinite G] (hG : TauCeti.IsDemushkin p G) (i : ℕ) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p ^ i • x = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap1 G M (TauCeti.ZModTwist (TauCeti.demushkinCharacter hG) i))
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [Tate's theorem: an infinite Demushkin group has `p`-cohomological dimension exactly `2`](tates-theorem-an-infinite-demushkin-group-has-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective)
- [Source of `TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.lean#L213)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
