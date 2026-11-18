---
declaration: theorem
origin: cited
lean: TauCeti.exists_meromorphic_principalPart_eq
statement: formalized
proof: formalized
---

# Polynomial principal-part Mittag-Leffler theorem

Given an open set `Ω ⊆ ℂ`, a relatively
closed discrete subset `E ⊆ Ω`, and at each `a : E` a polynomial `P a : ℂ[X]` without constant term,
there exists `f : ℂ → ℂ` meromorphic on `Ω` and complex-differentiable on `Ω \ E` whose algebraic
principal part `meromorphicGerms.principalPart` at every `a : E` equals `P a`.

```lean
TauCeti.exists_meromorphic_principalPart_eq {Ω : Set ℂ} (hΩ : IsOpen Ω) {E : Set ℂ} (hEΩ : E ⊆ Ω)
  (hE : Eᶜ ∈ Filter.codiscreteWithin Ω) (P : ↑E → Polynomial ℂ)
  (hP : ∀ (a : ↑E), (P a).coeff 0 = 0) :
  ∃ f,
    ∃ (hf : MeromorphicOn f Ω),
      DifferentiableOn ℂ f (Ω \ E) ∧
        ∀ (a : ↑E), TauCeti.meromorphicGerms.principalPart (TauCeti.meromorphicGerms.mk f ⋯) = P a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mittag-Leffler theorem](the-mittag-leffler-theorem.md)
- [Taylor's formula to second order](../../calculus/part-02/taylors-formula-to-second-order.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_meromorphic_principalPart_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_meromorphic_principalPart_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_meromorphic_principalPart_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/MittagLeffler.html#TauCeti.exists_meromorphic_principalPart_eq)
- [Source of `TauCeti.exists_meromorphic_principalPart_eq` in TauCeti/Analysis/Complex/MittagLeffler.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/MittagLeffler.lean#L617)
