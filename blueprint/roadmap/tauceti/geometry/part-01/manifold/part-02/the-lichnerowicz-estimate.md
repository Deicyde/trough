---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul
statement: formalized
proof: formalized
---

# The Lichnerowicz estimate

On a closed manifold of dimension `n ≥ 2` with
`Ric ≥ (n - 1) k g`, every positive eigenvalue with a nonzero smooth eigenfunction
is at least `n k`. The eigen-equation is stated for the native `Δ = div grad`.
The real lower bound `k` need not be positive.

```lean
TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [Bundle.RiemannianBundle fun x => TangentSpace I x] {f : M → ℝ} {k lam : ℝ}
  [T2Space M] [IsManifold I (↑⊤) M] [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  [I.Boundaryless] [CompactSpace M] [MeasurableSpace M] [BorelSpace M] (hn : 2 ≤ Module.finrank ℝ E)
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (hlam : 0 < lam)
  (heig : ∀ (x : M), TauCeti.Manifold.laplaceBeltrami I f x = -lam * f x) (hne : ∃ x, f x ≠ 0)
  (hRic :
    ∀ (x : M) (v : TangentSpace I x),
      (↑(Module.finrank ℝ E) - 1) * k * ‖v‖ ^ 2 ≤
        (((CovariantDerivative.leviCivitaConnection I M).ricciTensor x) v) v) :
  ↑(Module.finrank ℝ E) * k ≤ lam
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Bochner formula](../part-01/the-bochner-formula.md)
- [The divergence theorem on a manifold without boundary](../../positive-scalar-curvature-surgery-and-bordism/the-divergence-theorem-on-a-manifold-without-bou.md)
- [Green's first identity on a manifold without boundary](../../positive-scalar-curvature-surgery-and-bordism/greens-first-identity-on-a-manifold-without-boun.md)
- [The Koszul formula](the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Lichnerowicz/Basic.html#TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Lichnerowicz/Basic.html#TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul)
- [Source of `TauCeti.Manifold.finrank_mul_le_of_laplaceBeltrami_eq_neg_mul` in TauCeti/Geometry/Manifold/Riemannian/Lichnerowicz/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Lichnerowicz/Basic.lean#L82)
