---
declaration: theorem
origin: cited
lean: Finset.image_map_integerProjection
statement: formalized
proof: formalized
---

# The integer projection computes the real projection

Mapping the integer projection of
`P` to `ℝ` gives the Collins projection of the real family of `P`.

```lean
Finset.image_map_integerProjection {n : ℕ} [DecidableEq (MvPolynomial (Fin n) ℝ)]
  (P : Finset (MvPolynomial (Fin (n + 1)) ℤ)) :
  Finset.image (⇑(MvPolynomial.map (Int.castRingHom ℝ))) P.integerProjection =
    P.integerFamily.collinsProjection
```

## Depends on

- [Finset.integerProjection](finset-integerprojection.md)

## Lean

Formalized in Tau Ceti as [`Finset.image_map_integerProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Integer.html#Finset.image_map_integerProjection).

## Sources

- [Tau Ceti documentation: `Finset.image_map_integerProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Integer.html#Finset.image_map_integerProjection)
- [Source of `Finset.image_map_integerProjection` in TauCeti/Geometry/RealAlgebraic/Projection/Integer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Projection/Integer.lean#L114)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
