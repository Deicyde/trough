---
declaration: def
origin: cited
lean: TauCeti.LazardRing.gradedCoordinateChangeLift
statement: formalized
---

# TauCeti.LazardRing.gradedCoordinateChangeLift

The graded universal property of `L[b₁, b₂, …]`: graded classifying maps correspond to
commutative graded formal group laws equipped with strict graded coordinates.

```lean
TauCeti.LazardRing.gradedCoordinateChangeLift.{u_1, u_2} {A : Type u_1} {σ : Type u_2} [CommRing A]
  [SetLike σ A] [AddSubgroupClass σ A] {𝒜 : ℕ → σ} [SetLike.GradedMonoid 𝒜] :
  { p //
      (∀ (d : Fin 2 →₀ ℕ),
          (MvPowerSeries.coeff d) (↑p.1).toPowerSeries ∈ 𝒜 (2 * (Finsupp.degree d - 1))) ∧
        ∀ (i : ℕ+), (PowerSeries.coeff (↑i + 1)) (↑p.2).toPowerSeries ∈ 𝒜 (2 * ↑i) } ≃
    (TauCeti.LazardRing.coordinateGrading →+*ᵍ 𝒜)
```

## Depends on

- [Lazard's theorem](lazards-theorem.md)
- [Strict coordinate changes of commutative formal group laws are representable](strict-coordinate-changes-of-commutative-formal.md)

## Proof depends on

- [Lazard's theorem, graded](lazards-theorem-graded.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.gradedCoordinateChangeLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/Grading.html#TauCeti.LazardRing.gradedCoordinateChangeLift).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.gradedCoordinateChangeLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/Grading.html#TauCeti.LazardRing.gradedCoordinateChangeLift)
- [Source of `TauCeti.LazardRing.gradedCoordinateChangeLift` in TauCeti/RingTheory/FormalGroup/CoordinateChange/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/CoordinateChange/Grading.lean#L170)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
