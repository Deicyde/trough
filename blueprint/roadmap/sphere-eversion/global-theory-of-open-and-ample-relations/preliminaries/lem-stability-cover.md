---
declaration: lemma
origin: cited
lean: Metric.exists_continuous_real_forall_closedBall_subset
statement: formalized
proof: formalized
---

# stability_cover

In a metric space $X$, let $U : ι → \operatorname{\mathcal{P}}{X}$ be a family of open subsets of $X$ and let $K : ι → \operatorname{\mathcal{P}}{X}$ be a locally-finite family of closed subsets such that $K_i ⊂ U_i$ for all $i$. There exists a continuous function $δ : X → ℝ_{> 0}$ such that:

$$
∀ x\, x',\; ∀ i, \left[x ∈ K_i \text{ and } d(x, x') < δ(x)\right] ⇒ x' ∈ U_i.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We first note that, for any given $i$, compactness of $K$ and openness of $V_i$ give a positive number $δ_i$ such that the $δ_i$-neighborhood of $K_i$ is contained in $V_i$. We now prove that solutions exist locally. Let $x$ be any point in $X$. From the local finiteness assumption, we get a neighborhood $U$ of $x$ such that $\{i | U ∩ V_i ≠ ∅\}$ is finite. The constant function with value the minimum of the corresponding $δ_i$ is a solution on $U$. Since the condition we put on $δ$ is convex, we can glue those local solutions using [Lemma exists_cont_diff_of_convex](../../loops/constructing-loops/lem-exists-cont-diff-of-convex.md).

## Lean

Formalized as [`Metric.exists_continuous_real_forall_closedBall_subset`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Metric.exists_continuous_real_forall_closedBall_subset).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 212](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L212)
