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

- [CategoryTheory.Functor.cubeComplex](categorytheory-functor-cubecomplex.md)
- [TauCeti.Khovanov.CircleTensor](tauceti-khovanov-circletensor.md)
- [TauCeti.PDCode.resolutionMergeMap](tauceti-pdcode-resolutionmergemap.md)
- [TauCeti.PDCode.resolutionSplitMap](tauceti-pdcode-resolutionsplitmap.md)

## Proof depends on

- [The enhanced state sum of a nonempty diagram is `(q + q⁻¹)` times its Jones polynomial at `t ^ (1/2) = -q`](the-enhanced-state-sum-of-a-nonempty-diagram-is.md)
- [Euler's formula for a PD-code](../other-results/eulers-formula-for-a-pd-code.md)
- [The Euler–Poincaré theorem in abelian `K₀`](../../algebra/grothendieck-groups-cartan-maps-and-euler-forms/part-01/the-euler-poincare-theorem-in-abelian-k0.md)
- [Hurwitz's transposition bound](../../group-theory/perm/hurwitzs-transposition-bound.md)
- [TauCeti.Khovanov.fiberwiseSplit](tauceti-khovanov-fiberwisesplit.md)
- [Two states differing exactly at a crossing do not both have two circles through it](two-states-differing-exactly-at-a-crossing-do-no.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval%E2%82%82_jonesPolynomial).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval%E2%82%82_jonesPolynomial)
- [Source of `TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial` in TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean#L198)
