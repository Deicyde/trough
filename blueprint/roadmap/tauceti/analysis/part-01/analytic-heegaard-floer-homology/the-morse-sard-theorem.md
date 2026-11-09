---
declaration: theorem
origin: cited
lean: ContDiff.addHaar_image_criticalPoints_eq_zero, TauCeti.addHaar_image_criticalPoints_eq_zero, TauCeti.interior_image_criticalPoints_eq_empty, TauCeti.addHaar_image_criticalPoints_eq_zero_of_finrank_le_add_two, TauCeti.interior_image_criticalPoints_eq_empty_of_finrank_le_add_two
statement: formalized
proof: formalized
---

# The Morse--Sard theorem

The critical values of a sufficiently smooth map between
finite-dimensional real normed spaces, that is the values it takes at the points where its Fréchet
derivative is not surjective, form a set of additive Haar measure zero. No relation between the
two dimensions is required.

```lean
ContDiff.addHaar_image_criticalPoints_eq_zero.{u, v} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {f : E → F}
  (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] {n : WithTop ℕ∞} (hf : ContDiff ℝ n f)
  (hk : ↑(Module.finrank ℝ E * Module.finrank ℝ E + 1) ≤ n) :
  ν (f '' {x | ¬Function.Surjective ⇑(fderiv ℝ f x)}) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sard's theorem on the locus where the derivative vanishes](../../part-02/calculus/part-02/sards-theorem-on-the-locus-where-the-derivative.md)

## Lean

Formalized in Tau Ceti as [`ContDiff.addHaar_image_criticalPoints_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/OutermostStratum.html#ContDiff.addHaar_image_criticalPoints_eq_zero).

## Other forms

**The Morse--Sard theorem on a set.** Formalized in Tau Ceti as [`TauCeti.addHaar_image_criticalPoints_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/OutermostStratum.html#TauCeti.addHaar_image_criticalPoints_eq_zero).

```lean
TauCeti.addHaar_image_criticalPoints_eq_zero.{u, v} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {U : Set E} {f : E → F}
  (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] {n : WithTop ℕ∞}
  (hf : ∀ x ∈ U, ContDiffAt ℝ n f x) (hk : ↑(Module.finrank ℝ E * Module.finrank ℝ E + 1) ≤ n) :
  ν (f '' (U ∩ {x | ¬Function.Surjective ⇑(fderiv ℝ f x)})) = 0
```

**The Morse--Sard theorem, in the form that carries no measure-theoretic data.** Formalized in Tau Ceti as [`TauCeti.interior_image_criticalPoints_eq_empty`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/OutermostStratum.html#TauCeti.interior_image_criticalPoints_eq_empty).

```lean
TauCeti.interior_image_criticalPoints_eq_empty.{u, v} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] {U : Set E} {f : E → F} {n : WithTop ℕ∞}
  (hf : ∀ x ∈ U, ContDiffAt ℝ n f x) (hk : ↑(Module.finrank ℝ E * Module.finrank ℝ E + 1) ≤ n) :
  interior (f '' (U ∩ {x | ¬Function.Surjective ⇑(fderiv ℝ f x)})) = ∅
```

**The Morse--Sard theorem at the sharp regularity, in codimension at most two.** Formalized in Tau Ceti as [`TauCeti.addHaar_image_criticalPoints_eq_zero_of_finrank_le_add_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/OutermostStratum.html#TauCeti.addHaar_image_criticalPoints_eq_zero_of_finrank_le_add_two).

```lean
TauCeti.addHaar_image_criticalPoints_eq_zero_of_finrank_le_add_two.{u, v} {E : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {F : Type v}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] [MeasurableSpace F]
  [BorelSpace F] {U : Set E} {f : E → F} (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure]
  {n : WithTop ℕ∞} (hf : ∀ x ∈ U, ContDiffAt ℝ n f x)
  (hcodim : Module.finrank ℝ E ≤ Module.finrank ℝ F + 2)
  (hk : ↑(Module.finrank ℝ E - Module.finrank ℝ F + 1) ≤ n) :
  ν (f '' (U ∩ {x | ¬Function.Surjective ⇑(fderiv ℝ f x)})) = 0
```

**The Morse--Sard theorem at the sharp regularity, in codimension at most two, in the form that carries no measure-theoretic data.** Formalized in Tau Ceti as [`TauCeti.interior_image_criticalPoints_eq_empty_of_finrank_le_add_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/OutermostStratum.html#TauCeti.interior_image_criticalPoints_eq_empty_of_finrank_le_add_two).

```lean
TauCeti.interior_image_criticalPoints_eq_empty_of_finrank_le_add_two.{u, v} {E : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {F : Type v}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {U : Set E} {f : E → F}
  {n : WithTop ℕ∞} (hf : ∀ x ∈ U, ContDiffAt ℝ n f x)
  (hcodim : Module.finrank ℝ E ≤ Module.finrank ℝ F + 2)
  (hk : ↑(Module.finrank ℝ E - Module.finrank ℝ F + 1) ≤ n) :
  interior (f '' (U ∩ {x | ¬Function.Surjective ⇑(fderiv ℝ f x)})) = ∅
```

## Sources

- [Tau Ceti documentation: `ContDiff.addHaar_image_criticalPoints_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/OutermostStratum.html#ContDiff.addHaar_image_criticalPoints_eq_zero)
- [Source of `ContDiff.addHaar_image_criticalPoints_eq_zero` in TauCeti/Analysis/Calculus/Sard/OutermostStratum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Sard/OutermostStratum.lean#L416)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
