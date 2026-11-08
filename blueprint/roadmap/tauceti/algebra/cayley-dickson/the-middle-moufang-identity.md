---
declaration: theorem
origin: cited
lean: TauCeti.CayleyDickson.moufang_middle, TauCeti.Octonion.moufang_middle
statement: formalized
proof: formalized
---

# The middle Moufang identity

`(z * x) * (y * z) = (z * (x * y)) * z`.

```lean
TauCeti.CayleyDickson.moufang_middle.{u_1} {R : Type u_1} [CommRing R]
  (x y z : TauCeti.CayleyDickson (Quaternion R)) : z * x * (y * z) = z * (x * y) * z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CayleyDickson.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_middle).

## Other forms

**The middle Moufang identity.** Formalized in Tau Ceti as [`TauCeti.Octonion.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_middle).

```lean
TauCeti.Octonion.moufang_middle.{u_1} {R : Type u_1} [CommRing R] (x y z : TauCeti.Octonion R) :
  z * x * (y * z) = z * (x * y) * z
```

## Sources

- [Tau Ceti documentation: `TauCeti.CayleyDickson.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_middle)
- [Source of `TauCeti.CayleyDickson.moufang_middle` in TauCeti/Algebra/CayleyDickson/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CayleyDickson/Artin.lean#L163)
