---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.DiskToUpperHalfPlaneCayleyWanted.bijOn_cayley_ball_upperHalfPlane, MathlibExt.Analysis.Complex.BlochWanted.bloch, MathlibExt.Analysis.Complex.HolomorphicDiskDiameterDerivBoundWanted.two_mul_norm_deriv_le_ediam_image_ball, MathlibExt.Analysis.Complex.NoProperHolomorphicMapUnitDiscWanted.not_exists_differentiableOn_ball_isCompact_preimage, MathlibExt.Analysis.Complex.UnimodularBoundaryImageContainsDiscWanted.ball_subset_image_of_norm_eq_one_on_sphere
statement: formalized
---

# Geometric function theory: its own results

5 results, 1 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html).

Conformal and univalent maps: Riemann mapping, Koebe and Bloch theorems, Schwarz–Pick and half-plane self-maps, starlike and univalent coefficient problems, Loewner equation, holomorphic motions.

## A Möbius map from the unit disk onto the upper half-plane

The function
$\phi(z) = i\,\frac{1-z}{1+z}$ maps the open unit disk $D = \{z \in \mathbb{C} : |z| < 1\}$
bijectively onto the upper half-plane $U = \{z \in \mathbb{C} : \operatorname{Im} z > 0\}$: it
maps $D$ into $U$, it is injective on $D$, and every point of $U$ is $\phi(z)$ for some $z \in D$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l1_63`.

Stated but not proved: `MathlibExt.Analysis.Complex.DiskToUpperHalfPlaneCayleyWanted.bijOn_cayley_ball_upperHalfPlane` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/DiskToUpperHalfPlaneCayleyWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/DiskToUpperHalfPlaneCayleyWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html#bij-on-cayley-ball-upper-half-plane).

## Bloch's theorem

There is a constant $B > 0$ with the following property. Let
$f : \mathbb{C} \to \mathbb{C}$ be holomorphic on the open unit disc $\mathbb{D} = \{z : |z| < 1\}$
with $f'(0) = 1$. Then there are an open connected set $V \subseteq \mathbb{D}$ and a point
$w \in \mathbb{C}$ such that $f$ is injective on $V$ and $f(V)$ is the open disc
$\{\zeta : |\zeta - w| < B\}$.

## Sources

- A. Bloch, Les théorèmes de M. Valiron sur les fonctions entières et la théorie de l'uniformisation, Ann. Fac. Sci. Toulouse 17 (1925), 1–22, DOI 10.5802/afst.335; see Ahlfors, Complex Analysis, Univalent Functions; Lean is universal B > 0 exact schlicht disc f '' V = ball w B for open connected V, stronger than Landau.

Formalized by `MathlibExt.Analysis.Complex.BlochWanted.bloch`, a theorem declared in [MathlibExt/Analysis/Complex/Bloch.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Bloch.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html#bloch).

## Diameter bound for the derivative at the center of the disc

Let $D$ be the open unit disc
in $\mathbb{C}$ and let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic on $D$. Then the diameter
$d = \sup_{z,w \in D} |f(z) - f(w)|$ of the image $f(D)$, which may be $+\infty$, satisfies
$2|f'(0)| \le d$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_78`.

Stated but not proved: `MathlibExt.Analysis.Complex.HolomorphicDiskDiameterDerivBoundWanted.two_mul_norm_deriv_le_ediam_image_ball` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/HolomorphicDiskDiameterDerivBoundWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/HolomorphicDiskDiameterDerivBoundWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html#two-mul-norm-deriv-le-ediam-image-ball).

## No proper holomorphic map from the unit disc to the complex plane

Let
$\Delta := \{z\in\mathbb{C}\mid |z|<1\}$ be the unit disc in the complex plane. There is no proper
holomorphic map $f:\Delta\to\mathbb{C}$, where proper means that the preimage under $f$ of every
compact subset of $\mathbb{C}$ is a compact subset of $\Delta$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_41`.

Stated but not proved: `MathlibExt.Analysis.Complex.NoProperHolomorphicMapUnitDiscWanted.not_exists_differentiableOn_ball_isCompact_preimage` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/NoProperHolomorphicMapUnitDiscWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/NoProperHolomorphicMapUnitDiscWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html#not-exists-differentiable-on-ball-is-com).

## Nonconstant holomorphic functions of modulus one on the unit circle cover the unit disc

Let $U\subseteq\mathbb{C}$ be a connected open set containing the closed unit disc
$\{z:|z|\le 1\}$, and let $f:\mathbb{C}\to\mathbb{C}$ be holomorphic on $U$ and non-constant on
$U$. If $|f(z)|=1$ whenever $|z|=1$, then every $w$ with $|w|<1$ is $f(z)$ for some $z\in U$; that
is, $f(U)$ contains the open unit disc.

The connectedness of $U$ is added to the source statement, which asks only for an open set: for
$U=\{z:|z|<2\}\cup\{z:|z-10|<1\}$, with $f=1$ on the first disc and $f(z)=z$ on the second, $f$
is non-constant and holomorphic on $U$ and has modulus one on the unit circle, but $f(U)$ does not
contain the open unit disc.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_25`, with the change above.

Stated but not proved: `MathlibExt.Analysis.Complex.UnimodularBoundaryImageContainsDiscWanted.ball_subset_image_of_norm_eq_one_on_sphere` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/UnimodularBoundaryImageContainsDiscWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/UnimodularBoundaryImageContainsDiscWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html#ball-subset-image-of-norm-eq-one-on-sphe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geometric function theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory)
