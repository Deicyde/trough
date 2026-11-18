---
declaration: theorem
origin: cited
lean: LerayHopf.exists_globalLerayHopfSolutionFull_torus3
statement: formalized
proof: formalized
---

# Leray–Hopf weak existence in Lean

[uda-lab/leray-hopf](https://github.com/uda-lab/leray-hopf) at commit [e704400f](https://github.com/uda-lab/leray-hopf/tree/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc), 2026-08-08.

> A Lean 4 + mathlib formalization of **Leray–Hopf weak existence** for the incompressible Navier–Stokes equations, on the periodic 3-torus 𝕋³ and on whole space ℝ³. Each domain carries a finite-horizon capstone and a global-in-time capstone — four machine-checked existence theorems in all — and every one of them is **kernel-only**: `#print axioms` returns only the standard kernel axioms (`propext`, `Classical.choice`, `Quot.sound`), with zero project axioms and no `sorryAx`.

*Quoted from [README.md](https://github.com/uda-lab/leray-hopf/blob/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Stability by multiplication by a slowly growing smooth function](../../../../undergraduate/distribution-calculus/spaces-s-r-d/stability-by-multiplication-by-a-slowly-growing.md)
- [$L^p$ functions](../../../../undergraduate/distribution-calculus/tempered-distributions/l-p-functions.md)
- [Tempered distributions](../../distribution-theory/tempered-distributions.md)
- [Fourier transform on $\mathrm{L}^2(\R^d)$](../../../../undergraduate/measures-and-integral-calculus/fourier-analysis/fourier-transform-on-l-2-r-d.md)
- [Stability by derivation](../../../../undergraduate/distribution-calculus/spaces-s-r-d/stability-by-derivation.md)
- [Multiplication by a function $C^\infty$ of slow growth](../../../../undergraduate/distribution-calculus/tempered-distributions/multiplication-by-a-function-c-infty-of-slow-gro.md)
- [Antiderivative of a continuous function](../../../../undergraduate/single-variable-real-analysis/integration/antiderivative-of-a-continuous-function.md)
- [Leibniz formula (Single Variable Real Analysis)](../../../../undergraduate/single-variable-real-analysis/differentiability/leibniz-formula.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`LerayHopf.exists_globalLerayHopfSolutionFull_torus3`](https://github.com/uda-lab/leray-hopf/blob/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc/LerayHopf/Torus/GlobalCapstone.lean#L110) (theorem)

No file its headlines import, directly or not (43 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.31.0-rc2, Mathlib at [15a89b24](https://github.com/leanprover-community/mathlib4/tree/15a89b2468bc01f1a6230d6e49ef5efc5286e502).
- 117 .lean files; its Lean libraries `LerayHopf` hold 113, declaring 890 names, with `sorry` in 4 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/uda-lab/leray-hopf/blob/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc/LICENSE)).

## Builds on

- Mathlib, at [15a89b24](https://github.com/leanprover-community/mathlib4/tree/15a89b2468bc01f1a6230d6e49ef5efc5286e502).

## Placement

Of its imports of Mathlib modules in an overview area, 135 of 182 are in Analysis, 2.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (135 of 182 imports, 2.7×), Linear algebra (19 of 182 imports, 1.8×), Topology (21 of 182 imports, 1.5×). *Proof depends on* names 8 of the 62 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [uda-lab/leray-hopf at e704400f](https://github.com/uda-lab/leray-hopf/tree/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc)
