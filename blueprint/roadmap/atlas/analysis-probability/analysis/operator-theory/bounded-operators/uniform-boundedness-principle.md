---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.PointwiseLimitOperatorsJointContinuityWanted.tendsto_apply_of_tendsto_pointwise_of_tendsto, MathlibExt.Analysis.OperatorTheory.WeaklyBoundedOperatorFamilyBoundedWanted.exists_bound_opNorm_of_forall_inner_bounded
statement: formalized
---

# Uniform boundedness principle

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/uniform-boundedness-principle/index.html).

## Pointwise convergent operators converge along convergent sequences

Let $E$ and $F$ be real
Banach spaces, let $(T_n)$ be a sequence of bounded linear operators from $E$ to $F$, and suppose
that for every $x \in E$ the sequence $(T_n x)$ converges to a limit $T x$. Then for every
sequence $x_n \to x$ in $E$ we have $T_n x_n \to T x$ in $F$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Operator theory; General theory of linear operators), problem `ma_proofbench_l1_68`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.PointwiseLimitOperatorsJointContinuityWanted.tendsto_apply_of_tendsto_pointwise_of_tendsto` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/PointwiseLimitOperatorsJointContinuityWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/PointwiseLimitOperatorsJointContinuityWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/uniform-boundedness-principle/index.html#tendsto-apply-of-tendsto-pointwise-of-te).

## Weakly bounded sets of operators are bounded

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $H$ and $K$ be Hilbert spaces over $\mathbb{K}$, and let $Q$ be a set of
bounded linear operators from $H$ to $K$. Suppose $Q$ is weakly bounded: for every $f \in H$
and $g \in K$ there is a real number $\alpha$ such that $|\langle A f, g \rangle| \le \alpha$
for all $A \in Q$. Then $Q$ is bounded in operator norm: there is a real number $M$ such that
$\|A\| \le M$ for all $A \in Q$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_60`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.WeaklyBoundedOperatorFamilyBoundedWanted.exists_bound_opNorm_of_forall_inner_bounded` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/WeaklyBoundedOperatorFamilyBoundedWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OperatorTheory/WeaklyBoundedOperatorFamilyBoundedWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/uniform-boundedness-principle/index.html#exists-bound-op-norm-of-forall-inner-bou).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniform boundedness principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/uniform-boundedness-principle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/bounded-operators/uniform-boundedness-principle)
