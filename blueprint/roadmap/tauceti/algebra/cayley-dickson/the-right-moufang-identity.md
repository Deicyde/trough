---
declaration: theorem
origin: cited
lean: TauCeti.CayleyDickson.moufang_right, TauCeti.Octonion.moufang_right
statement: formalized
proof: formalized
---

# The right Moufang identity

`x * (z * y * z) = ((x * z) * y) * z`.

```lean
TauCeti.CayleyDickson.moufang_right.{u_1} {R : Type u_1} [CommRing R]
  (x y z : TauCeti.CayleyDickson (Quaternion R)) : x * (z * y * z) = x * z * y * z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The left Moufang identity](the-left-moufang-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CayleyDickson.moufang_right`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_right).

## Other forms

**The right Moufang identity.** Formalized in Tau Ceti as [`TauCeti.Octonion.moufang_right`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_right).

```lean
TauCeti.Octonion.moufang_right.{u_1} {R : Type u_1} [CommRing R] (x y z : TauCeti.Octonion R) :
  x * (z * y * z) = x * z * y * z
```

## Sources

- [Tau Ceti documentation: `TauCeti.CayleyDickson.moufang_right`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_right)
- [Source of `TauCeti.CayleyDickson.moufang_right` in TauCeti/Algebra/CayleyDickson/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CayleyDickson/Artin.lean#L154)
