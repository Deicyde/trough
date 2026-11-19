---
declaration: lemma
origin: cited
lean: inductive_construction_of_loc
statement: formalized
proof: formalized
---

# inductive_construction_of_loc

Let $X$ a second countable locally compact metrizable topological space. Let $P₀$, $P₀'$ and $P₁$ be local predicates on function from $X$ to a set $Y$. Let $f₀ \!: X → Y$ be a function satisfying $P₀$ and $P₀'$. Assume that

- For every $x$ in $X$, there exists a function $f \!: X → Y$ which satisfies $P₀$ and satisfies $P₁$ near $x$.
- For every closed subsets $K₁$ and $K₂$ of $X$ and every open subsets $U₁$ and $U₂$ containing $K₁$ and $K₂$, for every function $f₁$ and $f₂$ satisfying $P₀$, if $f₁$ satisfies $P₀'$ and satisfies $P₁$ on $U₁$ and if $f₂$ satisfies $P₁$ on $U₂$ then there exists $f$ which satisfies $P₀$ and $P₀'$, and satisfies $P₁$ near $K₁ ∪ K₂$ and coincides with $f₁$ near $K₁ ∪ U₂^c$.

Then there exists $f$ which satisfies $P₀$, $P₀'$ and $P₁$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [inductive_construction](lem-inductive-construction.md)
- [exists_locally_finite_subcover_of_locally](lem-exists-locally-finite-subcover-of-locally.md)
- [restrict_germ_predicate](def-restrict-germ-predicate.md)

## Proof

The assumptions on the topology of $X$ and local existence of solutions allow to apply [Lemma exists_locally_finite_subcover_of_locally](lem-exists-locally-finite-subcover-of-locally.md) to get sequences of subsets $K$ and $U$ of $X$ indexed by natural numbers such that $K$ covers $X$, $U$ is locally finite and, for every $i$:

- $K_i$ is compact
- $U_i$ is open
- $K_i ⊂ U_i$
- there is a function $f \!: X → Y$ which satisfies $P₀$ and satisfies $P₁$ on $U_i$.

We then apply [Lemma inductive_construction](lem-inductive-construction.md) to the family of subsets $U$ with local predicates $\hat{P}₀$ combining $P₀$ and $P₀'$ and $\hat{P}₁^i$ asking that $P₁$ holds near $K_i$, and the trivial family of auxiliary predicates $\hat{P}'₀$.

For this we need to explain how the patching assumption of the current lemma implies the induction assumption of [Lemma inductive_construction](lem-inductive-construction.md). So we fix an index $i ∈ ℕ$ and a function $f$ which satisfies $\hat{P}₀$ and satisfies all $\hat{P}₁^j$ for $j < i$. We denote by $K$ the closed subset $\bigcup_{j < i} K_j$ and denote by $V$ an open neighborhood of $K$ such that $f$ satisfies $P₁$ on $V$. The patching assumption applied to $K$, $K_i$, $V$ and $U_i$ with functions $f$ and the local solution on $U_i$ gives a suitable new function.

## Lean

Formalized as [`inductive_construction_of_loc`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/inductive_construction_of_loc).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 294](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L294)
