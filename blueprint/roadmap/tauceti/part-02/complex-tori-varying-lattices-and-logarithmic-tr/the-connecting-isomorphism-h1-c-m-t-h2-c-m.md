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

- [AddEquiv.cyclicRep](addequiv-cyclicrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicConnectingEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.cyclicConnectingEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicConnectingEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.cyclicConnectingEquiv)
- [Source of `TauCeti.cyclicConnectingEquiv` in TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean#L391)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
