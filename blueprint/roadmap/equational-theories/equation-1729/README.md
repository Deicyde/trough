# Equation 1729

In this chapter we study magmas that satisfy equation 1729,

$$
x = (y \diamond y) \diamond ((y \diamond x) \diamond y).
$$

for all $x,y$. Using the squaring operator $Sy := y \diamond y$ and the left and right multiplication operators $L_y x := y \diamond x$ and $R_y x = x \diamond y$, this law can be written as

$$
L_{Sy} R_y L_{y} x = x.
$$

This implies that $L_y$ is injective and $L_{Sy}$ is surjective, hence $L_{Sy}$ is invertible. If $y$ is a square (i.e., $y \in SM$), then $L_y$ and $L_{Sy}$ are both invertible, hence now $R_y$ is also invertible, with inverse $R_y^{-1} = L_y L_{Sy}$. We rewrite this as

$$
L_y = R_y^{-1} L_{Sy}^{-1}
$$

for all $y \in SM$.

We have the following procedure for extending a small magma $SM$ satisfying 1729 to a larger one $M$:

- [Extending a 1729 magma](mag.md)
- [Definition of $SM$](sm-def.md)
- [Basic properties of $SM$](sm-1729.md)
- [Definition of $N$](n-def.md)
- [Basic properties of $N$](n-prop.md)
- [Definition of $R'_a$](ra-defn.md)
- [Basic properties of $R'_a$](ra-prop.md)
- [Using $L'_0$ to construct $L'_a$](l0-la.md)
- [Reduction to new axioms](eq1729-reduce-to-new-axioms.md)
- [Partial solution](part-sol.md)
- [Existence of partial solution](partial-exist.md)
- [Chain of partial solutions](chain.md)
- [Enlarging $L'_0$](enlarge-l0.md)
- [Enlarging $L'_0$ many times](enlarge-l0-many.md)
- [Enlarging $S'$ with induction hypothesis and axioms](enlarge-s-induct-axioms.md)
- [Enlarging $S'$ with induction hypothesis](enlarge-s-induct.md)
- [Enlarging $S'$](enlarge-s.md)
- [Enlarging $\diamond$](enlarge-op.md)
- [1729 does not imply 817](1729-refute-817.md)
