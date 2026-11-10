---
declaration: theorem
origin: cited
lean: InfModel.Equation28770_not_implies_Equation2
statement: formalized
proof: formalized
---

# Kisielewicz's second Austin law

[E28770](https://teorth.github.io/equational_theories/implications/?28770) $({x = (((y \diamond y) \diamond y) \diamond x) \diamond (y \diamond z)})$ is an Austin law.

## Depends on

- [Equation 2](../../selected-laws/part-01/eq2.md)
- [Equation 28770](../../selected-laws/part-03/equations-of-order-greater-than-4/eq28770.md)

## Proof

Using the $y^2$ and $y^3$ notation as before, the law reads

$$
x = (y^3 \diamond x) \diamond (y \diamond z).\qquad\text{(1)}
$$

In particular, for any $y$, the map $T_y \colon x \mapsto y^3 \diamond x$ is injective, hence bijective in a finite model $G$. In particular we can find a function $f : G \to G$ such that $T_y f(y) = y^3$ for all $y$ Applying (1) with $x = f(y)$, we conclude

$$
T_y(y \diamond z) = y^3 \diamond (y \diamond z) = f(y)
$$

and thus $y \diamond z$ is independent of $z$ by injectivity of $T_y$. Thus, the right-hand side of (1) does not depend on $x$, and so the model is trivial. This shows there are no non-trivial finite models.

To establish an infinite model, use $\mathbb{N}$ with $x \diamond y$ defined by requiring

$$
y \diamond y = 2^y; \quad 2^y \diamond y = 3^y
$$

and

$$
3^y \diamond x = 3^y 5^x
$$

for $x \neq 3^y$, and

$$
(3^y 5^x) \diamond z = x
$$

for $z \neq 3^y 5^x$. Finally set

$$
2^{3^y} \diamond z = 3^y
$$

for $z \neq 3^y, 2^{3^y}$. All other assignments of $\diamond$ may be made almost arbitrarily, such as setting them to $1$. It is then a routine matter to establish (1).

## Lean

Formalized as [`InfModel.Equation28770_not_implies_Equation2`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Equation28770_not_implies_Equation2).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 46](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/infinite_models.tex#L46)
