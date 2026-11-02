---
declaration: lemma
origin: cited
---

# obelix-extend

For any $E\in \mathscr{E}$ and any $a\in G$, there is an extension $E\subseteq E'\in \mathscr{E}$ where the functional equation holds for $a$.

## Depends on

- [partial-solution2](partial-solution2.md)

## Proof

**Case 1**: Assume $(a,b)\in E$ for some $b\in G$.

If $b\in {\rm dom}(E)$, then by condition (4) we are already done. So reduce to the case when $b\notin {\rm dom}(E)$. In particular, by (2) and (3) we know $a,b\neq 1$, and also by (6) we know that $ab^{-1}\notin {\rm dom}(E)\cup{\rm im}(E)$ (and is not $1$).

Take $c$ to be a generator of $G$ not appearing in the reduced form of any entry in $E$, and set $E':=E\cup\{(b,c),(cb^{-1},ab^{-1}\}$. Conditions (1), (3), and (5) are immediate. Condition (2) is also clear, where injectivity needs $ab^{-1}\notin {\rm im}(E)$. Condition (4) is also easy to check, using the fact that $E$ is injective, $cb^{-1}\neq c$, and $ab^{-1}\notin {\rm dom}(E)$.

Finally, for condition (6), a finite check works. The main case is checking that $ca^{-1}\notin {\rm dom}(E')\cup {\rm im}(E')$. This is clear since $a\neq 1$ and $a\neq b$ (by condition (5) for $E$). One should also note that by condition (5) (and the fact that $E$ is a function), there is no pair $(x,y)\in E$ with $(x,y)\neq (a,b)$ and $xy^{-1}=ab^{-1}$, so we don't ruin condition (6) for pairs already in $E$.

**Case 2**: Assume $a\notin {\rm dom}(E)$. If $(x,a)\in E$ for some (unique by (2)) $x\in G$, then applying Case 1 to $x$, we reduce to the case when $a\in {\rm dom}(E)$.

Thus, we may consider the case when $a\notin {\rm dom}(E)\cup {\rm im}(E)$. If $(x,y)\in E$ with $xy^{-1}=a$, then by applying Case 1 to $x$, we get $a\in {\rm im}(E)$, and reduce to a previously considered case. So, we may assume there is no such pair $(x,y)$. Fixing $b$ to be a generator of $G$ not appearing in the reduced forms for the entries in $E$, nor in $a$, then after passing to $E\cup\{(a,b)\}\in \mathscr{E}$ we again reduce to Case 1.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 233](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L233)
