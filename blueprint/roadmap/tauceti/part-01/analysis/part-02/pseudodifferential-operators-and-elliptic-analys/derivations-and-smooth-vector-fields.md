---
declaration: theorem
origin: cited
lean: TauCeti.exists_derivationEquivSmoothVectorField
statement: formalized
proof: formalized
---

# Derivations and smooth vector fields

On a finite-dimensional, Hausdorff, boundaryless real
manifold there is a `C^∞(M, ℝ)`-linear equivalence between derivations of `C^∞(M, ℝ)` and smooth
vector fields under which `δ f x = df_x (X x)`.

```lean
TauCeti.exists_derivationEquivSmoothVectorField.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [BoundarylessManifold I M] :
  ∃ e,
    ∀
      (δ :
        Derivation ℝ (ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤)
          (ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤))
      (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤) (x : M), (δ f) x = (d% ⇑f x) ((e δ) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's identity in the algebra of smooth functions](../../../geometry/part-02/manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../../../geometry/part-02/manifold/part-02/hadamards-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_derivationEquivSmoothVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorField/Derivation.html#TauCeti.exists_derivationEquivSmoothVectorField).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_derivationEquivSmoothVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorField/Derivation.html#TauCeti.exists_derivationEquivSmoothVectorField)
- [Source of `TauCeti.exists_derivationEquivSmoothVectorField` in TauCeti/Geometry/Manifold/VectorField/Derivation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorField/Derivation.lean#L374)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
