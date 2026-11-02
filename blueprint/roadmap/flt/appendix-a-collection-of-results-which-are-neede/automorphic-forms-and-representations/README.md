# Automorphic forms and representations

This section needs a lot of work; I am just attempting to write down some approximation to the (well-known) definitions but in great generality (far greater than we need). Some definitions below are short on details; indeed there may even be errors or imprecisions right now (because we are working in more generality than I am used to). It will be a very interesting project to get these details down. One reference (which leaves a lot of exercises) is Borel-Casselman in \[corvallis1\]. Even *stating* these definitions will be a big challenge in Lean; indeed one of the motivations of the project is that it forces us to write down all the below properly.

Let $G$ be a connected reductive group over a number field $N$. We note that $G(\mathbb{A}_N^f)$ is a (locally profinite) topological space and $G(N_\infty)$ is a real Lie group; their product is $G(\mathbb{A}_N)$. If $g\in G(\mathbb{A}_N)$, write $g_f\in G(\mathbb{A}_N^f)$ for the finite part and $g_\infty\in G(N_\infty)$ for its infinite part.

For some reason, in the literature people seem to fix a choice of maximal compact subgroup $U_\infty$ of $G(N_\infty)$. I believe that all such subgroups are conjugate, and probably this gives some route between the different definitions coming from the different choices.

Example: if $G=\operatorname{GL}_2$ and $N=\mathbb{Q}$ then $N_\infty=\mathbb{R}$ and $G(N_\infty)$ is just $\operatorname{GL}_2(\mathbb{R})$ with its usual Lie group structure and we can take $U_\infty$ to be $O_2(\mathbb{R})$; $G(\mathbb{A}_N^f)$ is the restricted product of $\operatorname{GL}_2(\mathbb{Q}_p)$ over $\operatorname{GL}_2(\mathbb{Z}_p)$, for all primes $p$.

By assumption, $G(N_\infty)$ admits a finite-dimensional (algebraic) representation $\rho$ with finite kernel. Consider $\rho$ as taking values in $GL_N(\mathbb{C})=\operatorname{Aut}_{\mathbb{C}}(V)$. Fix a hermitian sesquilinear form on $V$ which is $U_\infty$ invariant, and now define a norm $||g||_\rho$ on $G(N_\infty)$ by

$$
||g||_\rho=(\operatorname{tr} \rho(g)^*\rho(g))^{1/2},
$$

where the asterisk denotes adjoint with respect to the sesquilinear form. According to the article by Borel–Jacquet in \[corvallis1\] (p189), if $\rho'$ is another such choice then there exists a positive real $C$ and a positive integer $n$ such that $||g||_{\rho'}\leq C||g||_\rho^n$ for all $g\in G(N_\infty)$.

- [slowly\_increasing](slowly-increasing.md)
- [slowly\_increasing\_well\_defined](slowly-increasing-well-defined.md)
- [automorphic\_form](automorphic-form.md)
- [cuspidal\_automorphic\_form](cuspidal-automorphic-form.md)
- [automorphic\_form\_actions](automorphic-form-actions.md)
- [cuspidal\_automorphic\_form\_decomposition](cuspidal-automorphic-form-decomposition.md)
- [cuspidal\_automorphic\_representation](cuspidal-automorphic-representation.md)
- [automorphic\_representation](automorphic-representation.md)
- [automorphic\_representation\_local\_decomposition](automorphic-representation-local-decomposition.md)
