---
declaration: lemma
origin: cited
lean: PeriodicSpherePacking.aux2_ge', PeriodicSpherePacking.aux2_le'
statement: formalized
proof: formalized
---

# lattice-points-bound

For all $R$, we have the following inequality relating the number of lattice points from $\Lambda$ in a ball with the volume of the ball and the fundamental region $\mathcal{D}$:

$$
\frac{\mathrm{Vol}(\mathcal{B}_d(R - L))}{\mathrm{Vol}(\mathcal{D})}
\leq \left|\Lambda \cap \mathcal{B}_d(R)\right|
\leq \frac{\mathrm{Vol}(\mathcal{B}_d(R + L))}{\mathrm{Vol}(\mathcal{D})}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For the first inequality, it suffices to prove that $\mathcal{B}_d(R - L) \subseteq \bigcup_{x \in \Lambda \cap \mathcal{B}_d(R)} (x + \mathcal{D})$, since the cosets on the right are disjoint. For a vector $v \in \mathcal{B}_d(R - L)$, we have $\|v\| < R - L$ by definition. Since $\mathcal{D}$ is a fundamental domain, there exists a lattice point $x \in \Lambda$ such that $v \in x + \mathcal{D}$. Rearranging gives $v - x \in \mathcal{D}$, which means $\|v - x\| \leq L$. By the triangle inequality, $\|x\| < R$, i.e. $x \in \mathcal{B}_d(L)$, concluding the proof.

For the second inequality, we prove that $\bigcup_{x \in \Lambda \cap \mathcal{B}_d(R)} (x + \mathcal{D}) \subseteq \mathcal{B}_d(R + L)$. Consider a vector $x \in \Lambda \cap \mathcal{B}_d(R)$ and a vector $y \in x + \mathcal{D}$. From above, we know $\|x\| < R$ and $\|y - x\| \leq L$, so $\|y\| < R + L$, concluding the proof.

## Lean

Formalized as [`PeriodicSpherePacking.aux2_ge'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/PeriodicSpherePacking.aux2_ge'), [`PeriodicSpherePacking.aux2_le'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/PeriodicSpherePacking.aux2_le').

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/packings-density.tex, line 21](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/packings-density.tex#L21)
