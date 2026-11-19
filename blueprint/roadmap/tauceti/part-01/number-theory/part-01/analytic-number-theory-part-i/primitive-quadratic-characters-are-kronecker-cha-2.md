---
declaration: theorem
origin: cited
lean: DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite
statement: formalized
proof: formalized
---

# Primitive quadratic characters are Kronecker characters, with their discriminant

When
`2 ≠ 0`, a primitive quadratic character `χ` of level `N` is the character of the fundamental
discriminant `D = χ (-1) N`: `χ n = fundamentalDiscriminantCharCast R D n` at every integer `n`.
For the principal character, primitive only at level `1`, this is `D = 1`.

```lean
DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite.{u_1} {R : Type u_1}
  [CommRing R] [DecidableEq R] [NeZero 2] {N : ℕ} [NeZero N] {χ : DirichletCharacter R N}
  (hχ : χ.IsPrimitive) (hq : MulChar.IsQuadratic χ) (n : ℤ) :
  χ ↑n =
    (TauCeti.Multiquadratic.fundamentalDiscriminantCharCast R (if χ (-1) = 1 then ↑N else -↑N) ⋯) ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Primitive quadratic characters are Kronecker characters](primitive-quadratic-characters-are-kronecker-cha.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.html#DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.html#DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite)
- [Source of `DirichletCharacter.IsPrimitive.apply_eq_fundamentalDiscriminantCharCast_ite` in TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DirichletCharacter/Quadratic/FundamentalDiscriminant.lean#L196)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
