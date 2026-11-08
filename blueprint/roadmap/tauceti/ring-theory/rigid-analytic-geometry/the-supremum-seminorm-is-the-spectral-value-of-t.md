---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow
statement: formalized
proof: formalized
---

# The supremum seminorm is the spectral value of the minimal polynomial

Let `B` be an
affinoid algebra which is integral and torsion-free over an integrally closed domain `A`. For
`f : B` with minimal polynomial `X ^ d + ∑_{i < d} aᵢ X ^ i` over `A`,
`|f|sup = max_{i < d} |aᵢ|sup ^ (1 / (d - i))`.

```lean
TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A]
  [Algebra K A] {B : Type u_3} [CommRing B] [Algebra K B] [Algebra A B] [IsScalarTower K A B]
  (hB : TauCeti.IsAffinoidAlgebra K B) [IsDomain A] [IsIntegrallyClosed A]
  [Module.IsTorsionFree A B] [Algebra.IsIntegral A B] (f : B) :
  TauCeti.supSeminorm K f =
    ⨆ i, TauCeti.supSeminorm K ((minpoly A f).coeff ↑i) ^ (1 / (↑(minpoly A f).natDegree - ↑↑i))
```

## Depends on

- [TauCeti.supSeminorm](tauceti-supseminorm.md)

## Proof depends on

- [Kedlaya's Hilbert basis theorem for `A^r` (Kedlaya, Theorem 3.2)](../mv-power-series/kedlayas-hilbert-basis-theorem-for-a-r-kedlaya-t.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)
- [The Weierstrass division estimate in several variables](../mv-power-series/the-weierstrass-division-estimate-in-several-var.md)
- [The Weierstrass division identity](../p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MinimalPolynomial.html#TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MinimalPolynomial.html#TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow)
- [Source of `TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow` in TauCeti/RingTheory/Affinoid/MinimalPolynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/MinimalPolynomial.lean#L203)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
