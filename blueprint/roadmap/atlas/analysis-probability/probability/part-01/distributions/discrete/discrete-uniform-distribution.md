---
declaration: section
origin: cited
lean: PMF.uniformFinset, PMF.uniformFintype, PMF.uniformFinset_univ, PMF.toOuterMeasure_uniformFintype_apply, PMF.toMeasure_uniformFintype_apply
statement: formalized
proof: formalized
---

# Discrete uniform distribution

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html).

## Uniform distribution on a finite set

For a nonempty finite subset $s$ of a type $\alpha$,
the uniform distribution on $s$ is the probability mass function on $\alpha$ that gives mass
$1/|s|$ to each element of $s$ and mass $0$ to every other element of $\alpha$.

Formalized by `PMF.uniformFinset`, a definition declared in [MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html#uniform-finset).

## Uniform distribution on a finite type

For a nonempty finite type $\alpha$, the uniform
distribution on $\alpha$ is the probability mass function on $\alpha$ that gives mass $1/|\alpha|$
to every element of $\alpha$.

Formalized by `PMF.uniformFintype`, a definition declared in [MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html#uniform-fintype).

## Uniform distribution on the whole finite type

For a nonempty finite type $\alpha$, the
uniform distribution on the finite set of all elements of $\alpha$ equals the uniform
distribution on $\alpha$.

Formalized by `PMF.uniformFinset_univ`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html#uniform-finset-univ).

## Outer measure of an event under the uniform distribution

Let $\alpha$ be a nonempty finite
type. For every subset $s \subseteq \alpha$, the outer measure associated to the uniform
distribution on $\alpha$ assigns to $s$ the value $|s| / |\alpha|$, computed in the extended
nonnegative reals.

Formalized by `PMF.toOuterMeasure_uniformFintype_apply`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html#to-outer-measure-uniform-fintype-apply).

## Probability of an event under the uniform distribution

Let $\alpha$ be a nonempty finite
type carrying a σ-algebra. For every measurable set $s \subseteq \alpha$, the probability measure
associated to the uniform distribution on $\alpha$ gives $s$ the measure $|s| / |\alpha|$, computed
in the extended nonnegative reals.

Formalized by `PMF.toMeasure_uniformFintype_apply`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProbabilityMassFunction/Uniform.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html#to-measure-uniform-fintype-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete uniform distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/discrete-uniform-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/discrete/discrete-uniform-distribution)
