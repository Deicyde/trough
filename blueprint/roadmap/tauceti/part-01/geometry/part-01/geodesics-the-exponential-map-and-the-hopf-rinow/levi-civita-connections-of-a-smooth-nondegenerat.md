---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection
statement: formalized
proof: formalized
---

# Levi-Civita connections of a smooth nondegenerate metric family are jointly regular

For
a `C^(n+1)` vector field `Y`, the map `(p, x) ↦ ∇ᵖY(x)` into `Hom(TM, TM)` is `C^n`, where `∇ᵖ`
is a Levi-Civita connection of the metric at the parameter `p`. In particular it is smooth for a
smooth vector field.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {n : WithTop ℕ∞} {Y : (x : M) → TangentSpace I x}
  {EP : Type u_4} [NormedAddCommGroup EP] [NormedSpace ℝ EP] {HP : Type u_5} [TopologicalSpace HP]
  {IP : ModelWithCorners ℝ EP HP} {P : Type u_6} [TopologicalSpace P] [ChartedSpace HP P]
  [IsManifold IP 1 P] {g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P}
  {cov : P → CovariantDerivative I E fun x => TangentSpace I x}
  (hcov : ∀ (p : P), (g.metric p).IsLeviCivitaConnection (cov p)) (hn : n ≤ ↑⊤)
  (hY : ContMDiff I (I.prod (modelWithCornersSelf ℝ E)) (n + 1) fun y => ⟨y, Y y⟩) :
  ContMDiff (IP.prod I) (I.prod (modelWithCornersSelf ℝ (E →L[ℝ] E))) n fun q =>
    ⟨q.2, ↑(cov q.1) Y q.2⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Regularity.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Regularity.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.contMDiff_covariantDerivative_of_isLeviCivitaConnection` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Regularity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Regularity.lean#L275)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HopfRinow/STATUS.md)
