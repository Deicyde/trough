---
declaration: section
origin: cited
lean: MetaMathlibExt.landau_inequality, MetaMathlibExt.landau_inequality_abs, MetaMathlibExt.landau_inequality_complex, MathlibExt.Analysis.Calculus.LandauKolmogorovSecondOrderWanted.bddAbove_abs_deriv_and_iSup_le_two_mul_sqrt
statement: formalized
proof: formalized
---

# Landau–Kolmogorov inequality

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/landau-kolmogorov-inequality/index.html).

## Landau–Kolmogorov inequality

## Landau–Kolmogorov inequality

**Landau–Kolmogorov inequality** on `ℝ` (case `n = 2`, `k = 1`): if `f` is twice
continuously differentiable with `|f| ≤ M₀` and `|f''| ≤ M₂` everywhere, then
`(f' x)² ≤ 2 * M₀ * M₂` for every `x`.

Formalized by `MetaMathlibExt.landau_inequality`, a theorem declared in [MathlibExt/Analysis/Calculus/LandauKolmogorov.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/LandauKolmogorov.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/landau-kolmogorov-inequality/index.html#landau-inequality).

## Landau–Kolmogorov inequality, square-root form

Square-root form of the Landau–Kolmogorov inequality.

Formalized by `MetaMathlibExt.landau_inequality_abs`, a theorem declared in [MathlibExt/Analysis/Calculus/LandauKolmogorov.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/LandauKolmogorov.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/landau-kolmogorov-inequality/index.html#landau-inequality-abs).

## Landau–Kolmogorov inequality, complex-valued case

**Landau–Kolmogorov inequality, complex-valued case** (constant `4`): if
`f : ℝ → ℂ` is twice continuously differentiable with `‖f‖ ≤ M₀` and
`‖f''‖ ≤ M₂` everywhere, then `‖f' x‖² ≤ 4 * M₀ * M₂` for every `x`. The
constant `4` comes from applying the real inequality to the real and imaginary
parts and adding.

Formalized by `MetaMathlibExt.landau_inequality_complex`, a theorem declared in [MathlibExt/Analysis/Calculus/LandauKolmogorov.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/LandauKolmogorov.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/landau-kolmogorov-inequality/index.html#landau-inequality-complex).

## Landau's inequality $M_1 \le 2\sqrt{M_0 M_2}$

For $f \in C^2(\mathbb{R})$, let $M_k = \sup_x |f^{(k)}(x)|$.
Prove that $M_1 \le 2\sqrt{M_0 M_2}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_92`.

Formalized by `MathlibExt.Analysis.Calculus.LandauKolmogorovSecondOrderWanted.bddAbove_abs_deriv_and_iSup_le_two_mul_sqrt`, a theorem declared in [MathlibExt/Analysis/Calculus/LandauKolmogorov.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/LandauKolmogorov.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/landau-kolmogorov-inequality/index.html#bdd-above-abs-deriv-and-i-sup-le-two-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Landau–Kolmogorov inequality](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/landau-kolmogorov-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/inequalities/landau-kolmogorov-inequality)
