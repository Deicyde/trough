---
declaration: proposition
origin: cited
lean: ConNF.Support.strong_strong
statement: formalized
proof: formalized
---

# exists_strong

For every support $S$, there is a strong support $T \succeq S$.

## Depends on

- [Strong](def-strong.md)

## Proof

We define a relation $R$ on pairs $(A, N)$ where $A : \beta \rightsquigarrow \bot$ and $N$ is a near-litter by the following constructor. If $I = (\gamma,\delta,\varepsilon,A)$ and $t : \mathsf{Tang}_\delta$, then for any near-litter $N_1$ such that $N_1^\circ = f_{\delta,\varepsilon}(t)$ and any path $B : \delta \rightsquigarrow \bot$ and near-litter $N_2 \in \operatorname{\mathsf{supp}}(t)_B^{\mathcal N}$, we define $((A_\delta)_B, N_2) \mathrel{R} ((A_\varepsilon)_\bot, N_1)$. This is well-founded, because if $(B, N_2) \mathrel{R} (A, N_1)$ then $\iota(N_2) < \iota(N_1)$. For any small set $s$ of such pairs, the transitive closure of $s$ under $R$ is small.

Let $S$ be a support, and let $s$ be the transitive closure of the set of pairs $(A, N)$ such that $N \in \operatorname{\mathsf{im}} S_A^{\mathcal N}$. Generate a support $T$ from $S$ and $s$ using the fact that every small set is the range of some enumeration. This satisfies the second condition of being a strong support.

Now, for any base support $T$, we define its *interference support* to be a base support $U$ consisting of just the atoms in the interference of all near-litters that appear in $T$. We may extend this definition to structural supports.

Finally, if $U$ is the interference support of the $T$ defined above, the support $T + U$ is strong, and since $S \succeq T$, we conclude $S \preceq T + U$.

## Lean

Formalized as [`ConNF.Support.strong_strong`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Support.strong_strong).

## Sources

- [Consistency of New Foundations blueprint: chapters/counting.tex, line 32](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/counting.tex#L32)
