---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection, TauCeti.Manifold.hasDerivAt_ricciTensor_of_hasDerivAt_difference, TauCeti.Manifold.hasDerivAt_ricciTensor_sum_of_hasDerivAt_difference, TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_of_isLeviCivitaConnection
statement: formalized
proof: formalized
---

# The Palatini identity in a basis

In the setting of
`hasDerivAt_ricciTensor_of_isLeviCivitaConnection`, for every basis `b` of `T_x M`,

`∂ₛ Ric^s(u, v) = ∑ᵢ bᵢ* ((∇ᵗ_{bᵢ} Γ')(v, u) - (∇ᵗ_u Γ')(v, bᵢ))` at `s = t`,

where `bᵢ*` is the `i`-th coordinate in `b`.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP]
  [NormedSpace ℝ EP] {HP : Type u_5} [TopologicalSpace HP] {IP : ModelWithCorners ℝ EP HP}
  {P : Type u_6} [TopologicalSpace P] [ChartedSpace HP P] [IsManifold IP 1 P]
  (g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P) {c : ℝ → P}
  {cov : ℝ → CovariantDerivative I E fun x => TangentSpace I x} {t : ℝ}
  [∀ (s : ℝ), (cov s).ContMDiffCovariantDerivative ↑⊤]
  (hc : ContMDiffAt (modelWithCornersSelf ℝ ℝ) IP 2 c t)
  (hcov : ∀ (s : ℝ), (g.metric (c s)).IsLeviCivitaConnection (cov s)) (x : M) {ι : Type u_7}
  [Fintype ι] (b : Module.Basis ι ℝ (TangentSpace I x)) (u v : TangentSpace I x) :
  HasDerivAt (fun s => (((cov s).ricciTensor x) u) v)
    (∑ i,
      (b.repr
          ((((↑((cov t).hom ((cov t).hom (cov t)))
                    (fun y => deriv (fun s => (cov s).difference (cov t) y) t) x)
                  (b i))
                v)
              u -
            (((↑((cov t).hom ((cov t).hom (cov t)))
                    (fun y => deriv (fun s => (cov s).difference (cov t) y) t) x)
                  u)
                v)
              (b i)))
        i)
    t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](the-koszul-formula.md)
- [TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-contmdiffnondegeneratemetric-le.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/RicciVariation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection).

## Other forms

