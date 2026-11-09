---
declaration: theorem
origin: cited
lean: TauCeti.δ_cyclicRepShortComplex_groupCohomologyπOdd_one
statement: formalized
proof: formalized
---

# The integral connecting class

For the short exact sequence `0 → Λ → E → T → 0` of
cyclic representations, let `t` be killed by the norm `∑ j < m, AT^j`, lift it to `s : E`, and
write the norm `∑ j < m, AE^j s` as the image of a fixed point `v` of `AΛ`. Then the connecting
homomorphism sends the degree-`1` class of `t` to the degree-`2` class of `v`.

```lean
TauCeti.δ_cyclicRepShortComplex_groupCohomologyπOdd_one {Λ E T : Type} [AddCommGroup Λ]
  [AddCommGroup E] [AddCommGroup T] {m : ℕ} [NeZero m] {AΛ : Λ ≃+ Λ} {AE : E ≃+ E} {AT : T ≃+ T}
  {i : Λ →+ E} {p : E →+ T} {hΛ : (⇑AΛ)^[m] = id} {hE : (⇑AE)^[m] = id} {hT : (⇑AT)^[m] = id}
  {hi : ∀ (x : Λ), i (AΛ x) = AE (i x)} {hp : ∀ (x : E), p (AE x) = AT (p x)}
  {hpi : ∀ (x : Λ), p (i x) = 0} (hS : (i.cyclicRepShortComplex p hΛ hE hT hi hp hpi).ShortExact)
  (t : ↥(Rep.Hom.hom (AT.cyclicRep hT).norm.asHom).ker) (s : E) (hs : p s = ↑t)
  (v :
    ↥(Rep.Hom.hom
          ((AΛ.cyclicRep hΛ).applyAsHom (Multiplicative.ofAdd 1) -
            CategoryTheory.CategoryStruct.id (AΛ.cyclicRep hΛ))).ker)
  (hv : i ↑v = ∑ j ∈ Finset.range m, (⇑AE)^[j] s) :
  (CategoryTheory.ConcreteCategory.hom (groupCohomology.δ hS 1 2 ⋯))
      ((CategoryTheory.ConcreteCategory.hom
          (Rep.FiniteCyclicGroup.groupCohomologyπOdd (AT.cyclicRep hT) (Multiplicative.ofAdd 1) ⋯ 1
            ⋯))
        t) =
    (CategoryTheory.ConcreteCategory.hom
        (Rep.FiniteCyclicGroup.groupCohomologyπEven (AΛ.cyclicRep hΛ) (Multiplicative.ofAdd 1) ⋯ 2
          ⋯))
      v
```

## Depends on

- [AddEquiv.cyclicRep](addequiv-cyclicrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.δ_cyclicRepShortComplex_groupCohomologyπOdd_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.%CE%B4_cyclicRepShortComplex_groupCohomology%CF%80Odd_one).

## Sources

- [Tau Ceti documentation: `TauCeti.δ_cyclicRepShortComplex_groupCohomologyπOdd_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.%CE%B4_cyclicRepShortComplex_groupCohomology%CF%80Odd_one)
- [Source of `TauCeti.δ_cyclicRepShortComplex_groupCohomologyπOdd_one` in TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean#L356)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
