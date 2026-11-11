---
declaration: theorem
origin: cited
lean: TauCeti.iterate_frobeniusSchurRotate_eq_id
statement: formalized
proof: formalized
---

# Ng–Schauenburg

the `(n + 1)`-st iterate of `E_V^{(n+1)}` is the identity.

```lean
TauCeti.iterate_frobeniusSchurRotate_eq_id.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C]
  (V : C) (n : ℕ) : (TauCeti.frobeniusSchurRotate V n)^[n + 1] = id
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.iterate_frobeniusSchurRotate_eq_id`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.html#TauCeti.iterate_frobeniusSchurRotate_eq_id).

## Sources

- [Tau Ceti documentation: `TauCeti.iterate_frobeniusSchurRotate_eq_id`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.html#TauCeti.iterate_frobeniusSchurRotate_eq_id)
- [Source of `TauCeti.iterate_frobeniusSchurRotate_eq_id` in TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.lean#L230)
