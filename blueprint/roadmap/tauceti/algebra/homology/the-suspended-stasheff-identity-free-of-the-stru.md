---
declaration: theorem
origin: cited
lean: TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff
statement: formalized
proof: formalized
---

# The suspended Stasheff identity free of the structural coefficient holds exactly when the unsuspended one does

```lean
TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff.{uR, uA} {R : Type uR} {A : Type uA} [CommRing R]
  [AddCommMonoid A] [_root_.Module R A] (m : (k : ℕ) → (Fin k → A) →ₘₗ[R] A) (d : ℕ → ℤ) (x : ℕ → A)
  (n : ℕ) :
  TauCeti.AInfinity.suspendedStasheffSum m d x n = 0 ↔ TauCeti.AInfinity.stasheffSum m d x n = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Stasheff.html#TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Stasheff.html#TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff)
- [Source of `TauCeti.AInfinity.suspendedStasheffSum_eq_zero_iff` in TauCeti/Algebra/Homology/AInfinity/Stasheff.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/AInfinity/Stasheff.lean#L464)
