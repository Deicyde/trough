---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.DiscontinuousLinearFunctional.exists_discontinuous_linearMap_of_not_finiteDimensional, MathlibExt.Analysis.FunctionalAnalysis.DiscontinuousLinearFunctional.forall_linearMap_continuous_iff_finiteDimensional, MathlibExt.Analysis.FunctionalAnalysis.DiscontinuousLinearFunctional.exists_linearMap_not_continuousLinearMap
statement: formalized
proof: formalized
---

# Discontinuous linear functionals

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/discontinuous-linear-functionals/index.html).

## A discontinuous linear functional on an infinite-dimensional normed space

Let $E$ be a
normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. If $E$ is not finite-dimensional,
then there exists a linear functional $f \colon E \to \mathbb{K}$ that is not continuous.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.DiscontinuousLinearFunctional.exists_discontinuous_linearMap_of_not_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/DiscontinuousLinearFunctional.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/DiscontinuousLinearFunctional.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/discontinuous-linear-functionals/index.html#exists-discontinuous-linear-map-of-not-f).

## Every linear functional is continuous if and only if the space is finite-dimensional

Let $E$ be a normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Every linear
functional $f \colon E \to \mathbb{K}$ is continuous if and only if $E$ is finite-dimensional.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.DiscontinuousLinearFunctional.forall_linearMap_continuous_iff_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/DiscontinuousLinearFunctional.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/DiscontinuousLinearFunctional.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/discontinuous-linear-functionals/index.html#forall-linear-map-continuous-iff-finite).

## The algebraic dual is strictly larger than the topological dual

Let $E$ be a normed
space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. If $E$ is not finite-dimensional, then
there is a linear functional $f \colon E \to \mathbb{K}$ that differs from every continuous
linear functional $g \colon E \to \mathbb{K}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.DiscontinuousLinearFunctional.exists_linearMap_not_continuousLinearMap`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/DiscontinuousLinearFunctional.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/DiscontinuousLinearFunctional.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/discontinuous-linear-functionals/index.html#exists-linear-map-not-continuous-linear).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discontinuous linear functionals](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/discontinuous-linear-functionals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/discontinuous-linear-functionals)
