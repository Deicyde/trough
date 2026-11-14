---
declaration: lemma
origin: cited
lean: loc_immersion_rel_open
statement: formalized
proof: formalized
---

# loc_immersion_rel_open

The relation $\mathcal{R}$ above is open.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The main task is to fix $x_0 \notin B$ and $\varphi_0 \in L(E, E)$ which is injective on $x_0^\perp$ and prove that, for every $x$ close to $x_0$ and $\varphi$ close to $\varphi_0$, $\varphi$ is injective on $x^\perp$. This is a typical situation where geometric intuition makes it feel like there is nothing to prove.

One difficulty is that the subspace $x^\perp$ moves with $x$. We reduce to a fixed subspace by considering the restriction to $x_0^\perp$ of the orthogonal projection onto $x^\perp$. One can check this is an isomorphism as long as $x$ is not perpendicular to $x_0$. More precisely, we consider $f \!: J^1(E, E) \to ℝ \times L(x_0^\perp, E)$ which sends $(x, y, \varphi)$ to $(\langle x_0, x\rangle, \varphi \circ \operatorname{pr}_{x^\perp} \circ j_0)$ where $j_0$ is the inclusion of $x_0^\perp$ into $E$. The set $U$ of injective linear maps is open in $L(x_0^\perp, E)$ and the map $f$ is continuous hence the preimage of $\{0\}^c \times U$ is open. This is good enough for us because injectivity of $\varphi \circ \operatorname{pr}_{x^\perp} \circ j_0$ implies injectivity of $\varphi$ on the image of $\operatorname{pr}_{x^\perp} \circ j_0$ which is $x^\perp$ whenever $\langle x_0, x\rangle \neq 0$.

## Lean

Formalized as [`loc_immersion_rel_open`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/loc_immersion_rel_open).

## Sources

- [Sphere eversion blueprint: appendix.tex, line 21](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/appendix.tex#L21)
