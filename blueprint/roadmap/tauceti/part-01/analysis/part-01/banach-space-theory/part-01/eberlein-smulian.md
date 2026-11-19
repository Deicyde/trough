---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_toWeakSpace_iff_isSeqCompact
statement: formalized
proof: formalized
---

# Eberlein–Šmulian

Weak compactness is equivalent to weak sequential compactness,
without completeness or separability assumptions.

```lean
TauCeti.isCompact_toWeakSpace_iff_isSeqCompact.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {K : Set E} :
  IsCompact (⇑(toWeakSpace 𝕜 E) '' K) ↔ IsSeqCompact (⇑(toWeakSpace 𝕜 E) '' K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Šmulian's theorem](../../../part-03/normed/part-03/smulians-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_toWeakSpace_iff_isSeqCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.html#TauCeti.isCompact_toWeakSpace_iff_isSeqCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_toWeakSpace_iff_isSeqCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.html#TauCeti.isCompact_toWeakSpace_iff_isSeqCompact)
- [Source of `TauCeti.isCompact_toWeakSpace_iff_isSeqCompact` in TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.lean#L151)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
