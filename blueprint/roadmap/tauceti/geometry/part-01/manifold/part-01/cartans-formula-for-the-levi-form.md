---
declaration: theorem
origin: cited
lean: TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv
statement: formalized
proof: formalized
---

# Cartan's formula for the Levi form

For vector fields `V` and `W` tangent to the kernel of
a one-form `α` near `x`, `α_x ([V, W]_x) = -dα_x (V_x, W_x)`.

```lean
TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {x : M}
  {α : TauCeti.RoughForm I M ℝ 1} {V W : (y : M) → TangentSpace I y}
  (hα : (MDiffAt fun y => ⟨y, α y⟩) x) (hV : (MDiffAt fun y => ⟨y, V y⟩) x)
  (hW : (MDiffAt fun y => ⟨y, W y⟩) x) (hVα : ∀ᶠ (y : M) in nhds x, V y ∈ α.ker y)
  (hWα : ∀ᶠ (y : M) in nhds x, W y ∈ α.ker y) :
  (α x) ![VectorField.mlieBracket I V W x] = -(TauCeti.mextDeriv α x) ![V x, W x]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/VectorField.html#TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/VectorField.html#TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv)
- [Source of `TauCeti.RoughForm.apply_mlieBracket_eq_neg_mextDeriv` in TauCeti/Geometry/Manifold/DifferentialForm/VectorField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/VectorField.lean#L285)
