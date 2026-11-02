---
declaration: lemma
origin: cited
lean: MellinOfSmooth1b
statement: formalized
proof: formalized
---

# MellinOfSmooth1b

Given $0\lt \sigma_1\le\sigma_2$, for any $s$ such that $\sigma_1\le\mathcal Re(s)\le\sigma_2$, we have

$$
\mathcal{M}(\widetilde{1_{\epsilon}})(s) = O\left(\frac{1}{\epsilon|s|^2}\right).
$$

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [MellinOfSmooth1a](mellinofsmooth1a.md)
- [MellinOfPsi](mellinofpsi.md)

## Proof

Use Lemma [MellinOfSmooth1a](mellinofsmooth1a.md) and the bound in Lemma [MellinOfPsi](mellinofpsi.md).

## Lean

Formalized as [`MellinOfSmooth1b`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinOfSmooth1b).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
