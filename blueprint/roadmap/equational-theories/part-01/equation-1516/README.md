# Equation 1516

In this chapter we study magmas that satisfy equation 1516,

$$
x = (y \diamond y) \diamond (x \diamond (x \diamond y))\qquad\text{(1)}
$$

for all $x,y$. Using the squaring operator $Sy := y \diamond y$ and the left and right multiplication operators $L_y x := y \diamond x$ and $R_y x = x \diamond y$, this law can be written as

$$
L_{Sy} L_x L_x y = x.
$$

We begin by studying a greedily constructed translation invariant model

$$
x \diamond y = x+f(y-x)\qquad\text{(2)}
$$

on the carrier $\mathbb{Z}$ with some function $f:\mathbb{Z} \to \mathbb{Z}$ with $f(0)=0$. This ensures that $Sx = x$. If $y = x+h$, then $L_x y = x + f(h)$, $L_x^2 y = x + f^2(h)$, and $L_y L_x^2 y = y + f(f^2(h)-h)$, so the law (1) simplifies to

$$
f(f^2(h)-h) = -h.\qquad\text{(3)}
$$

Thus, if we let $E = \{ (h, f(h))\}$ be the graph of $f$, then we have the following property: if $(a,b), (b,c) \in E$, then $(c-a,-a) \in E$. This helps motivate the following definition.

- [1516 seed](1516-seed.md)

This definition has an extension property:

- [1516 extension](1516-ext.md)

For technical reasons (which will be helpful later when we expand the magma) we also give a variant that will ensure a useful “double surjectivity” property:

- [1516 extension variant](1516-ext-var.md)
- [Base magma](1516-base.md)

Note from (1) and the hypothesis $Sa=a$ that $R_a c = a$ if and only if $c=a$. Thus, the requirement that $a,b$ be distinct in (ii) is necessary.

*The proof of [Base magma](1516-base.md) is shown with its statement.*

Let us denote by $A$ the free group over $\mathbb{N}$. Note that a magma with the same properties as in [Base magma](1516-base.md) but having carrier $A$ can be constructed similarly. The same thing is true for the following results. In fact, the Lean implementation has $A$ whenever $\mathbb{Z}$ is; this has been done to reuse some preexisting code.

Now we construct a more complex 1516 magma, whose carrier $G$ is $\mathbb{Z} \cup G'$, where

$$
G' := \{ (a,c,n) \in \mathbb{Z} \times \mathbb{Z} \times \mathbb{N} : a \neq c\}.
$$

The first component $\mathbb{Z}$ will represent the squares, and the second component $G'$ will represent the non-squares. The most important coordinate of an element $(a,c,n)$ of $G'$ is $a$; the other two components $c,n$ are technical, with $n$ being needed to ensure a certain infinite surjectivity property, and $c$ being such that $L_c (a,c,n)$ remains at one's disposal to select at certain stages of the inductive process.

The 1516 magma constructed in [Base magma](1516-base.md) will be the restriction of $G$ to $\mathbb{Z}$; thus $a \diamond b$ is already defined in $G$ for $a,b \in \mathbb{Z}$, but the rest of the multiplication table is not currently defined. By construction, $S$ is already defined and equal to the identity on $\mathbb{Z}$, and we have the 1516 equation

$$
L_{Sa} L_b L_b a = b
$$

for $a,b \in \mathbb{Z}$, with the left multiplication operators $L_b$ currently only defined as maps from $\mathbb{Z}$ to $\mathbb{Z}$. Among other things, this means that $L_a = L_{Sa}$ is surjective as a map from $\mathbb{Z}$ to $\mathbb{Z}$ for any $a \in \mathbb{Z}$.

We extend the squaring map $S$ to all of $G$ by declaring $S(a,c,n) := a$, thus $S$ maps $G$ to $\mathbb{Z}$. To create a 1516 magma structure on all of $G$, we need to extend the left multiplication operators $L_b$, $b \in \mathbb{Z}$ as maps from $G$ to $G$, and also introduce additional maps $L_x: G \to G$ for $x \in G'$, satisfying the following axioms:

- Axiom A: For any $x \in G'$, $L_x x = Sx$.
- Axiom B: For any $x \in G'$ and $b \in \mathbb{Z}$, $L_{Sx} L_b L_b x = b$.
- Axiom C: For any $x \in G$ and $y \in G'$, $L_{Sx} L_y L_y x = y$.

We first address Axiom B, which purely concerns how to extend the $L_b$ operators for $b \in \mathbb{Z}$, and also impose an additional technical “infinitely surjective” requirement that will help us satisfy Axiom C later. We first need some preparatory lemmas. We begin by locating some useful elements $c_{y,b}$ of $\mathbb{Z}$ for all $y \in G'$ and $b \in \mathbb{Z}$.

- [Useful elements](aux.md)

Let $c_{y,b}$ be as above. Define a *partial solution* to be a partial assignment of $L_{c'} y \in G$ for $c' \in \mathbb{Z}$ and $y \in G$ that satisfies the following properties:

- (a) If $y \in \mathbb{Z}$, then $L_{c'} y$ agrees with the operation defined in [Base magma](1516-base.md).
- (b) If $y = (a,c,0) \in G'$, then $L_a y = a$.
- (c) If $y = (a,c,n) \in G'$ and $n \neq 0$, then $L_a y = (a,c,0)$.
- (d) If $y = (a,c,n) \in G'$ and $b \in \mathbb{Z}$, then $L_{c_{y,b}} y = b$.
- (e) For any $a,c$, $L_c (a,c,n)$ is only defined for finitely many $n$.
- (f) If $y = (a,c,n) \in G'$ and $c' \in \mathbb{Z}$ are such that $L_{c'} y$ is defined, then $L_{c'} L_{c'} y$ and $L_a L_{c'} L_{c'} y$ are defined, with $L_a L_{c'} L_{c'} y$ equal to $c'$.
- (g) If $y = (a,c,n) \in G'$ and $c' \in \mathbb{Z}$ are such that $c' \neq a$ and $L_{c'} y$ is defined, then $L_{c'} y \neq c'$.

- [Existence of partial solution](part-exist.md)

We can make $L_{c'} y$ defined in a partial solution:

- [First extension](first-ext.md)

We can also insert inverses of $L_{c'}$:

- [Second extension](second-ext.md)

Now we can establish Axiom B.

- [Obtaining Axiom B](axiom-b.md)

Finally, we construct the remaining $L_x$.

- [Obtaining Axioms A, C](axiom-c.md)
- [1516-no-255](1516-no-255.md)
