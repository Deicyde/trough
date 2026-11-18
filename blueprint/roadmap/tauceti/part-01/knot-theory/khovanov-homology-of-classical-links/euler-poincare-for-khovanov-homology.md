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

- [TauCeti.OrientedPDCode.khovanovComplex](tauceti-orientedpdcode-khovanovcomplex.md)

## Proof depends on

- [Euler–Poincaré for cubes](euler-poincare-for-cubes.md)
- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

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
                (j - ↑S.card)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.html#TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex)
- [Source of `TauCeti.OrientedPDCode.homologyEulerChar_khovanovComplex` in TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/EulerCharacteristic.lean#L178)
