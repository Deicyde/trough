---
declaration: section
origin: cited
lean: Real.tendsto_sum_alternating_harmonic, Real.not_summable_abs_alternating_harmonic
statement: formalized
proof: formalized
---

# Alternating harmonic series

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/alternating-harmonic-series/index.html).

## The alternating harmonic series sums to $\log 2$

The partial sums
$\sum_{i=0}^{k-1} (-1)^i / (i + 1)$ of real numbers converge to $\log 2$ as $k \to \infty$.

Formalized by `Real.tendsto_sum_alternating_harmonic`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/AlternatingHarmonic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/AlternatingHarmonic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/alternating-harmonic-series/index.html#tendsto-sum-alternating-harmonic).

## The alternating harmonic series is not absolutely summable

The series of real numbers
$\sum_{n \ge 0} \left|(-1)^n / (n + 1)\right|$ is not summable.

The series of absolute values is the harmonic series $\sum_{n \ge 0} 1 / (n + 1)$, which
diverges. In particular the convergence of the alternating harmonic series to $\log 2$ is only
conditional.

Formalized by `Real.not_summable_abs_alternating_harmonic`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/AlternatingHarmonic.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/AlternatingHarmonic.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/alternating-harmonic-series/index.html#not-summable-abs-alternating-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alternating harmonic series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/alternating-harmonic-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/convergence/alternating-harmonic-series)
