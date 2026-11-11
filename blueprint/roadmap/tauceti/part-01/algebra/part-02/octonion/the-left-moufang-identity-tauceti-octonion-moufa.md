---
declaration: theorem
origin: cited
lean: TauCeti.Octonion.moufang_left
statement: formalized
proof: formalized
---

# The left Moufang identity (`TauCeti.Octonion.moufang_left`)

`(z * x * z) * y = z * (x * (z * y))`.

```lean
TauCeti.Octonion.moufang_left.{u_1} {R : Type u_1} [CommRing R] (x y z : TauCeti.Octonion R) :
  z * x * z * y = z * (x * (z * y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Octonion.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_left).

## Sources

- [Tau Ceti documentation: `TauCeti.Octonion.moufang_left`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_left)
- [Source of `TauCeti.Octonion.moufang_left` in TauCeti/Algebra/Octonion/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Octonion/Basic.lean#L766)
