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

- [modularity\_lifting\_theorem](modularity-lifting-theorem.md)
