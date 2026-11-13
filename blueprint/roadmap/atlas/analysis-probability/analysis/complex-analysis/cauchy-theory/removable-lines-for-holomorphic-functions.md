---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.realAxis, MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.imagAxis, MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.coordAxes, MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.differentiable_of_continuous_of_differentiableOn_compl_coordAxes
statement: formalized
---

# Removable lines for holomorphic functions

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions/index.html).

## Real axis

The real axis is the set $\{z \in \mathbb{C} : \operatorname{Im} z = 0\}$.

Formalized by `MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.realAxis`, a definition declared in [WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions/index.html#real-axis).

## Imaginary axis

The imaginary axis is the set
$\{z \in \mathbb{C} : \operatorname{Re} z = 0\}$.

Formalized by `MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.imagAxis`, a definition declared in [WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions/index.html#imag-axis).

## Coordinate axes

The coordinate axes of $\mathbb{C}$: the union of the real axis and the
imaginary axis.

Formalized by `MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.coordAxes`, a definition declared in [WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions/index.html#coord-axes).

## Continuous functions holomorphic off the coordinate axes are entire

Let
$f : \mathbb{C} \to \mathbb{C}$ be continuous on all of $\mathbb{C}$ and holomorphic on the
complement of the coordinate axes. Then $f$ is holomorphic on all of $\mathbb{C}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_27`.

Stated but not proved: `MathlibExt.Analysis.Complex.ContinuousHolomorphicOffAxesEntireWanted.differentiable_of_continuous_of_differentiableOn_compl_coordAxes` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ContinuousHolomorphicOffAxesEntireWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions/index.html#differentiable-of-continuous-of-differen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Removable lines for holomorphic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/removable-lines-for-holomorphic-functions)
