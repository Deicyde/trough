---
declaration: theorem
origin: cited
lean: TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential
statement: formalized
proof: formalized
---

# The theorem of Rockafellar and Rüschendorf

Every `c`-cyclically monotone set is
contained in the `c`-superdifferential of a `c`-concave potential: there is a `φ` with
`φ x + φᶜ y = c (x, y)` at every point `(x, y)` of the set, where `φᶜ` is the infimal
`c`-transform of `φ`.

```lean
TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential.{u, v} {X : Type u}
  {Y : Type v} {c : X × Y → ℝ} {S : Set (X × Y)} (hS : TauCeti.IsCyclicallyMonotone c S) :
  ∃ φ, TauCeti.IsCConcave c φ ∧ S ⊆ TauCeti.cSuperdifferential c φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/CTransform/CyclicalMonotonicity.html#TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/CTransform/CyclicalMonotonicity.html#TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential)
- [Source of `TauCeti.IsCyclicallyMonotone.exists_isCConcave_subset_cSuperdifferential` in TauCeti/MeasureTheory/OptimalTransport/CTransform/CyclicalMonotonicity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/OptimalTransport/CTransform/CyclicalMonotonicity.lean#L289)
