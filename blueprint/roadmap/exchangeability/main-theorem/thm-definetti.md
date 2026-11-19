---
declaration: theorem
origin: cited
lean: Exchangeability.DeFinetti.deFinetti_RyllNardzewski_equivalence
statement: formalized
---

# de Finetti–Ryll-Nardzewski equivalence (martingale route)

For an infinite sequence $(X_n)_{n \in \mathbb{N}}$ of random variables taking values in a *standard Borel space* $\alpha$ (with $\alpha$ nonempty), the following are equivalent:

1. $(X_n)$ is contractable
2. $(X_n)$ is exchangeable
3. $(X_n)$ is conditionally i.i.d. (i.e., there exists a directing kernel $\nu$)

This is the default project export. The proof constructs $\nu$ from the tail $\sigma$-algebra $\mathcal{T}$ via $\nu(\omega)(B) = \mathbb{E}[\mathbf{1}_{X_0 \in B} \mid \mathcal{T}](\omega)$.

## Depends on

- [Exchangeable implies Contractable](../easy-directions/exchangeable-implies-contractable/thm-contractable-of-exchangeable.md)
- [Conditionally i.i.d. implies Exchangeable](../easy-directions/conditionally-i-i-d-implies-exchangeable/thm-exchangeable-of-conditionallyiid.md)
- [Contractable implies Conditionally i.i.d. (via Martingale)](../main-implication-contractable-implies-conditiona/via-martingale-aldous-proof/thm-conditionallyiid-of-contractable-martingale.md)

## Lean

Stated as [`Exchangeability.DeFinetti.deFinetti_RyllNardzewski_equivalence`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.deFinetti_RyllNardzewski_equivalence); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 608](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L608)
