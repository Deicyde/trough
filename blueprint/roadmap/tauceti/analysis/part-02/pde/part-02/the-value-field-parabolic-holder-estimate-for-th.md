---
declaration: theorem
origin: cited
lean: TauCeti.holderWith_heatDuhamelPotential
statement: formalized
proof: formalized
---

# The value-field parabolic Hölder estimate for the Duhamel potential

If the forcing
is jointly measurable and its spatial slices on `[0,T]` are bounded by `M` and `α`-Hölder with
constant `H`, where `0 < α ≤ 2`, then its Duhamel potential is parabolically `α`-Hölder on the
closed slab, with constant `T H (1 + M_α) + M max(1,T)`. Here `M_α` is the heat-kernel moment.
No temporal continuity of the forcing is assumed.

```lean
TauCeti.holderWith_heatDuhamelPotential.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : ℝ → E → F} {H α : NNReal}
  (hf : MeasureTheory.StronglyMeasurable (Function.uncurry f)) {T M : NNReal}
  (hM : ∀ r ∈ Set.Icc 0 ↑T, ∀ (y : E), ‖f r y‖ ≤ ↑M) (hH : ∀ r ∈ Set.Icc 0 ↑T, HolderWith H α (f r))
  (hα : 0 < α) (hα₂ : α ≤ 2) :
  HolderWith (T * H * (1 + TauCeti.heatKernelMoment E α) + M * max 1 T) α fun p =>
    TauCeti.heatDuhamelPotential f (↑p).time (↑p).space
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The parabolic Hölder estimate of the Cauchy heat potential](../part-01/the-parabolic-holder-estimate-of-the-cauchy-heat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.holderWith_heatDuhamelPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Holder.html#TauCeti.holderWith_heatDuhamelPotential).

## Sources

- [Tau Ceti documentation: `TauCeti.holderWith_heatDuhamelPotential`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Holder.html#TauCeti.holderWith_heatDuhamelPotential)
- [Source of `TauCeti.holderWith_heatDuhamelPotential` in TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Holder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/Holder.lean#L135)
