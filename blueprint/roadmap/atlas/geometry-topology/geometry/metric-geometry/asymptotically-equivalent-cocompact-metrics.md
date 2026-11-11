---
declaration: section
origin: cited
lean: MathlibExt.Geometry.CocompactAsymptoticallyEquivalentMetricsWanted.OWR1319022Data, MathlibExt.Geometry.CocompactAsymptoticallyEquivalentMetricsWanted.conjecture, MathlibExt.Geometry.CocompactAsymptoticallyEquivalentMetricsWanted.conjecture_refuted
statement: formalized
---

# Asymptotically equivalent cocompact metrics

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/asymptotically-equivalent-cocompact-metrics/index.html).

## Cocompact asymptotically equivalent length-space pair

Let $\Gamma$ be a group acting on a
complete metric space $(M, d_1)$. A cocompact asymptotically equivalent length-space pair on $M$
is a function $d_2 \colon M \times M \to \mathbb{R}$ with the following properties. It is a
metric: $d_2(x, y) \ge 0$, $d_2(x, y) = 0$ if and only if $x = y$, $d_2(x, y) = d_2(y, x)$ and
$d_2(x, z) \le d_2(x, y) + d_2(y, z)$. It is complete: every sequence that is Cauchy for $d_2$
converges for $d_2$ to some point of $M$. Both $d_1$ and $d_2$ have approximate midpoints: for
$i = 1, 2$, all $x, y \in M$ and every $\varepsilon > 0$ there is $z \in M$ with
$\max(d_i(x, z), d_i(z, y)) \le d_i(x, y)/2 + \varepsilon$. The action is by isometries of both:
$d_i(g x, g y) = d_i(x, y)$ for all $g \in \Gamma$, $x, y \in M$ and $i = 1, 2$. The action is
cocompact: some compact set $K \subseteq M$ (compact for $d_1$) contains a point $g x$ of the orbit
of every $x \in M$. The two metrics induce the same topology: for every $x \in M$ and every
$\varepsilon > 0$ there is $\delta > 0$ with $d_2(x, y) < \varepsilon$ whenever
$d_1(x, y) < \delta$, and there is $\delta > 0$ with $d_1(x, y) < \varepsilon$ whenever
$d_2(x, y) < \delta$. Finally, $d_1$ and $d_2$ are asymptotically equivalent: for every
$\varepsilon > 0$ there is a real number $R$ such that
$|d_1(x, y) / d_2(x, y) - 1| < \varepsilon$ for all $x, y \in M$ with $d_1(x, y) \ge R$.

For complete metric spaces the approximate-midpoint property is equivalent to being a length
space.

Formalized by `MathlibExt.Geometry.CocompactAsymptoticallyEquivalentMetricsWanted.OWR1319022Data`, a structure declared in [WantedExt/Geometry/CocompactAsymptoticallyEquivalentMetricsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/CocompactAsymptoticallyEquivalentMetricsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/asymptotically-equivalent-cocompact-metrics/index.html#owr1319022-data).

## Bounded-difference conjecture for cocompact asymptotically equivalent metrics

The statement
that for every group $\Gamma$, every complete metric space $(M, d_1)$ on which $\Gamma$ acts, and
every cocompact asymptotically equivalent length-space pair on $M$ with second metric $d_2$, there
is a real number $C$ such that $|d_1(x, y) - d_2(x, y)| \le C$ for all $x, y \in M$.

## Sources

- open question of [OWR-1319-022] (Geometric Group Theory, Hyperbolic Dynamics and Symplectic Geometry (2007), Oberwolfach Reports, DOI 10.4171/owr/2006/33, pp. 1991--2058).

Formalized by `MathlibExt.Geometry.CocompactAsymptoticallyEquivalentMetricsWanted.conjecture`, a definition declared in [WantedExt/Geometry/CocompactAsymptoticallyEquivalentMetricsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/CocompactAsymptoticallyEquivalentMetricsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/asymptotically-equivalent-cocompact-metrics/index.html#conjecture).

## Negative answer to the cocompact asymptotic-metrics question

The conjecture is false: there
exist a group $\Gamma$, a complete metric space $(M, d_1)$ on which $\Gamma$ acts, and a cocompact
asymptotically equivalent length-space pair on $M$ with second metric $d_2$, such that for every
real number $C$ there are points $x, y \in M$ with $|d_1(x, y) - d_2(x, y)| > C$.

Counterexample of Le Donne, Nalon, Nicolussi Golo and Ryoo (arXiv:2503.00560, 2025), Example 4.2:
on the Engel group, a left-invariant Riemannian metric and its canonical asymptotic
sub-Riemannian metric are complete, left-invariant (transitive, hence cocompact), asymptotic,
yet their difference is unbounded.

## Sources

- E. Le Donne, L. Nalon, S. Nicolussi Golo, S.-Y. Ryoo, Asymptotics of Riemannian Lie groups with nilpotency step 2, arXiv preprint (2025), arXiv:2503.00560, https://arxiv.org/abs/2503.00560.

Stated but not proved: `MathlibExt.Geometry.CocompactAsymptoticallyEquivalentMetricsWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Geometry/CocompactAsymptoticallyEquivalentMetricsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/CocompactAsymptoticallyEquivalentMetricsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/asymptotically-equivalent-cocompact-metrics/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotically equivalent cocompact metrics](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/asymptotically-equivalent-cocompact-metrics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/metric-geometry/asymptotically-equivalent-cocompact-metrics)
