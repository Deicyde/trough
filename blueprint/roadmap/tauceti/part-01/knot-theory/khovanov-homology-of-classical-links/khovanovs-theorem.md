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

- [TauCeti.OrientedPDCode.khovanovComplex](tauceti-orientedpdcode-khovanovcomplex.md)

## Proof depends on

- [Euler–Poincaré for Khovanov homology](euler-poincare-for-khovanov-homology.md)
- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval%E2%82%82_jonesPolynomial).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval%E2%82%82_jonesPolynomial)
- [Source of `TauCeti.OrientedPDCode.khovanovEulerChar_eq_mul_eval₂_jonesPolynomial` in TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean#L198)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
