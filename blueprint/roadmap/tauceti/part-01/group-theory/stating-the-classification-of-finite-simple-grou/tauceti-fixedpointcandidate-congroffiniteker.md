---
declaration: def
origin: cited
lean: TauCeti.FixedPointCandidate.congrOfFiniteKer
statement: formalized
---

# TauCeti.FixedPointCandidate.congrOfFiniteKer

Transport the candidate through an equivariant surjection with finite kernel whose only
fixed point is the identity.

```lean
TauCeti.FixedPointCandidate.congrOfFiniteKer.{u_1, u_2} {G : Type u_1} {H : Type u_2} [Group G]
  [Group H] {F : G →* G} {F' : H →* H} (ψ : G →* H) [Finite ↥ψ.ker] (hψ : ψ.comp F = F'.comp ψ)
  (hsurj : Function.Surjective ⇑ψ) (hker : Disjoint ψ.ker (TauCeti.fixedSubgroup F)) :
  TauCeti.FixedPointCandidate F ≃* TauCeti.FixedPointCandidate F'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FixedPointCandidate.congrOfFiniteKer`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FixedPointCandidate/FiniteKernel.html#TauCeti.FixedPointCandidate.congrOfFiniteKer).

## Sources

- [Tau Ceti documentation: `TauCeti.FixedPointCandidate.congrOfFiniteKer`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FixedPointCandidate/FiniteKernel.html#TauCeti.FixedPointCandidate.congrOfFiniteKer)
- [Source of `TauCeti.FixedPointCandidate.congrOfFiniteKer` in TauCeti/GroupTheory/FixedPointCandidate/FiniteKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FixedPointCandidate/FiniteKernel.lean#L26)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGStatement/STATUS.md)
