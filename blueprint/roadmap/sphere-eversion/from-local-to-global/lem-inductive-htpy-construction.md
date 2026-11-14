---
declaration: lemma
origin: cited
lean: inductive_htpy_construction
statement: formalized
proof: formalized
---

# inductive_htpy_construction

Let $X$ be a topological space and $Y$ be any set. Let $P₀$ and $P₁$ be local predicates on maps from $X$ to $Y$. Let $P₀'$ be a local predicate on maps from $ℝ × X → Y$. Assume that for every $a$, $b$ and $t$ in $ℝ$, every $x$ in $X$ and every $f \!: ℝ × X → Y$, if $f$ satisfies $P₂$ at $(at + b, x)$ then $(t, x) ↦ f(at+b, x)$ satisfies $P₀'$ at $(t, x)$. Let $f₀ \!: X → Y$ be a function satisfying $P₀$ and such that $(t, x) ↦ f₀(x)$ satisfies $P₀'$.

Let $K$ and $U$ be families of subsets of $X$ indexed by some $\mathcal{I}_{N}$. Assume that $U$ is locally finite and $K$ covers $X$.

Assume that, for every $i$ in $\mathcal{I}_{N}$ and every $f \!: X → Y$ satisfying $P₀$ and satisfying $P₁$ on $\bigcup_{j < i} K_j$, there exists $F \!: ℝ × X → Y$ such that

- for all $t$, $F(t, \cdot)$ satisfies $P₀$
- $F$ satisfies $P₀'$
- $F(1, \cdot)$ satisfies $P₁$ on $\bigcup_{j ≤ i} K_j$
- $F(t, x) = f(x)$ whenever $x$ is not in $U_i$ or $t$ is near $(-∞, 0]$
- $F(t, x) = F(1, x)$ whenever $t$ is near $[1, +∞)$.

Then there exists $F \!: ℝ × X → Y$ such that

- for all $t$, $F(t, \cdot)$ satisfies $P₀$
- $F$ satisfies $P₀'$
- $F(0, \cdot) = f₀$
- $F(1, \cdot)$ satisfies $P₁$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [inductive_construction](lem-inductive-construction.md)
- [restrict_germ_predicate](def-restrict-germ-predicate.md)

## Proof

Carefully checking all details is a bit technical but the strategy is as follows. We fix an increasing sequence $T \!: \mathcal{I}_{N} → [0, 1)$ starting at $0$, say $i ↦ 1 - 1/2^i$. We want to build a sequence of homotopies $F_i \!: ℝ × X → Y$ where each $F_i$ is time-independent on $[T_i, + ∞) × X$ and, assuming $i$ isn't maximal, $F_{S(i)}$ is built from $F_i$ by applying the induction assumption to $F_i(T_i, \cdot)$ and rescaling the obtained homotopy by the affine map sending $[0, 1]$ to $[T_i, T_{S(i)}]$.

Hence we want to apply [Lemma inductive_construction](lem-inductive-construction.md) with source space $\hat{X} = ℝ × X$. We use as the background local predicate $\hat{P}₀$ at $(t, x)$ the constraint on a function $F$ that $F(t, \cdot)$ satisfies $P₀$ at $x$ and $P₀'$ at $(t, x)$ and if $t = 0$ then $F(t, x) = f₀(x)$. As the target family of local predicates $\hat{P}₁$ we use for every $i ∈ \mathcal{I}_{N}$ the constraint on $F$ at $(t, x)$ that if $t = 1$ and $x$ is near $K_i$ then $F(t, \cdot)$ should satisfy $P₂$ at $x$. As the auxiliary family of predicates $\hat{P₂}$ at index $i$ we use the constraint of being time-independent on $[T_i, + ∞) × X$.

In order to explain how the induction assumption of the current lemma implies the induction assumption of [Lemma inductive_construction](lem-inductive-construction.md), we fix $i ∈ \mathcal{I}_{N}$ and a map $F \!: ℝ × X → Y$ that satisfies $\hat{P}₀$, is time-independent on $[T_i, + ∞) × X$ and satisfies $\hat{P}₁^j$ for all $j < i$. By this last requirement and the time independence property, we get that $F(T_i, \cdot)$ satisfies $P₁$ near $\bigcup_{j < i} K_j$. Our induction assumption applied to $F(T_i, \cdot)$ then gives $F' \!: ℝ × X → Y$ such that

- for all $t$, $F'(t, \cdot)$ satisfies $P₀$
- $F'$ satisfies $P₀'$
- $F'(1, \cdot)$ satisfies $P₁$ on $\bigcup_{j ≤ i} K_j$
- $F'(t, x) = f(x)$ whenever $x$ is not in $U_i$ or $t$ is near $(-∞, 0]$
- $F'(t, x) = F(1, x)$ whenever $t$ is near $[1, +∞)$.

As the new map required by the inductive assumption of [Lemma inductive_construction](lem-inductive-construction.md), we pick

$$
F'' \!: (t, x) ↦
\begin{cases}
F(t, x) \text{ if $t ≤ T_i$}\\
F'\left((t - T_i)/(T_{S(i)} - T_i), x\right) \text{ if $t > T_i$}
\end{cases}
$$

Fully checking that $F''$ is suitable is fairly technical but mostly straightforward. Care is required in particular to check that $F''$ coincides with $F$ near $(T_i, x)$ for every $x$. This uses both the fact that $F$ is time-independent on $[T_i, + ∞) × X$ and that $F'$ is time-independent near $(-∞, 0] × X$ hence in particular near $(0, x)$.

## Lean

Formalized as [`inductive_htpy_construction`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/inductive_htpy_construction).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 178](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L178)
