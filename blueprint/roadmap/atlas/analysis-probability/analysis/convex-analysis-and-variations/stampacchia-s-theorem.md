---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.Stampacchia.stampacchia_eq_of_univ, MathlibExt.Analysis.InnerProductSpace.Stampacchia.exists_unique_stampacchia, MathlibExt.Analysis.InnerProductSpace.Stampacchia.exists_unique_stampacchia_bilinear, MathlibExt.Analysis.InnerProductSpace.Stampacchia.exists_eq_of_coercive
statement: formalized
proof: formalized
---

# Stampacchia's theorem

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem/index.html).

## Variational inequality on the whole space reduces to an equation

On the whole space, a variational-inequality solution satisfies `A u = f`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Stampacchia.stampacchia_eq_of_univ`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem/index.html#stampacchia-eq-of-univ).

## Stampacchia's theorem, operator form

For a coercive bounded linear
operator `A` on a real Hilbert space, a nonempty closed convex set `K`, and
`f ∈ E`, there is exactly one `u ∈ K` with `⟪A u - f, v - u⟫_ℝ ≥ 0` for all
`v ∈ K`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Stampacchia.exists_unique_stampacchia`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem/index.html#exists-unique-stampacchia).

## Stampacchia's theorem, bilinear-form form

For a coercive bounded
bilinear form `B` on a real Hilbert space, a nonempty closed convex set `K`,
and a continuous linear functional `φ`, there is exactly one `u ∈ K` with
`B u (v - u) ≥ φ (v - u)` for all `v ∈ K`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Stampacchia.exists_unique_stampacchia_bilinear`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem/index.html#exists-unique-stampacchia-bilinear).

## Coercive bounded operators on a real Hilbert space are surjective

A coercive bounded linear operator on a real Hilbert space is surjective.
This is the whole-space case of Stampacchia's theorem (compare Mathlib's
Lax–Milgram theorem, which is the analogous statement for bilinear forms).

Formalized by `MathlibExt.Analysis.InnerProductSpace.Stampacchia.exists_eq_of_coercive`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Stampacchia.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem/index.html#exists-eq-of-coercive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stampacchia's theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/stampacchia-s-theorem)
