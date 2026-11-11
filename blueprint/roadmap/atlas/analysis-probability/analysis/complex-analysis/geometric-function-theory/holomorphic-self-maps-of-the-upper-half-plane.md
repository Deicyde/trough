---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.UpperHalfPlaneSchwarzLemmaWanted.norm_le_norm_cayley_of_upperHalfPlane_bounded_vanishing_at_I, MathlibExt.Analysis.Complex.UpperHalfPlaneSelfMapDerivBoundWanted.norm_deriv_I_le_sqrt_three_halves_of_mapsTo_upperHalfPlane, MathlibExt.Analysis.Complex.UpperHalfPlaneSelfMapIterateConvergesWanted.tendsto_iterate_two_mul_I_of_fixed_I, MathlibExt.Analysis.Complex.UpperHalfPlaneSelfMapSurjectiveWanted.image_upperHalfPlane_eq_of_real_on_real
statement: formalized
---

# Holomorphic self-maps of the upper half-plane

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane/index.html).

## Schwarz lemma on the upper half-plane

Let
$\mathbb{H}=\{z\in\mathbb{C} : \mathrm{Im}\,z>0\}$ be the upper half-plane, and let $F$ be a
complex function that is holomorphic on $\mathbb{H}$, satisfies $|F(z)|\le 1$ for every
$z\in\mathbb{H}$, and vanishes at $i$. Then for every $z\in\mathbb{H}$,

$$|F(z)|\le\left|\frac{z-i}{z+i}\right|.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l1_20`.

Stated but not proved: `MathlibExt.Analysis.Complex.UpperHalfPlaneSchwarzLemmaWanted.norm_le_norm_cayley_of_upperHalfPlane_bounded_vanishing_at_I` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/UpperHalfPlaneSchwarzLemmaWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/UpperHalfPlaneSchwarzLemmaWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane/index.html#norm-le-norm-cayley-of-upper-half-plane).

## Derivative bound at $i$ for a self-map of the upper half-plane

Let
$\mathbb{H}=\{z\in\mathbb{C} : \mathrm{Im}\,z>0\}$ be the upper half-plane, and let $f$ be a
complex function that is holomorphic on $\mathbb{H}$, maps $\mathbb{H}$ into $\mathbb{H}$, and
satisfies $f(i)=e^{2\pi i/3}$. Then $|f'(i)|\le\sqrt{3/2}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_62`.

Stated but not proved: `MathlibExt.Analysis.Complex.UpperHalfPlaneSelfMapDerivBoundWanted.norm_deriv_I_le_sqrt_three_halves_of_mapsTo_upperHalfPlane` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/UpperHalfPlaneSelfMapDerivBoundWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/UpperHalfPlaneSelfMapDerivBoundWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane/index.html#norm-deriv-i-le-sqrt-three-halves-of-map).

## Iterates of a self-map of the upper half-plane fixing $i$

Let
$\mathbb{H}=\{z\in\mathbb{C} : \mathrm{Im}\,z>0\}$ be the upper half-plane, and let $f$ be a
complex function that is holomorphic on $\mathbb{H}$, maps $\mathbb{H}$ into $\mathbb{H}$, and
satisfies $f(i)=i$ and $f(2i)=\frac{15}{8}i$. Then the iterates $f^{\circ n}(2i)$ converge to $i$
as $n\to\infty$, where $f^{\circ n}$ is the $n$-fold composite of $f$ with itself.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_34`.

Stated but not proved: `MathlibExt.Analysis.Complex.UpperHalfPlaneSelfMapIterateConvergesWanted.tendsto_iterate_two_mul_I_of_fixed_I` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/UpperHalfPlaneSelfMapIterateConvergesWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/UpperHalfPlaneSelfMapIterateConvergesWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane/index.html#tendsto-iterate-two-mul-i-of-fixed-i).

## Surjectivity for half-plane self-maps that are real on the real axis

Let
$\mathbb{C}_{+} = \{z \in \mathbb{C} : \operatorname{Im} z > 0\}$ be the open upper half-plane and
$\overline{\mathbb{C}_{+}} = \{z \in \mathbb{C} : \operatorname{Im} z \ge 0\}$ the closed one. Let
$f : \mathbb{C} \to \mathbb{C}$ be continuous on $\overline{\mathbb{C}_{+}}$ with
$f(\overline{\mathbb{C}_{+}}) \subseteq \overline{\mathbb{C}_{+}}$, suppose $f(x)$ is real for
every real $x$, and suppose $f$ is holomorphic on $\mathbb{C}_{+}$ and not constant on
$\mathbb{C}_{+}$. Then $f(\mathbb{C}_{+}) = \mathbb{C}_{+}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_71`.

Stated but not proved: `MathlibExt.Analysis.Complex.UpperHalfPlaneSelfMapSurjectiveWanted.image_upperHalfPlane_eq_of_real_on_real` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/UpperHalfPlaneSelfMapSurjectiveWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/UpperHalfPlaneSelfMapSurjectiveWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane/index.html#image-upper-half-plane-eq-of-real-on-rea).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Holomorphic self-maps of the upper half-plane](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-self-maps-of-the-upper-half-plane)
