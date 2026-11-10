---
declaration: theorem
origin: cited
lean: TauCeti.weylDenominator_eq_weylNumerator_zero, RootPairing.dotAlternatization_one
statement: formalized
proof: formalized
---

# The Weyl denominator identity

the Weyl denominator is the Weyl numerator of the weight
`0`,

`∏_{α > 0} (1 - e^{-α}) = ∑_{w ∈ W} sgn(w) e^{w ⬝ 0}`,

an identity in the integral group algebra of the weight space. Written without the dot action, the
right-hand side is `∑_{w ∈ W} sgn(w) e^{w(ρ) - ρ}`.

This is the case `λ = 0` of the Weyl character formula, in which the character of the trivial
module is `1`.

```lean
TauCeti.weylDenominator_eq_weylNumerator_zero.{u, v, w, x} {ι : Type u} {R : Type v} {M : Type w}
  {N : Type x} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι] [CharZero R] (b : P.Base) [LinearOrder R]
  [IsStrictOrderedRing R] [Invertible 2] [P.IsCrystallographic] [P.IsReduced] [P.IsRootSystem]
  [Fintype ↥P.weylGroup] : TauCeti.weylDenominator P b = TauCeti.weylNumerator P b 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weylDenominator_eq_weylNumerator_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Identity.html#TauCeti.weylDenominator_eq_weylNumerator_zero).

## Other forms

**The Weyl denominator identity for a root datum.** Formalized in Tau Ceti as [`RootPairing.dotAlternatization_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Integral.html#RootPairing.dotAlternatization_one).

```lean
RootPairing.dotAlternatization_one.{u_1, u_2, u_3} {ι : Type u_1} {M : Type u_2} {N : Type u_3}
  [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N) [Finite ι] (b : P.Base) [P.IsReduced]
  [Fintype ↥P.weylGroup] : (P.dotAlternatization b) 1 = TauCeti.weylDenominator P b
```

## Sources

- [Tau Ceti documentation: `TauCeti.weylDenominator_eq_weylNumerator_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Identity.html#TauCeti.weylDenominator_eq_weylNumerator_zero)
- [Source of `TauCeti.weylDenominator_eq_weylNumerator_zero` in TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Identity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Identity.lean#L130)
