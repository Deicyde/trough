---
declaration: lemma
origin: cited
lean: LocallyFinite.exists_forall_eventually_of_indexType
statement: formalized
proof: formalized
---

# exists_forall_eventually_of_index_type

Let $X$ be a topological space and let $Y$ be any set. Let $f$ be a sequence of functions from $X$ to $Y$ indexed by $\mathcal{I}_{N}$ for some $N$. Let $V$ be a family of subsets of $X$ indexed by $\mathcal{I}_{N}$ such that, for every non-maximal $n$, $f_{S(n)}$ coincides with $f_n$ outside $V_{S(n)}$. If $V$ is locally finite then there exists $F \!: X → Y$ such that, for every $x$ and every sufficiently large $n$, $F$ coincides with $f_n$ near $x$.

## Depends on

- [index_type](def-index-type.md)

## Proof

The assumption that $V$ is locally finite gives, for every $x$ in $X$, a subset $U_x$ of $X$ such that $U_x$ is a neighborhood of $x$ and intersects only finite many $V_n$'s. In particular we can find an upper bound $n₀(x)$ of the set of indices $n$ in $\mathcal{I}_{N}$ such that $V_n$ intersects $U_X$. Since, for every non-maximal $n$, $f_{S(n)}$ coincides with $f_n$ outside $V_{S(n)}$, we get by induction that, for all $n ≥ n₀(x)$, $f_n$ coincides with $f_{n₀(x)}$ on $U_x$.

We now define $F$ as $x ↦ f_{n₀(x)}(x)$. We claim that, for every $x$, $F$ coincides with $f_n$ on $U_x$ as soon as $n$ is at least $n₀(x)$. Indeed let us fix $x$ and $n ≥ n₀(x)$ and $y ∈ U_x$. We have

$$
\begin{aligned}
f_n(y) &= f_{n₀(x)}(y) \text{ since $n ≥ n₀(x)$ and $y ∈ U_x$}\\
&= f_{\max(n₀(x), n₀(y))}(y) \text{ since $\max(n₀(x), n₀(y)) ≥ n₀(x)$ and $y ∈ U_x$}\\
&= f_{n₀(y)}(y) \text{ since $\max(n₀(x), n₀(y)) ≥ n₀(y)$ and $y ∈ U_y$}\\
&= F(y) \text{ by definition of $F$}.
\end{aligned}
$$

## Lean

Formalized as [`LocallyFinite.exists_forall_eventually_of_indexType`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/LocallyFinite.exists_forall_eventually_of_indexType).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 36](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L36)
