---
declaration: lemma
origin: cited
lean: exists_contDiff_of_convex₂
statement: formalized
proof: formalized
---

# exists_cont_diff_of_convex₂

Let $E₁$, $E₂$ and $F$ be real vector spaces. Assume $E₁$ and $E₂$ are finite dimensional. Let $n$ be a natural number or $+\infty$. Let $P$ be a property of pairs $(x, f)$ with $x ∈ E₁$ and $f : E₂ → F$. Assume that, for every $x$, the space of functions $f$ such that $P(x, f)$ holds is convex. Assume that for every $x₀$ in $E₁$ there is a neighborhood $U$ of $x₀$ and a function $φ : E₁ × E₂ → F$ which is $C^n$ on $U × E₂$ and such that $P(x, φ(x, \cdot))$ holds for every $x$ in $U$. There there is a global $C^n$ function $φ \!: E₁ × E₂ → F$ such that $P(x, φ(x, \cdot))$ holds for every $x$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is completely analogous to the previous proof.

## Lean

Formalized as [`exists_contDiff_of_convex₂`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/exists_contDiff_of_convex₂).

## Sources

- [Sphere eversion blueprint: loops.tex, line 605](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L605)
