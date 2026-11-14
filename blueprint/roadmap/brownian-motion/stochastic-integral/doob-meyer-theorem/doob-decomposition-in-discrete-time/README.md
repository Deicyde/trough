# Doob decomposition in discrete time

- [Predictable part](def-predictablepart.md)
- [Martingale part](def-martingalepart.md)

In what follows, we fix a process $X : \mathbb{N} \to \Omega \to E$ and a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, and denote by $A$ the predictable part of $X$ and by $M$ its martingale part.

- [predictablePart_zero](lem-predictablepart-zero.md)
- [martingalePart_zero](lem-martingalepart-zero.md)
- [predictablePart_add_one](lem-predictablepart-add-one.md)
- [Martingale.predictablePart_eq_zero](lem-martingale-predictablepart-eq-zero.md)
- [isStronglyPredictable.predictablePart_eq](lem-isstronglypredictable-predictablepart-eq.md)
- [martingalePart_eq_zero](lem-martingalepart-eq-zero.md)
- [Martingale.martingalePart_eq](lem-martingale-martingalepart-eq.md)
- [predictablePart_smul](lem-predictablepart-smul.md)
- [martingalePart_smul](lem-martingalepart-smul.md)
- [predictablePart_add](lem-predictablepart-add.md)
- [martingalePart_add](lem-martingalepart-add.md)
- [adapted_predictablePart](lem-adapted-predictablepart.md)
- [predictable_predictablePart](lem-predictable-predictablepart.md)
- [martingale_martingalePart](lem-martingale-martingalepart.md)
- [Submartingale.monotone_predictablePart](lem-submartingale-monotone-predictablepart.md)
- [Submartingale.predictablePart_nonneg](lem-submartingale-predictablepart-nonneg.md)

TODO: define $\tau^T_{A_{n+1}>c}$ as the hitting time of $A_{n+1} > c$ but with the convention that it is equal to $T$ if the hitting time is greater than $T$ (`hittingBtwn`).

In the next lemmas, we write $\tau^T(c) = \tau^T_{A_{n+1}>c}$ for brevity.
