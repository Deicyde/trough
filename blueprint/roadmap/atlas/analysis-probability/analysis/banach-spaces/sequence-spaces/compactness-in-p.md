---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Lp.Compactness.lpRestrict, MathlibExt.Analysis.Normed.Lp.Compactness.lpRestrict_apply, MathlibExt.Analysis.Normed.Lp.Compactness.lpExtend, MathlibExt.Analysis.Normed.Lp.Compactness.lpExtend_apply, MathlibExt.Analysis.Normed.Lp.Compactness.lpLift, MathlibExt.Analysis.Normed.Lp.Compactness.lpTrunc, MathlibExt.Analysis.Normed.Lp.Compactness.lpLift_apply, MathlibExt.Analysis.Normed.Lp.Compactness.lpTrunc_apply
statement: formalized
proof: formalized
---

# Compactness in ℓ^p

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html).

## Restriction and zero extension

## Restriction of an $\ell^p$ sequence to its first coordinates

The restriction of an `ℓ^p` sequence to its first `N` coordinates.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpRestrict`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-restrict).

## Pointwise action of the $\ell^p$ restriction

The restriction acts coordinatewise.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpRestrict_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-restrict-apply).

## Zero extension of a finite coordinate vector

The extension of a coordinate vector on `Fin N` by `0` to a total
coordinate function on `ℕ`.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpExtend`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-extend).

## Pointwise action of the zero extension

The extension acts coordinatewise.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpExtend_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-extend-apply).

## Lift of a coordinate function to a truncated $\ell^p$ sequence

The lift of a coordinate function on `ℕ` to an `ℓ^p` sequence, keeping
only its first `N` coordinates.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpLift`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-lift).

## Truncation of an $\ell^p$ sequence, zeroing all but its first coordinates

The all-`p` coordinate extension of finite truncation to the first `N`
coordinates, also defined at `p = ∞`. For finite `p ≥ 1`,
`lpTrunc_eq_lpSchauderBasis_proj` identifies it with the canonical
continuous linear Schauder projection.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpTrunc`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-trunc).

## Pointwise action of the finite $\ell^p$ lift

The lift acts coordinatewise.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpLift_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-lift-apply).

## Pointwise action of $\ell^p$ truncation

Truncation acts coordinatewise.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpTrunc_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-trunc-apply).

## Truncation equals the Schauder basis projection

For finite `p ≥ 1`, coordinate truncation is the canonical bundled
Schauder-basis projection.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.lpTrunc_eq_lpSchauderBasis_proj`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#lp-trunc-eq-lp-schauder-basis-proj).

## Truncation is a contraction on $\ell^p$

Truncation is a contraction.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.norm_lpTrunc_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#norm-lp-trunc-le).

## Tail of an $\ell^p$ vector is no larger than the vector

The tail of a vector is no larger than the vector itself.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.norm_sub_lpTrunc_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#norm-sub-lp-trunc-le).

## Tails shrink as the truncation length grows

Tails shrink as the truncation length grows.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.norm_sub_lpTrunc_mono`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#norm-sub-lp-trunc-mono).

## Norm bound for the finite $\ell^p$ lift

The target `ℓ^p` norm of the finite lift is bounded by
`N ^ (1 / p)` times the supremum norm of its first `N` coordinates.
The norm on the source Pi type `Fin N → 𝕜` is the supremum norm.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.norm_lpLift_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#norm-lp-lift-le).

## Truncations of an $\ell^p$ vector converge to it

The truncations of an `ℓ^p` vector converge to the vector.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.tendsto_lpTrunc`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#tendsto-lp-trunc).

## Tail of a single $\ell^p$ vector can be made small

The tail of a single vector can be made arbitrarily small.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.exists_norm_sub_lpTrunc_lt`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#exists-norm-sub-lp-trunc-lt).

## Uniform vanishing of tails

The tails of the elements of a set `K` vanish uniformly: for every
`ε > 0` there is `N` such that every `x ∈ K` is within `ε` of its truncation
to the first `N` coordinates.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.UniformTailVanishing`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#uniform-tail-vanishing).

## Riesz–Fréchet–Kolmogorov criterion for total boundedness in $\ell^p$

The Riesz–Fréchet–Kolmogorov criterion for `ℓ^p (ℕ, 𝕜)`, `1 ≤ p < ∞`:
a set is totally bounded if and only if it is bounded and its tails vanish
uniformly.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.totallyBounded_iff_bounded_and_uniformTailVanishing`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#totally-bounded-iff-bounded-and-uniform).

## Riesz–Fréchet–Kolmogorov criterion for compactness in $\ell^p$

Compact form of the Riesz–Fréchet–Kolmogorov criterion.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.isCompact_iff_isComplete_and_bounded_and_uniformTailVanishing`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#is-compact-iff-is-complete-and-bounded-a).

## Riesz–Fréchet–Kolmogorov relative compactness criterion in $\ell^p$

Relative-compact form of the Riesz–Fréchet–Kolmogorov criterion.

Formalized by `MathlibExt.Analysis.Normed.Lp.Compactness.isCompact_closure_iff_bounded_and_uniformTailVanishing`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Compactness.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Compactness.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html#is-compact-closure-iff-bounded-and-unifo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compactness in ℓ^p](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/compactness-in-p)
