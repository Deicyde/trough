---
declaration: theorem
origin: cited
lean: TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace, TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection
statement: formalized
proof: formalized
---

# The Schwarz reflection principle

Let `U` be an open set mapped into itself by the
reflection `ρ` in the hyperplane `{a} × E`, and let `w` be weakly harmonic on `U ∩ H`, where
`H = {x | a < x.fst}`, and zero almost everywhere on `U` off `H`. Suppose that `w` is weakly
differentiable on all of `U`, with weak gradient `G` vanishing almost everywhere on `U` off `H`,
so that `w` vanishes on the flat boundary `U ∩ {a} × E` in the Sobolev sense. Then there is a
function `h` harmonic on `U` and odd under `ρ` that agrees almost everywhere on `U ∩ H` with `w`,
and whose gradient agrees almost everywhere on `U ∩ H` with `G`.

```lean
TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {a : ℝ} {U : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {w : WithLp 2 (ℝ × E) → ℝ}
  {G : WithLp 2 (ℝ × E) → WithLp 2 (ℝ × E)}
  (hharm : TauCeti.WeaklyHarmonicOn MeasureTheory.volume (U ⊓ TauCeti.normalHalfSpace a) w)
  (hU : Set.MapsTo ⇑(TauCeti.normalReflection E a) ↑U ↑U)
  (hw : TauCeti.HasWeakFDerivOn MeasureTheory.volume U w fun x => (innerSL ℝ) (G x))
  (hG0 :
    ∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑U,
      x ∉ TauCeti.normalHalfSpace a → G x = 0)
  (hw0 :
    ∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑U,
      x ∉ TauCeti.normalHalfSpace a → w x = 0) :
  ∃ h,
    InnerProductSpace.HarmonicOnNhd h ↑U ∧
      (∀ x ∈ U, h ((TauCeti.normalReflection E a) x) = -h x) ∧
        w =ᵐ[MeasureTheory.volume.restrict ↑(U ⊓ TauCeti.normalHalfSpace a)] h ∧
          (fun x => gradient h x) =ᵐ[MeasureTheory.volume.restrict ↑(U ⊓ TauCeti.normalHalfSpace a)]
            G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Weyl's lemma for continuous functions](../part-03/weyls-lemma-for-continuous-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.html#TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace).

## Other forms

**The Schwarz reflection principle, weak form.** Formalized in Tau Ceti as [`TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.html#TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection).

```lean
TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {a : ℝ}
  {U : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {w : WithLp 2 (ℝ × E) → ℝ}
  {G : WithLp 2 (ℝ × E) → WithLp 2 (ℝ × E)}
  (hharm : TauCeti.WeaklyHarmonicOn MeasureTheory.volume (U ⊓ TauCeti.normalHalfSpace a) w)
  (hU : Set.MapsTo ⇑(TauCeti.normalReflection E a) ↑U ↑U)
  (hw : TauCeti.HasWeakFDerivOn MeasureTheory.volume U w fun x => (innerSL ℝ) (G x))
  (hG0 :
    ∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑U,
      x ∉ TauCeti.normalHalfSpace a → G x = 0) :
  TauCeti.WeaklyHarmonicOn MeasureTheory.volume U fun x =>
    w x - w ((TauCeti.normalReflection E a) x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.html#TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace)
- [Source of `TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace` in TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.lean#L230)
