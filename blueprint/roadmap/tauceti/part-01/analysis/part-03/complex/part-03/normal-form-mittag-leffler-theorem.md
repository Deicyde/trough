---
declaration: theorem
origin: cited
lean: TauCeti.exists_meromorphicNFOn_prescribed_principal_parts
statement: formalized
proof: formalized
---

# Normal-form Mittag-Leffler theorem

Under the hypotheses of
`exists_meromorphic_prescribed_principal_parts`, the realizing function `f : ℂ → F` can be chosen in
meromorphic normal form on `Ω` (`MeromorphicNFOn f Ω`), taking its analytic value at removable
points and `0` at poles.

```lean
TauCeti.exists_meromorphicNFOn_prescribed_principal_parts.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {Ω : Set ℂ} (hΩ : IsOpen Ω) {E : Set ℂ}
  (hEΩ : E ⊆ Ω) (hE : Eᶜ ∈ Filter.codiscreteWithin Ω) (P : ↑E → ℂ → F)
  (hP : ∀ (a : ↑E), MeromorphicAt (P a) ↑a) :
  ∃ f,
    MeromorphicNFOn f Ω ∧
      (∀ (a : ↑E), ∃ g, AnalyticAt ℂ g ↑a ∧ ∀ᶠ (z : ℂ) in nhdsWithin ↑a {↑a}ᶜ, f z - P a z = g z) ∧
        DifferentiableOn ℂ f (Ω \ E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mittag-Leffler theorem](the-mittag-leffler-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_meromorphicNFOn_prescribed_principal_parts`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_meromorphicNFOn_prescribed_principal_parts).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_meromorphicNFOn_prescribed_principal_parts`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_meromorphicNFOn_prescribed_principal_parts)
- [Source of `TauCeti.exists_meromorphicNFOn_prescribed_principal_parts` in TauCeti/Analysis/Complex/MittagLeffler.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/MittagLeffler.lean#L549)
