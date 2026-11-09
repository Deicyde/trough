---
declaration: theorem
origin: cited
lean: TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex, TauCeti.PDCode.homologyEulerChar_khovanovBracket
statement: formalized
proof: formalized
---

# Euler–Poincaré for Khovanov homology

over a Noetherian ring with the rank-nullity property,
such as `ℤ` or a field, the homology Euler characteristic of the quantum component `j` of the
normalized Khovanov complex is the coefficient of `qʲ` in the enhanced state sum, the signed count
of enhanced states of quantum degree `j`.

```lean
TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex.{u} {n : ℕ} (D : TauCeti.OrientedPDCode n)
  (hD : D.IsPlanar) (R : Type u) [CommRing R] [IsNoetherianRing R] [HasRankNullity.{u, u} R]
  (j : ℤ) :
  HomologicalComplex.homologyEulerChar (D.khovanovComplex hD R j) = D.enhancedStateSum.coeff j
```

## Depends on

- [CategoryTheory.Functor.cubeComplex](../khovanov-homology-of-classical-links/categorytheory-functor-cubecomplex.md)
- [TauCeti.Khovanov.CircleTensor](../khovanov-homology-of-classical-links/tauceti-khovanov-circletensor.md)
- [TauCeti.PDCode.resolutionMergeMap](../khovanov-homology-of-classical-links/tauceti-pdcode-resolutionmergemap.md)
- [TauCeti.PDCode.resolutionSplitMap](../khovanov-homology-of-classical-links/tauceti-pdcode-resolutionsplitmap.md)

## Proof depends on

- [Euler's formula for a PD-code](eulers-formula-for-a-pd-code.md)
- [Euler–Poincaré for cubes](../../algebra/homology/euler-poincare-for-cubes.md)
- [Hurwitz's transposition bound](../../group-theory/permutations/hurwitzs-transposition-bound.md)
- [TauCeti.Khovanov.fiberwiseSplit](../khovanov-homology-of-classical-links/tauceti-khovanov-fiberwisesplit.md)
- [Two states differing exactly at a crossing do not both have two circles through it](../khovanov-homology-of-classical-links/two-states-differing-exactly-at-a-crossing-do-no.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex).

## Other forms

**Euler–Poincaré for the unnormalized Khovanov complex.** Formalized in Tau Ceti as [`TauCeti.PDCode.homologyEulerChar_khovanovBracket`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/EulerCharacteristic.html#TauCeti.PDCode.homologyEulerChar_khovanovBracket).

```lean
TauCeti.PDCode.homologyEulerChar_khovanovBracket.{u} {n : ℕ} (D : TauCeti.PDCode n)
  (hD : D.IsPlanar) (R : Type u) [CommRing R] (j : ℤ) [IsNoetherianRing R]
  [HasRankNullity.{u, u} R] :
  HomologicalComplex.homologyEulerChar (D.khovanovBracket hD R j) =
    ∑ S,
      ↑(↑S.card).negOnePow *
        ↑(Module.finrank R
            ↥((TauCeti.Khovanov.circleQuantumGrading R
                    (D.ResolvedCircle (TauCeti.PDCode.cubeState S))).piece
                ℤ (j - ↑S.card)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex)
- [Source of `TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex` in TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean#L178)
