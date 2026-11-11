---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul
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

- [The contact Moser lemma, local form](the-contact-moser-lemma-local-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul)
- [Source of `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul` in TauCeti/Geometry/Contact/Darboux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Contact/Darboux.lean#L294)
