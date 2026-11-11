---
declaration: theorem
origin: cited
lean: Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card
statement: formalized
proof: formalized
---

# `PSL_n(F)` is simple for `n ≥ 3`, over every field

```lean
Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card.{u_1, u_2} {ι : Type u_1}
  {F : Type u_2} [Fintype ι] [DecidableEq ι] [Field F] (h : 3 ≤ Fintype.card ι) :
  IsSimpleGroup (Matrix.ProjectiveSpecialLinearGroup ι F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iwasawa's theorem for `PSL`](iwasawas-theorem-for-psl.md)

## Lean

Formalized in Tau Ceti as [`Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.html#Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card).

## Sources

- [Tau Ceti documentation: `Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.html#Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card)
- [Source of `Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_three_le_card` in TauCeti/LinearAlgebra/Projectivization/PSL/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.lean#L126)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
