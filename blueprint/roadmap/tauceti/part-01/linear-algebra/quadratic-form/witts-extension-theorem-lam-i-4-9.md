---
declaration: theorem
origin: cited
lean: QuadraticMap.IsometryEquiv.exists_extension
statement: formalized
proof: formalized
---

# Witt's extension theorem (Lam I.4.9)

An isometry between regular subspaces of a
finite-dimensional quadratic space extends to an isometry of the whole space. No regularity
hypothesis on the ambient form is needed.

```lean
QuadraticMap.IsometryEquiv.exists_extension.{u, v} {K : Type u} [Field K] [Invertible 2]
  {V : Type v} [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] {Q : QuadraticForm K V}
  {W W' : Submodule K V}
  (f : (QuadraticMap.restrict Q W).IsometryEquiv (QuadraticMap.restrict Q W'))
  (hW : QuadraticMap.Nondegenerate) : ∃ e, ∀ (x : ↥W), e ↑x = ↑(f x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticMap.IsometryEquiv.exists_extension`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Extension.html#QuadraticMap.IsometryEquiv.exists_extension).

## Sources

- [Tau Ceti documentation: `QuadraticMap.IsometryEquiv.exists_extension`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Extension.html#QuadraticMap.IsometryEquiv.exists_extension)
- [Source of `QuadraticMap.IsometryEquiv.exists_extension` in TauCeti/LinearAlgebra/QuadraticForm/Witt/Extension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/QuadraticForm/Witt/Extension.lean#L47)
