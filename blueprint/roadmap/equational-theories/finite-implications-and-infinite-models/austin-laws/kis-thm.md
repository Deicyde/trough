---
declaration: theorem
origin: cited
lean: InfModel.Finite.Equation374794_implies_Equation2, InfModel.Equation374794_not_implies_Equation2
statement: formalized
proof: formalized
---

# Kisielewicz's first Austin law

[E374794](https://teorth.github.io/equational_theories/implications/?374794) $({x = (((y \diamond y) \diamond y) \diamond x) \diamond ((y \diamond y) \diamond z)})$ is an Austin law.

## Depends on

- [Equation 374794](../../selected-laws/part-03/equations-of-order-greater-than-4/eq374794.md)
- [Equation 2](../../selected-laws/part-01/eq2.md)

## Proof

First we show that every finite model of [E374794](https://teorth.github.io/equational_theories/implications/?374794) is trivial. Write $y^2 := y \diamond y$ and $y^3 := y^2 \diamond y$. For any $y,z$, introduce the functions ${f_y: x \mapsto y^3 \diamond x}$ and ${g_{yz}: x \mapsto x \diamond (y^2 \diamond z)}$. [E374794](https://teorth.github.io/equational_theories/implications/?374794) says that $g_{yz}(f_y(x))=x$, hence by finiteness $g_{yz}=f_y^{-1}$, showing that $g_{yz}$ does not depend on the value of $z$. Since

$$
f_y(y^2 \diamond z) = g_{yz}(y^3),
$$

it follows that $f_y(y^2 \diamond z)=f_y(y^3)$ which by injectivity of $f_y$ implies that $z\mapsto y^2 \diamond z$ is a constant function (with $y$ fixed). Substituting $y^2$ for $y$ shows that the same is true for $z\mapsto (y^2 \diamond y^2) \diamond z$, and since

$$
f_y(z) = (y^2 \diamond y) \diamond z = (y^2 \diamond y^2) \diamond z
$$

we conclude that $f_y$ is also a constant function. But this function is already known to be injective, thus there do not exist distinct elements in its domain, showing that the model must be trivial.

To construct an infinite model, consider the magma of positive integers $\mathbb{Z}^+$ with the operation $x \diamond y$ defined by

$$
x \diamond y =
\begin{cases}
2^y, & x=  y            \\
3^y, & x=  1,\ y \neq 1 \\
z, & x=3^z,\ y \neq x \\
1, & else
\end{cases}.
$$

Then $y \diamond y = 2^y$ and $(y \diamond y) \diamond y = 1$ for all $y$. If $x\neq 1$ we have that

$$
((y \diamond y) \diamond y) \diamond x = 3^x,
$$

and since $(y \diamond y) \diamond z$ is a power of two for all $y, z$ it follows that

$$
3^x \diamond ((y \diamond y) \diamond z) = x.
$$

The case $x=1$ requires a further argument: observe that $w = (y \diamond y) \diamond z$ evaluates to one unless $z = 2^y$, in which case it evaluates to $2^{2^y}$ (which is greater than or equal to four). In particular, $w$ never takes the value two. Thus

$$
(((y \diamond y) \diamond y) \diamond 1) \diamond ((y \diamond y) \diamond z) = 2 \diamond w = 1,
$$

concluding our proof that this magma is a model of [E374794](https://teorth.github.io/equational_theories/implications/?374794)

## Lean

Formalized as [`InfModel.Finite.Equation374794_implies_Equation2`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Finite.Equation374794_implies_Equation2), [`InfModel.Equation374794_not_implies_Equation2`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Equation374794_not_implies_Equation2).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 13](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L13)
