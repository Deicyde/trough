---
declaration: theorem
origin: cited
lean: TauCeti.mextDeriv_vectorBundlePoincareHomotopy
statement: formalized
proof: formalized
---

# The relative Poincaré identity

For a closed `C¹` form `η` of positive degree on the total
space of a `C²` vector bundle over a `C²` base, `d β = η - ρ^* η`, where `β` is the relative
Poincaré operator of `η` and `ρ = 0 ∘ π` is the retraction onto the zero section.

```lean
TauCeti.mextDeriv_vectorBundlePoincareHomotopy.{u_1, u_2, u_3, u_4, u_5, u_6} {B : Type u_1}
  {FV : Type u_2} {V : B → Type u_3} [(b : B) → AddCommGroup (V b)]
  [(b : B) → _root_.Module ℝ (V b)] {EB : Type u_4} {HB : Type u_5} [NormedAddCommGroup EB]
  [NormedSpace ℝ EB] [TopologicalSpace HB] {IB : ModelWithCorners ℝ EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] [NormedAddCommGroup FV] [NormedSpace ℝ FV] [(b : B) → TopologicalSpace (V b)]
  [TopologicalSpace (Bundle.TotalSpace FV V)] [FiberBundle FV V] {F : Type u_6}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} [VectorBundle ℝ FV V] [CompleteSpace F]
  [IsManifold IB 2 B] [ContMDiffVectorBundle 2 FV V IB]
  {η : TauCeti.RoughForm (IB.prod (modelWithCornersSelf ℝ FV)) (Bundle.TotalSpace FV V) F (k + 1)}
  (hη : TauCeti.IsSmoothForm (IB.prod (modelWithCornersSelf ℝ FV)) 1 η)
  (hclosed : TauCeti.mextDeriv η = 0) :
  TauCeti.mextDeriv (TauCeti.vectorBundlePoincareHomotopy η) =
    η -
      TauCeti.mpullback (IB.prod (modelWithCornersSelf ℝ FV)) (IB.prod (modelWithCornersSelf ℝ FV))
        (Bundle.zeroSection FV V ∘ Bundle.TotalSpace.proj) η
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mextDeriv_vectorBundlePoincareHomotopy`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Relative.html#TauCeti.mextDeriv_vectorBundlePoincareHomotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.mextDeriv_vectorBundlePoincareHomotopy`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Relative.html#TauCeti.mextDeriv_vectorBundlePoincareHomotopy)
- [Source of `TauCeti.mextDeriv_vectorBundlePoincareHomotopy` in TauCeti/Geometry/Manifold/DifferentialForm/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Relative.lean#L193)
