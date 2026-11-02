---
declaration: proposition
origin: cited
---

# Obtaining Axiom B

There exists a way to extend $L_b: \mathbb{Z} \to \mathbb{Z}$ to $L_b: G \to G$ for all $b \in \mathbb{Z}$, in such a way that Axiom B holds, and furthermore for each $b \in \mathbb{Z}$ and $x \in G'$, the set $\{ y \in G': L_b y = x \}$ is infinite. Also, we can ensure that $L_b x \neq x$ for any $b \in \mathbb{Z}$ and $x \in G'$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By iterating [First extension](first-ext.md) and [Second extension](second-ext.md) in alternation, we can find an increasing chain of partial solutions with the property that for any $y = (a,c,n) \in G'$ and $c' \in \mathbb{Z}$ and any natural number $k$, excluding the case where $c'=a$ and $n=0$, that one can find a partial solution on this chain for which $L_{c'} y$ is defined, and such that $L_{c'} z = y$ for at least $k$ distinct choices of $z \in G'$. Taking the limit of this chain, we can then find a fully defined operation $L_{c'} y$ for $c' \in \mathbb{Z}$ and $y \in G$ satisfying the properties (a)-(d), (f), (g) (but not (e)) of a partial solution, with the property that $y = (a,c,n) \in G'$ and $c' \in \mathbb{Z}$, excluding the case $c'=a$ and $n=0$, that there are infinitely many $z \in G'$ such that $L_{c'} z = y$. The excluded case $c'=a, n=0$ is also covered by property (b) of a partial solution. The claim follows.

## Sources

- [Equational Theories blueprint: chapter/1516.tex, line 147](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1516.tex#L147)
