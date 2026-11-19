---
declaration: lemma
origin: cited
lean: relative_inductive_construction_of_loc
statement: formalized
proof: formalized
---

# relative_inductive_construction_of_loc

Let $X$ a second countable locally compact metrizable topological space. Let $P₀$ and $P₁$ be local predicates on functions from $X$ to a set $Y$. Let $K$ be a closed subset of $X$. Let $f₀ \!: X → Y$ be a function satisfying $P₀$ and satisfying $P₁$ near $K$. Assume that

- For every $x$ in $X$, there exists a function $f \!: X → Y$ which satisfies $P₀$ and satisfies $P₁$ near $x$.
- For every closed subsets $K₁$ and $K₂$ of $X$ and every open subsets $U₁$ and $U₂$ containing $K₁$ and $K₂$, for every function $f₁$ and $f₂$ satisfying $P₀$, if $f₁$ satisfies $P₁$ on $U₁$ and if $f₂$ satisfies $P₁$ on $U₁$ then there exists $f$ which satisfies $P₀$, and satisfies $P₁$ near $K₁ ∪ K₂$ and coincides with $f₁$ near $K₁ ∪ U₂^c$.

Then there exists $f$ which satisfies $P₀$ and $P₁$ and coincides with $f₀$ near $K$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [inductive_construction_of_loc](lem-inductive-construction-of-loc.md)

## Proof

We reduce this to [Lemma inductive_construction_of_loc](lem-inductive-construction-of-loc.md) using as auxilliary local predicate $P₀'$ the constraint to coincide with $f₀$ near $K$.

Our patching condition almost matches the one from [Lemma inductive_construction_of_loc](lem-inductive-construction-of-loc.md) except that each $(K₁, K₂, U₁, U₂)$ should be replaced by $(K ∪ K₁, U ∪ U₁, K₂, U₂)$ where $U$ is a suitable neighborhood of $K$.

## Lean

Formalized as [`relative_inductive_construction_of_loc`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/relative_inductive_construction_of_loc).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 344](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L344)
