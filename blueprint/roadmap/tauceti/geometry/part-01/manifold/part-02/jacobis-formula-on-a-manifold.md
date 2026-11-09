---
declaration: theorem
origin: cited
lean: TauCeti.mvfderiv_det_apply
statement: formalized
proof: formalized
---

# Jacobi's formula on a manifold

If the entries of a matrix-valued function `A` are
differentiable at `x` and `A x` has invertible determinant, then along a tangent vector `v` the
derivative of `det A` is `det (A x) * trace ((A x)⁻¹ * dA (v))`, where `dA (v)` is the matrix of
the derivatives of the entries of `A` along `v`.

```lean
TauCeti.mvfderiv_det_apply.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  [CompleteSpace 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {n : Type u_5} [Fintype n] [DecidableEq n] {A : M → Matrix n n 𝕜} {x : M}
  (hA : ∀ (i j : n), (MDiffAt fun y => A y i j) x) (hdet : IsUnit (A x).det)
  (v : TangentSpace I x) :
  ((d% fun y => (A y).det) x) v =
    (A x).det * ((A x)⁻¹ * Matrix.of fun i j => ((d% fun y => A y i j) x) v).trace
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's inverse formula](../../../../analysis/part-02/calculus/part-01/jacobis-inverse-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mvfderiv_det_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/MFDeriv/Det.html#TauCeti.mvfderiv_det_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.mvfderiv_det_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/MFDeriv/Det.html#TauCeti.mvfderiv_det_apply)
- [Source of `TauCeti.mvfderiv_det_apply` in TauCeti/Geometry/Manifold/MFDeriv/Det.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/MFDeriv/Det.lean#L41)
