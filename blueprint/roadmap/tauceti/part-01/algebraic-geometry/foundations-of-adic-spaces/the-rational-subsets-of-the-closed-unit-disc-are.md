---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion
statement: formalized
proof: formalized
---

# The rational subsets of the closed unit disc are exactly the finite unions of holed discs

**The rational subsets of the closed unit disc are exactly the finite unions of holed discs**,
over an algebraically closed nontrivially normed ultrametric field. The forward direction is
`exists_finset_eq_iUnion_holedDisc_of_mem_spaRationalFamily` and the converse is
`IsHoledDiscUnion.mem_spaRationalFamily`.

```lean
TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion.{u_2} {K : Type u_2}
  [NontriviallyNormedField K] [IsUltrametricDist K] [NonarchimedeanRing K] [IsAlgClosed K]
  {U : Set ↑(TauCeti.ValuationSpectrum.closedPolydisc 1 K)} :
  ⇑(Homeomorph.setCongr ⋯).symm ⁻¹' U ∈
      TauCeti.ValuationSpectrum.spaRationalFamily
        (TauCeti.Huber.powerBoundedSubring
          ↥(TauCeti.Huber.weightedRestrictedSubring (fun x => {1}) ⋯)) ↔
    TauCeti.ValuationSpectrum.IsHoledDiscUnion U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/PolynomialDomain.html#TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/PolynomialDomain.html#TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion)
- [Source of `TauCeti.ValuationSpectrum.mem_spaRationalFamily_iff_isHoledDiscUnion` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/PolynomialDomain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/PolynomialDomain.lean#L489)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
