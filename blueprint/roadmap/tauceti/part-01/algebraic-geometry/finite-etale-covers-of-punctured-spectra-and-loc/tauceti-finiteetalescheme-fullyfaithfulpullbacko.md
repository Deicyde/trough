---
declaration: def
origin: cited
lean: TauCeti.FiniteEtaleScheme.fullyFaithfulPullbackιOfTwoLeDepthStalk
statement: formalized
---

# TauCeti.FiniteEtaleScheme.fullyFaithfulPullbackιOfTwoLeDepthStalk

Let `X` be a locally Noetherian scheme and `U` an open subscheme such that the local ring
`𝒪_{X,x}` has depth at least two at every point `x ∉ U`. Then restriction of finite étale schemes
over `X` to `U` is fully faithful.

```lean
TauCeti.FiniteEtaleScheme.fullyFaithfulPullbackιOfTwoLeDepthStalk.{u} {X : AlgebraicGeometry.Scheme}
  [AlgebraicGeometry.IsLocallyNoetherian X] (U : X.Opens)
  (h : ∀ x ∉ U, 2 ≤ IsLocalRing.depth ↧↑(X.presheaf.stalk x)) :
  (TauCeti.FiniteEtaleScheme.pullback U.ι).FullyFaithful
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Algebraic Hartogs principle](../other-results/algebraic-hartogs-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.fullyFaithfulPullbackιOfTwoLeDepthStalk`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/FullyFaithful.html#TauCeti.FiniteEtaleScheme.fullyFaithfulPullback%CE%B9OfTwoLeDepthStalk).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.fullyFaithfulPullbackιOfTwoLeDepthStalk`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/FullyFaithful.html#TauCeti.FiniteEtaleScheme.fullyFaithfulPullback%CE%B9OfTwoLeDepthStalk)
- [Source of `TauCeti.FiniteEtaleScheme.fullyFaithfulPullbackιOfTwoLeDepthStalk` in TauCeti/AlgebraicGeometry/FiniteEtale/FullyFaithful.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/FullyFaithful.lean#L153)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
