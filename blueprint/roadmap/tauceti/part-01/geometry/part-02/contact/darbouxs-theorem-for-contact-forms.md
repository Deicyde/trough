---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul, TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart, TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart_of_finrank_eq
statement: formalized
proof: formalized
---

# Darboux's theorem for contact forms

Let `α` be a `C^(r+1)` one-form (`r ≥ 1`) on an open
subset `W` of a finite-dimensional real normed space, which is a contact form at `x₀ ∈ W`. Then
some `C^r` diffeomorphism `ψ` of the space fixing `x₀` pulls `α` back, on a neighbourhood of
`x₀`, to a positive multiple `g • α_lin` of the osculating model form
`α_lin(x) = α(x₀) + ½ ι_{x - x₀} dα(x₀)`, whose exterior derivative is the constant form
`dα(x₀)`. Its second summand is the radial primitive `ContinuousLinearMap.liouvilleFormCLM` of
`dα(x₀)`, evaluated at `x - x₀`.

```lean
TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] {α : V → V [⋀^Fin 1]→L[ℝ] ℝ}
  {W : Set V} {x₀ : V} {r : ℕ∞} (hr : 1 ≤ r) (hW : IsOpen W) (hx₀ : x₀ ∈ W)
  (hα : ContDiffOn ℝ (↑r + 1) α W) (hc : TauCeti.IsContactFormAt α x₀) :
  ∃ ψ g,
    ψ x₀ = x₀ ∧
      ∀ᶠ (x : V) in nhds x₀,
        0 < g x ∧
          (α (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) =
            g x •
              (α x₀ +
                ((ContinuousAlternatingMap.flatL ℝ V ℝ) (extDeriv α x₀)).liouvilleFormCLM (x - x₀))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [The contact Darboux theorem](../symplectic-geometry-and-hamiltonian-mechanics/the-contact-darboux-theorem.md)
- [The contact Moser lemma, local form](the-contact-moser-lemma-local-form.md)
- [Darboux's theorem](../symplectic/part-01/darbouxs-theorem.md)
- [The inverse function theorem for manifolds](../manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Poincaré lemma on manifolds](../manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul).

## Other forms

**The Darboux theorem for contact forms.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Strict.html#TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart).

```lean
TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] {α : TauCeti.SmoothForm I M ℝ 1}
  (hα : α.IsContactForm) (x₀ : M) :
  ∃ n chart,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            ∀ (v : TangentSpace I x),
              (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                    (↑chart.toPartialEquiv x))
                  ![(d% ↑chart.toPartialEquiv x) v] =
                (↑α x) ![v]
```

**The Darboux theorem for contact forms, in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart_of_finrank_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Strict.html#TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart_of_finrank_eq).

```lean
TauCeti.SmoothForm.IsContactForm.exists_strictDarbouxChart_of_finrank_eq.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm I M ℝ 1} (hα : α.IsContactForm) {n : ℕ}
  (hn : Module.finrank ℝ E = 2 * n + 1) (x₀ : M) :
  ∃ chart,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          ∀ (v : TangentSpace I x),
            (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                  (↑chart.toPartialEquiv x))
                ![(d% ↑chart.toPartialEquiv x) v] =
              (↑α x) ![v]
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul)
- [Source of `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul` in TauCeti/Geometry/Contact/Darboux/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Contact/Darboux/Basic.lean#L302)
