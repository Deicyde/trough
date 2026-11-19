---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.SelfImprovement.SdpStatementWithSlackness.of_isSummedSdp, MIPRE.LIDT.Co.SelfImprovement.sdp_statement_with_slackness, MIPRE.LIDT.Co.SelfImprovement.selfImprovementHelper, MIPRE.LIDT.Co.SelfImprovement.selfImprovementHelperError_pos, MIPRE.LIDT.Co.SelfImprovement.SelfImprovementConclusion, MIPRE.LIDT.Co.SelfImprovement.selfImprovement, MIPRE.LIDT.Co.SelfImprovement.selfImprovement_of_axisParallel_selfConsistency
statement: formalized
proof: formalized
---

# Self-improvement, in a symmetric model

Consider an $(\varepsilon, \delta, \gamma)$-good symmetric strategy in $S$ for the low individual degree test, as in Lemma [Commutativity of points, in a symmetric model](../part-05/lem-co-commutativity-points.md), with point measurements $A^u$ in $\mathcal{P}$. Let the bipartite reading of $S$ be a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)) whose first player's operators contain no nonzero abelian projection, and let $d \geq 1$. Let $G$ be a measurement in $\mathcal{P}$ whose outcomes are the polynomials, with $\mathop{\mathbb{E}}_u \mathrm{cons}(A^u, G^{[u]}) \leq \nu$ for a uniformly random point $u$, where $G^{[u]}$ is $G$ evaluated at $u$, and put

$$
\sigma = 3000\, m \Bigl(\varepsilon^{1/32} + \delta^{1/32} + \Bigl(\frac{d}{q}\Bigr)^{1/32}\Bigr).
$$

Then there are a projective submeasurement $H$ in $\mathcal{P}$ whose outcomes are the polynomials and $Z \geq 0$ in $\mathcal{P}$ with $\mathop{\mathbb{E}}_u A^u_{g(u)} \leq Z$ for every polynomial $g$, such that

1. *(completeness)* $\mathrm{ev}\bigl(L(H_{\mathrm{total}})\bigr) \geq 1 - \nu - \sigma$;
2. *(consistency with the points)* $\mathop{\mathbb{E}}_u \mathrm{cons}(A^u, H^{[u]}) \leq \sigma$;
3. *(self-closeness)* $\sum_g \| (L(H_g) - R(H_g)) \Psi \|^2 \leq \sigma$;
4. *(boundedness)* $\mathrm{ev}\bigl(L(Z)\, R(1 - H_{\mathrm{total}})\bigr) \leq \sigma$.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Finite pairs](../part-04/def-finite-pair.md)
- [Global variance of the points, in a symmetric model](lem-co-global-variance-of-points.md)
- [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md)
- [The summed semidefinite form in the doubled model](cor-summed-sdp-doubled.md)

## Proof depends on

- [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md)
- [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.SelfImprovement.selfImprovement` in `MIPRE/Background/LIDT/MIPStarRE/LDT/SelfImprovement/`, rewritten over the symmetric model (`planning/c6b-plan.md`, milestone M10), with two of its inputs replaced. It first produces a submeasurement $\widehat{H}$ with the four properties at the error $\eta = 100\, m (\sqrt{\varepsilon} + \sqrt{\delta} + \sqrt{d/q})$, $\widehat{H}$ being strongly self-consistent in place of self-close. The semidefinite program supplies a measurement $T$ whose outcomes are the polynomials and $Z \in \mathcal{P}$ with $Z \geq A_g = \mathop{\mathbb{E}}_u A^u_{g(u)}$ and $T_g Z = T_g A_g$ for every $g$, and $\widehat{H}_h = \mathop{\mathbb{E}}_u A^u_{h(u)} T_h A^u_{h(u)}$; the vendored proof obtains $T$ and $Z$ from finite-dimensional strong duality, and here they are the summed form of Theorem [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md) in the first player's algebra of the finite pair (Corollary [The summed semidefinite form in the doubled model](cor-summed-sdp-doubled.md)), whose fields are exactly the three the proof consumes. The four properties of $\widehat{H}$ are Cauchy–Schwarz estimates for the vector state, with the global variance of the points (Lemma [Global variance of the points, in a symmetric model](lem-co-global-variance-of-points.md)) bounding the cost of moving $u$. Since $d \geq 1$, $\eta > 0$, and orthonormalization (Lemma [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md), item 2) rounds $\widehat{H}$ to a projective $H$ at the error $100\, \eta^{1/4}$, where the vendored proof rounds in finite dimension at any $\eta \geq 0$. Data processing and the completeness transfers of Lemma [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md) carry the four properties from $\widehat{H}$ to $H$, and the accumulated error is at most $\sigma$. When $\varepsilon$, $\delta$ or $d/q$ exceeds $1$, $\sigma \geq 1$ and $H = 0$, $Z = 1$ will do. Where the vendored proof uses the permutation invariance of the state, the port uses $\mathrm{ev}(L(x)) = \mathrm{ev}(R(x))$ (Lemma [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)).

## Lean

Formalized as [`MIPRE.LIDT.Co.SelfImprovement.SdpStatementWithSlackness.of_isSummedSdp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.SdpStatementWithSlackness.of_isSummedSdp), [`MIPRE.LIDT.Co.SelfImprovement.sdp_statement_with_slackness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.sdp_statement_with_slackness), [`MIPRE.LIDT.Co.SelfImprovement.selfImprovementHelper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.selfImprovementHelper), [`MIPRE.LIDT.Co.SelfImprovement.selfImprovementHelperError_pos`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.selfImprovementHelperError_pos), [`MIPRE.LIDT.Co.SelfImprovement.SelfImprovementConclusion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.SelfImprovementConclusion), [`MIPRE.LIDT.Co.SelfImprovement.selfImprovement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.selfImprovement), [`MIPRE.LIDT.Co.SelfImprovement.selfImprovement_of_axisParallel_selfConsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SelfImprovement.selfImprovement_of_axisParallel_selfConsistency).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3981](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3981)
