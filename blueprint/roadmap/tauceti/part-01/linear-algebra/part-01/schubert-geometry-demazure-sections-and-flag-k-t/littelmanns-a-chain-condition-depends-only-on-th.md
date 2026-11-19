---
declaration: theorem
origin: cited
lean: TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd
statement: formalized
proof: formalized
---

# Littelmann's `a`-chain condition depends only on the ends

For minimal coset
representatives `y ≤ x`, there is an `a`-chain from `x` down to `y` exactly when the denominator
of `a` divides `d_λ(x, y)`.

```lean
TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd.{u, w, x} {ι : Type u} {M : Type w} {N : Type x}
  [AddCommGroup M] [AddCommGroup N] {P : RootPairing ι ℤ M N} {b : P.Base} [Finite ι] [P.IsReduced]
  {lam : M} {a : ℚ} (hlam : lam ∈ P.dominantChamber b) {x y : ↥P.weylGroup}
  (hx : (TauCeti.weylCoxeterSystem P b).IsMinimalCosetRep (P.wallIndices b lam) x)
  (hy : (TauCeti.weylCoxeterSystem P b).IsMinimalCosetRep (P.wallIndices b lam) y)
  (hyx : (TauCeti.weylCoxeterSystem P b).BruhatLE y x) :
  (∃ C, ↑(RelSeries.head C) = x ∧ ↑(RelSeries.last C) = y ∧ TauCeti.IsAChain a lam C) ↔
    a.den ∣ TauCeti.intervalBondGcd b lam x y
```

## Depends on

- [TauCeti.intervalBondGcd](tauceti-intervalbondgcd.md)

## Proof depends on

- [Deodhar's lemma](../../../group-theory/coxeter/deodhars-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.html#TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.html#TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd)
- [Source of `TauCeti.exists_isAChain_iff_den_dvd_intervalBondGcd` in TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.lean#L410)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
