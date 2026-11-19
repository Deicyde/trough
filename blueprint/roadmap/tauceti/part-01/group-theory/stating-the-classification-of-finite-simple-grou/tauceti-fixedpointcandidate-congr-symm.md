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
- [Source of `TauCeti.FixedPointCandidate.congr_symm` in TauCeti/GroupTheory/FixedPointCandidate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/FixedPointCandidate.lean#L103)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CFSGStatement/STATUS.md)
