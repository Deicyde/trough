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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.coordinateChangeLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.html#TauCeti.LazardRing.coordinateChangeLift).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.coordinateChangeLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.html#TauCeti.LazardRing.coordinateChangeLift)
- [Source of `TauCeti.LazardRing.coordinateChangeLift` in TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FormalGroup/CoordinateChange/Lazard.lean#L73)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
