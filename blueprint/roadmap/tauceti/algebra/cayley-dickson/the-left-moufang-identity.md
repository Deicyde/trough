---
declaration: theorem
origin: cited
lean: TauCeti.CayleyDickson.moufang_left, TauCeti.Octonion.moufang_left
statement: formalized
proof: formalized
---

# The left Moufang identity

`(z * x * z) * y = z * (x * (z * y))`.

```lean
TauCeti.CayleyDickson.moufang_left.{u_1} {R : Type u_1} [CommRing R]
  (x y z : TauCeti.CayleyDickson (Quaternion R)) : z * x * z * y = z * (x * (z * y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CayleyDickson.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_left).

## Other forms

**The left Moufang identity.** Formalized in Tau Ceti as [`TauCeti.Octonion.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_left).

```lean
TauCeti.Octonion.moufang_left.{u_1} {R : Type u_1} [CommRing R] (x y z : TauCeti.Octonion R) :
  z * x * z * y = z * (x * (z * y))
```

## Sources

- [Tau Ceti documentation: `TauCeti.CayleyDickson.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_left)
- [Source of `TauCeti.CayleyDickson.moufang_left` in TauCeti/Algebra/CayleyDickson/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CayleyDickson/Artin.lean#L142)
