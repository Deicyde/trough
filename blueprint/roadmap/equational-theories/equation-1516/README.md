# Equation 1516

In this chapter we study magmas that satisfy equation 1516,

$$
x = (y \diamond y) \diamond (x \diamond (x \diamond y))
$$

for all $x,y$. Using the squaring operator $Sy := y \diamond y$ and the left and right multiplication operators $L_y x := y \diamond x$ and $R_y x = x \diamond y$, this law can be written as

$$
L_{Sy} L_x L_x y = x.
$$

We begin by studying a greedily constructed translation invariant model

$$
x \diamond y = x+f(y-x)
$$

on the carrier $\mathbb{Z}$ with some function $f:\mathbb{Z} \to \mathbb{Z}$ with $f(0)=0$. This ensures that $Sx = x$. If $y = x+h$, then $L_x y = x + f(h)$, $L_x^2 y = x + f^2(h)$, and $L_y L_x^2 y = y + f(f^2(h)-h)$, so the law 1516 simplifies to

$$
f(f^2(h)-h) = -h.
$$

Thus, if we let $E = \{ (h, f(h))\}$ be the graph of $f$, then we have the following property: if $(a,b), (b,c) \in E$, then $(c-a,-a) \in E$. This helps motivate the following definition.

- [1516 seed](1516-seed.md)
- [1516 extension](1516-ext.md)
- [1516 extension variant](1516-ext-var.md)
- [Base magma](1516-base.md)
- [Useful elements](aux.md)
- [Existence of partial solution](part-exist.md)
- [First extension](first-ext.md)
- [Second extension](second-ext.md)
- [Obtaining Axiom B](axiom-b.md)
- [Obtaining Axioms A, C](axiom-c.md)
- [1516-no-255](1516-no-255.md)
