---
declaration: theorem
origin: cited
lean: Matrix.FullShellLieAlgebra.lie_jacobi, Matrix.ShellLieAlgebra.lie_jacobi
statement: formalized
proof: formalized
---

# The Jacobi identity, for a positive definite `B` with even diagonal

```lean
Matrix.FullShellLieAlgebra.lie_jacobi.{u_1, u_2} {I : Type u_1} [Fintype I] {B : Matrix I I ℤ}
  {Y : Type u_2} [AddCommGroup Y] {D : B.ShellCartanDatum Y} [LinearOrder I] (hB : B.PosDef)
  (hdiag : ∀ (i : I), Even (B i i)) (x y z : Matrix.FullShellLieAlgebra D) :
  ⁅x, ⁅y, z⁆⁆ + ⁅y, ⁅z, x⁆⁆ + ⁅z, ⁅x, y⁆⁆ = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.FullShellLieAlgebra.lie_jacobi`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.html#Matrix.FullShellLieAlgebra.lie_jacobi).

## Other forms

**The Jacobi identity, for a positive definite `B` with even diagonal.** Formalized in Tau Ceti as [`Matrix.ShellLieAlgebra.lie_jacobi`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/Basic.html#Matrix.ShellLieAlgebra.lie_jacobi).

```lean
Matrix.ShellLieAlgebra.lie_jacobi.{u_1} {I : Type u_1} [Fintype I] {B : Matrix I I ℤ}
  [LinearOrder I] (hB : B.PosDef) (hdiag : ∀ (i : I), Even (B i i)) (x y z : B.ShellLieAlgebra) :
  ⁅x, ⁅y, z⁆⁆ + ⁅y, ⁅z, x⁆⁆ + ⁅z, ⁅x, y⁆⁆ = 0
```

## Sources

- [Tau Ceti documentation: `Matrix.FullShellLieAlgebra.lie_jacobi`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.html#Matrix.FullShellLieAlgebra.lie_jacobi)
- [Source of `Matrix.FullShellLieAlgebra.lie_jacobi` in TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/NormTwoShell/FullCartan/Basic.lean#L447)
