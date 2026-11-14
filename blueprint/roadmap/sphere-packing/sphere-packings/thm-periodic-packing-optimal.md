---
declaration: theorem
origin: cited
lean: periodic_constant_eq_constant
statement: formalized
---

# periodic-packing-optimal

For all $d$, the periodic sphere packing constant in $\mathbb{R}^d$ is equal to the sphere packing constant in $\mathbb{R}^d$.

## Depends on

- [SpherePacking.density](spherepacking-density.md)
- [Periodic-sphere-packing-constant](def-periodic-sphere-packing-constant.md)

## Proof

The following proof was written by Junyan Xu in the thread for [Issue \#80](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/issues/80) of the repository.

Given an arbitrary packing $P$ of upper density $\Delta$ and an arbitrary $\epsilon > 0$, we want to produce a periodic packing with density at least $\Delta - \epsilon$. Given a set $S$ (of nonzero volume), we shall call the quantity $\frac{\left| S \cap P \right|}{\left| S \right|}$ the density of $P$ in $S$, where $\left| S \right|$ denotes the volume of $S$.

Choose $\ell > 0$ such that

$$
\frac{(\ell - 4r)^d}{\ell^d} > 1 - \frac{\epsilon}{3}
$$

(where $r$ is the radius of the balls in $P$ and $d$ is the dimension). Then choose $R_0 > 0$ such that for all $R > R_0$, we have

$$
\frac{\left( R + \sqrt{d}\,\ell \right)^d - \left( R - \sqrt{d}\,\ell \right)^d}{R^d} < \frac{\epsilon}{3}
$$

By definition of upper density, there exists $R > R_0$ such that the density of $P$ in $B(0,R)$ is at least $\Delta - \frac{\epsilon}{3}$.

The Euclidean space is covered by disjoint hypercubes of side length $\ell$ of the form $\prod_{i=1}^d \left[ n_i\ell, (n_i+1)\ell \right)$ with $n_i \in \mathbb{Z}$. Since these hypercubes have diameter $\sqrt{d}\ell$, those that intersect $B(0,R)$ must be contained in $B(0,R+\sqrt{d}\ell)$. Thus the hypercubes contained in $B(0,R+\sqrt{d}\ell)$ cover $B(0,R)$. Similarly, the hypercubes not contained in $B(0,R)$ cannot intersect $B(0,R-\sqrt{d}\ell)$. Denote the union of hypercubes contained in $B(0,R+\sqrt{d}\ell)$ by $T$ and the union of those contained in $B(0,R)$ by $S$, we then have

$$
S \subseteq B(0,R) \subseteq T \subseteq B(0,R+\sqrt{d}\ell)
$$

and

$$
T \setminus S \subseteq B(0,R+\sqrt{d}\ell) \setminus B(0,R-\sqrt{d}\ell)
$$

The density of $P$ in $S$ is

$$
\begin{aligned}
\frac{\left| S \cap P \right|}{\left| S \right|}
&\ge \frac{\left| B(0,R) \cap P \right| - \left| B(0,R) \setminus S \right|}{\left| B(0,R) \right|} \\
&> \left( \Delta - \frac{\epsilon}{3} \right) - \frac{\left| T \setminus S \right|}{\left| B(0,R) \right|} \\
&> \left( \Delta - \frac{\epsilon}{3} \right) - \frac{\epsilon}{3}
\end{aligned}
$$

Therefore, the density of $P$ in some hypercube $C \subseteq S$ is at least $\Delta - \frac{2\epsilon}{3}$. If a ball in $P$ (thus of diameter $2r$) is not completely contained in $C$, it cannot intersect the hypercube $C'$ with the same center as $C$ with side length $\ell-4r$, so excluding these balls from $C\cap P$ decreases the density in $C$ by at most $\frac{\left| C \setminus C' \right|}{\left| C \right|} = \frac{\ell^d - (\ell-4r)^d}{\ell^d} < \frac{\epsilon}{3}$, and gives rise to a periodic packing of density $> \Delta - \epsilon$ with $C$ as a fundamental domain.

## Lean

Stated as [`periodic_constant_eq_constant`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/periodic_constant_eq_constant); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/lattice-periodic-packings.tex, line 48](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/lattice-periodic-packings.tex#L48)
