---
declaration: section
origin: cited
lean: Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.Separable, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.residual, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.norm_sum_smul_le, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.eq_single_of_norm_sum_smul_eq, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun.map_nodup, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun.mem_range, Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun.range_eq
statement: formalized
proof: formalized
---

# Successive projection algorithm

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html).

## Separable data matrix

A separable data matrix: columns `m j` are sub-convex combinations of `r` linearly
independent archetypes `w k`, and every archetype is a column (Gillis–Vavasis Assumption 1).

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.Separable`, a structure declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#separable).

## Residual of a column in the successive projection algorithm

The residual of column `j`: its projection onto the orthogonal complement of the span of
the columns indexed by `S`.

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.residual`, a definition declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#residual).

## Run of the successive projection algorithm

`S` (most recent pick first) is a run of the successive projection algorithm: each pick
maximizes the residual norm given the earlier picks (ties broken arbitrarily).

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun`, a definition declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#is-sparun).

## Norm bound for a sub-convex combination of vectors

Gillis–Vavasis Lemma 1 (`f = ‖·‖²`), bound: a sub-convex combination of vectors of norm
at most `M` has norm at most `M`.

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.norm_sum_smul_le`, a theorem declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#norm-sum-smul-le).

## Equality case of the sub-convex combination norm bound

Gillis–Vavasis Lemma 1 (`f = ‖·‖²`), equality case: for linearly independent vectors of
norm at most `M > 0`, a sub-convex combination of norm `M` is a vertex `w k` with
`‖w k‖ = M`.

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.eq_single_of_norm_sum_smul_eq`, a theorem declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#eq-single-of-norm-sum-smul-eq).

## SPA recovers archetypes

**SPA recovers archetypes** (Gillis–Vavasis Theorem 1, noiseless case): in the first `r`
picks of any SPA run on a separable matrix with `r` archetypes, the picked columns are
pairwise distinct.

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun.map_nodup`, a theorem declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#map-nodup).

## SPA recovers archetypes

**SPA recovers archetypes** (Gillis–Vavasis Theorem 1, noiseless case): each of the first
`r` picks of any SPA run is an archetype.

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun.mem_range`, a theorem declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#mem-range).

## Successive projection finds every archetype after r picks

After exactly `r` picks, SPA has found every archetype.

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.IsSPARun.range_eq`, a theorem declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#range-eq).

## Existence of successive projection runs of every length

SPA runs of every length exist (on a nonempty set of columns).

Formalized by `Cslib.MachineLearning.MatrixFactorization.SuccessiveProjection.exists_isSPARun`, a theorem declared in [CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/MatrixFactorization/SuccessiveProjection.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html#exists-is-sparun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Successive projection algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/unsupervised-learning/successive-projection-algorithm)
