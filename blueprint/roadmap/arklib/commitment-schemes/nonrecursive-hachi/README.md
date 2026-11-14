# Nonrecursive Hachi

ArkLib formalizes a nonrecursive variant of the Hachi lattice-based multilinear polynomial commitment ([Nguyen et al. 2026](https://eprint.iacr.org/2026/156)), which builds on Greyhound (Nguyen and Seiler 2024). The recursive opening of the paper, which carries each iteration's evaluation claim to the next ring instead of closing it, is not formalized. Section [The Subfield $R_q^H \cong \mathbb{F}_{q^k}$ (Hachi Lemma 5)](../../supporting-theories/the-subfield-r-q-h-cong-f-q-k-hachi-lemma-5/README.md) covers the extension-field packing that the scheme uses.

Throughout, $R_q=\mathbb{Z}_q[X]/(X^{2^\alpha}+1)$. The committed data is a multilinear polynomial over $R_q$ in $r+m$ variables, and a query is an evaluation point. Honest range parameters consist of a balanced digit base $b$, a ball radius $\gamma$ and a zero-check digit base $b_0$, subject to

$$
1\lt b\leq q/2,\qquad 1\lt b_0\leq q/2,\qquad
\lfloor b/2\rfloor\leq\gamma,\qquad \lfloor b_0/2\rfloor\leq\gamma\leq b_0-1.
$$

The remaining parameters are the challenge weight $\omega$, the digit count $\tau$ and bound $z_{\max}$ for the folded witness, a sumcheck dimension $M$, and a ring homomorphism $\mathbb{Z}_q\to\mathbb{F}$ into the field over which the sumcheck runs. Write $\delta_b=\lceil\log_b q\rceil$, and write $\mu_0$ and $n_0$ for the column and row counts of the linear relation that the ring-switching step produces.

- [Nonrecursive Hachi](def-hachi-nonrecursive.md)
- [Perfect correctness of nonrecursive Hachi](thm-hachi-correctness.md)

With the honest range constraint $\gamma\leq b_0-1$, the last assumption forces $\gamma=b_0-1$.

Soundness. The soundness side is formalized for the reduction chain, not for the scheme. Each subprotocol carries a coordinate-wise special soundness certificate whose extraction may instead output an escape event: a Module-SIS solution for the public matrices, or a collision in the lift commitment.

- [Special soundness of one Hachi iteration](thm-hachi-iteration-cwss.md)

Binding of the scheme and knowledge soundness of its opening, as commitment-scheme properties, are not formalized. The scheme's terminal verifier and the soundness-side terminal check use the same decision procedure.
