---
declaration: section
origin: cited
lean: OAI.PlanarAnderson.anderson_spectrum_ae
statement: formalized
proof: formalized
---

# 261. Localization and delocalization in the Anderson model

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the predicted spectral contrast for the lattice Anderson model with independent uniform site potentials. In dimension two, every positive disorder strength gives almost surely pure-point spectrum. In every fixed dimension *d* ≥ 3, sufficiently weak positive disorder gives purely absolutely continuous spectrum on a fixed open interval with nonzero spectral weight.

## Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three

For each fixed dimension *d* ≥ 3 and each fixed sufficiently small positive disorder strength, we prove that the Anderson operator on ℤ$^{d}$ with independent uniform site potentials almost surely has purely absolutely continuous spectrum with nonzero weight on an open energy interval. The interval may depend on *d* but is independent of the disorder strength. This settles the purely absolutely continuous energy-range question in Simon's Problem 1 for this model.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf).

## Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder

For each fixed positive disorder strength, we prove that the nearest-neighbor Anderson operator on the square lattice with independent uniform site potentials almost surely has pure-point spectral type throughout its spectrum. This resolves the pure-point assertion of the two-dimensional Anderson localization conjecture for the uniform single-site law.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The linked formalization proves a supporting spectral statement for the nearest-neighbor Anderson operator on $\mathbb Z^2$. For every disorder strength $h>0$ with independent site potentials uniform on $[-h,h]$, it constructs the bounded self-adjoint operator almost surely and identifies its spectrum as the real interval $[-4-h,4+h]$.

This selected statement identifies the spectral set. It does not assert the pure-point spectral type claimed in the accompanying paper.

## Lean: Almost-sure spectrum of the planar Anderson operator

Stated in [PlanarAndersonSpectrum.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarAndersonSpectrum.lean).

```lean
theorem anderson_spectrum_ae {h : ℝ} (hh : 0 < h) :
    ∀ᵐ v ∂disorderLaw h, ∃ H : Hilbert →L[ℂ] Hilbert,
      IsAndersonOperator v H ∧ IsSelfAdjoint H ∧ spectrum ℂ H = spectralInterval h
```

Proved in [lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean, line 674](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean#L674).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/261.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/261.md)
