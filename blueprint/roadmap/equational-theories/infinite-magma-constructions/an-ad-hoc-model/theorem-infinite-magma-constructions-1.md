---
declaration: theorem
origin: cited
---

# theorem-infinite\_magma\_constructions-1

There exists a magma which satisfies Equation 3342,

$$
x \diamond y = y \diamond (x \diamond (x \diamond x)),
$$

but such that none of the laws

$$
\begin{aligned}
x \diamond x &= x \diamond ((x \diamond x) \diamond x) \\
x \diamond y &= x \diamond ((y \diamond y) \diamond y) \\
x \diamond x &= ((x \diamond x) \diamond x) \diamond x \\
x \diamond y &= ((x \diamond x) \diamond x) \diamond y.
\end{aligned}
$$

hold.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We begin with some informal motivation. Writing

$$
f(x) := x \diamond (x \diamond x),
$$

we conclude that

$$
x \diamond y = y \diamond f(x)
$$

and hence on iteration

$$
x \diamond y = f(x) \diamond f(y).
$$

In particular, $x \diamond x = f(x) \diamond f(x)$, and

$$
f(x) = x \diamond (x \diamond x) = (x \diamond x) \diamond f(x) = (f(x) \diamond f(x)) \diamond f(x).
$$

If $f$ is surjective, this would imply

$$
x = (x \diamond x) \diamond x
$$

and hence the four laws stated above would hold in this case.

This motivates the use of a non-surjective $f$. We will take $G$ to be the space of polynomials $\mathbb{Z}[t]$ of one variable with integer coefficients, and let $f: G \to G$ be the multiplication by $t$ map:

$$
f(P) := tP.
$$

This is of course non-surjective. The magma operation will be constructed as follows:

- If $P$ is a polynomial with $P(0) \neq 0$, then $t^n P \diamond t^n P = t^n P \diamond t^{n+1} P = 2P$ for all $n \geq 0$, and $t^{n+m} P \diamond 2t^n P = 2t^n P \diamond t^{n+m+1} P = t^{m+1} P$ for all $n, m \geq 0$. (This is well-defined since the $t^n P$, $2t^n P$ are all distinct polynomials.)
- We define $P \diamond Q = 0$ if not covered by the above laws.

It is a routine matter to verify (fdef) and (xop), so that equation 3342 holds. However, one can check that the four laws in the conclusion fail with $x=y=1$.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 858](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L858)
