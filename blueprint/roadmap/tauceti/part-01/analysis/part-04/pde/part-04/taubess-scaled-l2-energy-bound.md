---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le
statement: formalized
proof: formalized
---

# Taubes's scaled `L²` energy bound

On a compact boundaryless Riemannian four-manifold `M`
with orientation `o`, let `ω` be a closed self-dual two-form, `F` a closed two-form and `η` a
two-form. Let `α`, `β`, `Dα`, `Dβ` be sections of families of seminormed groups, standing for the
components `α`, `β` of the normalized spinor and for `∇_a α`, `∇β`, with `|α|²` and `|β|²` of
class `C²` and `|∇_a α|²` continuous. Suppose that `1 ≤ r`, `0 ≤ K ≤ r` and
`256 c² ≤ r`, and that at every point

* `|α|² + |β|² ≤ 1 + K / r`;
* `-Δ|α|² / 2 + |∇_a α|² - (r / 4) (1 - |α|²) |α|² ≤ K₁`;
* `-Δ|β|² / 2 + |∇β|² + (r / 4) (|α|² + |β|² + 1) |β|² ≤ c |β| (|∇_a α| + |α| + |β|)`;
* `⟨ω, F⟩ / 2 = (r / 8) (1 - |α|² + |β|²) - ⟨ω, η⟩ / 4`;
* `|2 F⁺ + η|² ≤ (r² / 8) ((1 - |α|² + |β|²)² + 4 |α|² |β|²)`, where `F⁺ = (F + ⋆F) / 2`.

The last two are consequences of the curvature equation `F + ⋆F = (r / 4) ω - q(√r χ) - η` for
`F = i F_a`. Then, with all integrals against the Riemannian volume,

`r⁻¹ ∫ |F|² + ∫ |∇_a α|² + ∫ |∇β|² + r ∫ (1 - |α|² - |β|²)² ≤`
`2 (4 ⟨[F], [ω]⟩ + 2 ∫ ⟨ω, η⟩ + 2 K Vol(M)) + (5 / 3) K₁ Vol(M) + 2 Vol(M) +`
`(∫ |η|² - ∫ F ∧ F) / r`.

The right side does not depend on the solution: `⟨[F], [ω]⟩` and `∫ F ∧ F` depend only on the
de Rham class of `F`, which is `2π c₁(E)` for the curvature of a connection on the line `E`.

```lean
TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le.{u_1, u_2, u_3,
    u_4, u_5, u_6, u_7}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M]
  [MeasurableSpace M] [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} {F₁ : M → Type u_6} {F₂ : M → Type u_7}
  [(x : M) → SeminormedAddCommGroup (A x)] [(x : M) → SeminormedAddCommGroup (B x)]
  [(x : M) → SeminormedAddCommGroup (F₁ x)] [(x : M) → SeminormedAddCommGroup (F₂ x)] {r : ℝ}
  (o : TauCeti.Manifold.Orientation I M (Fin (2 + 2))) {ω F η : TauCeti.SmoothForm I M ℝ 2}
  {α : (x : M) → A x} {β : (x : M) → B x} {Dα : (x : M) → F₁ x} {Dβ : (x : M) → F₂ x} {K K₁ c : ℝ}
  (hr : 1 ≤ r) (hK : 0 ≤ K) (hKr : K ≤ r) (hcr : 256 * c ^ 2 ≤ r)
  (hα : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖α x‖ ^ 2)
  (hβ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖β x‖ ^ 2)
  (hDα : Continuous fun x => ‖Dα x‖ ^ 2) (hαβ : ∀ (x : M), ‖α x‖ ^ 2 + ‖β x‖ ^ 2 ≤ 1 + K / r)
  (hWα :
    ∀ (x : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) x / 2) + ‖Dα x‖ ^ 2 -
          r / 4 * (1 - ‖α x‖ ^ 2) * ‖α x‖ ^ 2 ≤
        K₁)
  (hWβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun y => ‖β y‖ ^ 2) x / 2 + ‖Dβ x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖))
  (hω : ω ∈ TauCeti.compactlySupportedClosedForms I M 2)
  (hω' : ω ∈ TauCeti.SmoothForm.selfDualForms o) (hF : F ∈ TauCeti.closedForms I M 2)
  (hFω :
    ∀ (x : M),
      ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑F x) / 2 =
        r / 8 * (1 - ‖α x‖ ^ 2 + ‖β x‖ ^ 2) -
          ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x)) (↑η x) / 4)
  (hFη :
    ∀ (x : M),
      ((TauCeti.alternatingFormInner (TangentSpace I x) 2)
            (2 • ↑((TauCeti.SmoothForm.selfDualPart o) F) x + ↑η x))
          (2 • ↑((TauCeti.SmoothForm.selfDualPart o) F) x + ↑η x) ≤
        r ^ 2 / 8 * ((1 - ‖α x‖ ^ 2 + ‖β x‖ ^ 2) ^ 2 + 4 * ‖α x‖ ^ 2 * ‖β x‖ ^ 2)) :
  r⁻¹ *
            ∫ (x : M),
              ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑F x))
                (↑F x) ∂TauCeti.riemannianVolume I M +
          ∫ (x : M), ‖Dα x‖ ^ 2 ∂TauCeti.riemannianVolume I M +
        ∫ (x : M), ‖Dβ x‖ ^ 2 ∂TauCeti.riemannianVolume I M +
      r * ∫ (x : M), (1 - ‖α x‖ ^ 2 - ‖β x‖ ^ 2) ^ 2 ∂TauCeti.riemannianVolume I M ≤
    2 *
            (4 *
                  ((TauCeti.poincarePairing I M o) ((TauCeti.deRhamCohomology.mk I 2) ⟨F, hF⟩))
                    ((TauCeti.compactlySupportedDeRhamCohomology.mk I 2) ⟨ω, hω⟩) +
                2 *
                  ∫ (x : M),
                    ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑ω x))
                      (↑η x) ∂TauCeti.riemannianVolume I M +
              2 * K * TauCeti.riemannianTotalVolume I M) +
          5 / 3 * K₁ * TauCeti.riemannianTotalVolume I M +
        2 * TauCeti.riemannianTotalVolume I M +
      (∫ (x : M),
            ((TauCeti.alternatingFormInner (TangentSpace I x) 2) (↑η x))
              (↑η x) ∂TauCeti.riemannianVolume I M -
          TauCeti.integralTopForm o (TauCeti.RoughForm.wedge ↑F ↑F)) /
        r
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-hodgestar.md)

## Proof depends on

- [Chern–Weil against the Riemannian measure](../../../../geometry/part-02/manifold/part-01/chern-weil-against-the-riemannian-measure.md)
- [The integrated Weitzenböck inequality for `α`](../part-02/the-integrated-weitzenbock-inequality-for.md)
- [Taubes's `L²` bound on `β`](taubess-l2-bound-on.md)
- [Taubes's `L¹` defect bound](taubess-l1-defect-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/EnergyBound.html#TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/EnergyBound.html#TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le)
- [Source of `TauCeti.SeibergWitten.inv_mul_integral_add_integral_add_integral_add_mul_integral_le` in TauCeti/Analysis/PDE/SeibergWitten/EnergyBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/EnergyBound.lean#L209)
