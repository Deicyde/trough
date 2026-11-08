---
declaration: theorem
origin: cited
lean: Refutation_1485.not_3457, Refutation_1485.not_3511, Refutation_1485.not_2087_2124
statement: formalized
---

# 1485 does not imply 1483

[E1485](https://teorth.github.io/equational_theories/implications/?1485) does not imply any of the following laws:

- Equation 3457: $x \diamond x = x \diamond ((x \diamond x) \diamond y)$.
- Equation 2087: $x = ((y \diamond x) \diamond x) \diamond (x \diamond x)$.
- Equation 2124: $x = ((y \diamond y) \diamond x) \diamond (x \diamond x)$.
- Equation 3511: $x \diamond y = x \diamond ((x \diamond y) \diamond x)$.

## Depends on

- [Equation 1485](../selected-laws/part-02/eq1485.md)

## Proof depends on

- [Completion property](greedy-prop.md)
- [Reversing the claims](rev-claim.md)

## Proof

Computer check reveals that the carrier $G_0=\{0,1,2,3 ,4\}$ with incidence matrix

$$
\begin{pmatrix}
1 & 1 & 0 & 0 & 1 \\
1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 0 \\
\end{pmatrix}
$$

is a relaxed weak central groupoid if we declare the paths $0 \to 0 \to 0$, $0 \to 0 \to 1$, $0 \to 1 \to 1$, $1 \to 0 \to 0$, $1 \to 1 \to 0$, $1 \to 1 \to 1$ to be bad, and all other paths in the directed graph to be good. We can also check the following axioms:

- Anti-3457: There exist $x,y,z,w$ with $x \to z \to x$, $z \to w \to y$ both good, and $x \to z \to w$ bad. (One can take $x=1$, $y=4$, $z = 0$, $w = 0$.)
- Anti-2087: There exist $x,y,z,w,u$ with $y \to z \to x$, $z \to w \to x$, and $x \to u \to x$ good, and $w \to x \to u$ is bad. (One can take $x=1, y=2$, $z=4$, $w=1$, $u=0$.)
- Anti-2124: There exists $x,y,z,w,u$ with $y \to z \to y$, $z \to w \to x$ and $x \to u \to x$ good, and $w \to x \to u$ bad. (One can take $x=1$, $y=2$, $z=4$, $w = 1$, $u=0$.)
- Anti-3511: There exists $x,y,z,w$ with $x \to z \to y$ and $z \to w \to x$ good, and $x \to z \to w$ bad. (One can take $x=1$, $y=3$, $z = 1$, $w=0$.)

Let $G_*$ be a finite partial extension of $G_0$ to be chosen later. By [Completion property](greedy-prop.md), we can complete this to a complete weak central groupoid $G$ with carrier $G_0 \times \mathbb{N}$. Depending on how we choose $G_*$, we can ensure that this $G$ refutes one of the four laws 3457, 2087, 2124, 3511:

- Refuting 3457: Let $x,y,z,w$ be as in the claim Anti-3457, then select $G_*$ to be the directed graph with edges $(x,0) \to (z,2) \to (x,0) \to (z,2) \to (w,3) \to (y,1)$. One can check that this is a partial extension, and that $G$ will refute 3457 with $x,y$ replaced by $(x,0),(y,1)$.
- Refuting 2087: Let $x,y,z,w,u$ be as in the claim Anti-2087, then select $G_*$ to be the directed graph with edges $(y,1) \to (z,2) \to (x,0)$ and $(z,2) \to (w,3) \to (x,0) \to (u,4) \to (x,0)$. One can check that this is a partial extension, and that $G$ will refute 2087 with $x,y$ replaced by $(x,0),(y,1)$.
- Refuting 2124: Let $x,y,z,w,u$ be as in the claim Anti-2124, then select $G_*$ to be the directed graph with edges $(y,1) \to (z,2) \to (y,1)$ and $(z,2) \to (w,3) \to (x,0) \to (u,4) \to (x,0)$. One can check that this is a partial extension, and that $G$ will refute 2124 with $x,y$ replaced by $(x,0),(y,1)$.
- Refuting 3511: Let $x,y,z,w$ be as in the claim Anti-3511, then select $G_*$ to be the directed graph with edges $(x,0) \to (z,2) \to (y,1)$ and $(z,2) \to (w,3) \to (x,0)$. One can check that this is a partial extension, and that $G$ will refute 3511 with $x,y$ replaced by $(x,0),(y,1)$.

## Lean

Stated as [`Refutation_1485.not_3457`](https://teorth.github.io/equational_theories/docs/find/#doc/Refutation_1485.not_3457), [`Refutation_1485.not_3511`](https://teorth.github.io/equational_theories/docs/find/#doc/Refutation_1485.not_3511), [`Refutation_1485.not_2087_2124`](https://teorth.github.io/equational_theories/docs/find/#doc/Refutation_1485.not_2087_2124); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/weak_central_groupoids.tex, line 99](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/weak_central_groupoids.tex#L99)
