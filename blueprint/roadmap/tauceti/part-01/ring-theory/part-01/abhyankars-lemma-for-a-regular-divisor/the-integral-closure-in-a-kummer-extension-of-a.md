---
declaration: theorem
origin: cited
lean: TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible
statement: formalized
proof: formalized
---

# The integral closure in a Kummer extension of a discrete valuation ring

If `L` is
generated over the fraction field `K` of a discrete valuation ring `A` by an `n`-th root `α` of a
uniformizer `π` of `A`, then the integral closure of `A` in `L` is `A[α]`. Together with
`TauCeti.IsDiscreteValuationRing.minpoly_eq_of_pow_eq_of_irreducible` and
`minpoly.equivAdjoin`, it is `A[X] ⧸ (X ^ n - π)`.

```lean
TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible.{u_1, u_2, u_3}
  {A : Type u_1} [CommRing A] [IsDomain A] [IsDiscreteValuationRing A] {π : A} {n : ℕ}
  {K : Type u_2} {L : Type u_3} [Field K] [Algebra A K] [IsFractionRing A K] [Field L] [Algebra K L]
  [Algebra A L] [IsScalarTower A K L] {α : L} (hπ : Irreducible π) (hn : n ≠ 0)
  (hα : α ^ n = (algebraMap A L) π) (hgen : K⟮α⟯ = ⊤) : integralClosure A L = A[α]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Kummer.html#TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Kummer.html#TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible)
- [Source of `TauCeti.IsDiscreteValuationRing.integralClosure_eq_adjoin_of_pow_eq_of_irreducible` in TauCeti/RingTheory/DiscreteValuationRing/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DiscreteValuationRing/Kummer.lean#L143)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
