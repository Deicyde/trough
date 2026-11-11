---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm
statement: formalized
proof: formalized
---

# Wirtinger identity on manifolds

For an invariant pair `(form, J)`, the standard energy
density minus twice the symplectic area density is the Cauchy--Riemann defect square:
$$e(F) - 2 \omega_x(F \partial_s, F \partial_t) =
  \omega_x(F \partial_s + J_x F \partial_t, J_x(F \partial_s + J_x F \partial_t)).$$

```lean
TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {form : TauCeti.SmoothTwoForm I M}
  {J : TauCeti.SmoothAlmostComplexStructure I M} (hinv : form.Invariant J) (x : M)
  (F : ℝ × ℝ →ₗ[ℝ] TangentSpace I x) :
  form.stdComplexLineEnergyDensity J x F -
      2 *
        TauCeti.SmoothBundleForm.eval₂ form x (F TauCeti.stdComplexLineReal)
          (F TauCeti.stdComplexLineImag) =
    TauCeti.SmoothBundleForm.eval₂ form x
      (F TauCeti.stdComplexLineReal +
        (fun x => ⇑(J.toEndomorphism x)) x (F TauCeti.stdComplexLineImag))
      ((fun x => ⇑(J.toEndomorphism x)) x
        (F TauCeti.stdComplexLineReal +
          (fun x => ⇑(J.toEndomorphism x)) x (F TauCeti.stdComplexLineImag)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Energy.html#TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Energy.html#TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm)
- [Source of `TauCeti.SmoothTwoForm.Invariant.stdComplexLineEnergyDensity_sub_two_mul_twoForm` in TauCeti/Geometry/Symplectic/Manifold/Energy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Manifold/Energy.lean#L314)
