---
declaration: def
origin: cited
lean: TauCeti.LazardRing.gradedLift
statement: formalized
---

# The graded universal property of the Lazard ring

for a commutative ring `A` graded by
`𝒜`, graded ring homomorphisms `L →+*ᵍ A` correspond to commutative formal group laws over `A`
whose coefficient of every monomial `X^(d 0) Y^(d 1)` lies in `𝒜 (2 (d 0 + d 1 - 1))`, that is,
whose coefficient `aᵢⱼ` lies in `𝒜 (2 (i + j - 1))` for all `i, j ≥ 1`. A formal group law
corresponds to the homomorphism `TauCeti.LazardRing.lift` classifying it.

```lean
TauCeti.LazardRing.gradedLift.{u_1, u_5} {A : Type u_1} [CommRing A] {σ : Type u_5} [SetLike σ A]
  [AddSubgroupClass σ A] {𝒜 : ℕ → σ} [SetLike.GradedMonoid 𝒜] :
  { F //
      F.IsComm ∧
        ∀ (d : Fin 2 →₀ ℕ),
          (MvPowerSeries.coeff d) F.toPowerSeries ∈ 𝒜 (2 * (Finsupp.degree d - 1)) } ≃
    (TauCeti.LazardRing.grading →+*ᵍ 𝒜)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.gradedLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Basic.html#TauCeti.LazardRing.gradedLift).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.gradedLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Basic.html#TauCeti.LazardRing.gradedLift)
- [Source of `TauCeti.LazardRing.gradedLift` in TauCeti/RingTheory/FormalGroup/LazardRing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FormalGroup/LazardRing/Basic.lean#L462)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
