---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Doubling.ev_L, MIPRE.LIDT.Co.Doubling.inner_L_mul_R, MIPRE.LIDT.Co.Doubling.bornProb_model_eq, MIPRE.LIDT.Co.Doubling.qBipartiteConsDefect_model, MIPRE.LIDT.Co.Doubling.dis_model, MIPRE.LIDT.Co.Doubling.inconsistency_model, MIPRE.LIDT.Co.Doubling.bipartiteConsError_model, MIPRE.LIDT.Co.Doubling.bipartiteConsError_components_le_two_mul, MIPRE.LIDT.Co.bipartiteConsError_eq_inconsistency
statement: formalized
proof: formalized
---

# The role average in the doubled model

Let $M$ be a finite pair in a unit state $\psi$, and $D(M)$ its doubled model (Definition [The doubled model](../part-05/def-doubled-model.md)). Write $x = (x^1, x^2)$ for $x \in \mathcal{P}$. For all $x, y \in \mathcal{P}$,

$$
\langle \Psi, L(x) R(y) \Psi \rangle = \tfrac{1}{2} \bigl( \langle \psi, x^1 y^2 \psi \rangle +
\langle \psi, y^1 x^2 \psi \rangle \bigr).
$$

So the Born probability of $D(M)$ at $(x, y)$ is the average of the Born probabilities of $M$ at $(x^1, y^2)$ and at $(y^1, x^2)$. The same holds exactly for the submeasurement consistency defect $\max(0, \mathrm{total} - \mathrm{match})$ of two submeasurements, for its average over a question distribution, and for the disagreement and the inconsistency of positive operator valued measurements. Consequently, if the averaged defect of two families $X$, $Y$ in $D(M)$ is at most $\sigma$, then each of the two defects of $M$, at $(X^1, Y^2)$ and at $(Y^1, X^2)$, is at most $2\sigma$. For measurements, the averaged defect of $M$ is its inconsistency, weighted by the question distribution.

## Depends on

- [The doubled model](../part-05/def-doubled-model.md)
- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)

## Proof

$L(x) R(y) = x^1 y^2 \oplus y^1 x^2$, because $y^1 \in \mathcal{A}_c$ and $x^2 \in \mathcal{B}_c$ commute. The vector state $\Psi = (\psi, \psi)/\sqrt{2}$ averages the two blocks. In the defect the maximum with $0$ is inactive on both sides, since the summands are Born probabilities of positive elements, so the defect is the sum of the off-diagonal Born probabilities, and that sum halves too. The two defects of $M$ are nonnegative and average to at most $\sigma$, so each is at most $2\sigma$ (`reports/c6b-paper-proofs.md`, Section 4, Theorems C and E).

## Lean

Formalized as [`MIPRE.LIDT.Co.Doubling.ev_L`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.ev_L), [`MIPRE.LIDT.Co.Doubling.inner_L_mul_R`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.inner_L_mul_R), [`MIPRE.LIDT.Co.Doubling.bornProb_model_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.bornProb_model_eq), [`MIPRE.LIDT.Co.Doubling.qBipartiteConsDefect_model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.qBipartiteConsDefect_model), [`MIPRE.LIDT.Co.Doubling.dis_model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.dis_model), [`MIPRE.LIDT.Co.Doubling.inconsistency_model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.inconsistency_model), [`MIPRE.LIDT.Co.Doubling.bipartiteConsError_model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.bipartiteConsError_model), [`MIPRE.LIDT.Co.Doubling.bipartiteConsError_components_le_two_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.bipartiteConsError_components_le_two_mul), [`MIPRE.LIDT.Co.bipartiteConsError_eq_inconsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.bipartiteConsError_eq_inconsistency).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3439](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3439)
