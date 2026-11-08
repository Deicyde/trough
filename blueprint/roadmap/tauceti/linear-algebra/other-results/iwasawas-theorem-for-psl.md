---
declaration: theorem
origin: cited
lean: Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top
statement: formalized
proof: formalized
---

# Iwasawa's theorem for `PSL`

On at least two coordinates, the projective special linear
group is simple as soon as the special linear group is perfect.

```lean
Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top.{u_1, u_2} {ι : Type u_1}
  {F : Type u_2} [Fintype ι] [DecidableEq ι] [Field F] [Nontrivial ι]
  (h : commutator (Matrix.SpecialLinearGroup ι F) = ⊤) :
  IsSimpleGroup (Matrix.ProjectiveSpecialLinearGroup ι F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.html#Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top).

## Sources

- [Tau Ceti documentation: `Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.html#Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top)
- [Source of `Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top` in TauCeti/LinearAlgebra/Projectivization/PSL/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.lean#L117)
