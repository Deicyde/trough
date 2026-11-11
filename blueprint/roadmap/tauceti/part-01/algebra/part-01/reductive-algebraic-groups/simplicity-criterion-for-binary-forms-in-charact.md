---
declaration: theorem
origin: cited
lean: TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP
statement: formalized
proof: formalized
---

# Simplicity criterion for binary forms in characteristic `p`

The binary forms of degree `d`
are simple exactly when `d + 1 = (a + 1) pᵐ` for some `a < p` and some `m`, that is, when every
base-`p` digit of `d` except the leading one is `p - 1`.

```lean
TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP.{u} {k : Type u} [Field k] {d : ℕ} (p : ℕ)
  [Fact (Nat.Prime p)] [CharP k p] :
  IsAtom (TauCeti.SpecialLinear.binaryForms k d) ↔ ∃ a < p, ∃ m, d + 1 = (a + 1) * p ^ m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lucas' theorem for divisibility, one digit at a time](../../../../part-02/other-areas/data/lucas-theorem-for-divisibility-one-digit-at-a-ti.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/SpecialLinear/BinaryForm/Basic.html#TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP).

## Sources

- [Tau Ceti documentation: `TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/SpecialLinear/BinaryForm/Basic.html#TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP)
- [Source of `TauCeti.SpecialLinear.isAtom_binaryForms_iff_of_charP` in TauCeti/Algebra/AlgebraicGroup/SpecialLinear/BinaryForm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/SpecialLinear/BinaryForm/Basic.lean#L733)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
