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
- [Source of `TauCeti.CartanRealization.isMinimal_iff_cartanCenter_le_corootSpan` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L378)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KacMoody/STATUS.md)
