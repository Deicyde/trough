---
declaration: theorem
origin: cited
lean: TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank
statement: formalized
proof: formalized
---

# TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank

A realization has dimension at least twice the number of nodes minus the matrix rank.
The addition form avoids truncated subtraction and applies in every characteristic.

```lean
TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank.{u_1, u_2, u_3} {I : Type u_1}
  {K : Type u_2} {H : Type u_3} [Fintype I] [Field K] [AddCommGroup H] [_root_.Module K H]
  {A : Matrix I I K} (R : TauCeti.CartanRealization A H) [FiniteDimensional K H] :
  2 * Fintype.card I ≤ A.rank + Module.finrank K H
```

## Depends on

- [TauCeti.CartanRealization](tauceti-cartanrealization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank).

## Sources

- [Tau Ceti documentation: `TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank)
- [Source of `TauCeti.CartanRealization.two_mul_card_le_rank_add_finrank` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L336)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KacMoody/STATUS.md)
