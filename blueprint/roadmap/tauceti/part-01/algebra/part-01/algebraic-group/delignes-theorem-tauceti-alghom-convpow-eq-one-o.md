---
declaration: theorem
origin: cited
lean: TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk, TauCeti.AlgHom.convPow_finrank_eq_one
statement: formalized
proof: formalized
---

# Deligne's theorem (`TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk`)

Every point of a commutative and cocommutative Hopf algebra which is
finite flat of constant stalk rank `n` over `R` is killed by `n`.

```lean
TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk.{u_1, u_2, u_3} {R : Type u_1} {H : Type u_2}
  [CommRing R] [CommRing H] [HopfAlgebra R H] [Coalgebra.IsCocomm R H] [Module.Finite R H]
  [Module.Flat R H] {n : ℕ} (hn : ∀ (p : PrimeSpectrum R), Module.rankAtStalk H p = n)
  {A : Type u_3} [CommSemiring A] [Algebra R A] (x : WithConv (H →ₐ[R] A)) : x ^ n = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/KilledByRank.html#TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk).

## Other forms

**Deligne's theorem, free case.** Formalized in Tau Ceti as [`TauCeti.AlgHom.convPow_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/KilledByRank.html#TauCeti.AlgHom.convPow_finrank_eq_one).

```lean
TauCeti.AlgHom.convPow_finrank_eq_one.{u_1, u_2, u_3} {R : Type u_1} {H : Type u_2} [CommRing R]
  [CommRing H] [HopfAlgebra R H] [Coalgebra.IsCocomm R H] [Module.Free R H] [Module.Finite R H]
  {A : Type u_3} [CommSemiring A] [Algebra R A] (x : WithConv (H →ₐ[R] A)) :
  x ^ Module.finrank R H = 1
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/KilledByRank.html#TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk)
- [Source of `TauCeti.AlgHom.convPow_eq_one_of_rankAtStalk` in TauCeti/Algebra/AlgebraicGroup/KilledByRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/KilledByRank.lean#L177)
