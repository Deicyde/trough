---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant
statement: formalized
proof: formalized
---

# The crossing constant approaches `1 / #Aut_K(L)`

For every `δ < 1 / #Aut_K(L)` there is
a level `r` such that the crossing constant of every cyclic group whose order is divisible by
`f ^ r` exceeds `δ`.

The level depends only on `δ`, `f` and the order of `Aut_K(L)`, not on the cyclic group, so a
consumer that can choose an auxiliary group of any level pushes the crossing bound arbitrarily
close to `1 / #Aut_K(L)`.

```lean
TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant.{u_1, u_2, u_4} (K : Type u_1)
  (L : Type u_2) [CommSemiring K] [Semiring L] [Algebra K L] (f : ℕ) {δ : ℝ}
  (hδ : δ < 1 / ↑(Nat.card (L ≃ₐ[K] L))) :
  ∃ r,
    ∀ (H : Type u_4) [inst : Group H] [inst_1 : Fintype H] [IsCyclic H],
      f ^ r ∣ Nat.card H → δ < TauCeti.NumberField.Chebotarev.crossingConstant K L f
```

## Depends on

- [The crossing constant](the-crossing-constant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.html#TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.html#TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant)
- [Source of `TauCeti.NumberField.Chebotarev.exists_forall_lt_crossingConstant` in TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.lean#L100)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
