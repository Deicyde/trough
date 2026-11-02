---
declaration: definition
origin: cited
not_ready: true
---

# automorphic\_form

An *automorphic form* is a function $\phi:G(\mathbb{A}_N)\to\mathbb{C}$ satisfying the following conditions:

- $\phi$ is locally constant on $G(\mathbb{A}_N^f)$ and $C^\infty$ on $G(N_\infty)$. In other words, for every $g_\infty$, $\phi(-,g_\infty)$ is locally constant, and for every $g_f$, $\phi(g_f,-)$ is smooth.
- $\phi$ is left-invariant under $G(N)$;
- $\phi$ is right-$U_\infty$-finite (that is, the space spanned by $x\mapsto \phi(xu)$ as $u$ varies over $U_\infty$ is finite-dimensional);
- $\phi$ is right $K_f$-finite, where $K_f$ is one (or equivalently all) compact open subgroups of $G(\mathbb{A}_N^f)$;
- $\phi$ is $\mathcal{z}$-finite, where $\mathcal{z}$ is the centre of the universal enveloping algebra of the Lie algebra of $G(N_\infty)$, acting via differential operators. Equivalently $\phi$ is annihiliated by a finite index ideal of this centre, so morally $\phi$ satisfies lots of differential equations of a certain type;
- For all $g_f$, the function $g_\infty\mapsto \phi(g_f g\infty)$ is slowly-increasing in the sense above.

## Depends on

- [slowly\_increasing\_well\_defined](slowly-increasing-well-defined.md)
- [connected\_reductive\_group](../algebraic-groups/connected-reductive-group.md)
- [lie\_group\_from\_algebraic\_group](../structures-on-the-points-of-an-affine-variety/lie-group-from-algebraic-group.md)
- [topology\_on\_affine\_variety\_computation](../structures-on-the-points-of-an-affine-variety/topology-on-affine-variety-computation.md)

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/chtopbestiary.tex, line 170](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/chtopbestiary.tex#L170)
