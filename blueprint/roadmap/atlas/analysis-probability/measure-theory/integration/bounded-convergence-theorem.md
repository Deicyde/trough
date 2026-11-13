---
declaration: section
origin: cited
lean: MeasureTheory.tendsto_integral_norm_sub_of_bounded_convergence, MeasureTheory.tendsto_integral_of_bounded_convergence
statement: formalized
proof: formalized
---

# Bounded convergence theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/bounded-convergence-theorem/index.html).

## Bounded convergence theorem, $L^1$ form

Let $\mu$ be a finite measure on a measurable
space $\alpha$, let $G$ be a real normed space, let $C$ be a real number, and let
$F_n : \alpha \to G$ for $n \in \mathbb{N}$ and $f : \alpha \to G$ be functions. Suppose that each
$F_n$ is almost everywhere strongly measurable, that for every $n$ we have $\|F_n(a)\| \le C$ for
$\mu$-almost every $a$, and that $F_n \to f$ in $\mu$-measure. Then
$\int_\alpha \|F_n(a) - f(a)\| \, d\mu(a) \to 0$ as $n \to \infty$.

Formalized by `MeasureTheory.tendsto_integral_norm_sub_of_bounded_convergence`, a theorem declared in [MathlibExt/MeasureTheory/Function/BoundedConvergence.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Function/BoundedConvergence.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/bounded-convergence-theorem/index.html#tendsto-integral-norm-sub-of-bounded-con).

## Bounded convergence theorem

Let $\mu$ be a finite measure on a measurable space $\alpha$,
let $G$ be a real normed space, let $C$ be a real number, and let $F_n : \alpha \to G$ for
$n \in \mathbb{N}$ and $f : \alpha \to G$ be functions. Suppose that each $F_n$ is almost
everywhere strongly measurable, that for every $n$ we have $\|F_n(a)\| \le C$ for $\mu$-almost
every $a$, and that $F_n \to f$ in $\mu$-measure (in probability). Then
$\int_\alpha F_n \, d\mu \to \int_\alpha f \, d\mu$ as $n \to \infty$.

Formalized by `MeasureTheory.tendsto_integral_of_bounded_convergence`, a theorem declared in [MathlibExt/MeasureTheory/Function/BoundedConvergence.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Function/BoundedConvergence.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/bounded-convergence-theorem/index.html#tendsto-integral-of-bounded-convergence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded convergence theorem](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/bounded-convergence-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/integration/bounded-convergence-theorem)
