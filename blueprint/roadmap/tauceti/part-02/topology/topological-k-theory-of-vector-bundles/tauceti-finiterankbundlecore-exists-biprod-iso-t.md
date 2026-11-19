---
declaration: theorem
origin: cited
lean: TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial
statement: formalized
proof: formalized
---

# TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial

Over a compact normal base, in particular a compact Hausdorff base, every real or complex
finite-rank core is a direct summand of a trivial core.

```lean
TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial.{u_1, u_2} {𝕜 : Type u_1} {B : Type u_2}
  [RCLike 𝕜] [TopologicalSpace B] [CompactSpace B] [NormalSpace B]
  (A : TauCeti.FiniteRankBundleCore 𝕜 B) :
  ∃ N D, Nonempty (A ⊞ D ≅ TauCeti.FiniteRankBundleCore.trivial 𝕜 B N)
```

## Depends on

- [TauCeti.FiniteRankBundleCore](tauceti-finiterankbundlecore.md)

## Proof depends on

- [The ranges of a continuous family of projections form a vector bundle](the-ranges-of-a-continuous-family-of-projections.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/Complement.html#TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/Complement.html#TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial)
- [Source of `TauCeti.FiniteRankBundleCore.exists_biprod_iso_trivial` in TauCeti/Topology/VectorBundle/FiniteRank/Complement.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/FiniteRank/Complement.lean#L239)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
