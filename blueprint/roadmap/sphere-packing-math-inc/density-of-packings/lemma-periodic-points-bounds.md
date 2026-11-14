---
declaration: lemma
origin: cited
lean: PeriodicSpherePacking.aux2_ge', PeriodicSpherePacking.aux2_le'
statement: formalized
proof: formalized
---

# periodic-points-bounds

For all $R$, we have the following inequality relating the number of points from $X$ (periodic w.r.t. $\Lambda$) in a ball with the number of points from $\Lambda$:

$$
\left|\Lambda \cap \mathcal{B}_d(R - L)\right|\left|X / \Lambda\right|
\leq \left|X \cap \mathcal{B}_d(R)\right|
\leq \left|\Lambda \cap \mathcal{B}_d(R + L)\right|\left|X / \Lambda\right|
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For the first inequality, we notice that $\bigcup_{x \in \Lambda \cap \mathcal{B}_d(R - L)} (x + \mathcal{D}) \subseteq \mathcal{B}_d(R)$, because for $x \in \Lambda \cap \mathcal{B}_d(R - L)$ and $y \in x + \mathcal{D}$, we have $\|x\| < R - L$ and $\|y - x\| \leq L$, so $\|y\| < R$ by triangle inequality. Intersecting both sides with $X$ and simplifying, we have

$$
\left(\bigcup_{x \in \Lambda \cap \mathcal{B}_d(R - L)} (x + \mathcal{D})\right) \cap X = \bigcup_{x \in \Lambda \cap \mathcal{B}_d(R - L)} ((x + \mathcal{D}) \cap X) \subseteq \mathcal{B}_d(R) \cap X
$$

Consider the (finite) cardinality on both sides and noting that $|(x + \mathcal{D}) \cap X| = |X / \Lambda|$ for all $x$, we see that $|\Lambda \cap \mathcal{B}_d(R - L)||X / \Lambda| \leq |X \cap \mathcal{B}_d(R)|$, as desired.

The proof of the second inequality is similar. We again observe that $\mathcal{B}_d(R) \subseteq \bigcup_{x \in \Lambda \cap \mathcal{B}_d(R + L)} (x + \mathcal{D})$, which follows from the tiling property of fundamental domain (i.e. every point can be translated by a $\Lambda$ lattice point into $\mathcal{D}$). Intersecting both sides with $X$ and considering cardinality of both sides concludes the proof.

There are several technicalities when formalising in Lean, such as having to prove $|\Lambda \cap \mathcal{B}_d(R)|$ is countable and finite. Those are handled at `aux3`.

## Lean

Formalized as [`PeriodicSpherePacking.aux2_ge'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/PeriodicSpherePacking.aux2_ge'), [`PeriodicSpherePacking.aux2_le'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/PeriodicSpherePacking.aux2_le').

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/packings-density.tex, line 38](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/packings-density.tex#L38)
