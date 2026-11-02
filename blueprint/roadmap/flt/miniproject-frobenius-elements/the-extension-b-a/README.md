# The extension $B/A$.

The precise set-up we'll work in is the following. We fix $G$ a finite group acting on $B$ a commutative ring, and we have another commutative ring $A$ such that $B$ is an $A$-algebra and the image of $A$ in $B$ is precisely the $G$-invariant elements of $B$. We don't ever need the map $A\to B$ to be injective so we don't assume this.

We start with a construction which is fundamental to everything, and which explains why we need $G$ to be finite.

- [MulSemiringAction.charpoly](mulsemiringaction-charpoly.md)

Clearly $F_b$ is a monic polynomial.

- [MulSemiringAction.monic\_charpoly](mulsemiringaction-monic-charpoly.md)

It's also clear that $F_b$ has degree $|G|$ and has $b$ as a root. Also $F_b$ is $G$-invariant, because acting by some $\gamma\in G$ just permutes the order of the factors. Hence we can descend $F_b$ to a monic polynomial $M_b(X)$ of degree $|G|$ in $A[X]$. We will also refer to $M_b$ as the characteristic polynomial of $b$, even though it's not even well-defined if the map $A\to B$ isn't injective.

- [Algebra.IsInvariant.charpoly\_mem\_lifts](algebra-isinvariant-charpoly-mem-lifts.md)
- [Algebra.IsInvariant.isIntegral](algebra-isinvariant-isintegral.md)
