---
declaration: theorem
origin: cited
---

# Natural central groupoid axiom

[E26302](https://teorth.github.io/equational_theories/implications/?26302) $({x = (y \diamond ((z \diamond x) \diamond w)) \diamond (x \diamond w)})$ characterizes natural central groupoids.

## Depends on

- [Equation 26302](../selected-laws/part-03/equations-of-order-greater-than-4/eq26302.md)

## Proof

See \[knuth, Theorem 5\]. The proof is quite lengthy; a sketch is as follows. It is easy to see that natural central groupoids satisfy [E26302](https://teorth.github.io/equational_theories/implications/?26302). Conversely, if this law holds, then

$$
\begin{aligned}
(y \diamond z) \diamond (z \diamond w) &= (( x \diamond ((w \diamond (y \diamond z)) \diamond w)) \diamond ((y \diamond z) \diamond w)) \diamond (z \diamond w)\\
&= z
\end{aligned}
$$

so we have a central groupoid. Setting $y = (t \diamond t) \diamond t$, $z = t \diamond (t \diamond t)$, $w = t \diamond t$ in [E26302](https://teorth.github.io/equational_theories/implications/?26302) we also obtain

$$
(x \diamond t) \diamond t = (t \diamond t) \diamond t.
$$

Using the notation

$$
x^{(1)} := (x \diamond x) \diamond x, \quad x^{(2)} := x \diamond (x \diamond x)
$$

we then have

$$
\begin{aligned}
x \diamond t &= ((x \diamond x) \diamond (x \diamond t)) \diamond ((x \diamond t) \diamond t) \\
&= x \diamond t^{(1)}.
\end{aligned}
$$

A lengthy computer-assisted argument then gave the dual identity

$$
t^{(2)} \diamond x = t \diamond x
$$

Together, these give

$$
x^{(2)} \diamond y^{(1)} = x \diamond y.
$$

Multiplying on the left by $x = x^{(1)}\diamond x^{(2)}$, one can conclude that

$$
x^{(2)} = x \diamond (x \diamond y).
$$

One then has

$$
\begin{aligned}
(x \diamond y)^{(1)} &= ((y \diamond x) \diamond (x \diamond y)) \diamond (x \diamond y) \\
&= x \diamond (x \diamond y) \\
&= x^{(2)}
\end{aligned}
$$

and a similar argument gives

$$
(x \diamond y)^{(2)} = y^{(1)}.
$$

Since $(x \diamond x)^{(1)} = x^{(2)}$ and $(x \diamond x)^{(2)} = x^{(1)}$, we conclude that $x^{(1)}$ and $x^{(2)}$ are idempotent. Since $x = x^{(1)} \diamond x^{(2)}$, we see that every $x$ is the product of two idempotents. One can show that this representation is unique, and gives a canonical identification with a natural central groupoid.

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 188](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/implications.tex#L188)
