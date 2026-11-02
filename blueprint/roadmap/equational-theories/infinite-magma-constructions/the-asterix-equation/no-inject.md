---
declaration: corollary
origin: cited
---

# no-inject

There exists a solution $f:\mathbb{Z} \to \mathbb{Z}$ to fh such that the map $h \mapsto h + f(h)$ is not injective.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Select integers $h_0,h_1,h_2,h'_0,h'_1,h'_2$ such that the quantities

$$
0, h_0, h_1, h_2, h_0+h_1+h_2, -h_1-h_2, h'_0, h'_1, h'_2, h'_0+h'_1+h'_2, -h'_1-h'_2
$$

are all distinct, but such that

$$
h_0 + h_1 = h'_0 + h'_1 \neq 0
$$

(there are many assignments of variables that accomplish this). Then set

$$
\begin{aligned}
E_0 &:= \{0,h_0, h'_0\}\\
E_1 &:= E_0 \cup \{ h_1, h'_1, h_0+h_1+h_2, h'_0+h'_1+h'_2\}\\
E_2 &:= E_2 \cup \{ h_2, h'_2, -h_1-h_2, -h'_1-h'_2\}
\end{aligned}
$$

and define $f: E_1 \to E_2$ by the formulae

$$
\begin{aligned}
f(0) &:= 0 \\
f(h_0) &:= h_1 \\
f(h_1) &:= h_2 \\
f(h_0+h_1+h_2) &:= -h_1-h_2 \\
f(h'_0) &:= h'_1 \\
f(h'_1) &:= h'_2 \\
f(h'_0+h'_1+h'_2) &:= -h'_1-h'_2.
\end{aligned}
$$

One can then check that $(E_0, E_1, E_2, f)$ is a partial solution to fh, and by construction $h \mapsto h + f(h)$ is not injective on $E_1$. Using [Enlarging a partial solution](iteration.md) to extend this partial solution to a full solution, we obtain the claim.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 154](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L154)
