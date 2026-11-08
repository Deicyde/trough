---
declaration: theorem
origin: cited
lean: TauCeti.BrauerGroup.orderOf_mk_eq_two
statement: formalized
proof: formalized
---

# A self-opposite Brauer class other than the identity has order exactly `2`

This is the
sharp form of `TauCeti.BrauerGroup.orderOf_mk_dvd_two`.

```lean
TauCeti.BrauerGroup.orderOf_mk_eq_two.{u} {K : Type u} [Field K] {A : CSA K}
  (h : IsBrauerEquivalent A (TauCeti.CSA.op A)) (h1 : TauCeti.BrauerGroup.mk A ≠ 1) :
  orderOf (TauCeti.BrauerGroup.mk A) = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BrauerGroup.orderOf_mk_eq_two`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Group.html#TauCeti.BrauerGroup.orderOf_mk_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.BrauerGroup.orderOf_mk_eq_two`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Group.html#TauCeti.BrauerGroup.orderOf_mk_eq_two)
- [Source of `TauCeti.BrauerGroup.orderOf_mk_eq_two` in TauCeti/Algebra/BrauerGroup/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/BrauerGroup/Group.lean#L269)
