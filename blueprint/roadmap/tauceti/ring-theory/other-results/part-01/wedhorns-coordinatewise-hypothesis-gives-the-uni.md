---
declaration: theorem
origin: cited
lean: TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded
statement: formalized
proof: formalized
---

# Wedhorn's coordinatewise hypothesis gives the uniform bound

Each weighted monomial set is
a finite pointwise product of powers of the weighted variables, so it lies in the product of the
bounded sets containing those powers — and a finite pointwise product of bounded sets is bounded.

This is what makes `TauCeti.Huber.IsWeightBounded` the right hypothesis for the summability
theorem rather than a stronger one invented for it: the two are reached from the same place.

```lean
TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded.{u_1, u_2} {k : ℕ} {A : Type u_1}
  {B : Type u_2} [CommSemiring A] [CommSemiring B] [TopologicalSpace B] {φ : A →+* B}
  {T : Fin k → Set A} {b : Fin k → B} (h : TauCeti.Huber.IsWeightedVarPowerBounded φ T b) :
  TauCeti.Huber.IsWeightBounded φ T b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/WeightedEval/Basic.html#TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/WeightedEval/Basic.html#TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded)
- [Source of `TauCeti.Huber.isWeightBounded_of_isWeightedVarPowerBounded` in TauCeti/RingTheory/Huber/WeightedEval/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/WeightedEval/Basic.lean#L185)
