---
declaration: theorem
origin: cited
lean: TauCeti.exists_meromorphic_prescribed_principal_parts
statement: formalized
proof: formalized
---

# The Mittag-Leffler theorem

Let `Ω ⊆ ℂ` be open and let `E ⊆ Ω` satisfy
`Eᶜ ∈ Filter.codiscreteWithin Ω`. Given meromorphic germs `P : E → ℂ → F` with
`MeromorphicAt (P a) a.val` for every `a : E`, there exists a function `f : ℂ → F` meromorphic on
`Ω` and complex-differentiable on `Ω \ E` such that at every `a : E`, `f - P a` agrees on
`𝓝[≠] a.val` with a function complex-analytic at `a.val`.

```lean
TauCeti.exists_meromorphic_prescribed_principal_parts.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] {Ω : Set ℂ} (hΩ : IsOpen Ω) {E : Set ℂ} (hEΩ : E ⊆ Ω)
  (hE : Eᶜ ∈ Filter.codiscreteWithin Ω) (P : ↑E → ℂ → F) (hP : ∀ (a : ↑E), MeromorphicAt (P a) ↑a) :
  ∃ f,
    MeromorphicOn f Ω ∧
      (∀ (a : ↑E), ∃ g, AnalyticAt ℂ g ↑a ∧ ∀ᶠ (z : ℂ) in nhdsWithin ↑a {↑a}ᶜ, f z - P a z = g z) ∧
        DifferentiableOn ℂ f (Ω \ E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Master prescribed-isolated-singularities theorem (punctured-germ form)](master-prescribed-isolated-singularities-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_meromorphic_prescribed_principal_parts`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_meromorphic_prescribed_principal_parts).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_meromorphic_prescribed_principal_parts`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_meromorphic_prescribed_principal_parts)
- [Source of `TauCeti.exists_meromorphic_prescribed_principal_parts` in TauCeti/Analysis/Complex/MittagLeffler.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/MittagLeffler.lean#L531)
