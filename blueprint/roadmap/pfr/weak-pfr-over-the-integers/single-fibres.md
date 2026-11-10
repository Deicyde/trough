---
declaration: lemma
origin: cited
lean: single_fibres
statement: formalized
proof: formalized
---

# single-fibres

Let $\phi:G\to H$ be a homomorphism and $A,B\subseteq G$ be finite subsets. If $x,y\in H$ then let $A_x=A\cap \phi^{-1}(x)$ and $B_y=B\cap \phi^{-1}(y)$. There exist $x,y\in H$ such that $A_x,B_y$ are both non-empty and

$$
d[\phi(U_A);\phi(U_B)]\log \frac{\lvert A\rvert\lvert B\rvert}{\lvert A_x\rvert\lvert B_y\rvert}\leq (\mathbb{H}(\phi(U_A))+\mathbb{H}(\phi(U_B)))(d(U_A,U_B)-d(U_{A_x},U_{B_y})).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [General fibring identity](../the-fibring-lemma/fibring-ident.md)

## Proof

The random variables $(U_A\mid \phi(U_A)=x)$ and $(U_B\mid \phi(U_B)=y)$ are equal in distribution to $U_{A_x}$ and $U_{B_y}$ respectively (both are uniformly distributed over their respective fibres). It follows from [General fibring identity](../the-fibring-lemma/fibring-ident.md) that

$$
\begin{aligned}
\sum_{x,y\in H}\frac{\lvert A_x\rvert\lvert B_y\rvert}{\lvert A\rvert\lvert B\rvert}d[U_{A_x};U_{B_y}]
&=d[U_A\mid \phi(U_A); U_B\mid \phi(U_B)]\\
&\leq d[U_A;U_B]-d[\phi(U_A);\phi(U_B)].
\end{aligned}
$$

Therefore with $M:=\mathbb{H}(\phi(U_A))+\mathbb{H}(\phi(U_B))$ we have

$$
\left(\sum_{x,y\in H}\frac{\lvert A_x\rvert\lvert B_y\rvert}{\lvert A\rvert\lvert B\rvert}Md[U_{A_x};U_{B_y}]\right)+Md[\phi(U_A);\phi(U_B)]\leq Md[U_A;U_B].
$$

Since

$$
M=\sum_{x,y\in H}\frac{\lvert A_x\rvert\lvert B_y\rvert}{\lvert A\rvert\lvert B\rvert}\log \frac{\lvert A\rvert\lvert B\rvert}{\lvert A_x\rvert\lvert B_y\rvert}
$$

we have

$$
\sum_{x,y\in H} \frac{\lvert A_x\rvert\lvert B_y\rvert}{\lvert A\rvert\lvert B\rvert}\left(Md[U_{A_x};U_{B_y}]+d[\phi(U_A);\phi(U_B)]\log \frac{\lvert A\rvert\lvert B\rvert}{\lvert A_x\rvert\lvert B_y\rvert}\right)\leq  Md[U_A;U_B].
$$

It follows that there exists some $x,y\in H$ such that $\lvert A_x\rvert,\lvert B_y\rvert\neq 0$ and

$$
Md[U_{A_x};U_{B_y}]+d[\phi(U_A);\phi(U_B)]\log \frac{\lvert A\rvert\lvert B\rvert}{\lvert A_x\rvert\lvert B_y\rvert}\leq  Md[U_A;U_B].
$$

## Lean

Formalized as [`single_fibres`](https://teorth.github.io/pfr/docs/find/#doc/single_fibres).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 142](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/weak_pfr.tex#L142)
