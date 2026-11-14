---
declaration: theorem
origin: cited
lean: MIPRE.SummedSdp.IsSummedSdp, MIPRE.SummedSdp.IsSummedSdp.sum_mul_eq, MIPRE.SummedSdp.IsFaithfulTrace, MIPRE.SummedSdp.isSummedSdp_of_firstOrder, MIPRE.SummedSdp.isSummedSdp_of_isMaxOn, MIPRE.SummedSdp.isSummedSdp_of_le, MIPRE.Orthonormalization.exists_isMaxOn_obj, MIPRE.Orthonormalization.exists_isSummedSdp, MIPRE.Orthonormalization.exists_isSummedSdp_centralizer, MIPRE.Orthonormalization.exists_isSummedSdp_finitePairA, MIPRE.Orthonormalization.exists_isSummedSdp_finitePairB
statement: formalized
proof: formalized
---

# The summed semidefinite form, in a commutant with a vector trace

Let $t$ be a set of bounded operators on a Hilbert space $\mathcal{H}$, and let $\mathcal{M}$ be the commutant of $t \cup t^*$: the operators commuting with every element of $t$ and with its adjoint. Let $\xi_1, \dots, \xi_n \in \mathcal{H}$ be vectors such that $\tau(x) = \sum_k \langle \xi_k, x \xi_k \rangle$ is tracial on $\mathcal{M}$ and separates it. Let $A_1, \dots, A_m \in \mathcal{M}$ be self-adjoint. Then there is a measurement $T$ in $\mathcal{M}$, positive elements $T_1, \dots, T_m$ with $\sum_i T_i = 1$, such that $Z = \sum_i T_i A_i$ satisfies:

1. $Z$ is self-adjoint;
2. $A_i \leq Z$ for every $i$;
3. $T_i Z = T_i A_i$ for every $i$.

Conversely, for a measurement $T$ in $\mathcal{M}$, items 1 and 2 imply item 3. In a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)), each player's operators are such a commutant, with the pair's vector trace, so the conclusion holds in each of them. These are the data of the semidefinite program that the vendored proof obtains from Lemma 9.2 of (JNVWY21qld), which this replaces.

## Depends on

- [Finite pairs](../part-04/def-finite-pair.md)

## Proof

The measurements of $\mathcal{M}$ form a weak-operator compact set, and $f(T) = \sum_i \mathrm{Re}\, \tau(T_i A_i)$ is weak-operator continuous, being a finite sum of matrix coefficients. So $f$ has a maximizer $T$. Perturbing $T$ toward a single outcome $h$ by $T'_i = K T_i K + \delta_{ih}(1 - K^2)$, with $K = 1 - \varepsilon P$ for $0 \leq P \leq 1$ in $\mathcal{M}$, expands $f(T')$ exactly to second order in $\varepsilon$. Maximality then gives the first-order condition $\mathrm{Re}\, \tau(P A_h) \leq \mathrm{Re}\, \tau(P Z)$ for all such $P$. Let $W = \frac{1}{2}(Z + Z^*)$, and let $N$ be the negative part of $W - A_h$, which lies in $\mathcal{M}$. The condition at $P = N / (1 + \|N\|)$ gives $\mathrm{Re}\, \tau(N^2) \leq 0$, since $N (W - A_h) = -N^2$; so $N = 0$ by faithfulness, and $A_h \leq W$. Then $\mathrm{Re}\, \tau(T_h (W - A_h)) \geq 0$ for every $h$, with sum $\mathrm{Re}\, \tau(W - Z) = 0$, and faithfulness of $\tau$ makes each product vanish: $W T_h = A_h T_h$. Summing over $h$ gives $W = Z^*$, hence $Z = W$ (`reports/c6b-paper-proofs.md`, Section 5, Theorem 10 and Corollary 11). The weak-operator compactness of the unit ball is that of the vendored orthonormalization development.

## Lean

Formalized as [`MIPRE.SummedSdp.IsSummedSdp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SummedSdp.IsSummedSdp), [`MIPRE.SummedSdp.IsSummedSdp.sum_mul_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SummedSdp.IsSummedSdp.sum_mul_eq), [`MIPRE.SummedSdp.IsFaithfulTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SummedSdp.IsFaithfulTrace), [`MIPRE.SummedSdp.isSummedSdp_of_firstOrder`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SummedSdp.isSummedSdp_of_firstOrder), [`MIPRE.SummedSdp.isSummedSdp_of_isMaxOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SummedSdp.isSummedSdp_of_isMaxOn), [`MIPRE.SummedSdp.isSummedSdp_of_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SummedSdp.isSummedSdp_of_le), [`MIPRE.Orthonormalization.exists_isMaxOn_obj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isMaxOn_obj), [`MIPRE.Orthonormalization.exists_isSummedSdp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isSummedSdp), [`MIPRE.Orthonormalization.exists_isSummedSdp_centralizer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isSummedSdp_centralizer), [`MIPRE.Orthonormalization.exists_isSummedSdp_finitePairA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isSummedSdp_finitePairA), [`MIPRE.Orthonormalization.exists_isSummedSdp_finitePairB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isSummedSdp_finitePairB).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3584](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3584)
