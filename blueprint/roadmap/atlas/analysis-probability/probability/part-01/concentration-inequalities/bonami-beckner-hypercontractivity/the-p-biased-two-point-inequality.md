---
declaration: section
origin: cited
lean: StatMech.Probability.pcx_g, StatMech.Probability.pcx_KEY_pos, StatMech.Probability.pcx_OneVarCore, StatMech.Probability.pcx_two_point_value
statement: formalized
proof: formalized
---

# The p-biased two-point inequality

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality/index.html).

## Convex auxiliary function for the p-biased inequality

`(1-p)(1 - p t)^q + p(1 + (1-p) t)^q - 1 - 2q(q-1) p²(1-p)² t²`, convex and nonnegative on
`[-1/(1-p), 1/p]` for `1 ≤ q ≤ 2`.

Formalized by `StatMech.Probability.pcx_g`, a definition declared in [MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality/index.html#pcx-g).

## Pointwise bound for the p-biased inequality holds

The pointwise bound `pih_KEY p q` for `0 < p < 1` and `1 ≤ q ≤ 2`.

Formalized by `StatMech.Probability.pcx_KEY_pos`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality/index.html#pcx-key-pos).

## One-variable p-biased inequality

The one-variable `p`-biased inequality for `0 < p < 1` and `1 ≤ q ≤ 2`.

Formalized by `StatMech.Probability.pcx_OneVarCore`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality/index.html#pcx-one-var-core).

## p-biased two-point inequality

The **`p`-biased two-point inequality**: for `0 < p < 1`, `1 ≤ q ≤ 2` and real `u, v`,
`((1-p) u + p v)² + 4(q-1) p²(1-p)²(u - v)² ≤ ((1-p)|u|^q + p|v|^q)^(2/q)`.

Formalized by `StatMech.Probability.pcx_two_point_value`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Hypercontractivity/PBiasedConvexity.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality/index.html#pcx-two-point-value).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The p-biased two-point inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/the-p-biased-two-point-inequality)
