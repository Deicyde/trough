---
declaration: lemma
origin: cited
lean: TileStructure.Forest.local_dens2_tree_bound
statement: formalized
proof: formalized
---

# local dens2 tree bound

Let ${\mathfrak u} \in {\mathfrak U}$ and $J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))$. Then

$$
\mu(F \cap J) \le 2^{201a^3} \operatorname{\operatorname{dens}}_2({\mathfrak T}({\mathfrak u})) \mu(J)\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

*Proof of local dens2 tree bound.* We prove the inequality with the constant $2^{201a^3}$ replaced by $2 ^ {200a^3 + 14a}$; this is stronger because $a \geq 4$. It suffices to show the existence of a tile ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ and an $r \geq 4 D ^ {{\mathrm{s}}({\mathfrak p})}$ such that $J \subset B({\mathrm{c}}({\mathfrak p}), r)$ and $\mu(B({\mathrm{c}}({\mathfrak p}), r)) ≤ 2 ^ {200a^3 + 14a} \mu(J)$, because then it follows from the definition [(27)](../../proof-of-metric-space-carleson-overview/README.md) of $\operatorname{\operatorname{dens}}_2$ that

$$
\mu(F \cap J) \le \mu(F \cap B({\mathrm{c}}({\mathfrak p}), r))
$$

$$
\le \operatorname{\operatorname{dens}}_2({\mathfrak T}({\mathfrak u})) \mu(B({\mathrm{c}}({\mathfrak p}), r)) \le 2^{200a^3 + 14a} \operatorname{\operatorname{dens}}_2({\mathfrak T}({\mathfrak u}))\mu(J)\,.
$$

In particular, these criteria are satisfied, with $r = 4 D ^ {{\mathrm{s}}({\mathfrak p})}$, by any ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ such that $J \subseteq B({\mathrm{c}}({\mathfrak p}, 4 D ^ {{\mathrm{s}}({\mathfrak p})}))$ and $\mu({\mathcal{I}}({\mathfrak p})) \le 2^{100a^3 + 10a} \mu(J)$, because then by the doubling property [(5)](../../introduction/README.md),

$$
\mu(B({\mathrm{c}}({\mathfrak p}), 4 D ^ {{\mathrm{s}}({\mathfrak p})})) \le 2^{4a} \mu(B({\mathrm{c}}({\mathfrak p}), D ^ {{\mathrm{s}}({\mathfrak p})} / 4))
$$

$$
\le 2^{4a} \mu({\mathcal{I}}({\mathfrak p})) \le 2^{100a^3 + 14a} \mu(J)\,.
$$

Suppose first that $s(J) = S$. Then $J = I_0$, so [(9)](../../proof-of-metric-space-carleson-overview/README.md) and the fact that $J \in \mathcal{J}({\mathfrak T}({\mathfrak u})) \subseteq \mathcal{J}_0({\mathfrak T}({\mathfrak u}))$ imply that $s(J) = -S$. Thus $S = 0$. It follows that $J$ is the only dyadic cube, so any ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ has ${\mathcal{I}}({\mathfrak p}) = J$, and therefore satisfies $J \subseteq B({\mathrm{c}}({\mathfrak p}, 4 D ^ {{\mathrm{s}}({\mathfrak p})}))$ and $\mu({\mathcal{I}}({\mathfrak p})) \le 2^{100a^3 + 10a} \mu(J)$.

It remains to consider the case $s(J) < S$. Then, by [(7)](../../proof-of-metric-space-carleson-overview/README.md) and [(8)](../../proof-of-metric-space-carleson-overview/README.md), there exists some cube $J' \in \mathcal{D}$ with $s(J') = s(J) + 1$ and $J \subset J'$. By definition of $\mathcal{J}({\mathfrak T}({\mathfrak u}))$ there exists some ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ such that ${\mathcal{I}}({\mathfrak p}) \subset B(c(J'), 100 D^{s(J') + 1})$.

Since $c(J) \in J \subset J' \subset B(c(J'), 4D^{s(J')})$, the triangle inequality, $s(J') = s(J) + 1$ and $D=2^{100a^2}$ imply

$$
B(c(J'), 204D^{s(J')+1}) \subset B(c(J), 204D^{s(J') + 1} + 4D^{s(J')})
\subset B(c(J), 2^8 D^{s(J) + 2})\,.
$$

From the doubling property [(5)](../../introduction/README.md), $D=2^{100a^2}$ and [(10)](../../proof-of-metric-space-carleson-overview/README.md), we obtain

$$
\mu(B(c(J'), 204D^{s(J') + 1})) \leq 2 ^ {200a^3 + 10a} \mu(J)\,.\qquad\text{(24)}
$$

If $J \subset B({\mathrm{c}}({\mathfrak p}), 4 D^{{\mathrm{s}}({\mathfrak p})})$, then we need only check that $\mu({\mathcal{I}}({\mathfrak p})) \le 2^{100a^3 + 10a} \mu(J)$. This follows immediately from ${\mathcal{I}}({\mathfrak p}) \subset B(c(J'), 100 D^{s(J') + 1})$ and (24).

From now on we assume $J \not \subset B({\mathrm{c}}({\mathfrak p}), 4 D^{{\mathrm{s}}({\mathfrak p})})$. Since

$$
{\mathrm{c}}({\mathfrak p}) \in {\mathcal{I}}({\mathfrak p}) \subset B(c(J'), 100 D^{s(J') + 1})\, ,
$$

we have by [(10)](../../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality

$$
J \subset J' \subset B(c(J'), 4D^{s(J')}) \subset B({\mathrm{c}}({\mathfrak p}), 104 D^{s(J') + 1})\,.
$$

In particular this implies $104 D^{s(J') + 1} > 4D^{{\mathrm{s}}({\mathfrak p})}$. By the triangle inequality we also have

$$
B({\mathrm{c}}({\mathfrak p}), 104 D^{s(J') + 1}) \subset B(c(J), 204 D^{s(J') + 1})\,,
$$

so from (24),

$$
\mu( B({\mathrm{c}}({\mathfrak p}), 104 D^{s(J') + 1})) \le 2^{200a^3 + 10a} \mu(J)\,,
$$

which proves ${\mathfrak p}$ satisfies the needed criteria with $r=104 D^{s(J') + 1}$.

## Lean

Formalized as [`TileStructure.Forest.local_dens2_tree_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.local_dens2_tree_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4988](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4988)
