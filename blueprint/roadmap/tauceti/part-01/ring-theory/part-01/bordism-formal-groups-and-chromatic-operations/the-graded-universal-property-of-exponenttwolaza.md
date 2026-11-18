---
declaration: def
origin: cited
lean: TauCeti.ExponentTwoLazardRing.gradedLift
statement: formalized
---

# The graded universal property of `ExponentTwoLazardRing`

for a commutative ring `A` graded
by `𝒜`, graded ring homomorphisms out of `ExponentTwoLazardRing` correspond to commutative formal
group laws `F` over `A` with `[2]_F = 0` whose coefficient of every monomial `X^(d 0) Y^(d 1)` lies
in `𝒜 (d 0 + d 1 - 1)`. A formal group law corresponds to the homomorphism
`TauCeti.ExponentTwoLazardRing.lift` classifying it.

```lean
TauCeti.ExponentTwoLazardRing.gradedLift.{u_2, u_3} {A : Type u_2} {σ : Type u_3} [CommRing A]
  [SetLike σ A] [AddSubmonoidClass σ A] {𝒜 : ℕ → σ} [GradedRing 𝒜] :
  { F //
      F.IsComm ∧
        F.nsmulSeries 2 = 0 ∧
          ∀ (d : Fin 2 →₀ ℕ), (MvPowerSeries.coeff d) F.toPowerSeries ∈ 𝒜 (Finsupp.degree d - 1) } ≃
    (TauCeti.ExponentTwoLazardRing.grading →+*ᵍ 𝒜)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExponentTwoLazardRing.gradedLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/ExponentTwo/Universal.html#TauCeti.ExponentTwoLazardRing.gradedLift).

## Sources

- [Tau Ceti documentation: `TauCeti.ExponentTwoLazardRing.gradedLift`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/ExponentTwo/Universal.html#TauCeti.ExponentTwoLazardRing.gradedLift)
- [Source of `TauCeti.ExponentTwoLazardRing.gradedLift` in TauCeti/RingTheory/FormalGroup/ExponentTwo/Universal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/ExponentTwo/Universal.lean#L327)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
