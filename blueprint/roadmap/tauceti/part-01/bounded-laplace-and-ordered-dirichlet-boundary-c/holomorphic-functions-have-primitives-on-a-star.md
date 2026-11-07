---
declaration: theorem
origin: cited
lean: TauCeti.Contour.isExactOn_of_starConvex
statement: formalized
proof: formalized
---

# Holomorphic functions have primitives on a star-shaped set

If `U` is open and
star-shaped about some point, then every function holomorphic on `U` has a primitive on `U`.

```lean
TauCeti.Contour.isExactOn_of_starConvex {U : Set ℂ} {f : ℂ → ℂ} {x : ℂ} (hU : IsOpen U)
  (hstar : StarConvex ℝ x U) (hf : DifferentiableOn ℂ f U) : Complex.IsExactOn f U
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Generalized winding number](../../part-02/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number.md)
- [The homology Cauchy theorem](../../part-02/contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.isExactOn_of_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Primitive.html#TauCeti.Contour.isExactOn_of_starConvex).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.isExactOn_of_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Primitive.html#TauCeti.Contour.isExactOn_of_starConvex)
- [Source of `TauCeti.Contour.isExactOn_of_starConvex` in TauCeti/Analysis/Contour/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Primitive.lean#L253)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
