---
declaration: lemma
origin: cited
---

# Useful elements

One can assign $c_{y,b} \in \mathbb{Z}$ for each $y = (a,c,n) \in G'$ and $b \in \mathbb{Z}$ with the following properties:

- (i) For all $y = (a,c,n) \in G'$ and $b \in \mathbb{Z}$, $c_{y,b} \neq a,b,c$ and $L_a L_{c_{y,b}} b = c_{y,b}$.
- (ii) For all $y \in G'$, the map $b \mapsto c_{y,b}$ is injective.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $y = (a,c,n)$. By [Base magma](1516-base.md) (iii), we can find $c_{y,a} \neq a,c$ such that $L_a R_a c_{y,a} = c_{y,a}$, or equivalently $L_a L_{c_{y,a}} a = c_{y,a}$. Next, for any $b \neq a$, we can apply [Base magma](1516-base.md) (ii) to find $c_{y,b} \neq b, c, c_{y,a}$ such that $R_a c_{y,b} = b$; note that as $R_a a = Sa = a \neq b$, this also implies that $c_{y,b} \neq a$, and that the $c_{y,b}$ are distinct as $b$ variables. We now have $L_a L_{c_{y,b}} b = L_{Sa} L_{c_{y,b}} L_{c_{y,b}} a = c_{y,b}$ for such $b$, giving the claim.

## Sources

- [Equational Theories blueprint: chapter/1516.tex, line 84](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1516.tex#L84)
