---
declaration: theorem
origin: cited
lean: TauCeti.SobolevSection.isCompactOperator_lowerOrderL
statement: formalized
proof: formalized
---

# Rellich's theorem for Sobolev sections

On a compact manifold without boundary, given by a
finite bundle atlas of a Hausdorff manifold, the inclusion `W^{k+1,p}(V) → W^{k,p}(V)` is a compact
operator for every order `k` and every `1 ≤ p < ∞`.

```lean
TauCeti.SobolevSection.isCompactOperator_lowerOrderL.{u, u_1, u_2, u_3} {E : Type u}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {M : Type u_1} [TopologicalSpace M]
  [ChartedSpace E M] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] {V : M → Type u_3}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → TopologicalSpace (V x)] [FiberBundle F V]
  (A : TauCeti.FiniteBundleAtlas E M F V) [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ F]
  [(x : M) → AddCommGroup (V x)] [(x : M) → _root_.Module ℝ (V x)] [VectorBundle ℝ F V]
  [ContMDiffVectorBundle (↑⊤) F V (modelWithCornersSelf ℝ E)] (μ : MeasureTheory.Measure E)
  [μ.IsAddHaarMeasure] (p : ENNReal) [Fact (1 ≤ p)] (k : ℕ) [T2Space M] (hp : p ≠ ⊤) :
  IsCompactOperator ⇑(A.sectionChartData.lowerOrderL μ p k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The endpoint local Morrey estimate](../../../../analysis/part-04/sobolev/part-01/the-endpoint-local-morrey-estimate.md)
- [The local Morrey inequality](../../../../analysis/part-04/sobolev/part-01/the-local-morrey-inequality.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](../../../../analysis/part-04/sobolev/part-02/meyers-serrin-h-w-in-w-k-p.md)
- [Rellich–Kondrachov on a disc](../../../../analysis/part-04/sobolev/part-02/rellich-kondrachov-on-a-disc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SobolevSection.isCompactOperator_lowerOrderL`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Sobolev/Rellich.html#TauCeti.SobolevSection.isCompactOperator_lowerOrderL).

## Sources

- [Tau Ceti documentation: `TauCeti.SobolevSection.isCompactOperator_lowerOrderL`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Sobolev/Rellich.html#TauCeti.SobolevSection.isCompactOperator_lowerOrderL)
- [Source of `TauCeti.SobolevSection.isCompactOperator_lowerOrderL` in TauCeti/Geometry/Manifold/VectorBundle/Sobolev/Rellich.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/Sobolev/Rellich.lean#L100)
