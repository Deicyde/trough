---
declaration: lemma
origin: cited
lean: nice_atlas
statement: formalized
proof: formalized
---

# nice_atlas

Let $M$ be a manifold modelled on the normed space $E$ and $(V_j)_{j ∈ J}$ a cover of $M$ by open sets. There exists some natural number $N$ and a family of smooth open embeddings $φ : \mathcal{I}_{N} × E → M$ such that

- for each $i$ there is some $j$ such that $φ_i(E) \subseteq V_j$,
- $i ↦ φ_i(E)$ is a locally-finite collection of sets in $M$,
- $⋃_i φ_i(B_E(0, 1)) = M$ where $B_E(0, 1)$ is the open unit ball in $E$.

## Depends on

- [index_type](../../from-local-to-global/def-index-type.md)

## Proof

The proof is a standard compact-exhaustion argument. Let $K_0, K_1, K_2, \ldots$ be a compact exhaustion of $M$ and define:

$$
\begin{aligned}
C_n &= K_{n+2} \smallsetminus K_{n+1}^o,\\
U_n &= K_{n+3}^o \smallsetminus K_n.
\end{aligned}
$$

Thus:

- $C_n$ is compact,
- $U_n$ is open,
- $C_n \subseteq U_n$,
- $\bigcup_n C_n = M$,
- $U_n \cap U_m = \emptyset$ if $|n - m| > 2$.

For any $y \in E$ and $r > 0$, fix a smooth diffeomorphism $f_{y,r} : E \simeq B_E(y, r)$ such that $f_{y,r}(0) = y$. For each $n$ and $x \in C_n$, let $\psi_x$ be a smooth chart mapping an open neighbourhood of $x$ to an open set of the model space $E$. Writing $y = \psi_x (x) \in E$, let:

$$
\begin{aligned}
B_{n, x} &= \psi_x^{-1} (B_E(y, r)),\\
W_{n, x} &= \psi_x^{-1} (f_{y,r} (B_E (0, 1))),\\
\end{aligned}
$$

for some $r > 0$ (which may depend on $n$, $x$) sufficiently small that:

- $B_E(y, r)$ lies in the target of the chart $\psi_x$,
- $B_{n,x}$ is contained in $U_n$,
- $B_{n,x}$ is contained in $V_j$ for some $j$.

Note that $x \in W_{n,x}$. For each $n$, choose a finite subcovering of $C_n$ by $W_{n, x_1}, \ldots, W_{n, x_{l_n}}$ and define $\iota \subseteq ℕ \times M$ by:

$$
\begin{aligned}
\iota = \bigcup_n \{ (n, x_1), \ldots, (n, x_{l_n}) \} .
\end{aligned}
$$

Note that $\iota$ is countable and furthermore:

- for each $i \in \iota$, there is some $j$ such that $B_i \subseteq V_j$,
- $(B_i)_{i \in \iota}$ is locally-finite (indeed more is true: $B_i$ meets only finitely-many $B_{i'}$ for $i, i' \in \iota$ since $B_{m, x} \cap B_{n, x'} = \emptyset$ if $|n - m| > 2$),
- $(W_i)_{i \in \iota}$ covers $M$.

Given $i = (n, x_j) \in \iota$, the required map $\phi_i : E \to M$ is just:

$$
\begin{aligned}
E \simeq B_E(y_j, r) \simeq B_{n,j} \subseteq M.
\end{aligned}
$$

Since $ι$ is countable, it is in bijection with some $\mathcal{I}_{N}$.

## Lean

Formalized as [`nice_atlas`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/nice_atlas).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 97](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L97)
