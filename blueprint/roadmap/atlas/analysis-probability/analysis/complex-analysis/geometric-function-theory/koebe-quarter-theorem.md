---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.KoebeQuarterWanted.koebe_quarter, MathlibExt.Analysis.Complex.UnivalentImageBoundaryDistLeOneWanted.infDist_zero_frontier_image_ball_le_one
statement: formalized
---

# Koebe quarter theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/koebe-quarter-theorem/index.html).

## Koebe quarter theorem

Let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic and injective on the
open unit disk $\mathbb{D} = \{z : |z| < 1\}$, with $f(0) = 0$ and $f'(0) = 1$. Then the image
$f(\mathbb{D})$ contains the open disk $\{w : |w| < 1/4\}$.

## Sources

- Koebe quarter theorem, conjectured by P. Koebe in 1907 and proved by L. Bieberbach, Sitzungsberichte der Preussischen Akademie der Wissenschaften (1916), 940–955; see Pommerenke, Univalent Functions; Lean is normalized schlicht inclusion ball (0:ℂ) (1/4) ⊆ f '' ball 0 1.

Formalized by `MathlibExt.Analysis.Complex.KoebeQuarterWanted.koebe_quarter`, a theorem declared in [MathlibExt/Analysis/Complex/KoebeQuarter.lean, line 2250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/KoebeQuarter.lean#L2250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/koebe-quarter-theorem/index.html#koebe-quarter).

## The boundary of a normalized univalent image of the disc is within distance one of the origin

**The boundary of a normalized univalent image of the disc is within distance one of the
origin.** Let $D=\{z\in\mathbb{C}:|z|<1\}$ be the unit disk and suppose $f:D\to\mathbb{C}$ is an
injective holomorphic function with $f(0)=0$ and $f'(0)=1$. Let $\Omega=f(D)$ and let
$\partial\Omega$ be its boundary. Then
$\mathrm{dist}(0,\partial\Omega)=\inf\{|z|:z\in\partial\Omega\}\le 1$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_18`.

Stated but not proved: `MathlibExt.Analysis.Complex.UnivalentImageBoundaryDistLeOneWanted.infDist_zero_frontier_image_ball_le_one` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/UnivalentImageBoundaryDistLeOneWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/UnivalentImageBoundaryDistLeOneWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/koebe-quarter-theorem/index.html#inf-dist-zero-frontier-image-ball-le-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Koebe quarter theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/koebe-quarter-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/koebe-quarter-theorem)
