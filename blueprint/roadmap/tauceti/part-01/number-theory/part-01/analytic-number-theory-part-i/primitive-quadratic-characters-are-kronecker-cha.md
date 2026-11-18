---
declaration: theorem
origin: cited
lean: DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq
statement: formalized
proof: formalized
---

# Primitive quadratic characters are Kronecker characters

A primitive quadratic character
`χ` of level `N ≠ 0` is the character of a fundamental discriminant `D` with `|D| = N`:
`χ n = fundamentalDiscriminantCharCast R D n` at every integer `n` (Montgomery–Vaughan,
Theorem 9.13). The discriminant `D` is the product of the prime discriminants of the local factors
of `χ`.

```lean
DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq.{u_1} {R : Type u_1} [CommRing R]
  {N : ℕ} [NeZero N] {χ : DirichletCharacter R N} (hχ : χ.IsPrimitive)
  (hq : MulChar.IsQuadratic χ) :
  ∃ D,
    ∃ (hD : D.IsFundamentalDiscr),
      D.natAbs = N ∧
        ∀ (n : ℤ), χ ↑n = (TauCeti.Multiquadratic.fundamentalDiscriminantCharCast R D hD) ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Chinese remainder theorem for units](../../../../part-02/other-areas/data/the-chinese-remainder-theorem-for-units.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.html#DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.html#DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq)
- [Source of `DirichletCharacter.IsPrimitive.exists_isFundamentalDiscr_apply_eq` in TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.lean#L113)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
