---
declaration: def
origin: cited
lean: Matrix.unitaryTransvectionSubgroup
statement: formalized
---

# The unitary transvection group of an isotropic point `p`

the isometries that are unitary
transvections `τ_{v,a}` along a representative `v` of `p`. It does not depend on the
representative (`Matrix.mem_unitaryTransvectionSubgroup_mk_iff`), and is abelian.

```lean
Matrix.unitaryTransvectionSubgroup.{u_1, u_2} {n : Type u_1} {K : Type u_2} [Fintype n]
  [DecidableEq n] [Field K] (Q : Matrix n n K) (σ : K →+* K) (p : ↥(Q.isotropicPoints σ)) :
  Subgroup ↥(Q.specialIsometryGroup σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.unitaryTransvectionSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Isometry/Transvection.html#Matrix.unitaryTransvectionSubgroup).

## Sources

- [Tau Ceti documentation: `Matrix.unitaryTransvectionSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Isometry/Transvection.html#Matrix.unitaryTransvectionSubgroup)
- [Source of `Matrix.unitaryTransvectionSubgroup` in TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Isometry/Transvection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/SpecialLinearGroup/Isometry/Transvection.lean#L96)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
