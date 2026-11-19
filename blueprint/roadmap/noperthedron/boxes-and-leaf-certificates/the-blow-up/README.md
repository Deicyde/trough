# The blow-up

In charts 0 and 4 each inner vertex $S$ has a *paired* outer vertex $\sigma(S)$: $\sigma(S) = S$ in chart 0, and in chart 4 $\sigma(S) = \tau S$ for the 30 copies of $C_3$ (Lemma [tau_pair](../../the-reduction/step-b-the-relative-rotation/lem-tau-pair.md)). At $r = 0$ the pair has $Q_j(0) S = B_j S = \sigma(S)$, so $\mathrm{gap}_{\sigma(S)}$ vanishes identically on $\rho = 0$, and no box touching $\rho = 0$ can have a positive lower bound for it.

- [Blow-up identity](lem-blowup-identity.md)

The bracket $L$ is again a polynomial of degree at most $2$ in each variable. Unlike the original paired gap, it is not forced to vanish at $\rho=0$: its boundary value is

$$
L(u,v,s_0,s_1,0)=\bigl\langle w,\ N_o M_j(c\times S)\bigr\rangle.
$$

This value records the first-order separation in the direction $c$. It can still vanish, for example when $c$ is parallel to $S$, and for fixed $S$ and $w$ it is linear in $c$, so it takes both signs on opposite faces of the cube. Choosing the vertex and screen direction separately for each box can nevertheless give a positive lower bound on boxes touching $\rho=0$.

The blow-up identity is an exact factorization, not a first-order approximation: the term $\rho\,c\times(c\times S)$ is retained in $L$. Since $\rho\ge0$ and the cleared denominators are positive, $L\ge0$ implies $\mathrm{gap}_{\sigma(S)}\ge0$. The checker bounds $L$ for the paired vertex and the ordinary gaps for the other outer vertices, allowing a single box certificate to handle both alignment and nearby poses.

- [Gap core](thm-gap-core.md)
