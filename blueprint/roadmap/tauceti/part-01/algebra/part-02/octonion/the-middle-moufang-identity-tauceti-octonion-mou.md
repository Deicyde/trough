---
declaration: theorem
origin: cited
lean: TauCeti.Octonion.moufang_middle
statement: formalized
proof: formalized
---

# The middle Moufang identity (`TauCeti.Octonion.moufang_middle`)

`(z * x) * (y * z) = (z * (x * y)) * z`.

```lean
TauCeti.Octonion.moufang_middle.{u_1} {R : Type u_1} [CommRing R] (x y z : TauCeti.Octonion R) :
  z * x * (y * z) = z * (x * y) * z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Octonion.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_middle).

## Sources

- [Tau Ceti documentation: `TauCeti.Octonion.moufang_middle`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_middle)
- [Source of `TauCeti.Octonion.moufang_middle` in TauCeti/Algebra/Octonion/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Octonion/Basic.lean#L787)
