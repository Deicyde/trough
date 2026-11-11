---
declaration: theorem
origin: cited
lean: QuadraticMap.euler_four_squares
statement: formalized
proof: formalized
---

# Euler's four-square identity for a quadratic map

Multiplying `(x, y, z, w)` by the
quaternion `a + bi + cj + dk` multiplies `Q x + Q y + Q z + Q w` by `a² + b² + c² + d²`. For
`Q = x ↦ x²` on a commutative ring this is `euler_four_squares`.

```lean
QuadraticMap.euler_four_squares.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} {N : Type u_3}
  [CommRing R] [AddCommGroup M] [AddCommGroup N] [_root_.Module R M] [_root_.Module R N]
  (Q : QuadraticMap R M N) (a b c d : R) (x y z w : M) :
  Q (a • x - b • y - c • z - d • w) + Q (a • y + b • x + c • w - d • z) +
        Q (a • z - b • w + c • x + d • y) +
      Q (a • w + b • z - c • y + d • x) =
    (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2) • (Q x + Q y + Q z + Q w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticMap.euler_four_squares`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/FourSquares.html#QuadraticMap.euler_four_squares).

## Sources

- [Tau Ceti documentation: `QuadraticMap.euler_four_squares`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/FourSquares.html#QuadraticMap.euler_four_squares)
- [Source of `QuadraticMap.euler_four_squares` in TauCeti/LinearAlgebra/QuadraticForm/FourSquares.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/QuadraticForm/FourSquares.lean#L38)
