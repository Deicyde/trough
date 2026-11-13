---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Lp.RellichKondrachov.rellichWeight, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.memRellichBall, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.rellichBall, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.norm_sq_eq_tsum, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.memRellichBall_of_support, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.norm_sub_lpTrunc_sq_eq, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.norm_sub_lpTrunc_sq_le, MathlibExt.Analysis.Normed.Lp.RellichKondrachov.lpTrunc_mem_span
statement: formalized
proof: formalized
---

# Rellich–Kondrachov theorem

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html).

## Rellich weight

The Rellich weight `1 + n ^ 2`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.rellichWeight`, a definition declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#rellich-weight).

## Membership in the Rellich ball via partial sums

Membership in the Rellich ball: every finite weighted partial sum is
bounded by `M ^ 2`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.memRellichBall`, a definition declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#mem-rellich-ball).

## Rellich ball of weighted square-summable sequences

The Rellich ball of radius `M`: sequences in `ℓ²(ℕ, 𝕜)` whose weighted
`ℓ²` energy is at most `M ^ 2`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.rellichBall`, a definition declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#rellich-ball).

## Squared $\ell^2$ norm as a sum of squared coordinates

The `ℓ²` norm squared is the sum of the squared coordinate norms.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.norm_sq_eq_tsum`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#norm-sq-eq-tsum).

## Finitely supported sequences in the Rellich ball

If `x` is supported in a finite set `S` and its weighted sum over `S` is
at most `M ^ 2`, then `x` lies in the Rellich ball.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.memRellichBall_of_support`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#mem-rellich-ball-of-support).

## Tail norm identity for $\ell^2$ truncation

The tail norm identity: the distance from `x` to its truncation is the
`ℓ²` norm of the tail.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.norm_sub_lpTrunc_sq_eq`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#norm-sub-lp-trunc-sq-eq).

## Tail estimate for the Rellich ball

The tail estimate: the squared distance from `x` to its truncation is at
most `M ^ 2 / (1 + N ^ 2)`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.norm_sub_lpTrunc_sq_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#norm-sub-lp-trunc-sq-le).

## Truncations lie in the span of the first basis vectors

Canonical truncations land in the span of the first `N` basis vectors.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.lpTrunc_mem_span`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#lp-trunc-mem-span).

## Rellich ball depends only on the absolute radius

The Rellich ball only depends on `|M|`, since the bound is on `M ^ 2`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.rellichBall_abs`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#rellich-ball-abs).

## Rellich–Kondrachov, total boundedness form

The Rellich ball is
totally bounded in `ℓ²(ℕ, 𝕜)`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.totallyBounded_rellichBall`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#totally-bounded-rellich-ball).

## Rellich–Kondrachov, closedness form

The Rellich ball is closed.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.isClosed_rellichBall`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#is-closed-rellich-ball).

## Rellich–Kondrachov, compactness form

The Rellich ball is compact in
`ℓ²(ℕ, 𝕜)`.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.isCompact_rellichBall`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#is-compact-rellich-ball).

## Rellich–Kondrachov, sequential form

Every sequence in the Rellich
ball has a subsequence converging in `ℓ²(ℕ, 𝕜)` to a point of the ball.

Formalized by `MathlibExt.Analysis.Normed.Lp.RellichKondrachov.exists_subseq_tendsto_of_memRellichBall`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/RellichKondrachov.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html#exists-subseq-tendsto-of-mem-rellich-bal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rellich–Kondrachov theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/function-spaces/rellich-kondrachov-theorem)
