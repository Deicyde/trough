---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.Rn, MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.ClosedUnitBall, MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.IsRadial, MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.exists_eLpNorm_le_sobolev_of_radial_of_tsupport_subset_compl_closedBall
statement: formalized
---

# Radial Sobolev embedding

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/radial-sobolev-embedding/index.html).

## Real $n$-space with the Euclidean norm

For a natural number $n$, $\mathbb{R}^n$ denotes the
$n$-dimensional real Euclidean space: real $n$-tuples with the Euclidean inner product and norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.Rn`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/radial-sobolev-embedding/index.html#rn).

## Closed unit ball of $\mathbb{R}^n$

For a natural number $n$, the closed unit ball of
$\mathbb{R}^n$ is the set $\{x \in \mathbb{R}^n : \|x\| \le 1\}$, where $\|\cdot\|$ is the Euclidean
norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.ClosedUnitBall`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/radial-sobolev-embedding/index.html#closed-unit-ball).

## Radial functions on $\mathbb{R}^n$

A function $f \colon \mathbb{R}^n \to \mathbb{R}$ is
radial if $f(x) = f(y)$ for all $x, y \in \mathbb{R}^n$ with $\|x\| = \|y\|$, where $\|\cdot\|$ is
the Euclidean norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.IsRadial`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/radial-sobolev-embedding/index.html#is-radial).

## Radial Sobolev embedding outside the unit ball

Let $n \ge 2$, let $B$ be the closed unit
ball of $\mathbb{R}^n$, and let $1 < p < 2$ and $p \le q \le \infty$. Then there is a constant
$C > 0$ such that every radial function $f \colon \mathbb{R}^n \to \mathbb{R}$ that has compact
support, whose closed support is contained in $\mathbb{R}^n \setminus B$, and which is $C^\infty$
on $\mathbb{R}^n \setminus B$, satisfies

$$\|f\|_{L^q} \le C \left( \|f\|_{L^p} + \big\| |Df| \big\|_{L^p} \right),$$

where the norms are taken with respect to Lebesgue measure and $|Df(x)|$ is the operator norm of
the derivative of $f$ at $x$.

Smoothness here means $C^\infty$. The source's formal statement asked for real-analyticity
instead, which makes the claim vacuous: an analytic, radial, compactly supported $f$ vanishes
outside the ball.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_80`, with the change above.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.RadialSobolevExteriorBallWanted.exists_eLpNorm_le_sobolev_of_radial_of_tsupport_subset_compl_closedBall` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/RadialSobolevExteriorBallWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/radial-sobolev-embedding/index.html#exists-e-lp-norm-le-sobolev-of-radial-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radial Sobolev embedding](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/radial-sobolev-embedding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/function-spaces/radial-sobolev-embedding)
