---
declaration: lemma
origin: cited
lean: exists_contDiff_of_convex
statement: formalized
proof: formalized
---

# exists_cont_diff_of_convex

Let $E$ and $F$ be real normed vector spaces. Assume that $E$ is finite dimensional. Let $P$ be a predicate on $E \times F$ such that for all $x$ in $E$, $\{y ~|~ P (x, y) \}$ is convex. Let $n$ be a natural number or $+\infty$. Assume that every $x$ has a neighbourhood $U$ on which there exists a $C^n$ function $f$ such that $\forall x ∈ U, P(x, f(x))$. Then there is a global $C^n$ function $f$ such that $\forall x, P(x, f(x))$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The assumption give us an open cover $(U_i)_{i ∈ I}$ of $E$ and functions $f_i \!: E → F$ that are smooth on $U_i$ and such that $P(x, f_i(x))$ for all $x$ in $U_i$. Let $ρ$ be a smooth partition of unity associated to this cover. The function $f = ∑ ρ_i f_i$ is smooth on $E$ and the convexity assumption on $P$ ensures it satisfies $\forall x, P(x, f(x))$. Indeed each value $f(x)$ is a convex combination of finitely many values $f_i(x)$ where $i$ satisfies that $x$ is in $U_i$.

## Lean

Formalized as [`exists_contDiff_of_convex`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/exists_contDiff_of_convex).

## Sources

- [Sphere eversion blueprint: loops.tex, line 579](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L579)
