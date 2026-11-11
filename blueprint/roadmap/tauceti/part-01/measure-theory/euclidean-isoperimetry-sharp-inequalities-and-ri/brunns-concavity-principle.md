---
declaration: theorem
origin: cited
lean: Convex.concaveOn_volume_real_preimage_prodMk_rpow, Convex.concaveOn_volume_real_hyperplaneSection_rpow, Convex.mul_volume_hyperplaneSection_rpow_add_mul_volume_hyperplaneSection_rpow_le, Convex.mul_volume_preimage_prodMk_rpow_add_mul_volume_preimage_prodMk_rpow_le
statement: formalized
proof: formalized
---

# Brunn's concavity principle

if every fiber of a convex set has finite volume, the
dimension root of the fiber volume is concave on the projection of the set.

```lean
Convex.concaveOn_volume_real_preimage_prodMk_rpow.{u_1, u_2} {P : Type u_1} {F : Type u_2}
  [AddCommGroup P] [_root_.Module ℝ P] [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {s : Set (P × F)} (hs : Convex ℝ s)
  (hfin : ∀ (p : P), MeasureTheory.volume (Prod.mk p ⁻¹' s) ≠ ⊤) :
  ConcaveOn ℝ (Prod.fst '' s) fun p =>
    MeasureTheory.volume.real (Prod.mk p ⁻¹' s) ^ (↑(Module.finrank ℝ F))⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Prékopa–Leindler inequality for the minimum on `ℝ`](../integral/part-02/prekopa-leindler-inequality-for-the-minimum-on-r.md)

## Lean

Formalized in Tau Ceti as [`Convex.concaveOn_volume_real_preimage_prodMk_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.html#Convex.concaveOn_volume_real_preimage_prodMk_rpow).

## Other forms

**Brunn's concavity principle for hyperplane sections.** Formalized in Tau Ceti as [`Convex.concaveOn_volume_real_hyperplaneSection_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.html#Convex.concaveOn_volume_real_hyperplaneSection_rpow).

```lean
Convex.concaveOn_volume_real_hyperplaneSection_rpow.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {s : Set E}
  (hs : Convex ℝ s) {e : E} (he : ‖e‖ = 1)
  (hfin : ∀ (t : ℝ), MeasureTheory.volume {y | ↑y + t • e ∈ s} ≠ ⊤) :
  ConcaveOn ℝ ((fun x => inner ℝ e x) '' s) fun t =>
    MeasureTheory.volume.real {y | ↑y + t • e ∈ s} ^ (↑(Module.finrank ℝ E - 1))⁻¹
```

**Brunn's concavity principle for hyperplane sections, extended form.** Formalized in Tau Ceti as [`Convex.mul_volume_hyperplaneSection_rpow_add_mul_volume_hyperplaneSection_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.html#Convex.mul_volume_hyperplaneSection_rpow_add_mul_volume_hyperplaneSection_rpow_le).

```lean
Convex.mul_volume_hyperplaneSection_rpow_add_mul_volume_hyperplaneSection_rpow_le.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {s : Set E} (hs : Convex ℝ s) {e : E} (he : ‖e‖ = 1) {t u : ℝ}
  (ht : t ∈ (fun x => inner ℝ e x) '' s) (hu : u ∈ (fun x => inner ℝ e x) '' s) {a b : ℝ}
  (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
  ENNReal.ofReal a * MeasureTheory.volume {y | ↑y + t • e ∈ s} ^ (↑(Module.finrank ℝ E - 1))⁻¹ +
      ENNReal.ofReal b * MeasureTheory.volume {y | ↑y + u • e ∈ s} ^ (↑(Module.finrank ℝ E - 1))⁻¹ ≤
    MeasureTheory.volume {y | ↑y + (a * t + b * u) • e ∈ s} ^ (↑(Module.finrank ℝ E - 1))⁻¹
```

**Brunn's concavity principle, extended form.** Formalized in Tau Ceti as [`Convex.mul_volume_preimage_prodMk_rpow_add_mul_volume_preimage_prodMk_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.html#Convex.mul_volume_preimage_prodMk_rpow_add_mul_volume_preimage_prodMk_rpow_le).

```lean
Convex.mul_volume_preimage_prodMk_rpow_add_mul_volume_preimage_prodMk_rpow_le.{u_1, u_2}
  {P : Type u_1} {F : Type u_2} [AddCommGroup P] [_root_.Module ℝ P] [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F]
  {s : Set (P × F)} (hs : Convex ℝ s) {p q : P} (hp : (Prod.mk p ⁻¹' s).Nonempty)
  (hq : (Prod.mk q ⁻¹' s).Nonempty) {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
  ENNReal.ofReal a * MeasureTheory.volume (Prod.mk p ⁻¹' s) ^ (↑(Module.finrank ℝ F))⁻¹ +
      ENNReal.ofReal b * MeasureTheory.volume (Prod.mk q ⁻¹' s) ^ (↑(Module.finrank ℝ F))⁻¹ ≤
    MeasureTheory.volume (Prod.mk (a • p + b • q) ⁻¹' s) ^ (↑(Module.finrank ℝ F))⁻¹
```

## Sources

- [Tau Ceti documentation: `Convex.concaveOn_volume_real_preimage_prodMk_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.html#Convex.concaveOn_volume_real_preimage_prodMk_rpow)
- [Source of `Convex.concaveOn_volume_real_preimage_prodMk_rpow` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Section.lean#L93)
