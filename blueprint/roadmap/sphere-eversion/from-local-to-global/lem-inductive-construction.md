---
declaration: lemma
origin: cited
lean: inductive_construction
statement: formalized
proof: formalized
---

# inductive_construction

Let $X$ be a topological space and $Y$ be any set. Let $U$ be a locally finite family of subsets of $X$ indexed by some $\mathcal{I}_{N}$. Let $P₀$ be a local predicate on functions from $X$ to $Y$, let $i ↦ P₁^i$ be a family of such predicates, and let $i ↦ P₂^i$ be a family of predicates on functions from $X$ to $Y$, all families being indexed by $\mathcal{I}_{N}$. Assume that

- there exists $f₀ \!: X → Y$ satisfying $P₀$ and $P₂^0$ ;
- for every $i$ in $\mathcal{I}_{N}$ and every $f \!: X → Y$ satisfying $P₀$, $P₂^i$ and every $P₁^j$ for $j < i$, there exists a function $f' \!: X → Y$ which coincides with $f$ outside $U_i$ and satisfies $P₀$ and every $P₁^j$ for $j ≤ i$ as well as $P₂^{S(i)}$ unless $i$ is maximal.

Then there exists $f \!: X → Y$ which satisfies $P₀$ and all $P₁^i$'s.

## Depends on

- [germ](def-germ.md)

## Proof depends on

- [exists_forall_eventually_of_index_type](lem-exists-forall-eventually-of-index-type.md)

## Proof

The main assumption from the lemma allows to build by induction a sequence $f$ of functions from $X$ to $Y$ indexed by $\mathcal{I}_{N}$ such that, for every $n ∈ \mathcal{I}_{N}$,

- $f_n$ satisfies $P₀$
- for every $i ≤ n$, $f_n$ satisfies $P₁^i$.
- $f_{S(n)}$ satisfies $P₂$ unless $n$ is maximal.
- $f_{S(n)}$ coincides with $f_n$ outside $U_{S(n)}$.

Note that the first term of this sequence isn't $f₀$ but the function obtained by applying the induction assumption to $f₀$.

The preceding lemma applied to this sequence gives a map $f$ which locally coincides with every element which is far enough in the sequence. Let $x$ be a point in $X$. Let $n$ be large enough to ensure $f$ coincides with $f_n$ near $x$. By definition this means $[f]_x = [f_n]_x$ and we know $P₀ [f_n]_x$ hence we get $P₀ [f]_x$. Now fix also $n$ in $\mathcal{I}_{N}$. Let $n'$ be large enough to be larger than $n$ and such that $[f]_x = [f_{n'}]_x$. Since $n' ≥ n$ we have $P₁^n [f_{n'}]_x$ hence $P₁^n [f]_x$.

## Lean

Formalized as [`inductive_construction`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/inductive_construction).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 117](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L117)
