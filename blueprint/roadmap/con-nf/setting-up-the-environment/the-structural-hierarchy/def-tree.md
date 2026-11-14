---
declaration: definition
origin: cited
lean: ConNF.Tree
statement: formalized
---

# tree

Let $\tau$ be any type, and let $\alpha$ be a type index. An *$\alpha$-tree of $\tau$* is a function $t$ that maps each $\alpha$-extended index $A$ to an object $t_A : \tau$; this defines its base derivatives. The type of $\bot$-trees of $\tau$ is canonically isomorphic to $\tau$. If $t$ is an $\alpha$-tree and $A : \alpha \rightsquigarrow \beta$, we define the derivative $t_A$ to be the $\beta$-tree defined by $(t_A)_B = t_{(A_B)}$. This derivative map is functorial: for any paths $A : \alpha \rightsquigarrow \beta$ and $B : \beta \rightsquigarrow \gamma$, we have $t_{(A_B)} = (t_A)_B$. If $\tau$ has a group structure, then so does its type of trees: $(t \cdot u)_A = t_A \cdot u_A$ and $(t^{-1})_A = (t_A)^{-1}$. If $\tau$ acts on $\upsilon$, then $\alpha$-trees of $\tau$ act on $\alpha$-trees of $\upsilon$: $(t(u))_A = t_A(u_A)$.

If $\#\tau \leq \#\mu$, there are at most $\#\mu$-many $\alpha$-trees of $\tau$, since there are less than $\operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu))$-many $\alpha$-extended indices, allowing us to conclude by [mathlib](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L104) as each such tree is a subset of $(\alpha \rightsquigarrow \bot) \times \tau$ of size less than $\operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu))$. If $\#\tau < \#\mu$, there are less than $\#\mu$-many $\alpha$-trees of $\tau$, since there are less than $\operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu))$-many $\alpha$-extended indices and strong limits are closed under exponentials.

## Depends on

- [path](def-path.md)

## Lean

Formalized as [`ConNF.Tree`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Tree).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 184](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L184)
