---
declaration: theorem
origin: cited
lean: TauCeti.vitali
statement: formalized
proof: formalized
---

# Vitali's convergence theorem

Let `Ω` be an open preconnected subset of `ℂ`. A locally
bounded sequence of holomorphic maps from `Ω` into a proper complex normed space `E` (for instance
`ℂ`) which converges pointwise on a subset `A ⊆ Ω` having an accumulation point in `Ω` converges
locally uniformly on `Ω` to a holomorphic map.

The pointwise limit on `A` need not be supplied: its existence is enough to determine the
holomorphic limit uniquely.

```lean
TauCeti.vitali.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] {Ω A : Set ℂ}
  [ProperSpace E] {F : ℕ → ℂ → E} (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω)
  (hF : ∀ (n : ℕ), DifferentiableOn ℂ (F n) Ω) (hb : TauCeti.IsLocallyBoundedOn F Ω) (hAΩ : A ⊆ Ω)
  {z₀ : ℂ} (hz₀ : z₀ ∈ Ω) (hacc : AccPt z₀ (Filter.principal A))
  (hpoint : ∀ z ∈ A, ∃ w, Filter.Tendsto (fun n => F n z) Filter.atTop (nhds w)) :
  ∃ g, DifferentiableOn ℂ g Ω ∧ TendstoLocallyUniformlyOn F g Filter.atTop Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Montel's selection theorem](../../../part-02/complex/part-02/montels-selection-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.vitali`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Vitali.html#TauCeti.vitali).

## Sources

- [Tau Ceti documentation: `TauCeti.vitali`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Vitali.html#TauCeti.vitali)
- [Source of `TauCeti.vitali` in TauCeti/Analysis/Complex/Conformal/Vitali.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Vitali.lean#L88)
