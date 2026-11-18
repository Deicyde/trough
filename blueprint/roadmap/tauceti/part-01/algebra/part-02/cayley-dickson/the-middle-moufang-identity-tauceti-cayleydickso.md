---
declaration: theorem
origin: cited
lean: TauCeti.CayleyDickson.moufang_middle
statement: formalized
proof: formalized
---

# The middle Moufang identity (`TauCeti.CayleyDickson.moufang_middle`)

`(z * x) * (y * z) = (z * (x * y)) * z`.

```lean
TauCeti.CayleyDickson.moufang_middle.{u_1} {R : Type u_1} [CommRing R]
  (x y z : TauCeti.CayleyDickson (Quaternion R)) : z * x * (y * z) = z * (x * y) * z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CayleyDickson.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_middle).

## Sources

- [Tau Ceti documentation: `TauCeti.CayleyDickson.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/CayleyDickson/Artin.html#TauCeti.CayleyDickson.moufang_middle)
- [Source of `TauCeti.CayleyDickson.moufang_middle` in TauCeti/Algebra/CayleyDickson/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/CayleyDickson/Artin.lean#L163)
