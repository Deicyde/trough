---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.Demiclosedness.demiclosedness_of_lipschitzWith_one, MathlibExt.Analysis.InnerProductSpace.Demiclosedness.fixedPoint_of_weakly_tendsto_of_forall_fixedPoint
statement: formalized
proof: formalized
---

# Browder's demiclosedness principle

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-s-demiclosedness-principle/index.html).

## Browder's demiclosedness principle

If `T` is nonexpansive,
`u n ⇀ x` weakly, and `u n - T (u n) → 0`, then `T x = x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Demiclosedness.demiclosedness_of_lipschitzWith_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Demiclosedness.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/Demiclosedness.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-s-demiclosedness-principle/index.html#demiclosedness-of-lipschitz-with-one).

## Fixed points of a nonexpansive map are weakly sequentially closed

The fixed-point set of a nonexpansive map is weakly sequentially
closed: if every `u n` is a fixed point of `T` and `u n ⇀ x` weakly,
then `T x = x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Demiclosedness.fixedPoint_of_weakly_tendsto_of_forall_fixedPoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Demiclosedness.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/Demiclosedness.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-s-demiclosedness-principle/index.html#fixed-point-of-weakly-tendsto-of-forall).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Browder's demiclosedness principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-s-demiclosedness-principle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/fixed-point-theory/browder-s-demiclosedness-principle)
