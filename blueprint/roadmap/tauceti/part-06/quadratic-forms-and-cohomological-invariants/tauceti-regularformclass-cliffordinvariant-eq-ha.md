---
declaration: theorem
origin: cited
lean: TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul
statement: formalized
proof: formalized
---

# TauCeti.RegularFormClass.cliffordInvariant\_eq\_hasseInvariant\_mul

**Lam's comparison of the Clifford and Hasse invariants** (Lam V.3.20). For a class of
rank `n` with discriminant `d`, `c(q) = s(q) · [(-1, d)]^C(n-1,2) · [(-1,-1)]^C(n+1,4)`, where
`C(n-1,2) = (n-1)(n-2)/2` and `C(n+1,4) = (n+1)n(n-1)(n-2)/24`.

```lean
TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul.{u} {K : Type u} [Field K]
  [Invertible 2] (x : TauCeti.RegularFormClass K) :
  x.cliffordInvariant =
    x.hasseInvariant *
        TauCeti.BrauerGroup.quaternionClassOnSquareClasses (TauCeti.squareClass (-1)) x.discr ^
          (x.rank - 1).choose 2 *
      TauCeti.BrauerGroup.quaternionClass (-1) (-1) ^ (x.rank + 1).choose 4
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.QuaternionAlgebra.nonempty\_algEquiv\_matrix\_tfae](tauceti-quaternionalgebra-nonempty-algequiv-matr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/RegularFormClass/Clifford.html#TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/RegularFormClass/Clifford.html#TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul)
- [Source of `TauCeti.RegularFormClass.cliffordInvariant_eq_hasseInvariant_mul` in TauCeti/LinearAlgebra/QuadraticForm/RegularFormClass/Clifford.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/QuadraticForm/RegularFormClass/Clifford.lean#L567)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
