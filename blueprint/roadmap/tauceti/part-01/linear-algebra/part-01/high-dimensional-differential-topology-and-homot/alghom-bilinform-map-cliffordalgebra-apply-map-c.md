---
declaration: theorem
origin: cited
lean: AlgHom.bilinForm_map_cliffordAlgebraι_apply_map_cliffordAlgebraι_apply
statement: formalized
proof: formalized
---

# AlgHom.bilinForm_map_cliffordAlgebraι_apply_map_cliffordAlgebraι_apply

For a vector `v` whose Clifford action is skew-adjoint with respect to `B`, applying
`ρ (ι Q v)` to both arguments scales `B` by `-Q v`.
No symmetry or positivity assumption on the form is needed.

```lean
AlgHom.bilinForm_map_cliffordAlgebraι_apply_map_cliffordAlgebraι_apply.{u_1, u_2, u_3}
  {K : Type u_1} {M : Type u_2} {W : Type u_3} [CommRing K] [AddCommGroup M] [_root_.Module K M]
  [AddCommGroup W] [_root_.Module K W] {Q : QuadraticForm K M}
  (ρ : CliffordAlgebra Q →ₐ[K] Module.End K W) (B : LinearMap.BilinForm K W) (v : M)
  (hρ : LinearMap.IsSkewAdjoint B ⇑(ρ ((CliffordAlgebra.ι Q) v))) (x y : W) :
  (B ((ρ ((CliffordAlgebra.ι Q) v)) x)) ((ρ ((CliffordAlgebra.ι Q) v)) y) = -Q v * (B x) y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgHom.bilinForm_map_cliffordAlgebraι_apply_map_cliffordAlgebraι_apply`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.html#AlgHom.bilinForm_map_cliffordAlgebra%CE%B9_apply_map_cliffordAlgebra%CE%B9_apply).

## Sources

- [Tau Ceti documentation: `AlgHom.bilinForm_map_cliffordAlgebraι_apply_map_cliffordAlgebraι_apply`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.html#AlgHom.bilinForm_map_cliffordAlgebra%CE%B9_apply_map_cliffordAlgebra%CE%B9_apply)
- [Source of `AlgHom.bilinForm_map_cliffordAlgebraι_apply_map_cliffordAlgebraι_apply` in TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Module/Metric.lean#L52)
- [Tau Ceti roadmap status: High-dimensional differential topology and homotopy spheres](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HomotopySpheres/STATUS.md)
