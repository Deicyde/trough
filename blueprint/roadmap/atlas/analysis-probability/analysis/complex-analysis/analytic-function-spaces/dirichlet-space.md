---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.DirichletSpace.hasSum_div_succ_pow_real, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.hasSum_div_succ_pow_complex, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_sq_dirichlet_coeff, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.summable_dirichletKernel_terms, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.memℓp_dirichletKernel, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletKernel, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletKernel_zero, MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_sq_dirichletKernel_of_ne_zero
statement: formalized
---

# Dirichlet space

33 results, 32 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html).

## Closed form of $\sum r^n/(n+1)$ for real $0<r<1$

**Closed form of $\sum r^n/(n+1)$ for real $0\lt r<1$.** The power series `∑' n, rⁿ / (n + 1)` sums to `-log (1 - r) / r`
for `0 < r < 1`: factor `1 / r` out of the logarithm series.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.hasSum_div_succ_pow_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#has-sum-div-succ-pow-real).

## Closed form of $\sum u^n/(n+1)$ for complex $u$ in the unit disc

The complex form: `∑' n, uⁿ / (n + 1)` sums to `-log (1 - u) / u`
for `u ≠ 0` in the unit disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.hasSum_div_succ_pow_complex`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#has-sum-div-succ-pow-complex).

## Squared norms of the Dirichlet kernel coefficients

The squared norms of the Dirichlet kernel coefficients are
`‖z‖ ^ (2 * n) / (n + 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_sq_dirichlet_coeff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-sq-dirichlet-coeff).

## Square-summability of the Dirichlet kernel coefficients

The Dirichlet kernel coefficients are summable in the `ℓ²` sense:
`∑' n, (‖z‖²)ⁿ / (n + 1)` converges, by comparison with the geometric series.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.summable_dirichletKernel_terms`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#summable-dirichlet-kernel-terms).

## Dirichlet kernel coefficients lie in ℓ²

The Dirichlet kernel coefficients are in `ℓ²` when `z` is in the disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.memℓp_dirichletKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#mem-p-dirichlet-kernel).

## Reproducing kernel of the Dirichlet space

The **Dirichlet kernel** at `z`: the `ℓ²(ℕ, ℂ)` sequence with
coefficients `(conj z)ⁿ / √(n + 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletKernel`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-kernel).

## Dirichlet kernel at the origin is the first basis vector

The Dirichlet kernel at `0` is the first standard basis vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletKernel_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-kernel-zero).

## Squared norm of the Dirichlet kernel away from the origin

The squared norm of the Dirichlet kernel is `-log (1 - ‖z‖²) / ‖z‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_sq_dirichletKernel_of_ne_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-sq-dirichlet-kernel-of-ne-zero).

## Squared norm of the Dirichlet kernel at the origin

The squared norm of the Dirichlet kernel at `0` is `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_sq_dirichletKernel_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-sq-dirichlet-kernel-zero).

## Norm of the Dirichlet kernel away from the origin

The norm of the Dirichlet kernel is `√(-log (1 - ‖z‖²) / ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_dirichletKernel_of_ne_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-dirichlet-kernel-of-ne-zero).

## Norm of the Dirichlet kernel at the origin

The norm of the Dirichlet kernel at `0` is `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_dirichletKernel_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-dirichlet-kernel-zero).

## Dirichlet kernel norm is bounded by the Szegő kernel norm

The Dirichlet kernel norm is bounded by the Hardy kernel norm:
`‖k_z‖² ≤ 1 / (1 - ‖z‖²)`, via `log x ≤ x - 1` at `x = (1 - ‖z‖²)⁻¹`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_sq_dirichletKernel_le_inv`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-sq-dirichlet-kernel-le-inv).

## Point evaluation on the Dirichlet space

Point evaluation on `𝒟(𝔻)`: the inner product with the Dirichlet kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEval`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval).

## Dirichlet-space point evaluation as a Taylor series

Point evaluation is the Taylor series `∑' n, a n * zⁿ / √(n + 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEval_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-eq-tsum).

## Absolute convergence of Taylor series in the Dirichlet space

The Taylor series of a `𝒟` function converges absolutely at every
point of the disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.summable_dirichletEval_terms`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#summable-dirichlet-eval-terms).

## Point evaluation as a bounded functional on the Dirichlet space

Point evaluation as a bounded linear functional on `𝒟(𝔻)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEvalCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-clm).

## Reproducing property of the Dirichlet kernel

The bounded point-evaluation functional acts by the inner product
with the Dirichlet kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEvalCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-clm-apply).

## Norm of Dirichlet-space point evaluation equals the kernel norm

The operator norm of point evaluation is the norm of the kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_dirichletEvalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-dirichlet-eval-clm).

## Closed-form norm of Dirichlet-space point evaluation

The operator norm of point evaluation is `√(-log (1 - ‖z‖²) / ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_dirichletEvalCLM_of_ne_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-dirichlet-eval-clm-of-ne-zero).

## Norm of Dirichlet-space point evaluation at the origin

The operator norm of point evaluation at `0` is `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_dirichletEvalCLM_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-dirichlet-eval-clm-zero).

## Pointwise bound for Dirichlet-space functions

