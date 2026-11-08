---
declaration: theorem
origin: cited
lean: TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial
statement: formalized
proof: formalized
---

# Khovanov's theorem

the graded Euler characteristic of the Khovanov homology of a nonempty
planar oriented code is `(q + q⁻¹)` times its Jones polynomial at `t ^ (1/2) = -q`, over a
Noetherian ring with the rank-nullity property, such as `ℤ` or a field. The hypothesis
`0 < componentCount` says that the diagram is nonempty; the empty diagram has graded Euler
characteristic `1` (`TauCeti.OrientedPDCode.khovanovEulerChar_empty`).

```lean
TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial.{u} {n : ℕ}
  (D : TauCeti.OrientedPDCode n) (hD : D.IsPlanar) (R : Type u) [CommRing R] [IsNoetherianRing R]
  [HasRankNullity.{u, u} R] (h : 0 < D.componentCount) :
  D.khovanovEulerChar hD R =
    (LaurentPolynomial.T 1 + LaurentPolynomial.T (-1)) *
      (LaurentPolynomial.eval₂ (Int.castRingHom (LaurentPolynomial ℤ))
          (-LaurentPolynomial.genericUnit ℤ))
        D.jonesPolynomial
```

## Depends on

- [CategoryTheory.Functor.cubeComplex](../khovanov-homology-of-classical-links/categorytheory-functor-cubecomplex.md)
- [TauCeti.Khovanov.CircleTensor](../khovanov-homology-of-classical-links/tauceti-khovanov-circletensor.md)
- [TauCeti.PDCode.resolutionMergeMap](../khovanov-homology-of-classical-links/tauceti-pdcode-resolutionmergemap.md)
- [TauCeti.PDCode.resolutionSplitMap](../khovanov-homology-of-classical-links/tauceti-pdcode-resolutionsplitmap.md)

## Proof depends on

- [The enhanced state sum of a nonempty diagram is `(q + q⁻¹)` times its Jones polynomial at `t ^ (1/2) = -q`](../khovanov-homology-of-classical-links/the-enhanced-state-sum-of-a-nonempty-diagram-is.md)
- [Euler's formula for a PD-code](eulers-formula-for-a-pd-code.md)
- [Euler–Poincaré for Khovanov homology](euler-poincare-for-khovanov-homology.md)
- [Hurwitz's transposition bound](../../group-theory/permutations/hurwitzs-transposition-bound.md)
- [TauCeti.Khovanov.fiberwiseSplit](../khovanov-homology-of-classical-links/tauceti-khovanov-fiberwisesplit.md)
- [Two states differing exactly at a crossing do not both have two circles through it](../khovanov-homology-of-classical-links/two-states-differing-exactly-at-a-crossing-do-no.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval%E2%82%82_jonesPolynomial).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval%E2%82%82_jonesPolynomial)
- [Source of `TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial` in TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean#L198)
