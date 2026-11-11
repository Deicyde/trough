---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective
statement: formalized
proof: formalized
---

# Noether normalisation in the dimension of the algebra

A nonzero dagger algebra is
finite over an injectively embedded overconvergent algebra in `dim A` variables.

```lean
TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective.{u_1, u_2} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A] [Algebra K A]
  [TauCeti.Dagger.IsDaggerAlgebra K A] [Nontrivial A] :
  ∃ n, ringKrullDim A = ↑n ∧ ∃ g, Function.Injective ⇑g ∧ g.Finite
```

## Depends on

- [TauCeti.Dagger.IsDaggerAlgebra](tauceti-dagger-isdaggeralgebra.md)

## Proof depends on

- [Krull dimension of the Monsky–Washnitzer algebra](krull-dimension-of-the-monsky-washnitzer-algebra.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/KrullDimension.html#TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/KrullDimension.html#TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective)
- [Source of `TauCeti.Dagger.IsDaggerAlgebra.exists_ringKrullDim_eq_finite_injective` in TauCeti/RingTheory/Dagger/KrullDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/KrullDimension.lean#L168)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
