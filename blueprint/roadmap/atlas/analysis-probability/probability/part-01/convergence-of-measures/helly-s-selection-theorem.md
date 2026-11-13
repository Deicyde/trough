---
declaration: section
origin: cited
lean: ProbabilityTheory.IsDistributionFunction, ProbabilityTheory.IsDistributionFunction.nonneg, ProbabilityTheory.IsDistributionFunction.le_one, ProbabilityTheory.IsDistributionFunction.mem_Icc, ProbabilityTheory.helly_selection
statement: formalized
proof: formalized
---

# Helly's selection theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html).

## Distribution function

A nondecreasing, right-continuous function
$F : \mathbb{R} \to \mathbb{R}$ (a Stieltjes function) is a (cumulative) distribution function if
$F(x) \to 0$ as $x \to -\infty$ and $F(x) \to 1$ as $x \to +\infty$.

These are exactly the distribution functions of probability measures on $\mathbb{R}$.

Formalized by `ProbabilityTheory.IsDistributionFunction`, a structure declared in [MathlibExt/Probability/HellySelection.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HellySelection.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html#is-distribution-function).

## Distribution functions are nonnegative

If $F$ is a distribution function on
$\mathbb{R}$, then $0 \le F(x)$ for every $x \in \mathbb{R}$.

Formalized by `ProbabilityTheory.IsDistributionFunction.nonneg`, a theorem declared in [MathlibExt/Probability/HellySelection.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HellySelection.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html#nonneg).

## Distribution functions are at most one

If $F$ is a distribution function on
$\mathbb{R}$, then $F(x) \le 1$ for every $x \in \mathbb{R}$.

Formalized by `ProbabilityTheory.IsDistributionFunction.le_one`, a theorem declared in [MathlibExt/Probability/HellySelection.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HellySelection.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html#le-one).

## Distribution functions take values in the unit interval

If $F$ is a distribution
function on $\mathbb{R}$, then $F(x) \in [0, 1]$ for every $x \in \mathbb{R}$.

Formalized by `ProbabilityTheory.IsDistributionFunction.mem_Icc`, a theorem declared in [MathlibExt/Probability/HellySelection.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HellySelection.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html#mem-icc).

## Helly's selection theorem

Let $(F_n)_{n \in \mathbb{N}}$ be a sequence of
distribution functions on $\mathbb{R}$. Then there are a strictly increasing map
$\varphi : \mathbb{N} \to \mathbb{N}$ and a nondecreasing, right-continuous function
$G : \mathbb{R} \to \mathbb{R}$ such that $F_{\varphi(k)}(x) \to G(x)$ as $k \to \infty$ at every
point $x \in \mathbb{R}$ at which $G$ is continuous.

The limit $G$ need not itself be a distribution function: it may lose mass to $\pm\infty$.

Formalized by `ProbabilityTheory.helly_selection`, a theorem declared in [MathlibExt/Probability/HellySelection.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HellySelection.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html#helly-selection).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Helly's selection theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/convergence-of-measures/helly-s-selection-theorem)