The pointwise bound for `𝒟` functions: `‖f(z)‖ ≤ ‖f‖ * ‖k_z‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.norm_dirichletEval_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#norm-dirichlet-eval-le).

## Dirichlet-space evaluation at the origin is the constant coefficient

Evaluation at `0` is the constant Taylor coefficient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEval_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-zero).

## Dirichlet-space evaluation of a single monomial

Evaluation of a monomial `c * zⁿ / √(n + 1)` (a single coefficient).

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEval_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-single).

## Conjugate reproducing property of the Dirichlet kernel

The reproducing property in the other order: `⟪a, k_z⟫ = conj (f(z))`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.inner_dirichletKernel_right`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#inner-dirichlet-kernel-right).

## Inner product of two Dirichlet kernels as a power series

The inner product of two Dirichlet kernels is the power series
`∑' n, (z * conj w)ⁿ / (n + 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.inner_dirichletKernel_dirichletKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#inner-dirichlet-kernel-dirichlet-kernel).

## Logarithmic formula for the inner product of Dirichlet kernels

The inner product of two Dirichlet kernels is the Dirichlet kernel
function `-log (1 - z * conj w) / (z * conj w)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.inner_dirichletKernel_dirichletKernel_eq_log`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#inner-dirichlet-kernel-dirichlet-kernel-2).

## Dirichlet kernel evaluated at its own point

Evaluation of the kernel at its own point: `f_z(k_z) = ‖k_z‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEval_dirichletKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-dirichlet-kernel).

## Sharpness of the Dirichlet-space pointwise bound

Evaluation of the kernel at its own point, in closed form:
`f_z(k_z) = -log (1 - ‖z‖²) / ‖z‖²`, so the pointwise bound is sharp.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DirichletSpace.dirichletEval_dirichletKernel_of_ne_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpace.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-eval-dirichlet-kernel-of-ne-ze).

## The Dirichlet space

The Dirichlet space $\mathcal{D}$ consists of the functions
$f : \mathbb{C} \to \mathbb{C}$ that are analytic on the open unit disc $\{z : |z| < 1\}$ and have
finite Dirichlet integral: $|f'|^2$ is integrable on the disc with respect to Lebesgue (area)
measure. The values of $f$ outside the disc are unconstrained.

## Sources

- `AMR-022-8011` (Hayman, Research Problems in Function Theory (2018), Problem 8.11, https://arxiv.org/abs/1809.07200).

Formalized by `MathlibExt.Analysis.DirichletSpacePolynomialDensityWanted.DirichletSpace`, an abbreviation declared in [WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#dirichlet-space).

## Polynomial multiples of a function in the Dirichlet space

For $g$ in the Dirichlet
space $\mathcal{D}$, the set $Pg$ consists of the functions $h \in \mathcal{D}$ for which there is
a polynomial $p$ with complex coefficients such that $h(z) = p(z) g(z)$ for all $|z| < 1$; only
values on the open unit disc are compared.

## Sources

- `AMR-022-8011` (Hayman, Research Problems in Function Theory (2018), Problem 8.11, with $Pg$ as defined in Problem 8.10), https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.DirichletSpacePolynomialDensityWanted.polyTimes`, a definition declared in [WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#poly-times).

## Density in the Dirichlet norm

A set $S$ of elements of the Dirichlet space $\mathcal{D}$
is dense in the Dirichlet norm when for every $u \in \mathcal{D}$ and every real $\varepsilon > 0$
there is $h \in S$ with

$$|h(0) - u(0)|^2 + \int_{|z| < 1} |h'(z) - u'(z)|^2 \, dA(z) < \varepsilon,$$

where $A$ is Lebesgue (area) measure on $\mathbb{C}$.

Formalized by `MathlibExt.Analysis.DirichletSpacePolynomialDensityWanted.IsDirichletDense`, a definition declared in [WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#is-dirichlet-dense).

## Hayman's Problem 8.11: polynomial density under domination

The statement that for all
$f$ and $g$ in the Dirichlet space $\mathcal{D}$: if the polynomial multiples $Pg$ are dense in
$\mathcal{D}$ in the Dirichlet norm and $|g(z)| \le |f(z)|$ for all $|z| < 1$, then the
polynomial multiples $Pf$ are also dense in $\mathcal{D}$ in the Dirichlet norm.

## Sources

- the open question of `AMR-022-8011` (Hayman, Research Problems in Function Theory (2018), Problem 8.11, https://arxiv.org/abs/1809.07200).

Formalized by `MathlibExt.Analysis.DirichletSpacePolynomialDensityWanted.conjecture`, a definition declared in [WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#conjecture).

## Polynomial density passes to dominating functions in the Dirichlet space

For all $f$ and $g$
in the Dirichlet space $\mathcal{D}$: if the polynomial multiples $Pg$ are dense in $\mathcal{D}$
in the Dirichlet norm and $|g(z)| \le |f(z)|$ for all $|z| < 1$, then the polynomial multiples
$Pf$ are dense in $\mathcal{D}$ in the Dirichlet norm. This answers Hayman's Problem 8.11
positively.

Resolved true: Richter and Sundberg (Michigan Math. J. 38 (1991) 355-379), and independently
Aleman, proved that in Dirichlet-type spaces $\mathcal{D}(\mu)$, including the classical Dirichlet
space, $|g| \le |f|$ with $g$ cyclic implies $f$ cyclic, where $g$ is cyclic when $Pg$ is dense
(restated in arXiv:2406.06182, Thm 5.12).

## Sources

- Emmanuel Fricain and Romain Lebreton, Cyclicity of the shift operator through Bezout identities, arXiv:2406.06182 (2024), https://arxiv.org/abs/2406.06182.

Stated but not proved: `MathlibExt.Analysis.DirichletSpacePolynomialDensityWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/DirichletSpacePolynomialDensityWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dirichlet space](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces/dirichlet-space)
