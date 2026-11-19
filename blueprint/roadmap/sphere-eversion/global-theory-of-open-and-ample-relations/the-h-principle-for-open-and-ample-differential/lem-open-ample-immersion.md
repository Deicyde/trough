---
declaration: lemma
origin: cited
lean: immersionRel_open_ample
statement: formalized
proof: formalized
---

# open_ample_immersion

The relation of immersions of $M$ into $N$ in positive codimension is open and ample.

## Depends on

- [ample_relation](def-ample-relation.md)

## Proof depends on

- [ample_codim_two](../../local-theory-of-convex-integration/ample-differential-relations/lem-ample-codim-two.md)

## Proof

For every $σ = (x, y, φ)$ in the immersion relation $\mathcal{R}$, and for every dual pair $(π, v)$, the slice $\mathcal{R}(σ, π, v)$ is the set of $w$ which do not belong to the image of $\ker π$ under $φ$. Since $\dim M > \dim N$, this image has codimension at least $2$ in $T_yN$, and [Lemma ample_codim_two](../../local-theory-of-convex-integration/ample-differential-relations/lem-ample-codim-two.md) concludes.

## Lean

Formalized as [`immersionRel_open_ample`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/immersionRel_open_ample).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 609](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L609)
