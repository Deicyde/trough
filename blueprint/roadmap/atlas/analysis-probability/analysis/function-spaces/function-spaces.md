---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.AgmonInequalitySchwartzLineWanted.exists_norm_toLp_top_le_mul_sqrt_norm_toLp_two_mul_sqrt_deriv, MathlibExt.Analysis.FunctionalAnalysis.ClosedL2SubspaceOfContinuousFiniteDimWanted.finiteDimensional_of_isClosed_of_le_range_toLp, MathlibExt.Analysis.FunctionalAnalysis.EhrlingInequalityWanted.ehrling_inequality, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook87Wanted.nonlinearInterpolationLp, MathlibExt.Analysis.FunctionalAnalysis.SobolevTraceR3PlaneBoundedWanted.exists_bound_integral_sq_trace_of_integral_sq_add_fderiv_sq_le_one, MathlibExt.Analysis.FunctionalAnalysis.YoungConvolutionSharpWanted.exists_eLpNorm_convolution_gt_one_sub_mul, MathlibExt.Analysis.FunctionalAnalysis.WeightedLadyzhenskayaPlaneWanted.exists_const_integral_pow_four_mul_weight_le
statement: formalized
---

# Function spaces and Sobolev inequalities: its own results

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html).

L^p and Sobolev spaces of functions: embeddings (Morrey, Rellich, radial, trace), Ehrling, Agmon, Ladyzhenskaya, Gagliardo–Nirenberg and weighted Hardy–Sobolev inequalities, sup-norm bounds by H¹ energy, L^p limits and weak convergence in L^p.

## Agmon's inequality on the line

There is a constant $C > 0$ such that every real-valued
Schwartz function $f \colon \mathbb{R} \to \mathbb{R}$ satisfies

$$\|f\|_{L^\infty} \le C \, \|f\|_{L^2}^{1/2} \, \|f'\|_{L^2}^{1/2},$$

where $f'$ is the derivative of $f$ and the $L^\infty$ and $L^2$ norms are taken with respect to
Lebesgue measure on $\mathbb{R}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_94`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.AgmonInequalitySchwartzLineWanted.exists_norm_toLp_top_le_mul_sqrt_norm_toLp_two_mul_sqrt_deriv` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/AgmonInequalitySchwartzLineWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/AgmonInequalitySchwartzLineWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#exists-norm-to-lp-top-le-mul-sqrt-norm-t).

## Closed subspaces of $L^2((0,1))$ inside $C((0,1))$ are finite-dimensional

Let $H$ be a
closed linear subspace of the real space $L^2([0,1])$ with respect to Lebesgue measure, and
suppose that every element of $H$ is the class of a continuous function $[0,1] \to \mathbb{R}$.
Then $H$ is finite-dimensional.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_11`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ClosedL2SubspaceOfContinuousFiniteDimWanted.finiteDimensional_of_isClosed_of_le_range_toLp` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ClosedL2SubspaceOfContinuousFiniteDimWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ClosedL2SubspaceOfContinuousFiniteDimWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#finite-dimensional-of-is-closed-of-le-ra).

## Ehrling's inequality

Let $X$, $Y$, $Z$ be real Banach spaces, let $i \colon X \to Y$ be an
injective compact bounded linear operator, and let $j \colon Y \to Z$ be an injective bounded
linear operator. Then for every $\varepsilon > 0$ there is $C_\varepsilon > 0$ such that
$\|i(u)\|_Y \le \varepsilon \|u\|_X + C_\varepsilon \|j(i(u))\|_Z$ for all $u \in X$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Normed linear spaces and Banach spaces; Banach lattices), problem `ma_proofbench_l2_36`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.EhrlingInequalityWanted.ehrling_inequality` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/EhrlingInequalityWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/EhrlingInequalityWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#ehrling-inequality).

## Nonlinear interpolation of Lipschitz maps on Lebesgue spaces (Scottish Book Problem 87)

Let $\mu$ be Lebesgue measure on $[0, 1]$, write $\|f\|_p$ for the $L^p(\mu)$ norm, let
$1 \le \beta < \alpha \le \infty$, and let $U$ map functions $\mathbb{R} \to \mathbb{R}$ to
functions $\mathbb{R} \to \mathbb{R}$. Suppose that $U$ maps $L^\beta(\mu)$ into $L^\beta(\mu)$;
that there is $L \ge 0$ with $\|Ux - Uy\|_\beta \le L \|x - y\|_\beta$ for all
$x, y \in L^\beta(\mu)$; and that there is $M_\alpha \ge 0$ such that every $x \in L^\alpha(\mu)$
has $Ux \in L^\alpha(\mu)$ and $\|Ux\|_\alpha \le M_\alpha \|x\|_\alpha$. Then for every $\gamma$
with $\beta < \gamma < \alpha$ there is $M_\gamma \ge 0$ such that every $x \in L^\gamma(\mu)$
has $Ux \in L^\gamma(\mu)$ and $\|Ux\|_\gamma \le M_\gamma \|x\|_\gamma$.

## Sources

- S. Banach, Problem 87 of the Scottish Book; affirmative solution by L. Maligranda, commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015). The linear case follows from the Riesz interpolation theorem, and Banach showed the case `α = ∞`; Maligranda's solution covers the nonlinear case as stated here, with `α = ⊤` allowed.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook87Wanted.nonlinearInterpolationLp` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook87Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook87Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#nonlinear-interpolation-lp).

