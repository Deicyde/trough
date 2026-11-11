---
declaration: theorem
origin: cited
lean: TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan
statement: formalized
proof: formalized
---

# TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan

A realization is minimal exactly when its full center lies in the coroot span.

```lean
TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan.{u_1, u_2, u_3} {I : Type u_1}
  {K : Type u_2} {H : Type u_3} [Fintype I] [Field K] [AddCommGroup H] [_root_.Module K H]
  {A : Matrix I I K} (R : TauCeti.CartanRealization A H) :
  R.IsMinimal ↔ R.cartanCenter ≤ R.corootSpan
```

## Depends on

- [TauCeti.CartanRealization](tauceti-cartanrealization.md)

## Proof depends on

- [TauCeti.CartanRealization.cartanCenter_inf_corootSpan](tauceti-cartanrealization-cartancenter-inf-coroo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan).

## Sources

- [Tau Ceti documentation: `TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan)
- [Source of `TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L368)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KacMoody/STATUS.md)
