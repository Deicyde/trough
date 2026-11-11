---
declaration: theorem
origin: cited
lean: Matrix.FullShellLieAlgebra.leibniz_lie, Matrix.ShellLieAlgebra.leibniz_lie
statement: formalized
proof: formalized
---

# The Leibniz form of the Jacobi identity, for a positive definite `B` with even diagonal

```lean
Matrix.FullShellLieAlgebra.leibniz_lie.{u_1, u_2} {I : Type u_1} [Fintype I] {B : Matrix I I ℤ}
  {Y : Type u_2} [AddCommGroup Y] {D : B.ShellCartanDatum Y} [LinearOrder I] (hB : B.PosDef)
  (hdiag : ∀ (i : I), Even (B i i)) (x y z : Matrix.FullShellLieAlgebra D) :
  ⁅x, ⁅y, z⁆⁆ = ⁅⁅x, y⁆, z⁆ + ⁅y, ⁅x, z⁆⁆
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobi identity, for a positive definite `B` with even diagonal](the-jacobi-identity-for-a-positive-definite-b-wi.md)

## Lean

Formalized in Tau Ceti as [`Matrix.FullShellLieAlgebra.leibniz_lie`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.html#Matrix.FullShellLieAlgebra.leibniz_lie).

## Other forms

**The Leibniz form of the Jacobi identity, for a positive definite `B` with even diagonal.** Formalized in Tau Ceti as [`Matrix.ShellLieAlgebra.leibniz_lie`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/Basic.html#Matrix.ShellLieAlgebra.leibniz_lie).

```lean
Matrix.ShellLieAlgebra.leibniz_lie.{u_1} {I : Type u_1} [Fintype I] {B : Matrix I I ℤ}
  [LinearOrder I] (hB : B.PosDef) (hdiag : ∀ (i : I), Even (B i i)) (x y z : B.ShellLieAlgebra) :
  ⁅x, ⁅y, z⁆⁆ = ⁅⁅x, y⁆, z⁆ + ⁅y, ⁅x, z⁆⁆
```

## Sources

- [Tau Ceti documentation: `Matrix.FullShellLieAlgebra.leibniz_lie`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.html#Matrix.FullShellLieAlgebra.leibniz_lie)
- [Source of `Matrix.FullShellLieAlgebra.leibniz_lie` in TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.lean#L467)
