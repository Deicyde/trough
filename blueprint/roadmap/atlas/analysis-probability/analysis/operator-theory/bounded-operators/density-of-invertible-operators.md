---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook173Wanted.ScottishBookProblem173Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook173Wanted.eidelheit173_refuted
statement: formalized
---

# Density of invertible operators

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/density-of-invertible-operators/index.html).

## Scottish Book Problem 173

Eidelheit's claim that for every real Banach space $E$, the
bounded linear operators $E \to E$ that have a bounded linear two-sided inverse are dense, for
the operator norm, in the space of all bounded linear operators on $E$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook173Wanted.ScottishBookProblem173Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook173Wanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook173Wanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/density-of-invertible-operators/index.html#scottish-book-problem173-claim).

## Negative answer to Scottish Book Problem 173

Eidelheit's claim in Problem 173 is false:
there is a real Banach space $E$ in which the bounded linear operators $E \to E$ that have a
bounded linear two-sided inverse are not dense, for the operator norm, in the space of all
bounded linear operators on $E$.

For instance, in an infinite-dimensional Hilbert space the invertible operators are not dense,
by the Fredholm-index obstruction: the unilateral shift cannot be approximated by invertible
operators.

## Sources

- M. Eidelheit, Problem 173 of the Scottish Book; see P. Halmos, A Hilbert Space Problem Book, Problem 109.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook173Wanted.eidelheit173_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook173Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook173Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/density-of-invertible-operators/index.html#eidelheit173-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Density of invertible operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/density-of-invertible-operators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/bounded-operators/density-of-invertible-operators)
