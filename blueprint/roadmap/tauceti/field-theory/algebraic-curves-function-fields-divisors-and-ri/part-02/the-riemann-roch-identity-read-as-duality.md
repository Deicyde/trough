---
declaration: theorem
origin: cited
lean: TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq
statement: formalized
proof: formalized
---

# The Riemann–Roch identity, read as duality

for a Riemann–Roch divisor `W`, the index of
specialty of `D` is `ℓ(W - D)` (Stichtenoth, Theorem 1.5.14 in the presence of Theorem 1.5.15).

```lean
TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] {W : TauCeti.Divisor k F} {g₀ : ℕ}
  (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  (hW : W.IsRiemannRochDivisor g₀) (D : TauCeti.Divisor k F) : D.indexOfSpecialty = ↑(W - D).dim
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.html#TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.html#TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq)
- [Source of `TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq` in TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.lean#L156)
