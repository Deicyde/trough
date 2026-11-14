---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Doubling.isFinitePair, MIPRE.LIDT.Co.Doubling.tr_diag2_L, MIPRE.LIDT.Co.Doubling.L_nonneg_iff, MIPRE.LIDT.Co.Doubling.R_nonneg_iff, MIPRE.LIDT.Co.Doubling.equiv_nonneg_iff, MIPRE.LIDT.Co.Doubling.isDyadicPair, MIPRE.LIDT.Co.Doubling.model_L_injective, MIPRE.LIDT.Co.SymModel.L_cfc, MIPRE.LIDT.Co.Doubling.cfc_mem_opsA
statement: formalized
proof: formalized
---

# The doubled model is a finite pair, with the order of its parts

Let $M$ be a finite pair in a unit state, and $D(M)$ its doubled model (Definition [The doubled model](../part-05/def-doubled-model.md)), read as a bipartite model with the placements $L$ and $R$.

1. $D(M)$ is a finite pair. Its placements are injective. The first player's operators $\{a \oplus b\}$ are the commutant of the second player's $\{b \oplus a\}$, and conversely. A vector trace $\tau$ of $M$'s first player's operators and a vector trace $\sigma$ of its second player's give the vector trace $\tau_D(a \oplus b) = \frac{1}{2}(\tau(a) + \sigma(b))$ of the first player's operators of $D(M)$, and symmetrically for the second player.
2. The orders agree: $x \geq 0$ in $\mathcal{P}$ if and only if $L(x) \geq 0$, if and only if $R(x) \geq 0$. When $\mathcal{A}$ and $\mathcal{B}$ are star-ordered, these also hold if and only if the preimage of $x$ in $\mathcal{A} \times \mathcal{B}$ is nonnegative.
3. If $M$ is a dyadic pair (Definition [Dyadic pairs](../part-05/def-dyadic-pair.md)), so is $D(M)$.
4. The continuous functional calculus of $\mathcal{P}$ is that of the operators: $L(f(x)) = f(L(x))$ for self-adjoint $x \in \mathcal{P}$ and every $f : \mathbb{R} \to \mathbb{R}$. The first player's operators of $M$ are closed under the functional calculus.

## Depends on

- [The doubled model](../part-05/def-doubled-model.md)
- [Dyadic pairs](../part-05/def-dyadic-pair.md)
- [Dyadic matrix units exclude abelian projections](../part-05/thm-no-abelian-dyadic.md)

## Proof

An operator on $\mathcal{H} \oplus \mathcal{H}$ that commutes with $R(0, 1) = 1 \oplus 0$ is block diagonal. Its first block commutes with $\mathcal{B}_c$, so it lies in $\mathcal{A}_c$, and its second block lies in $\mathcal{B}_c$ in the same way. So an operator commuting with every $R(y)$ is an $L(x)$, and symmetrically. The trace vectors are $(g_k, 0)/\sqrt{2}$ and $(0, h_l)/\sqrt{2}$, for the trace vectors $g_k$ of $\tau$ and $h_l$ of $\sigma$. Traciality and separation hold blockwise. A block-diagonal operator is positive exactly when each block is, which gives item 2 together with Lemma [The players' algebras of a finite pair, as commutants with their order](../part-05/lem-finite-pair-order.md). The dyadic matrix units of $\mathcal{A}$ and of $\mathcal{B}$ transfer to $\mathcal{A}_c$ and $\mathcal{B}_c$, and pair componentwise into units of $\mathcal{P}$. For item 4, $L$ is an injective $*$-homomorphism of C$^*$-algebras, so it preserves spectra and commutes with the functional calculus. The first player's operators of $M$ are a closed commutant, which contains the functional calculus of each of its self-adjoint elements (`reports/c6b-paper-proofs.md`, Section 4, Theorem A and Proposition H).

## Lean

Formalized as [`MIPRE.LIDT.Co.Doubling.isFinitePair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isFinitePair), [`MIPRE.LIDT.Co.Doubling.tr_diag2_L`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.tr_diag2_L), [`MIPRE.LIDT.Co.Doubling.L_nonneg_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.L_nonneg_iff), [`MIPRE.LIDT.Co.Doubling.R_nonneg_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.R_nonneg_iff), [`MIPRE.LIDT.Co.Doubling.equiv_nonneg_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.equiv_nonneg_iff), [`MIPRE.LIDT.Co.Doubling.isDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isDyadicPair), [`MIPRE.LIDT.Co.Doubling.model_L_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.model_L_injective), [`MIPRE.LIDT.Co.SymModel.L_cfc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.L_cfc), [`MIPRE.LIDT.Co.Doubling.cfc_mem_opsA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.cfc_mem_opsA).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3396](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3396)
