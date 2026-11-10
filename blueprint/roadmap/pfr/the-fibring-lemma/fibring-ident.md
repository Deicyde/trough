---
declaration: proposition
origin: cited
lean: rdist_of_indep_eq_sum_fibre, rdist_le_sum_fibre
statement: formalized
proof: formalized
---

# General fibring identity

Let $\pi : H \to H'$ be a homomorphism additive groups, and let $Z_1,Z_2$ be $H$-valued random variables. Then we have

$$
d[Z_1; Z_2] \geq d[\pi(Z_1);\pi(Z_2)] + d[Z_1|\pi(Z_1); Z_2 |\pi(Z_2)].
$$

Moreover, if $Z_1,Z_2$ are taken to be independent, then the difference between the two sides is

$$
I( Z_1 - Z_2 : (\pi(Z_1), \pi(Z_2))  |  \pi(Z_1 - Z_2) ).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Copy preserves Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-copy.md)
- [Existence of independent copies](../entropic-ruzsa-calculus/part-01/independent-exist.md)
- [Submodularity](../shannon-entropy-inequalities/part-01/submodularity.md)
- [Alternate formula for conditional mutual information](../shannon-entropy-inequalities/part-02/conditional-mutual-alt.md)
- [Chain rule](../shannon-entropy-inequalities/part-01/chain-rule.md)
- [Entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Alternate form of distance](../entropic-ruzsa-calculus/part-01/cond-dist-alt.md)

## Proof

Let $Z_1,Z_2$ be independent throughout (this is possible by [Copy preserves Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-copy.md) and [Existence of independent copies](../entropic-ruzsa-calculus/part-01/independent-exist.md)). By [Alternate form of distance](../entropic-ruzsa-calculus/part-01/cond-dist-alt.md), We have

$$
\begin{aligned}
& d[Z_1  |\pi(Z_1); Z_2 |\pi(Z_2)] \\
& = \mathbb{H}[Z_1 - Z_2 | \pi(Z_1),\pi(Z_2)] - \tfrac{1}{2} \mathbb{H}[Z_1 | \pi(Z_1)] - \tfrac{1}{2} \mathbb{H}[Z_2 | \pi(Z_2)] \\
& \leq  \mathbb{H}[Z_1 - Z_2 | \pi(Z_1+Z_2)]  - \tfrac{1}{2} \mathbb{H}[Z_1 | \pi(Z_1)] - \tfrac{1}{2}H[Z_2 | \pi(Z_2)] \\
& = d[Z_1;Z_2] - d[\pi(Z_1);\pi(Z_2)].
\end{aligned}
$$

In the middle step, we used [Submodularity](../shannon-entropy-inequalities/part-01/submodularity.md), and in the last step we used the fact that

$$
\mathbb{H}[Z_1 - Z_2 |  \pi(Z_1-Z_2)] = \mathbb{H}[Z_1 - Z_2] - \mathbb{H}[\pi(Z_1-Z_2)]
$$

(thanks to [Chain rule](../shannon-entropy-inequalities/part-01/chain-rule.md) and [Entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy.md)) and that

$$
\mathbb{H}[Z_i| \pi(Z_i)] = \mathbb{H}[Z_i] - \mathbb{H}[\pi(Z_i)]
$$

(since $Z_i$ determines $\pi(Z_i)$). This gives the claimed inequality. The difference between the two sides is precisely

$$
\mathbb{H}[Z_1 - Z_2  | \pi(Z_1 - Z_2)] - \mathbb{H}[Z_1 - Z_2  | \pi(Z_1),\pi(Z_2)].
$$

To rewrite this in terms of (conditional) mutual information, we use the identity

$$
\mathbb{H}[A|B] - \mathbb{H}[A | B,C] = \mathbb{I}[A : C | B],
$$

(which follows [Alternate formula for conditional mutual information](../shannon-entropy-inequalities/part-02/conditional-mutual-alt.md)) taking $A := Z_1 - Z_2$, $B := \pi(Z_1 - Z_2)$ and $C := (\pi(Z_1),\pi(Z_{2}))$, and noting that in this case $\mathbb{H}[A | B,C] = \mathbb{H}[A | C]$ since $C$ uniquely determines $B$ (this may require another helper lemma about entropy). This completes the proof.

## Lean

Formalized as [`rdist_of_indep_eq_sum_fibre`](https://teorth.github.io/pfr/docs/find/#doc/rdist_of_indep_eq_sum_fibre), [`rdist_le_sum_fibre`](https://teorth.github.io/pfr/docs/find/#doc/rdist_le_sum_fibre).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/fibring.tex, line 3](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/fibring.tex#L3)
