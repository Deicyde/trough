---
declaration: theorem
origin: cited
lean: TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt
statement: formalized
proof: formalized
---

# Master prescribed-isolated-singularities theorem (punctured-germ form)

Given an open set
`Ω ⊆ ℂ`, a subset `E ⊆ Ω` with `Eᶜ ∈ Filter.codiscreteWithin Ω`, and local germs `P : E → ℂ → F`
each complex-differentiable on `𝓝[≠] a.val`, there exists `f : ℂ → F` realizing
`HasPrescribedSingularities f Ω E P`.

```lean
TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {Ω : Set ℂ} (hΩ : IsOpen Ω) {E : Set ℂ}
  (hEΩ : E ⊆ Ω) (hE : Eᶜ ∈ Filter.codiscreteWithin Ω) (P : ↑E → ℂ → F)
  (hP : ∀ (a : ↑E), ∀ᶠ (z : ℂ) in nhdsWithin ↑a {↑a}ᶜ, DifferentiableAt ℂ (P a) z) :
  ∃ f, TauCeti.HasPrescribedSingularities f Ω E P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Laurent's theorem on an open concentric annulus](laurents-theorem-on-an-open-concentric-annulus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt)
- [Source of `TauCeti.exists_hasPrescribedSingularities_of_eventually_differentiableAt` in TauCeti/Analysis/Complex/MittagLeffler.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/MittagLeffler.lean#L462)
