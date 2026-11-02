# Equation 1729

In this chapter we study magmas that satisfy equation 1729,

$$
x = (y \diamond y) \diamond ((y \diamond x) \diamond y).\qquad\text{(1)}
$$

for all $x,y$. Using the squaring operator $Sy := y \diamond y$ and the left and right multiplication operators $L_y x := y \diamond x$ and $R_y x = x \diamond y$, this law can be written as

$$
L_{Sy} R_y L_{y} x = x.
$$

This implies that $L_y$ is injective and $L_{Sy}$ is surjective, hence $L_{Sy}$ is invertible. If $y$ is a square (i.e., $y \in SM$), then $L_y$ and $L_{Sy}$ are both invertible, hence now $R_y$ is also invertible, with inverse $R_y^{-1} = L_y L_{Sy}$. We rewrite this as

$$
L_y = R_y^{-1} L_{Sy}^{-1}\qquad\text{(2)}
$$

for all $y \in SM$.

We have the following procedure for extending a small magma $SM$ satisfying (1) to a larger one $M$:

- [Extending a 1729 magma](mag.md)

To build a magma satisfying 1729 but not 817, it thus suffices to produce

- a 1729 magma $SM$;
- a set $N$ of “non-squares”;
- a squaring map $S': N \to SM$;
- bijections $L'_a, R'_a: N \to N$ for all $a \in SM$ satisfying the axioms (i)-(iv); and
- an operation $\diamond': N \times N \to SM \uplus N$ satisfying the axioms (v)-(vii).

The magma $SM$ is defined as follows:

- [Definition of $SM$](sm-def.md)
- [Basic properties of $SM$](sm-1729.md)

We now define $N$, as well as some Cayley graph structures on it.

- [Definition of $N$](n-def.md)
- [Basic properties of $N$](n-prop.md)

We will define the right multiplication operators $R'_a: N \to N$ using the group action:

- [Definition of $R'_a$](ra-defn.md)
- [Basic properties of $R'_a$](ra-prop.md)

We defer construction of the squaring map $S': N \to SM$ for now, but turn to left-multiplication. From two applications of (2) and the exponent 4 hypothesis we have

$$
L'_a = (R'_a)^{-1} (L'_{2a})^{-1} = (R'_a)^{-1} L'_0 R'_{2a}.
$$

Thus, once $L'_0$ is specified, we can *define* $L'_a$ for all other $a \in SM$ by the rule

$$
L'_a := (R'_a)^{-1} L'_0 R'_{2a}.\qquad\text{(4)}
$$

Furthermore, from the $a=0$ case of (2) we must also have the axiom

- (i') $(L'_0)^2 = (R'_0)^{-1}$.

Conversely, we have

- [Using $L'_0$ to construct $L'_a$](l0-la.md)

We now write the other remaining axioms in terms of $L'_0$ rather than $L'_a$ using (4), [(5)](l0-la.md), [(3)](ra-defn.md), and the magma law on $SM$:

- (iii') If $R'_a x = y$ for some $a \in SM$ and some $x,y \in N$, then $(R'_{S'y})^{-1} L'_0 R'_{2S'y} (R'_{a - S'x})^{-1} L'_0 R'_{2(a - S'x)} y = x$.
- (iv') For all $x \in N$, we have $(R'_{S'x})^{-1} L'_0 R'_{2S'x} (R'_{S'x})^{-1} L'_0 R'_{2S'x} x = x$.
- (v) For all $x \in N$, we have $x \diamond' x = S'x$.
- (vi') For all $y \in N$ and $a \in SM$, we have $e_a y \diamond' y = a - S'y$.
- (vii') For all $x,y \in N$ with $x \diamond' y$ not already covered by rules (v) or (v'), we have $x \diamond' y = z$ for some $z \in N$. Furthermore, $z \diamond' x = (R'_{2S'x})^{-1} L'_0 e_0 e_{S'x} y$.

- [Reduction to new axioms](eq1729-reduce-to-new-axioms.md)

Our task is now to find a function $S': N \to SM$, a bijection $L'_0: N \to N$, and an operation $\diamond': N \times N \to M$ satisfying axioms (i'), (iii'), (iv'), (v), (vi'), (vii').

We will again use a greedy construction for this, but with some modifications. Firstly, the axiom (i'), together with [(3)](ra-defn.md) means that we cannot restrict $L'_0$ to be partially defined on just finitely many values: any relation of the form

$$
L'_0 x = y
$$

for some $x,y \in N$ would automatically imply that

$$
L'_0 (R'_0)^n x = (R'_0)^n y\qquad\text{(6)}
$$

and also

$$
L'_0 (R'_0)^n y = (R'_0)^{n-1} x\qquad\text{(7)}
$$

for all $n \in \mathbb{Z}$. Thus, $L'_0$ becomes defined on two right cosets $\langle e_0 \rangle x$, $\langle e_0 \rangle y$ of $N$, where $\langle e_0 \rangle := \{ e_0^n: n \in \mathbb{Z}\}$ is an infinite cyclic subgroup of $N$. In general, we will require that $L'_0$ is defined on a finite union of cosets of $\langle e_0\rangle$.

In a somewhat similar vein, axiom (vii'), if iterated naively, would mean that a given entry $x \diamond' y = z$ of the multiplication table could potentially generate an infinite sequence of further entries, which unfortunately do not have as regular a pattern as the iterations (6), (7) of axiom (i'). So we will need to truncate this iteration by creating an addition category of “pending” identities $I[x,y,z]$ of the form “$z \diamond' x = (R'_{2S'x})^{-1} L'_0 R'_0 e_{S'x} y$” for some $x,y,z \in N$, which will be temporarily undefined because $S'x$ is undefined. More precisely,

- [Partial solution](part-sol.md)
- [Existence of partial solution](partial-exist.md)
- [Chain of partial solutions](chain.md)

Now we seek to enlarge a partial solution. We first make an easy observation:

- [Enlarging $L'_0$](enlarge-l0.md)

As a corollary, we have

- [Enlarging $L'_0$ many times](enlarge-l0-many.md)

Next, we provide a tool for enlarging the domain of definition of $S'$. The main step is the following inductive one with extra axioms.

- [Enlarging $S'$ with induction hypothesis and axioms](enlarge-s-induct-axioms.md)
- [Enlarging $S'$ with induction hypothesis](enlarge-s-induct.md)

As a corollary, we have

- [Enlarging $S'$](enlarge-s.md)

Finally, we give a tool for enlarging $\diamond$:

- [Enlarging $\diamond$](enlarge-op.md)
- [1729 does not imply 817](1729-refute-817.md)
