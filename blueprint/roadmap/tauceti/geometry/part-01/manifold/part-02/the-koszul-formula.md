---
declaration: theorem
origin: cited
lean: CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul, CovariantDerivative.two_inner_leviCivitaConnection_eq_koszul, TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLeviCivitaConnection.two_apply_eq_koszul, TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLocalIsometry.two_apply_mfderiv_eq_koszul
statement: formalized
proof: formalized
---

# The Koszul formula

for a Levi-Civita connection, `2 ⟪∇_X Y, Z⟫` is the Koszul expression
of the metric. Mathlib's `CovariantDerivative.IsLeviCivitaConnection.apply_eq` is the same identity
with the expression written out; this form is the one `TauCeti.Manifold.koszul` controls.

```lean
CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [FiniteDimensional ℝ E] [IsManifold I 2 M]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} {X Y Z : (x : M) → TangentSpace I x}
  {x : M} (h : CovariantDerivative.IsLeviCivitaConnection I cov)
  (hX : (MDiffAt fun x => ⟨x, X x⟩) x) (hY : (MDiffAt fun x => ⟨x, Y x⟩) x)
  (hZ : (MDiffAt fun x => ⟨x, Z x⟩) x) :
  2 * inner ℝ ((↑cov Y x) (X x)) (Z x) = TauCeti.Manifold.koszul I X Y Z x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Basic.html#CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul).

## Other forms

**The Koszul formula.** Formalized in Tau Ceti as [`CovariantDerivative.two_inner_leviCivitaConnection_eq_koszul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Basic.html#CovariantDerivative.two_inner_leviCivitaConnection_eq_koszul).

```lean
CovariantDerivative.two_inner_leviCivitaConnection_eq_koszul.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [FiniteDimensional ℝ E] [IsManifold I 2 M]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {X Y Z : (x : M) → TangentSpace I x}
  {x : M} (hX : (MDiffAt fun x => ⟨x, X x⟩) x) (hY : (MDiffAt fun x => ⟨x, Y x⟩) x)
  (hZ : (MDiffAt fun x => ⟨x, Z x⟩) x) :
  2 * inner ℝ ((↑(CovariantDerivative.leviCivitaConnection I M) Y x) (X x)) (Z x) =
    TauCeti.Manifold.koszul I X Y Z x
```

**The Koszul formula.** Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLeviCivitaConnection.two_apply_eq_koszul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Basic.html#TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLeviCivitaConnection.two_apply_eq_koszul).

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLeviCivitaConnection.two_apply_eq_koszul.{u_1, u_2,
    u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {g : TauCeti.Manifold.ContMDiffNondegenerateMetric}
  {cov : CovariantDerivative I E fun x => TangentSpace I x} {X Y Z : (x : M) → TangentSpace I x}
  {x : M} [FiniteDimensional ℝ E] (h : g.IsLeviCivitaConnection cov)
  (hX : (MDiffAt fun x => ⟨x, X x⟩) x) (hY : (MDiffAt fun x => ⟨x, Y x⟩) x)
  (hZ : (MDiffAt fun x => ⟨x, Z x⟩) x) :
  2 * ((g.toContMDiffSection x) ((↑cov Y x) (X x))) (Z x) = g.koszul X Y Z x
```

**The Koszul formula through a local isometry.** Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLocalIsometry.two_apply_mfderiv_eq_koszul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/LocalIsometry.html#TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLocalIsometry.two_apply_mfderiv_eq_koszul).

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetric.IsLocalIsometry.two_apply_mfderiv_eq_koszul.{u_1, u_2,
    u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {H' : Type u_5}
  [TopologicalSpace H'] {J : ModelWithCorners ℝ F H'} {N : Type u_6} [TopologicalSpace N]
  [ChartedSpace H' N] [IsManifold J (↑⊤) N] {g : TauCeti.Manifold.ContMDiffNondegenerateMetric}
  {g' : TauCeti.Manifold.ContMDiffNondegenerateMetric} {f : M → N}
  {X Y Z : (y : N) → TangentSpace J y} {x : M} [FiniteDimensional ℝ E]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} (hf : g.IsLocalIsometry g' f)
  (h : g.IsLeviCivitaConnection cov) (hX : (MDiffAt fun y => ⟨y, X y⟩) (f x))
  (hY : (MDiffAt fun y => ⟨y, Y y⟩) (f x)) (hZ : (MDiffAt fun y => ⟨y, Z y⟩) (f x))
  {v : TangentSpace I x} (hXv : X (f x) = (mfderiv% f x) v) :
  2 *
      ((g'.toContMDiffSection (f x)) ((mfderiv% f x) ((↑cov (VectorField.mpullback I J f Y) x) v)))
        (Z (f x)) =
    g'.koszul X Y Z (f x)
```

## Sources

- [Tau Ceti documentation: `CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Basic.html#CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul)
- [Source of `CovariantDerivative.IsLeviCivitaConnection.two_inner_eq_koszul` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Basic.lean#L587)
