---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.SchwarzPick.schwarzPick, MathlibExt.Analysis.Complex.SchwarzPickDerivBoundWanted.norm_deriv_div_one_sub_sq_le_of_mapsTo_unitBall
statement: formalized
---

# Schwarz–Pick lemma

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/schwarz-pick-lemma/index.html).

## Schwarz–Pick lemma

Let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic on the open unit disc
$\mathbb{D} = \{z : |z| < 1\}$ and map $\mathbb{D}$ into itself. Then for all $z, w \in \mathbb{D}$,
$|f(z) - f(w)| / |1 - \overline{f(w)}\, f(z)| \le |z - w| / |1 - \bar w z|$.

## Sources

- Schwarz–Pick lemma, G. Pick (1916), building on Schwarz's lemma; see Ahlfors; Lean is holomorphic self-map of disc pseudo-hyperbolic distance nonincreasing inequality with star conj.

Formalized by `MathlibExt.Analysis.Complex.SchwarzPick.schwarzPick`, a theorem declared in [MathlibExt/Analysis/Complex/SchwarzPick.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/SchwarzPick.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/schwarz-pick-lemma/index.html#schwarz-pick).

## Schwarz–Pick lemma, derivative form

Let $\mathbb{D}=\{z\in\mathbb{C}:|z|<1\}$ be the open
unit disc. If $f:\mathbb{D}\to\mathbb{D}$ is holomorphic, then

\[
\frac{|f'(z)|}{1-|f(z)|^2}\le \frac{1}{1-|z|^2}\qquad\text{for all } z\in\mathbb{D}.
\]

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l1_86`.

Stated but not proved: `MathlibExt.Analysis.Complex.SchwarzPickDerivBoundWanted.norm_deriv_div_one_sub_sq_le_of_mapsTo_unitBall` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/SchwarzPickDerivBoundWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/SchwarzPickDerivBoundWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/schwarz-pick-lemma/index.html#norm-deriv-div-one-sub-sq-le-of-maps-to).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schwarz–Pick lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/schwarz-pick-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/schwarz-pick-lemma)
