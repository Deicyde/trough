---
declaration: theorem
origin: cited
lean: TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl
statement: formalized
proof: formalized
---

# TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl

Every realization is a minimal sub-realization plus a central
summand. The roots of the sub-realization are restrictions, and its coroots are the original
coroots, rather than merely abstractly isomorphic families.

```lean
TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl.{u_1, u_2, u_3} {I : Type u_1}
  {K : Type u_2} {H : Type u_3} [Fintype I] [Field K] [AddCommGroup H] [_root_.Module K H]
  {A : Matrix I I K} (R : TauCeti.CartanRealization A H) :
  ∃ M Z,
    ∃ (hc : R.corootSpan ≤ M) (hs : M ⊔ R.cartanCenter = ⊤),
      (R.restrict M hc hs).IsMinimal ∧ IsCompl M Z ∧ Z ≤ R.cartanCenter
```

## Depends on

- [TauCeti.CartanRealization](tauceti-cartanrealization.md)

## Proof depends on

- [TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan](tauceti-cartanrealization-isminimal-iff-cartance.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/CentralSplitting.html#TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl).

## Sources

- [Tau Ceti documentation: `TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/CentralSplitting.html#TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl)
- [Source of `TauCeti.CartanRealization.exists_isMinimal_restrict_isCompl` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/CentralSplitting.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/CentralSplitting.lean#L48)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KacMoody/STATUS.md)
