---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq
statement: formalized
proof: formalized
---

# The Chern identity for the large-parameter curvature equation

Let `ω` be a compactly
supported closed self-dual two-form on an oriented boundaryless Riemannian four-manifold, `F` a
closed two-form and `η` a two-form, and suppose that the `ω`-component of the large-parameter
curvature equation `⟨ω, F⟩ / 2 = (r / 8) (1 - s + t) - ⟨ω, η⟩ / 4` holds at every point. Then

`r ∫_M (1 - s + t) vol = 4 ⟨[F], [ω]⟩ + 2 ∫_M ⟨ω, η⟩ vol`,

where `⟨[F], [ω]⟩ = ∫_M F ∧ ω` is the Poincaré pairing of the de Rham classes. For a solution
with normalized spinor `α u₀ + β`, `s = |α|²`, `t = |β|²` and `F = i F_a`, the right side depends
only on the line bundle, through the class `[F] = 2π c₁(E)`, and on the perturbation.

```lean
TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  (o : TauCeti.Manifold.Orientation I M (Fin (2 + 2))) {ω F η : TauCeti.SmoothForm I M ℝ 2}
  {s t : M → ℝ} {r : ℝ} [SigmaCompactSpace M] (hω : ω ∈ TauCeti.compactlySupportedClosedForms I M 2)
  (hω' : ω ∈ TauCeti.SmoothForm.selfDualForms o) (hF : F ∈ TauCeti.closedForms I M 2)
  (hFω :
    ∀ (x : M),
      ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑F x) / 2 =
        r / 8 * (1 - s x + t x) -
          ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑η x) / 4) :
  (r * TauCeti.integralTopForm o fun x => (1 - s x + t x) • TauCeti.riemannianVolumeForm o x) =
    4 *
        ((TauCeti.poincarePairing I M o) ((TauCeti.deRhamCohomology.mk I 2) ⟨F, hF⟩))
          ((TauCeti.compactlySupportedDeRhamCohomology.mk I 2) ⟨ω, hω⟩) +
      2 *
        TauCeti.integralTopForm o fun x =>
          ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑η x) •
            TauCeti.riemannianVolumeForm o x
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.html#TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.html#TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq)
- [Source of `TauCeti.SeibergWitten.mul_integralTopForm_one_sub_add_eq` in TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.lean#L96)
