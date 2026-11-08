---
declaration: def
origin: cited
lean: RootPairing.reflectionBond
statement: formalized
---

# RootPairing.reflectionBond

The **bond** of two weights related by a reflection in a positive root: if `y = s_β x` for a
positive root `β`, it is `⟨y, β^∨⟩ = -⟨x, β^∨⟩`. For `y ≠ x` and a reduced root pairing the
positive root `β` is unique (`TauCeti.eq_of_isPos_of_reflection_eq`), so the bond is well defined
(`RootPairing.reflectionBond_eq_coroot'`). If no reflection in a positive root sends `x` to `y`, the
bond is `0`. For a cover `y ⋖ x` of the parabolic quotient `W / W_λ`, the bond of `x λ` and `y λ`
is the positive cover bond `b_λ(x, y)`.

```lean
RootPairing.reflectionBond.{u, v, w, x} {ι : Type u} {R : Type v} {M : Type w} {N : Type x}
  [CommRing R] [CharZero R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) (b : P.Base) (x y : M) : R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.reflectionBond`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/ReflectionBond.html#RootPairing.reflectionBond).

## Sources

- [Tau Ceti documentation: `RootPairing.reflectionBond`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/ReflectionBond.html#RootPairing.reflectionBond)
- [Source of `RootPairing.reflectionBond` in TauCeti/LinearAlgebra/RootSystem/ReflectionBond.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/ReflectionBond.lean#L56)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
