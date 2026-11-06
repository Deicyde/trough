# Equation 677

In this chapter we study finite magmas that satisfy equation 677,

$$
x = y \diamond (x \diamond ((y \diamond x) \diamond y))\qquad\text{(1)}
$$

for all $x,y$, and whether this implies equation 255,

$$
x = ((x \diamond x) \diamond x) \diamond x.\qquad\text{(2)}
$$

Using the usual notation $L_y x = y \diamond x$, $R_y x = x \diamond y$, $Sx = x \diamond x$, we can rewrite equation 677 as

$$
x = L_y L_x L_{L_y x} y = L_y (x \diamond R_y L_y x)\qquad\text{(3)}
$$

and 255 as

$$
x = (Sx \diamond x) \diamond x.
$$

We have the following equivalent characterizations of 255:

This for instance gives the implication for linear magmas:

In fact the argument gives a stronger obstruction to refuting 255:

Linear models $x \diamond y = \alpha x + \beta y + c$ on the finite field $F_p$ turn out to be classified into two types:

- (Type 1) $\alpha=1-\beta$, $\beta$ is a primitive tenth root of unity, and $c=0$. (These models are also translation-invariant.)
- (Type 2) $\alpha$ is a primitive third root of unity, $c$ is arbitrary, and $\beta$ solves $\beta^3+\beta+1=-\alpha$ and $\beta^4+\beta^3+2\beta^2+2\beta+1=0$.

An example of a Type I model is $x \diamond y = 2x-y$ on $F_5$. Examples of Type II models include $x \diamond y = 4x+3y$ and $x \diamond y = 4x+y$ on $F_7$. An exceptional class of Type II models are $x \diamond y = 5x-4y+c$ on $F_{31}$, these are the only Type II models that are translation-invariant and do not have idempotents (if $c \neq 0$).

- [A finite non-right-cancellative example](a-finite-non-right-cancellative-example/README.md)
- [The free 677 magma](the-free-677-magma/README.md)
