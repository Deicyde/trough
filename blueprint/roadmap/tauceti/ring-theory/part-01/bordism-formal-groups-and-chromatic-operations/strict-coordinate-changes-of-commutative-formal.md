---
declaration: def
origin: cited
lean: TauCeti.LazardRing.coordinateChangeLift
statement: formalized
---

# Strict coordinate changes of commutative formal group laws are representable

pairs of a
commutative formal group law `F` and a strict coordinate `φ` over `R` correspond to ring
homomorphisms `L[b₁, b₂, …] →+* R`. The homomorphism attached to `(F, φ)` restricts to the
homomorphism `L →+* R` classifying `F` and sends `bᵢ` to the coefficient of `X^(i + 1)` in `φ`.

```lean
TauCeti.LazardRing.coordinateChangeLift.{u_1} {R : Type u_1} [CommRing R] :
  { F // F.IsComm } × ↥TauCeti.FormalCoordinate.linearCoeff.ker ≃
    (MvPolynomial ℕ+ TauCeti.LazardRing →+* R)
```

## Depends on

- [TauCeti.FormalCoordinate](../formal-laurent-fields-puiseux-expansions-and-con/tauceti-formalcoordinate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.coordinateChangeLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.html#TauCeti.LazardRing.coordinateChangeLift).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.coordinateChangeLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.html#TauCeti.LazardRing.coordinateChangeLift)
- [Source of `TauCeti.LazardRing.coordinateChangeLift` in TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.lean#L73)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
