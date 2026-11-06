# A modularity lifting theorem

Suppose $\ell\geq5$ is a prime, that $F$ is a totally real field of even degree in which $\ell$ is unramified, and that $S$ is a finite set of finite places of $F$ not dividing $\ell$. Write $G_F$ for the absolute Galois group of $F$.

If $v\in S$ then let $F_v$ denote the completion of $F$ at $v$, fix an inclusion $\overline{F}\to\overline{F_v}$, let $\mathcal{O}_v$ denote the integers of $F_v$ and $k(v)$ the residue field. Let $I_v\subset G_F$ denote the inertia subgroup at $v$. Local class field theory (or a more elementary approach) gives a map $I_v\to\mathcal{O}_{F_v}^\times$ and hence a map $I_v\to k(v)^\times$. Let $J_v$ denote the kernel of this map.

Let $R$ be a complete local Noetherian $\mathbb{Z}_\ell$-algebra with finite residue field of characteristic $\ell$. We will be interested in representations $\rho:G_F\to\operatorname{GL}_2(R)$ with the following four properties.

- $\det(\rho)$ is the cyclotomic character;
- $\rho$ is unramified outside $S\cup\{\ell\}$;
- If $v\in S$ then $\rho(g)$ has trace equal to 2 for all $g\in J_v$;
- If $v\mid\ell$ is a place of $F$ then $\rho$ is flat at $v$.

In the last bullet point, “flat” means “projective limit of representations arising from finite flat group schemes”. Let us use the lousy temporary notation “$S$-good” to denote representations with these four properties.

Say $k$ is a finite extension of $\mathbb{Z}/\ell\mathbb{Z}$ and $\overline{\rho}:G_F\to\operatorname{GL}_2(k)$ is continuous, absolutely irreducible when restricted to $F(\zeta_\ell)$, and $S$-good. One can check that the functor representing $S$-good lifts of $\overline{\rho}$ is representable.

Right now we are very far from even stating this theorem in Lean.

I am not entirely sure where to find a proof of this in the literature, although it has certainly been known to the experts for some time. Theorem 3.3 of (Taylor 2006) comes close, although it assumes that $\ell$ is totally split in $F$ rather than just unramified. Another near-reference is Theorem 5.2 of ([Gee 2022](https://doi.org/10.2140/ent.2022.1.73)), although this assumes the slightly stronger assumption that the image of $\rho$ contains $\operatorname{SL}_2(\mathbb{Z}/p\mathbb{Z})$ (however it is well-known to the experts that this can be weakened to give the result we need). One reference for the proof is [Richard Taylor's 2018 Stanford course](https://math.berkeley.edu/~fengt/249A_2018.pdf).

Given this modularity lifting theorem, the strategy to show potential modularity of $\rho$ is to use Moret–Bailly to find an appropriate totally real field $F$, an auxiliary prime $p$, and an auxiliary elliptic curve over $F$ whose mod $\ell$ Galois representation is $\rho$ and whose mod $p$ Galois representation is induced from a character. By converse theorems (for example) the mod $p$ Galois representation is associated to an automorphic representation of $\operatorname{GL}_2/F$ and hence by Jacquet–Langlands it is modular. Now we use the modularity lifting theorem to deduce the modularity of the curve over $F$ and hence the modularity of the $\ell$-torsion.
