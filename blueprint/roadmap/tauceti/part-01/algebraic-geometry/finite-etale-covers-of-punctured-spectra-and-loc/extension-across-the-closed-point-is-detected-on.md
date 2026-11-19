---
declaration: theorem
origin: cited
lean: TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth
statement: formalized
proof: formalized
---

# Extension across the closed point is detected on the completion, for a Noetherian local ring `A` of depth at least two

a finite étale cover of the punctured spectrum of `A` extends
across the closed point if and only if its base change to the punctured spectrum of the
`𝔪`-adic completion `Â` extends across the closed point of `Spec Â`.

```lean
TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth.{u} {A : Type u} [CommRing A]
  [IsLocalRing A] [IsNoetherianRing A] (hdepth : 2 ≤ IsLocalRing.depth ↧A)
  (V : TauCeti.FiniteEtaleScheme ↑(TauCeti.IsLocalRing.puncturedSpectrum A)) :
  (∃ Y, Nonempty ((TauCeti.IsLocalRing.restrictPunctured A).obj Y ≅ V)) ↔
    ∃ Y,
      Nonempty
        ((TauCeti.IsLocalRing.restrictPunctured (AdicCompletion (IsLocalRing.maximalIdeal A) A)).obj
            Y ≅
          (TauCeti.IsLocalRing.pullbackPunctured ⋯).obj V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Algebraic Hartogs principle](../other-results/algebraic-hartogs-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Completion.html#TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Completion.html#TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth)
- [Source of `TauCeti.IsLocalRing.extends_iff_completion_extends_of_two_le_depth` in TauCeti/AlgebraicGeometry/FiniteEtale/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/Completion.lean#L132)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
