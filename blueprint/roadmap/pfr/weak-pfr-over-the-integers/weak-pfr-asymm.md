---
declaration: theorem
origin: cited
lean: weak_PFR_asymm
statement: formalized
proof: formalized
---

# weak-pfr-asymm

If $A,B\subseteq \mathbb{Z}^d$ are finite non-empty sets then there exist non-empty $A'\subseteq A$ and $B'\subseteq B$ such that

$$
\log\frac{\lvert A\rvert\lvert B\rvert}{\lvert A'\rvert\lvert B'\rvert}\leq 34d[U_A;U_B]
$$

such that $\max(\dim A',\dim B')\leq \frac{40}{\log 2} d[U_A;U_B]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [torsion-dist-shrinking](torsion-dist-shrinking.md)
- [pfr-projection](pfr-projection-2.md)
- [single-fibres](single-fibres.md)
- [dimension-def](dimension-def.md)

## Proof

Without loss of generality we can assume that $A$ and $B$ are not both inside (possibly distinct) cosets of the same subgroup of $\mathbb{Z}^d$, or we just replace $\mathbb{Z}^d$ with that subgroup. We prove the result by induction on $\lvert A\rvert+\lvert B\rvert$.

Let $\phi:\mathbb{Z}^d\to \mathbb{F}_2^d$ be the natural mod-2 homomorphism. By [Lemma torsion-dist-shrinking](torsion-dist-shrinking.md)

$$
\max(\mathbb{H}(\phi(U_A)),\mathbb{H}(\phi(U_B)))\leq 10d[U_A;U_B].
$$

We now apply [Lemma pfr-projection](pfr-projection-2.md), obtaining some subgroup $H\leq \mathbb{F}_2^d$ such that

$$
\log \lvert H\rvert \leq 40d[U_A;U_B]
$$

and

$$
\mathbb{H}(\tilde{\phi}(U_A))+\mathbb{H}(\tilde{\phi}(U_B))\leq 34 d[\tilde{\phi}(U_A);\tilde{\phi}(U_B)]
$$

where $\tilde{\phi}:\mathbb{Z}^d\to \mathbb{F}_2^d/H$ is $\phi$ composed with the projection onto $\mathbb{F}_2^d/H$.

By [Lemma single-fibres](single-fibres.md) there exist $x,y\in \mathbb{F}_2^d/H$ such that, with $A_x=A\cap \tilde{\phi}^{-1}(x)$ and similarly for $B_y$,

$$
\log \frac{\lvert A\rvert\lvert B\rvert}{\lvert A_x\rvert\lvert B_y\rvert}\leq 34(d[U_A;U_B]-d[U_{A_x};U_{B_y}]).
$$

Suppose first that $\lvert A_x\rvert+\lvert B_y\rvert=\lvert A\rvert+\lvert B\rvert$. This means that $\tilde{\phi}(A)=\{x\}$ and $\tilde{\phi}(B)=\{y\}$, and hence both $A$ and $B$ are in cosets of $\ker \tilde{\phi}$. Since by assumption $A,B$ are not in cosets of a proper subgroup of $\mathbb{Z}^d$ this means $\ker\tilde{\phi}=\mathbb{Z}^d$, and so (examining the definition of $\tilde{\phi}$) we must have $H=\mathbb{F}_2^d$. Then our bound on $\log\lvert H\rvert$ forces $d\leq \frac{40}{\log 2}d[U_A;U_B]$ and we are done with $A'=A$ and $B'=B$.

Otherwise,

$$
\lvert A_x\rvert+\lvert B_y\rvert \lt \lvert A\rvert+\lvert B\rvert.
$$

By induction we can find some $A'\subseteq A_x$ and $B'\subseteq B_y$ such that $\dim A',\dim B'\leq \frac{40}{\log 2} d[U_{A_x};U_{B_y}]\leq \frac{40}{\log 2}d[U_A;U_B]$ and

$$
\log \frac{\lvert A_x\rvert\lvert B_y\rvert}{\lvert A'\rvert\lvert B'\rvert}\leq 34d[U_{A_x};U_{B_y}].
$$

Adding these inequalities implies

$$
\log\frac{\lvert A\rvert\lvert B\rvert}{\lvert A'\rvert\lvert B'\rvert}\leq 34d[U_A;U_B]
$$

as required.

## Lean

Formalized as [`weak_PFR_asymm`](https://teorth.github.io/pfr/docs/find/#doc/weak_PFR_asymm).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 176](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/weak_pfr.tex#L176)
