---
declaration: def
origin: cited
lean: LinearMap.IsComplexPositiveDetLine
statement: formalized
---

# LinearMap.IsComplexPositiveDetLine

An element of the real determinant line of a complex-linear map `f` is **complex positive** if
it corresponds to a complex positive element of `det (ker f) ⊗ (det (coker f))^*`, that is, to
`(b₀ ∧ I • b₀ ∧ ⋯) ⊗ φ` for a complex basis `b` of the kernel and a functional `φ` positive on
`c₀ ∧ I • c₀ ∧ ⋯` for complex bases `c` of the cokernel
(`LinearMap.isComplexPositiveDetLine_iff`). These are the complex orientations of the determinant
lines of complex-linear Fredholm operators, such as complex Dirac and Cauchy–Riemann operators.

```lean
LinearMap.IsComplexPositiveDetLine.{u_1, u_2} {M : Type u_1} {N : Type u_2} [AddCommGroup M]
  [_root_.Module ℂ M] [_root_.Module ℝ M] [IsScalarTower ℝ ℂ M] [AddCommGroup N] [_root_.Module ℂ N]
  [_root_.Module ℝ N] [IsScalarTower ℝ ℂ N] (f : M →ₗ[ℂ] N) (z : (↑ℝ f).detLine) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsComplexPositiveDetLine`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.html#LinearMap.IsComplexPositiveDetLine).

## Sources

- [Tau Ceti documentation: `LinearMap.IsComplexPositiveDetLine`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.html#LinearMap.IsComplexPositiveDetLine)
- [Source of `LinearMap.IsComplexPositiveDetLine` in TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.lean#L122)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
