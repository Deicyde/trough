---
declaration: lemma
origin: cited
---

# Second extension

Suppose we have a partial solution, and let $c' \in \mathbb{Z}$ and $y = (a,c,n) \in G$. Then, unless one is in the case when $c'=a$ and $n=0$, then one can find $z \in G$ such that $L_{c'} z$ is currently undefined, but for which one can find an extension of the partial solution for which $L_{c'} z$ is now equal to $y$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Write $y = (a,c,n)$. There are several cases.

- Case 1: $L_{c'} y = w$ for some $w \in G'$. By Lemma [Useful elements](aux.md), $c_{w,c'}$ is distinct from $c'$, and from property (d) of a partial solution, $L_{c_{w,c'}} w = c'$. By property (e) of a partial solution, we can find $z = (c_{w,c'}, c', n')$ such that $L_{c'} z$ is currently undefined. Then set $L_{c'} z := y$, so that we have $L_{c_{w,c'}} L_{c'} L_{c'} z = c'$. One then verifies that all the axioms (a)-(g) of a partial solution are valid in this case.
- Case 2: $c' \neq a$ and $L_{c'} y = b$ for some $b \in \mathbb{Z}$. By property (g) of a partial solution, $c' \neq b$. By [Base magma](1516-base.md), we can find $a'$ such that $L_{a'} b = R_b a' = c'$ and $a' \neq c'$. By property (e) of a partial solution, we can find $z = (a', c', n')$ such that $L_{c'} z$ is currently undefined. Then set $L_{c'} z = y$, so that we have $L_{a'} L_{c'} L_{c'} z = c'$. One then verifies that all the axioms (a)-(g) of a partial solution are valid in this case.
- Case 3: $c' \neq a$ and $L_{c'} y$ is currently undefined. Use Lemma [First extension](first-ext.md) set $L_{c'} y$ equal to some $b \in \mathbb{Z}$, then apply the Case 2 analysis.
- Case 4: $c' = a$. Because we are excluding the case $n=0$, we are now in Case 1 thanks to property (c) of a partial solution.

## Sources

- [Equational Theories blueprint: chapter/1516.tex, line 132](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1516.tex#L132)
