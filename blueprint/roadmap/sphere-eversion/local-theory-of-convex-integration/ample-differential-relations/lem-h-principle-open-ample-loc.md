---
declaration: lemma
origin: cited
lean: RelLoc.FormalSol.improve
statement: formalized
proof: formalized
---

# h_principle_open_ample_loc

Let $\mathcal{F}$ be a formal solution of $\mathcal{R}$. Let $K_1 ⊂ E$ be a compact subset, and let $K_0$ be a compact subset of the interior of $K_1$. Assume $\mathcal{F}$ is holonomic near a closed subset $C$ of $E$. Let $ε$ be a positive real number.

If $\mathcal{R}$ is open and ample then there is a homotopy $\mathcal{F}_t$ such that:

1. $\mathcal{F}_0 = \mathcal{F}$
2. $\mathcal{F}_t$ is a formal solution of $\mathcal{R}$ for all $t$ ;
3. $\mathcal{F}_t(x) = \mathcal{F}(x)$ for all $t$ when $x$ is near $C$ or outside $K_1$.
4. $d(\operatorname{bs}\mathcal{F}_t(x), \operatorname{bs} \mathcal{F}(x)) ≤ ε$ for all $t$ and all $x$ ;
5. $\mathcal{F}_1$ is holonomic near $K_0$ ;
6. $t ↦ F_t$ is constant near $0$ and $1$.

## Depends on

- [ample_relation_loc](def-ample-relation-loc.md)

## Proof depends on

- [integration_step](../the-main-inductive-step/lem-integration-step.md)

## Proof

This is a straightforward induction using [Lemma integration_step](../the-main-inductive-step/lem-integration-step.md). Let $(e_1, \dots, e_n)$ be a basis of $E$, and let $(π_1, \dots, π_n)$ be the dual basis. Let $E'_i$ be the linear subspace of $E$ spanned by $(e_1, \dots, e_i)$, for $1 ≤ i ≤ n$, and let $E'_0$ be the zero subspace of $E$. Each $(π_i, e_i)$ is a dual pair and the kernel of $π_i$ contains $E'_{i - 1}$.

[Lemma integration_step](../the-main-inductive-step/lem-integration-step.md) allows to build a sequence of homotopies of formal solutions, each homotopy relating a formal solution which is $E'_i$–holonomic to one which is $E'_{i+1}$–holonomic (always near $K_0$). The shortness condition is always satisfies because $\mathcal{R}$ is ample. Each homotopy starts where the previous one stopped, stay at $C^0$ distance at most $ε/n$, and is relative to $C$ and the complement of $K_1$.

It then suffices to do a smooth concatenation of theses homotopies. We first pre-compose with a smooth map from $[0, 1]$ to itself that fixes $0$ and $1$ and has vanishing derivative to all orders at $0$ and $1$. Then we precompose by affine isomorphisms from $[0, 1]$ to $[i/n, (i + 1)/n]$ before joining them.

## Lean

Formalized as [`RelLoc.FormalSol.improve`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelLoc.FormalSol.improve).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 378](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L378)
