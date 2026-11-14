---
declaration: lemma
origin: cited
lean: tile_existence
statement: formalized
proof: formalized
---

# tile structure

For a given grid structure $(\mathcal{D}, c,s)$, there exists a tile structure $({\mathfrak P},{\mathcal{I}},{\Omega},{\mathcal{Q}},{\mathrm{c}},{\mathrm{s}})$.

## Depends on

- [ball metric entropy](../proof-of-metric-space-carleson-overview/ball-metric-entropy.md)
- [frequency ball cover](frequency-ball-cover.md)
- [disjoint frequency cubes](disjoint-frequency-cubes.md)
- [frequency cube cover](frequency-cube-cover.md)

## Proof

*Proof of tile structure.* First, we prove [(15)](../proof-of-metric-space-carleson-overview/README.md). If $I =I_0$, then [(15)](../proof-of-metric-space-carleson-overview/README.md) holds for all ${\mathfrak p} \in {\mathfrak P}(I)$ by [(33)](README.md) and [(32)](frequency-cube-cover.md). Now suppose that $I$ is not maximal in $\mathcal{D}$ with respect to set inclusion. Then we may assume by induction that for all $J \in \mathcal{D}$ with $I \subset J$ and all ${\mathfrak p}' \in {\mathfrak P}(J)$, [(15)](../proof-of-metric-space-carleson-overview/README.md) holds. Let $J$ be the unique minimal cube in $\mathcal{D}$ with $I \subsetneq J$.

Suppose that ${\vartheta} \in \Omega({\mathfrak p})$. If ${\vartheta}\in B_{{\mathfrak p}}(\mathcal{Q}({\mathfrak p}), 0.2)$, then since

$$
B_{{\mathfrak p}}(\mathcal{Q}({\mathfrak p}), 0.2)\subset B_{{\mathfrak p}}(\mathcal{Q}({\mathfrak p}), 1)\, ,
$$

we conclude that ${\vartheta}\in B_{{\mathfrak p}}(\mathcal{Q}({\mathfrak p}), 0.7)$. If not, by [(34)](README.md), there exists $z \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p})$ with ${\vartheta} \in \Omega(J,z)$. Using the triangle inequality and [(32)](frequency-cube-cover.md), we obtain

$$
d_{I^\circ}({\mathcal{Q}}({\mathfrak p}),{\vartheta}) \le d_{I^\circ}({\mathcal{Q}}({\mathfrak p}), z) + d_{I^\circ}(z, {\vartheta}) \le 0.7 + d_{I^\circ}(z, {\vartheta})\,.
$$

By [monotone cube metrics](../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and the induction hypothesis, this is estimated by

$$
\le 0.7 + 2^{-95a} d_{J^\circ}(z,{\vartheta}) \le 0.7 + 2^{-95a}\cdot 1 < 1\,.
$$

This shows the second inclusion in [(15)](../proof-of-metric-space-carleson-overview/README.md). The first inclusion is immediate from [(34)](README.md).

Next, we show [(13)](../proof-of-metric-space-carleson-overview/README.md). Let $I \in \mathcal{D}$.

If $I = I_0$, then disjointedness of the sets ${\Omega}({\mathfrak p})$ for ${\mathfrak p} \in {\mathfrak P}(I)$ follows from the definition [(33)](README.md) and [disjoint frequency cubes](disjoint-frequency-cubes.md). To obtain the inclusion in [(13)](../proof-of-metric-space-carleson-overview/README.md) one combines the inclusions [(29)](frequency-ball-cover.md) and [(31)](frequency-cube-cover.md) of [frequency cube cover](frequency-cube-cover.md) with [(33)](README.md).

Now we turn to the case where there exists $J \in \mathcal{D}$ with $I \subset J$ and $I\ne J$. In this case we use induction: It suffices to show [(13)](../proof-of-metric-space-carleson-overview/README.md) under the assumption that it holds for all cubes $J \in \mathcal{D}$ with $I \subset J$. As shown before definition [(34)](README.md), we may choose the unique inclusion minimal such $J$. To show disjointedness of the sets ${\Omega}({\mathfrak p}), {\mathfrak p} \in {\mathfrak P}(I)$ we pick two tiles ${\mathfrak p}, {\mathfrak p}' \in {\mathfrak P}(I)$ and ${\vartheta} \in {\Omega}({\mathfrak p}) \cap {\Omega}({\mathfrak p}')$. Then we are by [(34)](README.md) in one of the following four cases.

1\. There exist $z \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p})$ such that ${\vartheta} \in \Omega(J, z)$, and there exists $z' \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p}')$ such that ${\vartheta} \in \Omega(J, z')$. By the induction hypothesis, that [(13)](../proof-of-metric-space-carleson-overview/README.md) holds for $J$, we must have $z = z'$. By [disjoint frequency cubes](disjoint-frequency-cubes.md), we must then have ${\mathfrak p} = {\mathfrak p}'$.

2\. There exists $z \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p})$ such that ${\vartheta} \in \Omega(J,z)$, and ${\vartheta} \in B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), 0.2)$. Using the triangle inequality, [monotone cube metrics](../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and [(15)](../proof-of-metric-space-carleson-overview/README.md), we obtain

$$
d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'),z) \le d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\vartheta}) + d_{{\mathfrak p}'}(z, {\vartheta}) \le 0.2 + 2^{-95a} \cdot 1 < 0.3\,.
$$

