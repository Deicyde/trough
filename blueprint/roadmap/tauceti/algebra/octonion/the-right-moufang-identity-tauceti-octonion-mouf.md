---
declaration: theorem
origin: cited
lean: TauCeti.Octonion.moufang_right
statement: formalized
proof: formalized
---

# The right Moufang identity (`TauCeti.Octonion.moufang_right`)

`x * (z * y * z) = ((x * z) * y) * z`.

```lean
TauCeti.Octonion.moufang_right.{u_1} {R : Type u_1} [CommRing R] (x y z : TauCeti.Octonion R) :
  x * (z * y * z) = x * z * y * z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The left Moufang identity (`TauCeti.Octonion.moufang_left`)](the-left-moufang-identity-tauceti-octonion-moufa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Octonion.moufang_right`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_right).

## Sources

- [Tau Ceti documentation: `TauCeti.Octonion.moufang_right`](https://taucetiproject.org/docs/TauCeti/Algebra/Octonion/Basic.html#TauCeti.Octonion.moufang_right)
- [Source of `TauCeti.Octonion.moufang_right` in TauCeti/Algebra/Octonion/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Octonion/Basic.lean#L776)
