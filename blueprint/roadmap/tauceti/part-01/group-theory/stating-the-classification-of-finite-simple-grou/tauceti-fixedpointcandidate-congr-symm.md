---
declaration: theorem
origin: cited
lean: TauCeti.FixedPointCandidate.congr_symm
statement: formalized
proof: formalized
---

# TauCeti.FixedPointCandidate.congr_symm

```lean
TauCeti.FixedPointCandidate.congr_symm.{u_1, u_2} {G : Type u_1} [Group G] {G' : Type u_2}
  [Group G'] {F : G →* G} {F' : G' →* G'} (ψ : G ≃* G') (hψ : (↑ψ).comp F = F'.comp ↑ψ) :
  (TauCeti.FixedPointCandidate.congr ψ hψ).symm = TauCeti.FixedPointCandidate.congr ψ.symm ⋯
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FixedPointCandidate.congr_symm`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FixedPointCandidate.html#TauCeti.FixedPointCandidate.congr_symm).

## Sources

- [Tau Ceti documentation: `TauCeti.FixedPointCandidate.congr_symm`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FixedPointCandidate.html#TauCeti.FixedPointCandidate.congr_symm)
- [Source of `TauCeti.FixedPointCandidate.congr_symm` in TauCeti/GroupTheory/FixedPointCandidate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FixedPointCandidate.lean#L106)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGStatement/STATUS.md)
