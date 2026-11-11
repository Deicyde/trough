---
declaration: theorem
origin: cited
lean: TauCeti.vitali_of_tendsto
statement: formalized
proof: formalized
---

# Vitali's theorem with prescribed pointwise values

Under the hypotheses of `vitali`, if
the sequence converges pointwise on `A` to a specified function `g`, its locally uniform
holomorphic limit agrees with `g` throughout `A`.

No regularity of `g` away from `A` is assumed or concluded; when `A` is all of `Ω` the limit is
`g` itself, which is
`TauCeti.tendstoLocallyUniformlyOn_of_isLocallyBoundedOn_of_forall_tendsto`.

```lean
TauCeti.vitali_of_tendsto.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  {Ω A : Set ℂ} [ProperSpace E] {F : ℕ → ℂ → E} (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω)
  (hF : ∀ (n : ℕ), DifferentiableOn ℂ (F n) Ω) (hb : TauCeti.IsLocallyBoundedOn F Ω) (hAΩ : A ⊆ Ω)
  {z₀ : ℂ} (hz₀ : z₀ ∈ Ω) (hacc : AccPt z₀ (Filter.principal A)) {g : ℂ → E}
  (hpoint : ∀ z ∈ A, Filter.Tendsto (fun n => F n z) Filter.atTop (nhds (g z))) :
  ∃ q, DifferentiableOn ℂ q Ω ∧ Set.EqOn q g A ∧ TendstoLocallyUniformlyOn F q Filter.atTop Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vitali's convergence theorem](vitalis-convergence-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.vitali_of_tendsto`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Vitali.html#TauCeti.vitali_of_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.vitali_of_tendsto`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Vitali.html#TauCeti.vitali_of_tendsto)
- [Source of `TauCeti.vitali_of_tendsto` in TauCeti/Analysis/Complex/Conformal/Vitali.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Vitali.lean#L122)
