---
declaration: section
origin: cited
lean: MathlibExt.Biology.Epidemiology.NextGenerationMatrix.R0, MathlibExt.Biology.Epidemiology.NextGenerationMatrix.isHurwitz_sub_iff_R0_lt_one, MathlibExt.Biology.Epidemiology.NextGenerationMatrix.exists_re_pos_iff_one_lt_R0, MathlibExt.Biology.Epidemiology.NextGenerationMatrix.mem_spectrum_fromBlocks_zero₁₂, MathlibExt.Biology.Epidemiology.NextGenerationMatrix.isHurwitz_fromBlocks_zero₁₂_iff, MathlibExt.Biology.Epidemiology.NextGenerationMatrix.globalSolution_decay_of_R0_lt_one, MathlibExt.Biology.Epidemiology.NextGenerationMatrix.exists_re_pos_jacobian_of_one_lt_R0
statement: formalized
proof: formalized
---

# Next-generation matrix and the basic reproduction number

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html).

## Basic reproduction number of the next-generation matrix

The **basic reproduction number** `R₀ = ρ(F V⁻¹)`: the spectral radius (largest modulus of
a complex eigenvalue) of the next-generation matrix `F V⁻¹` (van den Driessche–Watmough 2002,
Eq. (4)). It is meaningful when `V` is invertible (for a nonsingular M-matrix it is).

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.R0`, a definition declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#r0).

## `R₀` as a threshold for the linearized infected subsystem

**`R₀` as a threshold for the linearized infected subsystem** (van den Driessche–Watmough
2002, proof of Theorem 2). If `F` is entrywise nonnegative and `V` is a nonsingular M-matrix,
then every eigenvalue of `F - V` has negative real part iff `R₀ = ρ(F V⁻¹) < 1`.

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.isHurwitz_sub_iff_R0_lt_one`, a theorem declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#is-hurwitz-sub-iff-r0-lt-one).

## `R₀ > 1` gives an unstable mode

**`R₀ > 1` gives an unstable mode** (van den Driessche–Watmough 2002, proof of Theorem 2).
If `F` is entrywise nonnegative and `V` is a nonsingular M-matrix, then `F - V` has an
eigenvalue with positive real part iff `R₀ = ρ(F V⁻¹) > 1`.

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.exists_re_pos_iff_one_lt_R0`, a theorem declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#exists-re-pos-iff-one-lt-r0).

## Eigenvalues of a block lower-triangular matrix

The complex eigenvalues of a block lower-triangular real matrix `[[A, 0], [C, D]]` are
those of `A` together with those of `D`.

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.mem_spectrum_fromBlocks_zero₁₂`, a theorem declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#mem-spectrum-from-blocks-zero).

## Hurwitz criterion for block lower-triangular matrices

A block lower-triangular real matrix `[[A, 0], [C, D]]` is Hurwitz iff both diagonal
blocks are.

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.isHurwitz_fromBlocks_zero₁₂_iff`, a theorem declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#is-hurwitz-from-blocks-zero-iff).

## Threshold theorem, stability half, conditional decay form

**Threshold theorem, stability half, conditional decay form** (van den Driessche–Watmough
2002, Theorem 2). Let `x₀` be an equilibrium of `x' = f(x)` on `ℝ^{ι ⊕ κ}` (infected
compartments `ι`, the others `κ`), with `f` differentiable at `x₀` and Jacobian
`[[F - V, 0], [C, D]]` as in their Lemma 1, where `F ≥ 0`, `V` is a nonsingular M-matrix and
`D` is Hurwitz. If `R₀ = ρ(F V⁻¹) < 1`, then every solution defined on all of `[0, ∞)`
starting near `x₀` decays exponentially. The statement concerns only solutions defined on all of `[0, ∞)`, so it is not by itself local exponential stability.

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.globalSolution_decay_of_R0_lt_one`, a theorem declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#global-solution-decay-of-r0-lt-one).

## Threshold theorem, instability half, spectral form

**Threshold theorem, instability half, spectral form** (van den Driessche–Watmough 2002,
Theorem 2). With `F ≥ 0` and `V` a nonsingular M-matrix, if `R₀ = ρ(F V⁻¹) > 1` then the
Jacobian `[[F - V, 0], [C, D]]` at the disease-free equilibrium has an eigenvalue with positive
real part (whatever `C` and `D`).

Formalized by `MathlibExt.Biology.Epidemiology.NextGenerationMatrix.exists_re_pos_jacobian_of_one_lt_R0`, a theorem declared in [MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Epidemiology/NextGenerationMatrix.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html#exists-re-pos-jacobian-of-one-lt-r0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Next-generation matrix and the basic reproduction number](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/epidemiology/next-generation-matrix-and-the-basic-reproductio)
