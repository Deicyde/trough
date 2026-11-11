---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.StripBoundedHolomorphicGrowthWanted.D, MathlibExt.Analysis.Complex.StripBoundedHolomorphicGrowthWanted.norm_le_two_div_pi_mul_log_of_abs_re_lt_one
statement: formalized
---

# Holomorphic maps from the disc into a strip

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-maps-from-the-disc-into-a-strip/index.html).

## The open unit disc $D$

The set $D=\{z\in\mathbb{C}:|z|<1\}$ is the open disc of radius $1$
about $0$.

Formalized by `MathlibExt.Analysis.Complex.StripBoundedHolomorphicGrowthWanted.D`, an abbreviation declared in [WantedExt/Analysis/Complex/StripBoundedHolomorphicGrowthWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/StripBoundedHolomorphicGrowthWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-maps-from-the-disc-into-a-strip/index.html#d).

## Growth bound for holomorphic maps from the unit disc into a vertical strip

Let
$D=\{z:|z|<1\}\subset\mathbb{C}$ be the unit disk and $g:D\to\mathbb{C}$ be a holomorphic
function such that $g(0)=0$ and $|\operatorname{Re} g(z)|<1$ for any $z\in D$. Then for any
$z\in D$,
\[
|g(z)|\le \frac{2}{\pi}\log\frac{1+|z|}{1-|z|}.
\]

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_86`.

Stated but not proved: `MathlibExt.Analysis.Complex.StripBoundedHolomorphicGrowthWanted.norm_le_two_div_pi_mul_log_of_abs_re_lt_one` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/StripBoundedHolomorphicGrowthWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/StripBoundedHolomorphicGrowthWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-maps-from-the-disc-into-a-strip/index.html#norm-le-two-div-pi-mul-log-of-abs-re-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Holomorphic maps from the disc into a strip](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-maps-from-the-disc-into-a-strip/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-maps-from-the-disc-into-a-strip)
