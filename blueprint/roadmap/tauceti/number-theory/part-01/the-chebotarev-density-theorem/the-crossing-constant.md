---
declaration: def
origin: cited
lean: TauCeti.NumberField.Chebotarev.crossingConstant
statement: formalized
---

# The crossing constant

The number of tagged elements of the auxiliary cyclic group `H` —
those whose order is divisible by `f` — divided by `#Aut_K(L) * #H`.

That is the tag proportion within `H`, divided in addition by the order of `Aut_K(L)`, which
enters only through its order: the denominator that turns a count of tags into the density
contributed by one auxiliary prime.

```lean
TauCeti.NumberField.Chebotarev.crossingConstant.{u_1, u_2, u_3} (K : Type u_1) (L : Type u_2)
  [CommSemiring K] [Semiring L] [Algebra K L] {H : Type u_3} [Group H] [Fintype H] (f : ℕ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Chebotarev.crossingConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.html#TauCeti.NumberField.Chebotarev.crossingConstant).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Chebotarev.crossingConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.html#TauCeti.NumberField.Chebotarev.crossingConstant)
- [Source of `TauCeti.NumberField.Chebotarev.crossingConstant` in TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/Crossing/CrossingConstant.lean#L60)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
