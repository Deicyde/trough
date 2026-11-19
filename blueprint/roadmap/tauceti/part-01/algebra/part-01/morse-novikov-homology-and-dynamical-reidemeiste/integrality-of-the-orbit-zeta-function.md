---
declaration: theorem
origin: cited
lean: TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct
statement: formalized
proof: formalized
---

# Integrality of the orbit zeta function

Under the hypotheses of the product formula, the
orbit zeta function is the image of the Euler product `∏ᵢ (1 - σ i e^(γ i)) ^ (-(ε i 1 * σ i))`
with integer coefficients.

```lean
TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct.{u_1, u_2, u_3} {ι : Type u_1}
  {H : Type u_2} [AddCommMonoid H] {N : H →+ ℝ} {γ : ι → H} {K : Type u_3} [CommRing K]
  [Algebra ℚ K] (hpos : ∀ (i : ι), 0 < N (γ i))
  (hfin : Filter.Tendsto (fun i => N (γ i)) Filter.cofinite Filter.atTop) (ε : ι → ℕ → ℤ)
  (σ : ι → ℤˣ) (hε : ∀ (i : ι) (k : ℕ), ε i (k + 1) = ε i 1 * ↑(σ i) ^ k) :
  TauCeti.NovikovSeries.orbitZeta K N γ ε =
    (TauCeti.NovikovSeries.mapRingHom (Int.castRingHom K) (AddMonoidHom.id H) ⋯)
      (TauCeti.NovikovSeries.eulerProduct γ hpos (fun i => ↑(σ i)) fun i => -(ε i 1 * ↑(σ i)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/OrbitZeta/Basic.html#TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/OrbitZeta/Basic.html#TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct)
- [Source of `TauCeti.NovikovSeries.orbitZeta_eq_mapRingHom_eulerProduct` in TauCeti/RingTheory/NovikovSeries/OrbitZeta/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/NovikovSeries/OrbitZeta/Basic.lean#L309)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseNovikov/STATUS.md)
