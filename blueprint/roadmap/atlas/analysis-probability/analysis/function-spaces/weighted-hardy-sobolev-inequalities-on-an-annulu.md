---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.R2, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.B, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.Omega1, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.Omega2, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.phi, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.exists_eLpNorm_le_weighted_grad_add_outer_annulus, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.R2, MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.B
statement: formalized
---

# Weighted Hardy–Sobolev inequalities on an annulus

13 results, 11 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html).

## Euclidean plane

The Euclidean plane.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.R2`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#r2).

## Open discs about the origin for the annulus Hardy inequality

For a real number $r$,
$B_r = \{x \in \mathbb{R}^2 : |x| < r\}$ is the open disc of radius $r$ about the origin of the
Euclidean plane $\mathbb{R}^2$, where $|x|$ is the Euclidean norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.B`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#b).

## Full annulus of the weighted Hardy inequality

$\Omega_1 = B_3 \setminus \overline{B}_1$,
where $B_r$ is the open disc of radius $r$ about the origin of the Euclidean plane $\mathbb{R}^2$
and $\overline{B}_1$ is the closure of $B_1$; that is, writing $|x|$ for the Euclidean norm,
$\Omega_1$ is the annulus $\{x \in \mathbb{R}^2 : 1 < |x| < 3\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.Omega1`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#omega1).

## Outer annulus of the weighted Hardy inequality

$\Omega_2 = B_3 \setminus \overline{B}_2$,
where $B_r$ is the open disc of radius $r$ about the origin of the Euclidean plane $\mathbb{R}^2$
and $\overline{B}_2$ is the closure of $B_2$; that is, writing $|x|$ for the Euclidean norm,
$\Omega_2$ is the annulus $\{x \in \mathbb{R}^2 : 2 < |x| < 3\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.Omega2`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#omega2).

## Weight of the annulus Hardy inequality

For $x$ in the Euclidean plane $\mathbb{R}^2$,
$\phi(x) = \max\{|x| - 1, 0\}$, where $|x|$ is the Euclidean norm; this is the distance from $x$
to the closed unit disc.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.phi`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#phi).

## Weighted Hardy inequality on the annulus

For $r > 0$ let $B_r$ be the open disc of
radius $r$ about the origin of $\mathbb{R}^2$, let $|x|$ be the Euclidean norm, and let
$\phi(x) = \max\{|x| - 1, 0\}$ be the distance from $x$ to the closed unit disc. Let
$\Omega_1 = B_3 \setminus \overline{B}_1$ and $\Omega_2 = B_3 \setminus \overline{B}_2$, with
Lebesgue measure. For every real number $p \ge 1$ there is a constant $C > 0$ such that every
function $u \colon \mathbb{R}^2 \to \mathbb{R}$ that is continuously differentiable on $\Omega_1$,
and for which $\|\phi \, |\nabla u|\|_{L^p(\Omega_1)}$ and $\|u\|_{L^p(\Omega_2)}$ are finite,
satisfies

$$\|u\|_{L^p(\Omega_1)} \le C \|\phi \, |\nabla u|\|_{L^p(\Omega_1)} + C \|u\|_{L^p(\Omega_2)}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_77`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedHardyInequalityWanted.exists_eLpNorm_le_weighted_grad_add_outer_annulus` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedHardyInequalityWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#exists-e-lp-norm-le-weighted-grad-add-ou).

## The plane of the critical weighted Sobolev inequality

$\mathbb{R}^2$ denotes the Euclidean
plane, the space of pairs of real numbers with the Euclidean norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.R2`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#r2-2).

## Discs about the origin for the critical weighted Sobolev inequality

For a real number $r$,
$B_r$ is the open disc $\{x \in \mathbb{R}^2 : |x| < r\}$ of radius $r$ about the origin of the
Euclidean plane $\mathbb{R}^2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.B`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#b-2).

## The annulus of the critical weighted Sobolev inequality

Let $B_r$ denote the open disc of
radius $r$ about the origin of the Euclidean plane $\mathbb{R}^2$. The annulus $\Omega_1$ is
$B_3 \setminus \overline{B}_1$, the set of points of $B_3$ outside the closure of $B_1$, that is,
$\Omega_1 = \{x \in \mathbb{R}^2 : 1 < |x| < 3\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.Omega1`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#omega1-2).

## The outer annulus of the critical weighted Sobolev inequality

Let $B_r$ denote the open
disc of radius $r$ about the origin of the Euclidean plane $\mathbb{R}^2$. The outer annulus
$\Omega_2$ is $B_3 \setminus \overline{B}_2$, the set of points of $B_3$ outside the closure of
$B_2$, that is, $\Omega_2 = \{x \in \mathbb{R}^2 : 2 < |x| < 3\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.Omega2`, an abbreviation declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#omega2-2).

## The weight of the critical weighted Sobolev inequality

For $x$ in the Euclidean plane
$\mathbb{R}^2$, the weight is $\phi(x) = \max\{|x| - 1, 0\}$, the distance from $x$ to the closed
unit disc.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.phi`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#phi-2).

## Sobolev conjugate exponent in dimension two

For a real number $p$, the Sobolev conjugate
exponent is $p^* = 2p/(2 - p)$ (at $p = 2$, where the denominator vanishes, this is $0$ by the
convention that division by zero gives zero).

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.pStar`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#p-star).

## Critical weighted Sobolev inequality on an annulus

For $r > 0$ let $B_r$ be the open disc
of radius $r$ about the origin in the Euclidean plane $\mathbb{R}^2$, let
$\Omega_1 = B_3 \setminus \overline{B}_1$ and $\Omega_2 = B_3 \setminus \overline{B}_2$, and let
$\phi(x) = \max\{|x| - 1, 0\}$, the distance from $x$ to the closed unit disc. Let $1 \le p < 2$
and $p^* = 2p/(2-p)$. Then there is a real number $C > 0$ such that every function
$u \colon \mathbb{R}^2 \to \mathbb{R}$ that is continuously differentiable on $\Omega_1$ and for
which $\|\phi \nabla u\|_{L^p(\Omega_1)}$ and $\|u\|_{L^p(\Omega_2)}$ are finite satisfies

$$\|\phi u\|_{L^{p^*}(\Omega_1)} \le C\|\phi \nabla u\|_{L^p(\Omega_1)} + C\|u\|_{L^p(\Omega_2)}.$$

Here the norms are taken with respect to Lebesgue measure, $\|\phi \nabla u\|_{L^p(\Omega_1)}$ is
the $L^p(\Omega_1)$ norm of $x \mapsto \phi(x)\,|\nabla u(x)|$, and $\nabla u(x)$ is the derivative
of $u$ at $x$ within $\Omega_1$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_65`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.AnnulusWeightedSobolevCriticalWanted.exists_eLpNorm_phi_mul_le_weighted_grad_add_outer_annulus` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/AnnulusWeightedSobolevCriticalWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html#exists-e-lp-norm-phi-mul-le-weighted-gra).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted Hardy–Sobolev inequalities on an annulus](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/function-spaces/weighted-hardy-sobolev-inequalities-on-an-annulu)
