---
declaration: def
origin: cited
lean: TauCeti.cyclicConnectingEquiv
statement: formalized
---

# The connecting isomorphism `H¹(C_m, T) ≃ H²(C_m, Λ)`

When multiplication by `m` is
bijective on `E`, for instance when `E` is a real vector space, the cohomology of `E` vanishes in
positive degrees and the connecting homomorphism of `0 → Λ → E → T → 0` is an isomorphism.

```lean
TauCeti.cyclicConnectingEquiv {Λ E T : Type} [AddCommGroup Λ] [AddCommGroup E] [AddCommGroup T]
  {m : ℕ} [NeZero m] {AΛ : Λ ≃+ Λ} {AE : E ≃+ E} {AT : T ≃+ T} {i : Λ →+ E} {p : E →+ T}
  {hΛ : (⇑AΛ)^[m] = id} {hE : (⇑AE)^[m] = id} {hT : (⇑AT)^[m] = id}
  {hi : ∀ (x : Λ), i (AΛ x) = AE (i x)} {hp : ∀ (x : E), p (AE x) = AT (p x)}
  {hpi : ∀ (x : Λ), p (i x) = 0} (hS : (i.cyclicRepShortComplex p hΛ hE hT hi hp hpi).ShortExact)
  (hm : Function.Bijective fun x => m • x) :
  ↑(groupCohomology (AT.cyclicRep hT) 1) ≃ₗ[ℤ] ↑(groupCohomology (AΛ.cyclicRep hΛ) 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicConnectingEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.cyclicConnectingEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicConnectingEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.cyclicConnectingEquiv)
- [Source of `TauCeti.cyclicConnectingEquiv` in TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean#L391)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexTori/STATUS.md)
