---
declaration: corollary
origin: cited
lean: extend_loops
statement: formalized
proof: formalized
---

# extend_loops

Let $U_0$ and $U_1$ be open sets in $E$. Let $K_0 ⊂ U_0$ and $K_1 ⊂ U_1$ be compact subsets. For any $γ_0 ∈ \operatorname{\mathcal{L}}(U_0, g, β, Ω)$ and $γ_1 ∈ \operatorname{\mathcal{L}}(U_1, g, β, Ω)$, there exists a neighborhood $U$ of $K_0 ∪ K_1$ and there exists $γ ∈ \operatorname{\mathcal{L}}(U, g, β, Ω)$ which coincides with $γ_0$ near $K_0\cup U_1^c$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [satisfied_or_refund](lem-satisfied-or-refund.md)

## Proof

Let $C_0 = K_0\cup U_1^c$ and $C_1 := K_1 ∖ U_0$. Since $C_0$ and $C_1$ are disjoint closed sets, there is some continuous cut-off $ρ \!: E → [0, 1]$ which vanishes on a neighborhood of $C_0$ and equals one on a neighborhood of $C_1$.

[Lemma satisfied_or_refund](lem-satisfied-or-refund.md) gives a homotopy of loops $γ_τ$ from $γ_0$ to $γ_1$ on $U_0 ∩ U_1$. Moreover, note that $γ_τ$ is defined on all of $E$. On $U_0' ∪ (U_0 ∩ U_1) ∪ U_1'$, which is a neighborhood of $K_0 ∪ K_1$, we set

$$
γ_x = γ_{ρ(x), x}
$$

which has the required properties.

## Lean

Formalized as [`extend_loops`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/extend_loops).

## Sources

- [Sphere eversion blueprint: loops.tex, line 520](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L520)