**The Palatini identity for a family of connections.** Formalized in Tau Ceti as [`TauCeti.Manifold.hasDerivAt_ricciTensor_of_hasDerivAt_difference`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Variation.html#TauCeti.Manifold.hasDerivAt_ricciTensor_of_hasDerivAt_difference).

```lean
TauCeti.Manifold.hasDerivAt_ricciTensor_of_hasDerivAt_difference.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] {C : (x : M) → TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] TangentSpace I x}
  {t : ℝ} {x : M} [T2Space M] [IsManifold I (↑⊤) M]
  {cov : ℝ → CovariantDerivative I E (TangentSpace I)}
  [∀ (s : ℝ), (cov s).ContMDiffCovariantDerivative ↑⊤]
  (hC : ∀ᶠ (y : M) in nhds x, HasDerivAt (fun s => (cov s).difference (cov t) y) (C y) t)
  (htors : (cov t).torsion x = 0)
  (hreg :
    ∀ (X Z : (y : M) → TangentSpace I y),
      (ContMDiff I I.tangent ↑⊤ fun y => ⟨y, X y⟩) →
        (ContMDiff I I.tangent ↑⊤ fun y => ⟨y, Z y⟩) →
          ContMDiffAt ((modelWithCornersSelf ℝ ℝ).prod I) (I.prod (modelWithCornersSelf ℝ E)) 2
            (fun q => ⟨q.2, (↑(cov q.1) Z q.2) (X q.2)⟩) (t, x))
  (u v : TangentSpace I x) :
  HasDerivAt (fun s => (((cov s).ricciTensor x) u) v)
    ((LinearMap.trace ℝ (TangentSpace I x))
        ((((ContinuousLinearMap.toLinearMap₁₂ (↑((cov t).hom ((cov t).hom (cov t))) C x)).compr₂
                  (ContinuousLinearMap.coeLM ℝ)).flip
              v).flip
          u) -
      (LinearMap.trace ℝ (TangentSpace I x)) ↑(((↑((cov t).hom ((cov t).hom (cov t))) C x) u) v))
    t
```

**The Palatini identity for a family of connections, in a basis.** Formalized in Tau Ceti as [`TauCeti.Manifold.hasDerivAt_ricciTensor_sum_of_hasDerivAt_difference`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Variation.html#TauCeti.Manifold.hasDerivAt_ricciTensor_sum_of_hasDerivAt_difference).

```lean
TauCeti.Manifold.hasDerivAt_ricciTensor_sum_of_hasDerivAt_difference.{u_1, u_2, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] {C : (x : M) → TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] TangentSpace I x}
  {t : ℝ} {x : M} [T2Space M] [IsManifold I (↑⊤) M]
  {cov : ℝ → CovariantDerivative I E (TangentSpace I)}
  [∀ (s : ℝ), (cov s).ContMDiffCovariantDerivative ↑⊤]
  (hC : ∀ᶠ (y : M) in nhds x, HasDerivAt (fun s => (cov s).difference (cov t) y) (C y) t)
  (htors : (cov t).torsion x = 0)
  (hreg :
    ∀ (X Z : (y : M) → TangentSpace I y),
      (ContMDiff I I.tangent ↑⊤ fun y => ⟨y, X y⟩) →
        (ContMDiff I I.tangent ↑⊤ fun y => ⟨y, Z y⟩) →
          ContMDiffAt ((modelWithCornersSelf ℝ ℝ).prod I) (I.prod (modelWithCornersSelf ℝ E)) 2
            (fun q => ⟨q.2, (↑(cov q.1) Z q.2) (X q.2)⟩) (t, x))
  {ι : Type u_4} [Fintype ι] (b : Module.Basis ι ℝ (TangentSpace I x)) (u v : TangentSpace I x) :
  HasDerivAt (fun s => (((cov s).ricciTensor x) u) v)
    (∑ i,
      (b.repr
          ((((↑((cov t).hom ((cov t).hom (cov t))) C x) (b i)) v) u -
            (((↑((cov t).hom ((cov t).hom (cov t))) C x) u) v) (b i)))
        i)
    t
```

**The Palatini identity: the first variation of the Ricci tensor.** Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/RicciVariation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_of_isLeviCivitaConnection).

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_of_isLeviCivitaConnection.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP]
  [NormedSpace ℝ EP] {HP : Type u_5} [TopologicalSpace HP] {IP : ModelWithCorners ℝ EP HP}
  {P : Type u_6} [TopologicalSpace P] [ChartedSpace HP P] [IsManifold IP 1 P]
  (g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P) {c : ℝ → P}
  {cov : ℝ → CovariantDerivative I E fun x => TangentSpace I x} {t : ℝ}
  [∀ (s : ℝ), (cov s).ContMDiffCovariantDerivative ↑⊤]
  (hc : ContMDiffAt (modelWithCornersSelf ℝ ℝ) IP 2 c t)
  (hcov : ∀ (s : ℝ), (g.metric (c s)).IsLeviCivitaConnection (cov s)) (x : M)
  (u v : TangentSpace I x) :
  HasDerivAt (fun s => (((cov s).ricciTensor x) u) v)
    ((LinearMap.trace ℝ (TangentSpace I x))
        ((((ContinuousLinearMap.toLinearMap₁₂
                      (↑((cov t).hom ((cov t).hom (cov t)))
                        (fun y => deriv (fun s => (cov s).difference (cov t) y) t) x)).compr₂
                  (ContinuousLinearMap.coeLM ℝ)).flip
              v).flip
          u) -
      (LinearMap.trace ℝ (TangentSpace I x))
        ↑(((↑((cov t).hom ((cov t).hom (cov t)))
                (fun y => deriv (fun s => (cov s).difference (cov t) y) t) x)
              u)
            v))
    t
```

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/RicciVariation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_ricciTensor_sum_of_isLeviCivitaConnection` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/RicciVariation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/RicciVariation.lean#L111)
