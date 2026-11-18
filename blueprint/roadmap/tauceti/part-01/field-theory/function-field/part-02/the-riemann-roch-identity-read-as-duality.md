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

- [Riemann's theorem](riemanns-theorem.md)
- [The weak approximation theorem](the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.html#TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.html#TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq)
- [Source of `TauCeti.Divisor.IsRiemannRochDivisor.indexOfSpecialty_eq` in TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/RiemannRoch/Uniqueness.lean#L156)
