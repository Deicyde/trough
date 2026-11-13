---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.regularizedRisk, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelExpansion, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.mem_topologicalClosure_range_of_isMinimizer, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.exists_eq_kernelExpansion_of_isMinimizer, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.exists_kernelExpansion_isMinimizer, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.isMinimizer_unique, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelGram, MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelRidgeRisk
statement: formalized
proof: formalized
---

# Representer theorem

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html).

## Regularized risk in a reproducing kernel Hilbert space

The regularized risk `L (f x₁, …, f xₙ) + Ω ‖f‖` of `f` in the RKHS `H`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.regularizedRisk`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#regularized-risk).

## Kernel expansion map centered at the sample points

The kernel expansion map `c ↦ ∑ i, kerFun H (x i) (c i)`. Its range is the span of the
kernel functions at the sample points `x i`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelExpansion`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-expansion).

## The representer theorem

**The representer theorem** (closed-span form): if `Ω` is strictly increasing on `[0, ∞)`,
every global minimizer of the regularized risk lies in the closure of the span of the kernel
functions at the sample points.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.mem_topologicalClosure_range_of_isMinimizer`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#mem-topological-closure-range-of-is-mini).

## The representer theorem

**The representer theorem** (Schölkopf, Herbrich and Smola, Theorem 1): for a
finite-dimensional output space `V` (for instance a scalar kernel, `V = 𝕜`) and `Ω` strictly
increasing on `[0, ∞)`, every global minimizer of `L (f x₁, …, f xₙ) + Ω ‖f‖` is a kernel
expansion `∑ i, kerFun H (x i) (c i)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.exists_eq_kernelExpansion_of_isMinimizer`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#exists-eq-kernel-expansion-of-is-minimiz).

## Existence of a minimizer

For finite-dimensional `V`, a continuous loss bounded below,
and a continuous regularizer that is monotone on `[0, ∞)` and tends to `∞`, the regularized risk
has a global minimizer, and it can be taken to be a kernel expansion.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.exists_kernelExpansion_isMinimizer`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#exists-kernel-expansion-is-minimizer).

## Uniqueness of the minimizer

**Uniqueness of the minimizer** (real scalars): for a convex loss `L` and a regularizer `Ω`
that is strictly convex and monotone on `[0, ∞)` (for instance `Ω t = λ t²` with `λ > 0`), the
regularized risk has at most one global minimizer.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.isMinimizer_unique`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#is-minimizer-unique).

## Kernel Gram matrix

The Gram matrix `K i j = k(x i, x j)` of a real scalar kernel at the sample points, where
`k(x, y) = kernel H x y 1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelGram`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-gram).

## Kernel ridge regression objective

The kernel ridge objective `∑ i, (y i - f (x i))² + λ ‖f‖²`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelRidgeRisk`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-ridge-risk).

## Kernel ridge regression fit

The kernel ridge fit: the kernel expansion with coefficients `(K + λ I)⁻¹ y`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelRidgeFit`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-ridge-fit).

## Kernel ridge objective as a regularized risk

The kernel ridge objective is the regularized risk with the squared loss and
`Ω t = λ t²`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelRidgeRisk_eq_regularizedRisk`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-ridge-risk-eq-regularized-risk).

## Values of a kernel expansion at the sample points

The values of a kernel expansion at the sample points are `K c`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelExpansion_apply_sample`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-expansion-apply-sample).

## Kernel Gram matrix is positive semidefinite

The kernel Gram matrix is positive semidefinite.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.posSemidef_kernelGram`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#pos-semidef-kernel-gram).

## Fitted values of kernel ridge regression

The fitted values of kernel ridge regression are `K (K + λ I)⁻¹ y`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelRidgeFit_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-ridge-fit-apply).

## Kernel ridge regression

**Kernel ridge regression** (Kimeldorf and Wahba): for `λ > 0` the kernel ridge fit
minimizes `∑ i, (y i - f (x i))² + λ ‖f‖²` over the whole RKHS.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.kernelRidgeRisk_kernelRidgeFit_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#kernel-ridge-risk-kernel-ridge-fit-le).

## Kernel ridge fit is the unique minimizer

The kernel ridge fit is the unique minimizer for `λ > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RepresenterTheorem.eq_kernelRidgeFit_of_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/RepresenterTheorem.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#eq-kernel-ridge-fit-of-le).

## Projection onto Riesz representers with Pythagorean residual

Orthogonal projection onto the span of the Riesz representers preserves
the values of the functionals, and the Pythagorean identity holds for the
residual.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RepresenterTheorem.exists_mem_span_norm_sq_add`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RepresenterTheorem.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RepresenterTheorem.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#exists-mem-span-norm-sq-add).

## Projection onto Riesz representers does not increase the norm

Orthogonal projection onto the span of the Riesz representers does not
increase the norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RepresenterTheorem.exists_mem_span_values_eq_norm_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RepresenterTheorem.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RepresenterTheorem.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#exists-mem-span-values-eq-norm-le).

## Representer theorem

Any minimizer of a ridge-regularized problem
`F (fun i => L i g) + Λ * ‖g‖ ^ 2` with `Λ > 0` lies in the span of the
Riesz representers of the functionals `L i`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RepresenterTheorem.mem_span_of_isMinOn`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RepresenterTheorem.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RepresenterTheorem.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html#mem-span-of-is-min-on).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representer theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/representer-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/hilbert-spaces/representer-theorem)
