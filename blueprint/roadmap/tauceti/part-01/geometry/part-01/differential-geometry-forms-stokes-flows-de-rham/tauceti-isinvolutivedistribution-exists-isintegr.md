---
declaration: theorem
origin: cited
lean: TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold
statement: formalized
proof: formalized
---

# TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold

Every point of a finite-dimensional real `C^r` manifold with boundaryless model lies on a
local integral manifold of an involutive `C^m` distribution of constant rank `k`, for `1 ≤ m`
and `m + 1 ≤ r`.
The source is open in a `k`-dimensional subspace of the model space, its parametrization is an
embedding, and a flat chart identifies its image with an affine slice.

```lean
TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] {m : ℕ∞} (hm : 1 ≤ m) {r : WithTop ℕ∞} (hmr : ↑m + 1 ≤ r) [IsManifold I 1 M]
  [IsManifold I r M] {k : ℕ} {D : (x : M) → Submodule ℝ (TangentSpace I x)}
  (hinv : TauCeti.IsInvolutiveDistribution I D) (hD : TauCeti.IsContMDiffDistribution I (↑m) k D)
  (x : M) :
  ∃ W Φ U u f,
    Module.finrank ℝ ↥W = k ∧
      x ∈ Φ.source ∧
        (∀ y ∈ Φ.source, Submodule.map (↑(mfderiv% ↑Φ.toPartialEquiv y)) (D y) = W) ∧
          f u = x ∧
            Set.range f ⊆ Φ.source ∧
              Topology.IsEmbedding f ∧
                TauCeti.IsSliceChart Φ.toOpenPartialHomeomorph
                    (Set.range fun w => ↑Φ.toPartialEquiv x + ↑w) (Set.range f) ∧
                  TauCeti.IsIntegralManifold (modelWithCornersSelf ℝ ↥W) (↑m) D f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)
- [The local Frobenius theorem (`TauCeti.IsInvolutiveDistribution.exists_flatChart`)](../../part-02/manifold/part-02/the-local-frobenius-theorem-tauceti-isinvolutive.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Existence.html#TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold).

## Sources

- [Tau Ceti documentation: `TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Existence.html#TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold)
- [Source of `TauCeti.IsInvolutiveDistribution.exists_isIntegralManifold` in TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Existence.lean#L136)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
