---
declaration: theorem
origin: cited
lean: DirichletCharacter.LFunction_apply_one_pos
statement: formalized
proof: formalized
---

# DirichletCharacter.LFunction_apply_one_pos

The value at `s = 1` of the `L`-function of a nontrivial quadratic Dirichlet character is a
positive real number.

```lean
DirichletCharacter.LFunction_apply_one_pos {N : ℕ} {χ : DirichletCharacter ℂ N} [NeZero N]
  (hχ : MulChar.IsQuadratic χ) (hχ₁ : χ ≠ 1) : 0 < DirichletCharacter.LFunction χ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.LFunction_apply_one_pos`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Quadratic/Character.html#DirichletCharacter.LFunction_apply_one_pos).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.LFunction_apply_one_pos`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Quadratic/Character.html#DirichletCharacter.LFunction_apply_one_pos)
- [Source of `DirichletCharacter.LFunction_apply_one_pos` in TauCeti/NumberTheory/LSeries/Quadratic/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Quadratic/Character.lean#L86)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
