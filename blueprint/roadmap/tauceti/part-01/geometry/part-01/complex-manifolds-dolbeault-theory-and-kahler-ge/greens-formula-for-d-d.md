---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv, TauCeti.SmoothForm.integralTopForm_inner_mextDeriv_codifferential, TauCeti.SmoothForm.mextDeriv_wedge_hodgeStar
statement: formalized
proof: formalized
---

# Green's formula for `d*d`

on an oriented boundaryless Riemannian manifold,
`∫_M ⟨d*dα, β⟩ vol = ∫_M ⟨dα, dβ⟩ vol` for smooth `k`-forms `α` and `β`, one of them compactly
supported.

```lean
TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m k l : ℕ}
  [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hkl : k + 1 + l = m)
  (α β : TauCeti.SmoothForm I M ℝ k)
  (h : α ∈ TauCeti.compactlySupportedForms I M k ∨ β ∈ TauCeti.compactlySupportedForms I M k) :
  (TauCeti.integralTopForm o fun x =>
      ((TauCeti.alternatingFormInner (TangentSpace I x) k)
            (↑((TauCeti.SmoothForm.codifferential o hkl) ((TauCeti.mextDerivₗ I k) α)) x))
          (↑β x) •
        TauCeti.riemannianVolumeForm o x) =
    TauCeti.integralTopForm o fun x =>
      ((TauCeti.alternatingFormInner (TangentSpace I x) (k + 1)) (↑((TauCeti.mextDerivₗ I k) α) x))
          (↑((TauCeti.mextDerivₗ I k) β) x) •
        TauCeti.riemannianVolumeForm o x
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](tauceti-smoothform-hodgestar.md)

## Proof depends on

- [Orientation.hodgeStar](../../../analysis/part-01/four-dimensional-seiberg-witten-theory/orientation-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv).

## Other forms

**Green's formula for `dd*`.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.integralTopForm_inner_mextDeriv_codifferential`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.integralTopForm_inner_mextDeriv_codifferential).

```lean
TauCeti.SmoothForm.integralTopForm_inner_mextDeriv_codifferential.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m k l : ℕ}
  [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hkl : k + 1 + l = m)
  (α β : TauCeti.SmoothForm I M ℝ (k + 1))
  (h :
    α ∈ TauCeti.compactlySupportedForms I M (k + 1) ∨
      β ∈ TauCeti.compactlySupportedForms I M (k + 1)) :
  (TauCeti.integralTopForm o fun x =>
      ((TauCeti.alternatingFormInner (TangentSpace I x) (k + 1))
            (↑((TauCeti.mextDerivₗ I k) ((TauCeti.SmoothForm.codifferential o hkl) α)) x))
          (↑β x) •
        TauCeti.riemannianVolumeForm o x) =
    TauCeti.integralTopForm o fun x =>
      ((TauCeti.alternatingFormInner (TangentSpace I x) k)
            (↑((TauCeti.SmoothForm.codifferential o hkl) α) x))
          (↑((TauCeti.SmoothForm.codifferential o hkl) β) x) •
        TauCeti.riemannianVolumeForm o x
```

**Green's formula for the codifferential.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.mextDeriv_wedge_hodgeStar`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.mextDeriv_wedge_hodgeStar).

```lean
TauCeti.SmoothForm.mextDeriv_wedge_hodgeStar.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {k l : ℕ}
  (o : TauCeti.Manifold.Orientation I M (Fin (k + l + 1))) (α : TauCeti.SmoothForm I M ℝ k)
  (β : TauCeti.SmoothForm I M ℝ (k + 1)) :
  TauCeti.mextDeriv (TauCeti.RoughForm.wedge ↑α ↑((TauCeti.SmoothForm.hodgeStar o ⋯) β)) =
    (fun x =>
        ((TauCeti.alternatingFormInner (TangentSpace I x) (k + 1))
              (↑((TauCeti.mextDerivₗ I k) α) x))
            (↑β x) •
          TauCeti.riemannianVolumeForm o x) -
      fun x =>
      ((TauCeti.alternatingFormInner (TangentSpace I x) k) (↑α x))
          (↑((TauCeti.SmoothForm.codifferential o ⋯) β) x) •
        TauCeti.riemannianVolumeForm o x
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv)
- [Source of `TauCeti.SmoothForm.integralTopForm_inner_codifferential_mextDeriv` in TauCeti/Geometry/Manifold/Riemannian/Codifferential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Codifferential.lean#L524)
