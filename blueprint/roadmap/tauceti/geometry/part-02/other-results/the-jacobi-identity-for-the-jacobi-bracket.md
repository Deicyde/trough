---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi, TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi
statement: formalized
proof: formalized
---

# The Jacobi identity for the Jacobi bracket

For a contact form on a finite-dimensional
manifold and `C²` functions `f`, `g`, `k`,
`{f, {g, k}_α}_α + {g, {k, f}_α}_α + {k, {f, g}_α}_α = 0`.

```lean
TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm I M ℝ 1} {f g k : M → ℝ} [FiniteDimensional ℝ E] (hα : α.IsContactForm)
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 f)
  (hg : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 g)
  (hk : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 k) (x : M) :
  α.jacobiBracket f (α.jacobiBracket g k) x + α.jacobiBracket g (α.jacobiBracket k f) x +
      α.jacobiBracket k (α.jacobiBracket f g) x =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula for the Levi form](../../part-01/manifold/part-01/cartans-formula-for-the-levi-form.md)
- [TauCeti.SmoothForm.instModule](../../part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-instmodule.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Jacobi.html#TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi).

## Other forms

**The Jacobi identity for the Poisson bracket.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Bracket.html#TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi).

```lean
TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {σ : TauCeti.SmoothTwoForm I M} {f g : M → ℝ} [FiniteDimensional ℝ E] (h : σ.IsNondegenerate)
  (hσ : TauCeti.SmoothForm.IsClosed σ) {k : M → ℝ} (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 f)
  (hg : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 g)
  (hk : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 k) (x : M) :
  σ.poissonBracket f (σ.poissonBracket g k) x + σ.poissonBracket g (σ.poissonBracket k f) x +
      σ.poissonBracket k (σ.poissonBracket f g) x =
    0
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Jacobi.html#TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi)
- [Source of `TauCeti.SmoothForm.IsContactForm.jacobiBracket_jacobi` in TauCeti/Geometry/Contact/Jacobi.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Contact/Jacobi.lean#L406)
