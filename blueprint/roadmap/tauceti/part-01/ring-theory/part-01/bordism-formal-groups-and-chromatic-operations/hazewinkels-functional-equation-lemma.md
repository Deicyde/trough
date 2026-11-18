---
declaration: theorem
origin: cited
lean: TauCeti.coeff_inv_smul_𝔾ₐ_toPowerSeries_mem
statement: formalized
proof: formalized
---

# Hazewinkel's functional equation lemma

Let `f = b₁ X + ⋯` be a formal coordinate over `K`
whose linear coefficient `b₁` is a unit of `A`, and suppose that `f` satisfies the functional
equation. Then the formal group law `f⁻¹(f(X) + f(Y))` with logarithm `f`, the transport
`f⁻¹ • 𝔾ₐ` of the additive formal group law, has all its coefficients in `A`.

```lean
TauCeti.coeff_inv_smul_𝔾ₐ_toPowerSeries_mem.{u_1} {K : Type u_1} [CommRing K] {p : ℕ}
  [hp : Fact (Nat.Prime p)] {σ : K →+* K} {s : ℕ → K} {A : Subring K} (hσ : Set.MapsTo ⇑σ ↑A ↑A)
  (hσp : ∀ a ∈ A, ∃ b ∈ A, σ a - a ^ p = ↑p * b) (hs : ∀ (i : ℕ), ↑p * s i ∈ A)
  (f : TauCeti.FormalCoordinate K) (hf₁ : ∃ u ∈ A, u * (PowerSeries.coeff 1) f.toPowerSeries = 1)
  (hf : TauCeti.SatisfiesFunctionalEquation p σ s A f.toPowerSeries) (d : Fin 2 →₀ ℕ) :
  (MvPowerSeries.coeff d) (f⁻¹ • FormalGroup.𝔾ₐ).toPowerSeries ∈ A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.coeff_inv_smul_𝔾ₐ_toPowerSeries_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/FunctionalEquation.html#TauCeti.coeff_inv_smul_%F0%9D%94%BE%E2%82%90_toPowerSeries_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.coeff_inv_smul_𝔾ₐ_toPowerSeries_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/FunctionalEquation.html#TauCeti.coeff_inv_smul_%F0%9D%94%BE%E2%82%90_toPowerSeries_mem)
- [Source of `TauCeti.coeff_inv_smul_𝔾ₐ_toPowerSeries_mem` in TauCeti/RingTheory/FormalGroup/FunctionalEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/FunctionalEquation.lean#L448)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
