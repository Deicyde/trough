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

- [Eberlein–Šmulian, relative form](eberlein-smulian-relative-form.md)
- [Šmulian's theorem](../part-02/smulians-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_toWeakSpace_iff_isSeqCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.html#TauCeti.isCompact_toWeakSpace_iff_isSeqCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_toWeakSpace_iff_isSeqCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.html#TauCeti.isCompact_toWeakSpace_iff_isSeqCompact)
- [Source of `TauCeti.isCompact_toWeakSpace_iff_isSeqCompact` in TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.lean#L151)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