## Sobolev trace bound on the plane $z = 0$ in $\mathbb{R}^3$

Let $(f_n)_{n \in \mathbb{N}}$
be a sequence of continuously differentiable functions $\mathbb{R}^3 \to \mathbb{R}$, where
$\mathbb{R}^3$ has coordinates $(x, y, z)$ and the max norm. For $p \in \mathbb{R}^3$ write
$\|Df_n(p)\|$ for the operator norm of the derivative of $f_n$ at $p$, which equals
$|\partial_x f_n(p)| + |\partial_y f_n(p)| + |\partial_z f_n(p)|$, the sum of the absolute values
of the partial derivatives. Suppose that for every $n$ the function
$p \mapsto |f_n(p)|^2 + \|Df_n(p)\|^2$ is Lebesgue integrable on $\mathbb{R}^3$ with integral at
most $1$. Then there is a constant $C \ge 0$ such that for every $n$ the function
$(x, y) \mapsto |f_n(x, y, 0)|^2$ is Lebesgue integrable on $\mathbb{R}^2$ with integral at most
$C$.

Since $\|Df_n(p)\|$ is at least the Euclidean length $|\nabla f_n(p)|$ of the gradient, the
hypothesis implies the bound $\int_{\mathbb{R}^3} (|\nabla f_n|^2 + |f_n|^2) \le 1$ of the source
problem; conversely, if $f_n$ satisfies that bound, then $f_n / \sqrt{3}$ satisfies the hypothesis.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_56`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.SobolevTraceR3PlaneBoundedWanted.exists_bound_integral_sq_trace_of_integral_sq_add_fderiv_sq_le_one` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/SobolevTraceR3PlaneBoundedWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/SobolevTraceR3PlaneBoundedWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#exists-bound-integral-sq-trace-of-integr).

## The constant in Young's $L^1$–$L^p$ convolution inequality cannot be lowered

Let
$1 \le p \le \infty$ and $\varepsilon > 0$. Then there exist real-valued functions
$f \in L^1(\mathbb{R})$ and $g \in L^p(\mathbb{R})$ such that

$$
\|f * g\|_p > (1 - \varepsilon) \|f\|_1 \|g\|_p,
$$

where $(f * g)(x) = \int_{\mathbb{R}} f(t)\, g(x - t)\, dt$ and all norms are taken with
respect to Lebesgue measure.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l1_45`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.YoungConvolutionSharpWanted.exists_eLpNorm_convolution_gt_one_sub_mul` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/YoungConvolutionSharpWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/YoungConvolutionSharpWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#exists-e-lp-norm-convolution-gt-one-sub).

## Weighted Ladyzhenskaya inequality in the plane

There is a constant $C > 0$ such that
for every $C^1$ function $\omega : \mathbb{R}^2 \to \mathbb{R}$ with $\omega(x) > 0$ for all $x$
and $\|\nabla\omega/\omega\|_{L^\infty(\mathbb{R}^2)} \le 1$, and every smooth compactly supported
function $u : \mathbb{R}^2 \to \mathbb{R}$,

$$
\int_{\mathbb{R}^2} u^4 \omega \le C \|u\|_{L^2(\mathbb{R}^2)}^2
\int_{\mathbb{R}^2} \left(|\nabla u|^2 + |u|^2\right) \omega.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_48`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.WeightedLadyzhenskayaPlaneWanted.exists_const_integral_pow_four_mul_weight_le` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/WeightedLadyzhenskayaPlaneWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/WeightedLadyzhenskayaPlaneWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html#exists-const-integral-pow-four-mul-weigh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Function spaces and Sobolev inequalities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/function-spaces)
