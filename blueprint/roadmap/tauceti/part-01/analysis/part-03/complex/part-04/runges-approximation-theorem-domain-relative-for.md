---
declaration: theorem
origin: cited
lean: TauCeti.isRungeCompactPair_iff_approximation
statement: formalized
proof: formalized
---

# Runge's approximation theorem (domain-relative form)

for compact `K ⊆ Ω` with `Ω ⊆ ℂ`
open, `IsRungeCompactPair Ω K` holds if and only if every function holomorphic on an open
neighbourhood `U ⊇ K` can be uniformly approximated on `K` by functions holomorphic on `Ω`.

```lean
TauCeti.isRungeCompactPair_iff_approximation {Ω K : Set ℂ} (hΩ : IsOpen Ω) (hK : IsCompact K)
  (hKΩ : K ⊆ Ω) :
  TauCeti.IsRungeCompactPair Ω K ↔
    ∀ (U : Set ℂ),
      IsOpen U →
        K ⊆ U →
          ∀ (f : ℂ → ℂ),
            DifferentiableOn ℂ f U → ∀ ε > 0, ∃ g, DifferentiableOn ℂ g Ω ∧ ∀ z ∈ K, ‖f z - g z‖ < ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isRungeCompactPair_iff_approximation`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Runge/Approximation.html#TauCeti.isRungeCompactPair_iff_approximation).

## Sources

- [Tau Ceti documentation: `TauCeti.isRungeCompactPair_iff_approximation`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Runge/Approximation.html#TauCeti.isRungeCompactPair_iff_approximation)
- [Source of `TauCeti.isRungeCompactPair_iff_approximation` in TauCeti/Analysis/Complex/Runge/Approximation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Runge/Approximation.lean#L106)
