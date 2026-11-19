---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le, TauCeti.SeibergWitten.mul_integral_abs_one_sub_sub_le
statement: formalized
proof: formalized
---

# Taubes's `L¹` defect bound

On a closed oriented Riemannian four-manifold, let `ω` be a
closed self-dual two-form, `F` a closed two-form and `η` a two-form, and let `s` and `t ≥ 0` be
continuous functions with `s + t ≤ 1 + C / r`, where `r > 0` and `C ≥ 0`. If the `ω`-component of
the large-parameter curvature equation `⟨ω, F⟩ / 2 = (r / 8) (1 - s + t) - ⟨ω, η⟩ / 4` holds at
every point, then

`r ∫_M |1 - s - t| vol ≤ 4 ⟨[F], [ω]⟩ + 2 ∫_M ⟨ω, η⟩ vol + 2 C Vol(M)`.

For a solution with normalized spinor `χ = α u₀ + β`, `s = |α|²`, `t = |β|²` and `F = i F_a`,
this bounds `r ∫_M |1 - |χ|²| vol` independently of `r` and of the solution, given the class of
`F`, the perturbation `η` and the constant `C` of the pointwise bound `|χ|² ≤ 1 + C / r`.

```lean
TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  (o : TauCeti.Manifold.Orientation I M (Fin (2 + 2))) {ω F η : TauCeti.SmoothForm I M ℝ 2}
  {s t : M → ℝ} {r : ℝ} [CompactSpace M] {C : ℝ} (hr : 0 < r) (hC : 0 ≤ C) (hs : Continuous s)
  (ht : Continuous t) (ht₀ : ∀ (x : M), 0 ≤ t x) (hst : ∀ (x : M), s x + t x ≤ 1 + C / r)
  (hω : ω ∈ TauCeti.compactlySupportedClosedForms I M 2)
  (hω' : ω ∈ TauCeti.SmoothForm.selfDualForms o) (hF : F ∈ TauCeti.closedForms I M 2)
  (hFω :
    ∀ (x : M),
      ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑F x) / 2 =
        r / 8 * (1 - s x + t x) -
          ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑η x) / 4) :
  (r * TauCeti.integralTopForm o fun x => |1 - s x - t x| • TauCeti.riemannianVolumeForm o x) ≤
    (4 *
          ((TauCeti.poincarePairing I M o) ((TauCeti.deRhamCohomology.mk I 2) ⟨F, hF⟩))
            ((TauCeti.compactlySupportedDeRhamCohomology.mk I 2) ⟨ω, hω⟩) +
        2 *
          TauCeti.integralTopForm o fun x =>
            ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑η x) •
              TauCeti.riemannianVolumeForm o x) +
      2 * C * TauCeti.integralTopForm o (TauCeti.riemannianVolumeForm o)
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-hodgestar.md)

## Proof depends on

- [The Chern identity for the large-parameter curvature equation](../part-01/the-chern-identity-for-the-large-parameter-curva.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.html#TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le).

## Other forms

**Taubes's `L¹` defect bound against the Riemannian measure.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.mul_integral_abs_one_sub_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.html#TauCeti.SeibergWitten.mul_integral_abs_one_sub_sub_le).

```lean
TauCeti.SeibergWitten.mul_integral_abs_one_sub_sub_le.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  (o : TauCeti.Manifold.Orientation I M (Fin (2 + 2))) {ω F η : TauCeti.SmoothForm I M ℝ 2} {r : ℝ}
  [MeasurableSpace M] [BorelSpace M] [CompactSpace M] {A : M → Type u_4} {B : M → Type u_5}
  [(x : M) → SeminormedAddCommGroup (A x)] [(x : M) → SeminormedAddCommGroup (B x)]
  {α : (x : M) → A x} {β : (x : M) → B x} {K : ℝ} (hr : 0 < r) (hK : 0 ≤ K)
  (hs : Continuous fun x => ‖α x‖ ^ 2) (ht : Continuous fun x => ‖β x‖ ^ 2)
  (hαβ : ∀ (x : M), ‖α x‖ ^ 2 + ‖β x‖ ^ 2 ≤ 1 + K / r)
  (hω : ω ∈ TauCeti.compactlySupportedClosedForms I M 2)
  (hω' : ω ∈ TauCeti.SmoothForm.selfDualForms o) (hF : F ∈ TauCeti.closedForms I M 2)
  (hFω :
    ∀ (x : M),
      ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑F x) / 2 =
        r / 8 * (1 - ‖α x‖ ^ 2 + ‖β x‖ ^ 2) -
          ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑η x) / 4) :
  r * ∫ (x : M), |1 - ‖α x‖ ^ 2 - ‖β x‖ ^ 2| ∂TauCeti.riemannianVolume I M ≤
    4 *
          ((TauCeti.poincarePairing I M o) ((TauCeti.deRhamCohomology.mk I 2) ⟨F, hF⟩))
            ((TauCeti.compactlySupportedDeRhamCohomology.mk I 2) ⟨ω, hω⟩) +
        2 *
          ∫ (x : M),
            ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x))
              (↑η x) ∂TauCeti.riemannianVolume I M +
      2 * K * TauCeti.riemannianTotalVolume I M
```

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.html#TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le)
- [Source of `TauCeti.SeibergWitten.mul_integralTopForm_abs_one_sub_sub_le` in TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/ChernIdentity.lean#L145)
