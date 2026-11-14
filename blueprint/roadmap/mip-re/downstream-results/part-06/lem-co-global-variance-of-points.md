---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.GlobalVariance.weightedPointConditionedOperatorAtPolynomial, MIPRE.LIDT.Co.GlobalVariance.GlobalVarianceOfPointsStatement, MIPRE.LIDT.Co.GlobalVariance.localVarianceTransportChainBound, MIPRE.LIDT.Co.GlobalVariance.globalVarianceOfPoints
statement: formalized
proof: formalized
---

# Global variance of the points, in a symmetric model

Consider an $(\varepsilon, \delta, \gamma)$-good symmetric strategy in $S$ for the low individual degree test, as in Lemma [Commutativity of points, in a symmetric model](../part-05/lem-co-commutativity-points.md), with point measurements $A^u$ in $\mathcal{P}$, and let $G$ be a submeasurement in $\mathcal{P}$ whose outcomes are the polynomials. For a polynomial $g$ and a point $u$ put $W^u_g = L(A^u_{g(u)})\, R(\sqrt{G_g})$. Then for every polynomial $g$

$$
\mathop{\mathbb{E}}_{(u, v)} \bigl\| (W^u_g - W^v_g) \Psi \bigr\|^2 \leq 6 \Bigl(4 \varepsilon + 4 \delta + \frac{2md}{q}
\Bigr), \qquad \mathop{\mathbb{E}}_{u, v} \bigl\| (W^u_g - W^v_g) \Psi \bigr\|^2 \leq 24\, m \Bigl(\varepsilon + \delta +
\frac{md}{q}\Bigr),
$$

where on the left $u$ is a uniformly random point and $v$ is $u$ with a uniformly random coordinate replaced by a uniformly random element of $\mathbb{F}_q$, and on the right $u$ and $v$ are independent uniformly random points.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Local-to-global variance on the hypercube, for any vector state](lem-co-local-to-global.md)

## Proof depends on

- [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.GlobalVariance.globalVarianceOfPoints` in `MIPRE/Background/LIDT/MIPStarRE/LDT/GlobalVariance/`, rewritten over the symmetric model (`planning/c6b-plan.md`, milestone M6). Six comparisons carry $W^u_g$ to $W^v_g$ along an edge, each an averaged squared distance: the self-consistency test ($2\delta$), the axis-parallel test ($2\varepsilon$), the Schwartz–Zippel bound for the line through $u$ and $v$ ($md/q$, twice), and the first two undone at $v$ ($2\varepsilon$, $2\delta$); the triangle inequality for six steps loses a factor $6$. The global bound is Lemma [Local-to-global variance on the hypercube, for any vector state](lem-co-local-to-global.md) for the family $u \mapsto W^u_g$, which costs the factor $m$, with $6 (4\varepsilon + 4\delta + 2md/q) \leq 24 (\varepsilon + \delta + md/q)$. The vendored proof evaluates these variances on the weighted state $R(\sqrt{G_g})\, \rho\, R(\sqrt{G_g})$, which is not normalized; a vector state has no density, so here they are the variances of the weighted family on $\Psi$ itself, the same numbers. The consistency relations are used in both orders, which in a symmetric model is a theorem (Lemma [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)).

## Lean

Formalized as [`MIPRE.LIDT.Co.GlobalVariance.weightedPointConditionedOperatorAtPolynomial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.GlobalVariance.weightedPointConditionedOperatorAtPolynomial), [`MIPRE.LIDT.Co.GlobalVariance.GlobalVarianceOfPointsStatement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.GlobalVariance.GlobalVarianceOfPointsStatement), [`MIPRE.LIDT.Co.GlobalVariance.localVarianceTransportChainBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.GlobalVariance.localVarianceTransportChainBound), [`MIPRE.LIDT.Co.GlobalVariance.globalVarianceOfPoints`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.GlobalVariance.globalVarianceOfPoints).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3834](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3834)