Thus $z \in \Omega_1({\mathfrak p}')$ by [(32)](frequency-cube-cover.md). By [disjoint frequency cubes](disjoint-frequency-cubes.md), it follows that ${\mathfrak p} = {\mathfrak p}'$.

3\. There exists $z' \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p}')$ such that ${\vartheta} \in \Omega(J,z')$, and ${\vartheta} \in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.2)$. This case is the same as case 2., after swapping ${\mathfrak p}$ and ${\mathfrak p}'$.

4\. We have ${\vartheta} \in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.2) \cap B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), 0.2)$. In this case it follows that ${\mathfrak p} = {\mathfrak p}'$ since the sets $B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.2)$ are pairwise disjoint by the inclusion [(32)](frequency-cube-cover.md) and [disjoint frequency cubes](disjoint-frequency-cubes.md).

To show the inclusion in [(13)](../proof-of-metric-space-carleson-overview/README.md), let ${\vartheta} \in {Q}(X)$. By the induction hypothesis, there exists ${\mathfrak p} \in {\mathfrak P}(J)$ such that ${\vartheta} \in \Omega({\mathfrak p})$. By definition of the set ${\mathfrak P}$, we have ${\mathfrak p} = (J, z)$ for some $z \in \mathcal{Z}(J)$. Thus, by [(29)](frequency-ball-cover.md), there exists $z' \in \mathcal{Z}(I)$ with $z \in B_{I^\circ}(z', 0.7)$. Then by Lemma [frequency cube cover](frequency-cube-cover.md) there exists ${\mathfrak p}' \in {\mathfrak P}(I)$ with $z \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p}')$. Consequently, by [(34)](README.md), ${\vartheta} \in {\Omega}({\mathfrak p}')$. This completes the proof of [(13)](../proof-of-metric-space-carleson-overview/README.md).

Finally, we show [(14)](../proof-of-metric-space-carleson-overview/README.md). Let ${\mathfrak p}, {\mathfrak q} \in {\mathfrak P}$ with ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak q})$ and ${\Omega}({\mathfrak p}) \cap {\Omega}({\mathfrak q}) \ne \emptyset$. If we have ${\mathrm{s}}({\mathfrak p}) \ge {\mathrm{s}}({\mathfrak q})$, then it follows from [(8)](../proof-of-metric-space-carleson-overview/README.md) that $I = J$, thus ${\mathfrak p}, {\mathfrak q} \in {\mathfrak P}(I)$. By [(13)](../proof-of-metric-space-carleson-overview/README.md) we have then either ${\Omega}({\mathfrak p}) \cap {\Omega}({\mathfrak q}) = \emptyset$ or ${\Omega}({\mathfrak p}) = {\Omega}({\mathfrak q})$. By the assumption in [(14)](../proof-of-metric-space-carleson-overview/README.md) we have ${\Omega}({\mathfrak p}) \cap {\Omega}({\mathfrak q}) \ne \emptyset$, so we must have ${\Omega}({\mathfrak p}) = {\Omega}({\mathfrak q})$ and in particular ${\Omega}({\mathfrak q}) \subset {\Omega}({\mathfrak p})$.

So it remains to show [(14)](../proof-of-metric-space-carleson-overview/README.md) under the additional assumption that ${\mathrm{s}}({\mathfrak q}) > {\mathrm{s}}({\mathfrak p})$. In this case, we argue by induction on ${\mathrm{s}}({\mathfrak q})-{\mathrm{s}}({\mathfrak p})$. By [(7)](../proof-of-metric-space-carleson-overview/README.md), there exists a cube $J \in \mathcal{D}$ with $s(J) = {\mathrm{s}}({\mathfrak q}) - 1$ and $J \cap{\mathcal{I}}({\mathfrak p}) \ne \emptyset$. We pick one such $J$. By [(8)](../proof-of-metric-space-carleson-overview/README.md), we have ${\mathcal{I}}({\mathfrak p}) \subset J \subset {\mathcal{I}}({\mathfrak q})$.

Thus, by [(29)](frequency-ball-cover.md), there exists $z' \in \mathcal{Z}(J)$ with ${\mathcal{Q}}({\mathfrak q}) \in B_{J^\circ}(z', 0.7)$. Then by [frequency cube cover](frequency-cube-cover.md) there exists ${\mathfrak q}' \in {\mathfrak P}(J)$ with ${\mathcal{Q}}({\mathfrak q}) \in\Omega_1({\mathfrak q}')$. By [(34)](README.md), it follows that $\Omega({\mathfrak q}) \subset \Omega({\mathfrak q}')$. Note that then ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak q}')$ and ${\Omega}({\mathfrak p}) \cap {\Omega}({\mathfrak q}') \ne \emptyset$ and ${\mathrm{s}}({\mathfrak q}') - {\mathrm{s}}({\mathfrak p}) = {\mathrm{s}}({\mathfrak q}) - {\mathrm{s}}({\mathfrak p}) - 1$. Thus, we have by the induction hypothesis that $\Omega({\mathfrak q}') \subset \Omega({\mathfrak p})$. This completes the proof.

## Lean

Formalized as [`tile_existence`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tile_existence).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1252](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1252)
