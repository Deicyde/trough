---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq, TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_apply_eq
statement: formalized
proof: formalized
---

# Cartan's formula for a contact Hamiltonian vector field

a differentiable contact
Hamiltonian vector field `X` of `f` satisfies `L_X α = (R_α f) α`.

```lean
TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm I M ℝ 1} {f : M → ℝ} {X : (x : M) → TangentSpace I x}
  (hX : α.IsContactHamiltonianVectorField f X) (hXd : MDiff fun y => ⟨y, X y⟩) :
  TauCeti.mlieDerivForm X ↑α = fun x => (d% f x) (α.reebVectorField x) • ↑α x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Hamiltonian.html#TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq).

## Other forms

**Cartan's formula for a contact Hamiltonian vector field at a point where it is differentiable.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_apply_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Hamiltonian.html#TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_apply_eq).

```lean
TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_apply_eq.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {α : TauCeti.SmoothForm I M ℝ 1} {f : M → ℝ}
  {X : (x : M) → TangentSpace I x} (hX : α.IsContactHamiltonianVectorField f X) {x : M}
  (hXd : (MDiffAt fun y => ⟨y, X y⟩) x) :
  TauCeti.mlieDerivForm X (↑α) x = (d% f x) (α.reebVectorField x) • ↑α x
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Hamiltonian.html#TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq)
- [Source of `TauCeti.SmoothForm.IsContactHamiltonianVectorField.mlieDerivForm_eq` in TauCeti/Geometry/Contact/Hamiltonian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Contact/Hamiltonian.lean#L165)
