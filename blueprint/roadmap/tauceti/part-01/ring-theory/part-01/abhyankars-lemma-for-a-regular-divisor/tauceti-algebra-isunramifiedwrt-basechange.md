---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.IsUnramifiedWRT.baseChange
statement: formalized
proof: formalized
---

# TauCeti.Algebra.IsUnramifiedWRT.baseChange

Unramified extensions of a discrete valuation ring are stable under base change: if `L` is
unramified with respect to `A`, then every factor `L'` of `K' ⊗[K] L`, given by a surjective
`K'`-algebra map `φ : K' ⊗[K] L → L'`, is unramified with respect to `A'`.

```lean
TauCeti.Algebra.IsUnramifiedWRT.baseChange.{u_1, u_2, u_3, u_4, u_5, u_6} {A : Type u_1}
  {K : Type u_2} {L : Type u_3} {A' : Type u_4} {K' : Type u_5} {L' : Type u_6} [CommRing A]
  [IsDomain A] [IsDiscreteValuationRing A] [Field K] [Algebra A K] [IsFractionRing A K] [Field L]
  [Algebra A L] [Algebra K L] [IsScalarTower A K L] [FiniteDimensional K L]
  [Algebra.IsSeparable K L] [CommRing A'] [IsDomain A'] [IsDiscreteValuationRing A'] [Field K']
  [Algebra A' K'] [IsFractionRing A' K'] [Algebra A A'] [Algebra A K'] [Algebra K K']
  [IsScalarTower A A' K'] [IsScalarTower A K K'] [Field L'] [Algebra K' L'] [Algebra A' L']
  [IsScalarTower A' K' L'] (h : TauCeti.Algebra.IsUnramifiedWRT A L)
  (φ : TensorProduct K K' L →ₐ[K'] L') (hφ : Function.Surjective ⇑φ) :
  TauCeti.Algebra.IsUnramifiedWRT A' L'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Algebra.isUnramifiedWRT_iff_etale](tauceti-algebra-isunramifiedwrt-iff-etale.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.IsUnramifiedWRT.baseChange`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/BaseChange/Unramified.html#TauCeti.Algebra.IsUnramifiedWRT.baseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.IsUnramifiedWRT.baseChange`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/BaseChange/Unramified.html#TauCeti.Algebra.IsUnramifiedWRT.baseChange)
- [Source of `TauCeti.Algebra.IsUnramifiedWRT.baseChange` in TauCeti/RingTheory/DiscreteValuationRing/BaseChange/Unramified.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DiscreteValuationRing/BaseChange/Unramified.lean#L83)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
