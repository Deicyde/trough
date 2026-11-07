---
declaration: theorem
origin: cited
lean: TauCeti.map_δ_cyclicRepShortComplex
statement: formalized
proof: formalized
---

# Naturality under homomorphisms of cyclic groups

Suppose `χ : C_l → C_m` sends the
selected generator to its `d`-th power. Maps of exact sequences intertwining the `d`-th
iterates of the source automorphisms with the target automorphisms commute with the
connecting homomorphisms. This includes restriction, inflation, and coefficient maps.

```lean
TauCeti.map_δ_cyclicRepShortComplex {Λ E T : Type} [AddCommGroup Λ] [AddCommGroup E]
  [AddCommGroup T] {m : ℕ} [NeZero m] {AΛ : Λ ≃+ Λ} {AE : E ≃+ E} {AT : T ≃+ T} {i : Λ →+ E}
  {p : E →+ T} {hΛ : (⇑AΛ)^[m] = id} {hE : (⇑AE)^[m] = id} {hT : (⇑AT)^[m] = id}
  {hi : ∀ (x : Λ), i (AΛ x) = AE (i x)} {hp : ∀ (x : E), p (AE x) = AT (p x)}
  {hpi : ∀ (x : Λ), p (i x) = 0} (hS : (i.cyclicRepShortComplex p hΛ hE hT hi hp hpi).ShortExact)
  {l : ℕ} [NeZero l] {Λ' E' T' : Type} [AddCommGroup Λ'] [AddCommGroup E'] [AddCommGroup T']
  {AΛ' : Λ' ≃+ Λ'} {AE' : E' ≃+ E'} {AT' : T' ≃+ T'} {i' : Λ' →+ E'} {p' : E' →+ T'}
  {hΛ' : (⇑AΛ')^[l] = id} {hE' : (⇑AE')^[l] = id} {hT' : (⇑AT')^[l] = id}
  {hi' : ∀ (x : Λ'), i' (AΛ' x) = AE' (i' x)} {hp' : ∀ (x : E'), p' (AE' x) = AT' (p' x)}
  {hpi' : ∀ (x : Λ'), p' (i' x) = 0}
  (hS' : (i'.cyclicRepShortComplex p' hΛ' hE' hT' hi' hp' hpi').ShortExact)
  (χ : Multiplicative (ZMod l) →* Multiplicative (ZMod m)) (d : ℕ)
  (hχ : χ (Multiplicative.ofAdd 1) = Multiplicative.ofAdd 1 ^ d) (fΛ : Λ →+ Λ') (fE : E →+ E')
  (fT : T →+ T') (hfΛ : ∀ (x : Λ), fΛ ((⇑AΛ)^[d] x) = AΛ' (fΛ x))
  (hfE : ∀ (x : E), fE ((⇑AE)^[d] x) = AE' (fE x)) (hfT : ∀ (x : T), fT ((⇑AT)^[d] x) = AT' (fT x))
  (hfi : ∀ (x : Λ), fE (i x) = i' (fΛ x)) (hfp : ∀ (x : E), fT (p x) = p' (fE x)) (n q : ℕ)
  (hnq : n + 1 = q) (x : ↑(groupCohomology (AT.cyclicRep hT) n)) :
  (CategoryTheory.ConcreteCategory.hom
        (groupCohomology.map χ (fΛ.cyclicRepResHom hΛ hΛ' χ d hχ hfΛ) q))
      ((CategoryTheory.ConcreteCategory.hom (groupCohomology.δ hS n q hnq)) x) =
    (CategoryTheory.ConcreteCategory.hom (groupCohomology.δ hS' n q hnq))
      ((CategoryTheory.ConcreteCategory.hom
          (groupCohomology.map χ (fT.cyclicRepResHom hT hT' χ d hχ hfT) n))
        x)
```

## Depends on

- [AddEquiv.cyclicRep](addequiv-cyclicrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.map_δ_cyclicRepShortComplex`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.map_%CE%B4_cyclicRepShortComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.map_δ_cyclicRepShortComplex`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.map_%CE%B4_cyclicRepShortComplex)
- [Source of `TauCeti.map_δ_cyclicRepShortComplex` in TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean#L407)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
