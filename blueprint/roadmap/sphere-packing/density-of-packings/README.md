# Density of packings

The definition of density given in [Sphere packings](../sphere-packings/README.md) is inconvenient to work with, especially when our packing is a structured one, such as a periodic/lattice packing. This section fixes this problem.

Note that some of the proofs in this section have only been sketched. The finer details are formalised in Lean.

Observe that the finite density evaluated at some $R > 0$ measures the density of sphere packings within a bounded, open ball of radius $R$. As one might expect, there is a relationship between the finite density and the number of centers in the ball of radius $R$.

- [sp-finite-density-bound](lemma-sp-finite-density-bound.md)

Suppose further that $X$ is a periodic packing w.r.t. the lattice $\Lambda \subseteq \mathbb{R}^d$. Let $\mathcal{D}$ be a (bounded) fundamental region of $\Lambda$, say the parallelopiped $[0, 1]^n\Lambda$, and let $L$ be the bound on the norm of vectors in $\mathcal{D}$, i.e. a number satisfying $\forall x \in \mathcal{D}, \|x\| \leq L$.

- [lattice-points-bound](lemma-lattice-points-bound.md)

To link [Lemma sp-finite-density-bound](lemma-sp-finite-density-bound.md) and [Lemma lattice-points-bound](lemma-lattice-points-bound.md), we need a lemma relating $|\Lambda \cap \mathcal{B}|$ with $|X \cap \mathcal{B}|$, which is what the following lemma does:

- [periodic-points-bounds](lemma-periodic-points-bounds.md)

When we combine the inequalities above, we need one additional computational lemma.

- [volume-ball-ratio-limit](lemma-volume-ball-ratio-limit.md)

Finally, we can relate the density of a periodic sphere packing to the natural definition of density given by any of its fundamental domain:

- [psp-density](theorem-psp-density.md)
