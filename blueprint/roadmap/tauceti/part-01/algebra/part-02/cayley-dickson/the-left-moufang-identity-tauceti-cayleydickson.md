---
declaration: theorem
origin: cited
lean: TauCeti.CayleyDickson.moufang_left
statement: formalized
proof: formalized
---

# The left Moufang identity (`TauCeti.CayleyDickson.moufang_left`)

`(z * x * z) * y = z * (x * (z * y))`.

```lean
TauCeti.CayleyDickson.moufang_left.{u_1} {R : Type u_1} [CommRing R]
  (x y z : TauCeti.CayleyDickson (Quaternion R)) : z * x * z * y = z * (x * (z * y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CayleyDickson.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_left).

## Sources

- [Tau Ceti documentation: `TauCeti.CayleyDickson.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_left)
- [Source of `TauCeti.CayleyDickson.moufang_left` in TauCeti/Algebra/CayleyDickson/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/CayleyDickson/Artin.lean#L142)
