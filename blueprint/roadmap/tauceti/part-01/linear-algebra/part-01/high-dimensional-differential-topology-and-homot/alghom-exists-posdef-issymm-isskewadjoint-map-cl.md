---
declaration: theorem
origin: cited
lean: AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebraι
statement: formalized
proof: formalized
---

# AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebraι

A Clifford module equipped with a positive-definite quadratic form, whose quadratic space
has a finite orthogonal basis squaring to `-1`, admits a positive-definite symmetric form
making every Clifford vector skew-adjoint.

```lean
AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebraι.{u_1, u_2, u_3, u_4} {K : Type u_1}
  {M : Type u_2} {W : Type u_3} [CommRing K] [PartialOrder K] [IsOrderedAddMonoid K] [Invertible 2]
  [AddCommGroup M] [_root_.Module K M] [AddCommGroup W] [_root_.Module K W] {Q : QuadraticForm K M}
  (ρ : CliffordAlgebra Q →ₐ[K] Module.End K W) {I : Type u_4} [Finite I] (b : Module.Basis I K M)
  (hb : ∀ (i j : I), i ≠ j → QuadraticMap.IsOrtho Q (b i) (b j)) (hQ : ∀ (i : I), Q (b i) = -1)
  {Q₀ : QuadraticForm K W} (hpos : QuadraticMap.PosDef Q₀) :
  ∃ B,
    (LinearMap.BilinMap.toQuadraticMap B).PosDef ∧
      B.IsSymm ∧ ∀ (v : M), LinearMap.IsSkewAdjoint B ⇑(ρ ((CliffordAlgebra.ι Q) v))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebraι`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.html#AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebra%CE%B9).

## Sources

- [Tau Ceti documentation: `AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebraι`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.html#AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebra%CE%B9)
- [Source of `AlgHom.exists_posDef_isSymm_isSkewAdjoint_map_cliffordAlgebraι` in TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.lean#L69)
- [Tau Ceti roadmap status: High-dimensional differential topology and homotopy spheres](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HomotopySpheres/STATUS.md)
