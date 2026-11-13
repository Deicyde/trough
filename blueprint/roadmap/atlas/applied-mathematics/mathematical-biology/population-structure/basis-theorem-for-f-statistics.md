---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f4Form, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f3Form, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_eq_f4Form, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.fSpace, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f4Form_mem_fSpace, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_mem_fSpace, MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f3Form_mem_fSpace
statement: formalized
proof: formalized
---

# Basis theorem for f-statistics

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html).

## Per-locus f4 form

The per-locus `f4` form `x ↦ (x A - x B) * (x C - x D)` on frequency vectors `x : P → ℝ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f4Form`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f4-form).

## Per-locus f2 form

The per-locus `f2` form `x ↦ (x A - x B) ^ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f2-form).

## Per-locus f3 form

The per-locus `f3` form `x ↦ (x C - x A) * (x C - x B)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f3Form`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f3-form).

## Per-locus f2 form as a special f4 form

`f2Form A B = f4Form A B A B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_eq_f4Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f2-form-eq-f4-form).

## Space spanned by the per-locus f-statistics

The space `V_F` spanned by all per-locus f-statistics (all `f4Form`; `f2Form` and `f3Form`
are special cases).

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.fSpace`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f-space).

## Every f4 form lies in the f-statistic space

Every `f4Form` lies in `V_F`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f4Form_mem_fSpace`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f4-form-mem-f-space).

## Every f2 form lies in the f-statistic space

Every `f2Form` lies in `V_F`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_mem_fSpace`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f2-form-mem-f-space).

## Every f3 form lies in the f-statistic space

Every `f3Form` lies in `V_F`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f3Form_mem_fSpace`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f3-form-mem-f-space).

## f4 statistic as the integral of the f4 form

The `f4` statistic is the integral of the `f4` form of the frequency vector.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f4_eq_integral_f4Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f4-eq-integral-f4-form).

## Integral of a linear combination of f2 forms

A linear combination of `f2` forms integrates to the same linear combination of `f2`
statistics, for square-integrable frequencies.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.integral_sum_smul_f2Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#integral-sum-smul-f2-form).

## Symmetry of the per-locus f2 form

`f2Form` is symmetric.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_comm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f2-form-comm).

## Per-locus f2 form of a population with itself is zero

`f2Form A A = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_self`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f2-form-self).

## Per-locus f3 form is symmetric in its sources

`f3Form` is symmetric in its last two arguments.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f3Form_comm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f3-form-comm).

## Per-locus f3 form vanishes when target equals first source

`f3Form C C B = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f3Form_self_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f3-form-self-left).

## Polarization identity for the per-locus f4 form

`f4Form` in terms of `f2Form`: the polarization identity behind `f4_eq_f2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f4Form_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f4-form-eq).

## Per-locus f2 form in terms of f3 forms with a base population

`f2Form` in terms of the `f3` forms with base `o`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.f2Form_eq_f3Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#f2-form-eq-f3-form).

## Linear independence of Patterson's f2 basis

Patterson's `f2` basis: the forms `f2Form i j`, `i < j`, are linearly independent.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.linearIndependent_f2Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#linear-independent-f2-form).

## Patterson's f2 basis spans the f-statistic space

Patterson's `f2` basis: the forms `f2Form i j`, `i < j`, span `V_F`, i.e. every
f-statistic is a linear combination of the `f2 Pᵢ Pⱼ`, `i < j`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.span_f2Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#span-f2-form).

## Linear independence of Patterson's f3 basis

Patterson's `f3` basis with base population `o`: the forms `f3Form o i j` with
`i ≤ j`, `i ≠ o`, `j ≠ o` are linearly independent.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.linearIndependent_f3Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#linear-independent-f3-form).

## Patterson's f3 basis spans the f-statistic space

Patterson's `f3` basis with base population `o`: the forms `f3Form o i j` with
`i ≤ j`, `i ≠ o`, `j ≠ o` span `V_F`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.span_f3Form`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#span-f3-form).

## Dimension of the f-statistic space is n choose 2

The f-statistics of `n` populations span a space of dimension `n choose 2`. (A linear order
on the populations, used to index the `f2` basis, is chosen in the proof.)

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsBasis.finrank_fSpace`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsBasis.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html#finrank-f-space).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Basis theorem for f-statistics](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/basis-theorem-for-f-statistics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-structure/basis-theorem-for-f-statistics)
