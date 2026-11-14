---
declaration: proposition
origin: cited
lean: exist_loops
statement: formalized
proof: formalized
---

# ∃\_loops

Let $K$ a compact set in $E$. Let $Ω$ be an open set in $E × F$.

Let $β$ and $g$ be smooth maps from $E$ to $F$. Write $Ω_x := \{ y ∈ F \mid (x, y) ∈ Ω\}$, assume that $β(x) ∈ Ω_x$ for all $x$, and that $g(x) = β(x)$ near $K$.

If, for every $x$, $g(x)$ is in the convex hull of the connected component of $Ω_x$ containing $β(x)$, then there exists a smooth family of loops

$$
γ \!: E × [0, 1] × 𝕊^1 → F, (x, t, s) ↦ γ^t_x(s)
$$

such that, for all $x ∈ E$, all $t ∈ ℝ$ and all $s ∈ 𝕊^1$,

- $γ^t_x(s) ∈ Ω_x$
- $γ^0_x(s) = γ^t_x(1) = β(x)$
- $\bar γ^1_x = g(x)$
- $γ^t_x(s) = β(x)$ if $x$ is near $K$.

## Depends on

- [loop](def-loop.md)

## Proof depends on

- [∃\_surrounding_loops](../constructing-loops/lem-surrounding-loops.md)
- [reparametrization](../constructing-loops/lem-reparametrization.md)
- [exists_cont_diff_of_convex](../constructing-loops/lem-exists-cont-diff-of-convex.md)

## Proof

*Proof of Proposition ∃\_loops.* Let $γ^*$ be a family of loops surrounding the origin in $B_F(0,1)$ the open unit ball in $F$, constructed using [Lemma local_loops](../constructing-loops/lem-local-loops.md). For $x$ in some neighborhood $U^*$ of $K$ where $g = β$, we set $γ_x = g(x) + εγ^*$ where $ε > 0$ is sufficiently small to ensure that $B_{E\times F}((x,β(x)),2ε)\subseteq \Omega$ (recall $Ω$ is open and $K$ is compact). [Lemma ∃\_surrounding_loops](../constructing-loops/lem-surrounding-loops.md) extends this family to a continuous family of surrounding loops $γ_x$ for all $x$ (this is not yet our final $γ$).

We then need to approximate this continuous family by a smooth one. Some care is needed to ensure that it stays based at $β$. We can first reparametrize $γ$ on $[0,1] \times 𝕊^1$ to ensure that $γ$ is constant in a neighborhood of $C = \{(t, s) \in [0,1] \times 𝕊^1 \mid t = 0 \text{ or } s = 0\}$. Using [Lemma exists_cont_diff_of_convex](../constructing-loops/lem-exists-cont-diff-of-convex.md), we can find a smooth function that has distance at most $ε$ from $γ$ and coincides with $γ$ on $C$ (using the fact that $γ$ is already smooth near $C$). Since all loops that are sufficiently close to $γ$ still surround $g$, we can also ensure that the new smoothened $γ$ is still surrounding.

Then [Lemma reparametrization](../constructing-loops/lem-reparametrization.md) gives a family of circle diffeomorphisms $h_x$ such that $γ^1_x ∘ h_x$ has average $g(x)$.

Finally we choose a cut-off function function $χ$ which vanishes near $E ∖ U^*$ and equals one near $K$. As our final family of loops, we choose $χ(x)g(x) + (1-χ(x))(γ_x ∘ h_x)$. This operation does not change the average values of these loops, because it rescales them around their average value, but makes them constant near $K$. Also, those loops stay in $Ω$, thanks to our choice of $ε$.

## Lean

Formalized as [`exist_loops`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/exist_loops).

## Sources

- [Sphere eversion blueprint: loops.tex, line 29](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L29)
