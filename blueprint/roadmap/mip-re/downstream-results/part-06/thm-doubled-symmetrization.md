---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.Co.ProjStrat.lowIndividualDegreeFailureProbability, MIPRE.LIDT.Co.ProjStrat.PassesLowIndividualDegreeTest, MIPRE.LIDT.Co.Doubling.pairProjMeas, MIPRE.LIDT.Co.Doubling.symmStrat, MIPRE.LIDT.Co.Doubling.symmStrat_axisParallel_eq_roleAverage, MIPRE.LIDT.Co.Doubling.symmStrat_selfConsistency_eq_pointAgreement, MIPRE.LIDT.Co.Doubling.symmStrat_diagonal_eq_roleAverage, MIPRE.LIDT.Co.Doubling.symmStrat_isGood_three_mul
statement: formalized
proof: formalized
---

# Symmetrization after the bridge

Let $S$ be a projective strategy for the low individual degree test whose two players act in a finite pair $M$ with a unit state: for each player, projective point measurements and axis-parallel and diagonal-line measurements, the line measurements covariant under reparametrization. Pairing each measurement of the first player with the corresponding measurement of the second, componentwise in $\mathcal{P}$, gives a symmetric strategy $S_D$ in the doubled model $D(M)$ (Definition [The doubled model](../part-05/def-doubled-model.md)), covariant componentwise. Its failure probabilities are the role averages of those of $S$: the axis-parallel and diagonal-line tests of $S_D$ fail with the average, over the two assignments of the line and point roles to the players, of the corresponding failure probability of $S$; and its self-consistency test fails with the probability that the two players' point measurements disagree. Hence, if $S$ fails the test with probability at most $\varepsilon$, then $S_D$ is $(3\varepsilon, 3\varepsilon, 3\varepsilon)$-good, in the sense of Lemma [Commutativity of points, in a symmetric model](../part-05/lem-co-commutativity-points.md). These are the constants of the vendored role-register symmetrization, which this replaces.

## Depends on

- [The role average in the doubled model](lem-doubled-model-role-average.md)

## Proof

Each failure probability of $S_D$ is a bipartite consistency defect of $D(M)$ between two paired families, so it is the average of the two two-space defects of $M$ (Lemma [The role average in the doubled model](lem-doubled-model-role-average.md)). The paired families have the families of $S$ as components. The failure probability of $S$ is the mean of the three role averages, which are nonnegative, so each is at most $3\varepsilon$ (`reports/c6b-paper-proofs.md`, Section 4, Theorem D).

## Lean

Formalized as [`MIPRE.LIDT.Co.ProjStrat.lowIndividualDegreeFailureProbability`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ProjStrat.lowIndividualDegreeFailureProbability), [`MIPRE.LIDT.Co.ProjStrat.PassesLowIndividualDegreeTest`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ProjStrat.PassesLowIndividualDegreeTest), [`MIPRE.LIDT.Co.Doubling.pairProjMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.pairProjMeas), [`MIPRE.LIDT.Co.Doubling.symmStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.symmStrat), [`MIPRE.LIDT.Co.Doubling.symmStrat_axisParallel_eq_roleAverage`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.symmStrat_axisParallel_eq_roleAverage), [`MIPRE.LIDT.Co.Doubling.symmStrat_selfConsistency_eq_pointAgreement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.symmStrat_selfConsistency_eq_pointAgreement), [`MIPRE.LIDT.Co.Doubling.symmStrat_diagonal_eq_roleAverage`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.symmStrat_diagonal_eq_roleAverage), [`MIPRE.LIDT.Co.Doubling.symmStrat_isGood_three_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.symmStrat_isGood_three_mul).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3503](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3503)
