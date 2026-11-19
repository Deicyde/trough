---
declaration: definition
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.wordsUpTo, MIPRE.Tailored.Sofic.Measure.stageW, MIPRE.Tailored.Sofic.Measure.stageD, MIPRE.Tailored.Sofic.Measure.goodP, MIPRE.Tailored.Sofic.Measure.allVecs, MIPRE.Tailored.Sofic.Measure.invErr, MIPRE.Tailored.Sofic.Measure.Feasible, MIPRE.Tailored.Sofic.Measure.numG, MIPRE.Tailored.Sofic.Measure.maxNum, MIPRE.Tailored.Sofic.Measure.Covers, MIPRE.Tailored.Sofic.Measure.upperSeq
statement: formalized
---

# Pseudo-subgroup polytopes, discretized; I:927, I:1105

At stage $t$ take the words of length at most $t+2$ in the first $n+t$ letters, and the grid points of weight $M = P \cdot 2^t$ on its $P$ patterns. A grid point is feasible when every pattern of positive weight is locally closed (contains the empty word, closed under cancelling a pair, deleting a letter beyond the $n$ generators, and $u, v \mapsto u v^{-1}$ within the stage) and conjugation by each generator moves it by at most $4P$ in $\ell^1$. The upper value at stage $t$ is the best value of a feasible point, plus $2/2^t$, rounded up to a multiple of $2^{-t}$. This replaces the paper's pseudo IRS polytope and its linear program by an exhaustive search over a grid, with the invariance relaxed to absorb rounding.

## Depends on

- [Subgroup tests and their sofic value; I:439–520](../part-01/def-subgroup-test.md)
- [The associated subgroup test; I:2086](../part-01/def-assoc-test.md)
- [From word indicators to invariant random subgroups](lem-irs-of-good.md)

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.wordsUpTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.wordsUpTo), [`MIPRE.Tailored.Sofic.Measure.stageW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.stageW), [`MIPRE.Tailored.Sofic.Measure.stageD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.stageD), [`MIPRE.Tailored.Sofic.Measure.goodP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.goodP), [`MIPRE.Tailored.Sofic.Measure.allVecs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.allVecs), [`MIPRE.Tailored.Sofic.Measure.invErr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.invErr), [`MIPRE.Tailored.Sofic.Measure.Feasible`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.Feasible), [`MIPRE.Tailored.Sofic.Measure.numG`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.numG), [`MIPRE.Tailored.Sofic.Measure.maxNum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.maxNum), [`MIPRE.Tailored.Sofic.Measure.Covers`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.Covers), [`MIPRE.Tailored.Sofic.Measure.upperSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.upperSeq).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 492](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L492)
