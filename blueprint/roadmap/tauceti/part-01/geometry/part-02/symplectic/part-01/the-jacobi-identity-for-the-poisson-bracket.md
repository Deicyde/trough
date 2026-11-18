---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi
statement: formalized
proof: formalized
---

# The Jacobi identity for the Poisson bracket

For a nondegenerate closed form on a
finite-dimensional manifold and `C²` functions `f`, `g`, `k`,
`{f, {g, k}} + {g, {k, f}} + {k, {f, g}} = 0`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Bracket.html#TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Bracket.html#TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi)
- [Source of `TauCeti.SmoothTwoForm.IsNondegenerate.poissonBracket_jacobi` in TauCeti/Geometry/Symplectic/Hamiltonian/Bracket.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/Bracket.lean#L214)
