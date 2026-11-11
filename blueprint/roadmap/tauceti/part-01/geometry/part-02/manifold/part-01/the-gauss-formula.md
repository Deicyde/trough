---
declaration: theorem
origin: cited
lean: CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv
statement: formalized
proof: formalized
---

# The Gauss formula

If `f : M → F` is a `C²` map into a real inner product space whose
differential preserves inner products, then `⟪∇_X Y, w⟫ = ⟪D_X (df Y), df w⟫` for a Levi-Civita
connection `∇`: it is the tangential part of the ambient derivative of `df Y : y ↦ df_y (Y y)`.

```lean
CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv.{u_1, u_2, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsManifold I 2 M]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} {F : Type u_4} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {f : M → F} {x : M} (h : CovariantDerivative.IsLeviCivitaConnection I cov)
  (hf : ContMDiffAt I (modelWithCornersSelf ℝ F) 2 f x)
  (hg : ∀ (y : M) (v w : TangentSpace I y), inner ℝ v w = inner ℝ ((d% f y) v) ((d% f y) w))
  {X Y : (y : M) → TangentSpace I y} (hX : (MDiffAt fun y => ⟨y, X y⟩) x)
  (hY : (MDiffAt fun y => ⟨y, Y y⟩) x) (w : TangentSpace I x) :
  inner ℝ ((↑cov Y x) (X x)) w = inner ℝ (((d% fun y => (d% f y) (Y y)) x) (X x)) ((d% f x) w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Immersion.html#CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Immersion.html#CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv)
- [Source of `CovariantDerivative.IsLeviCivitaConnection.inner_apply_eq_inner_mvfderiv` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Immersion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Immersion.lean#L62)
