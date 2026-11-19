---
declaration: definition
origin: cited
lean: BohrSet.IsRegular
statement: formalized
---

# Regularity

We say $\nu:\widehat{G}\to \mathbb{R}$ is regular if, with $d=\mathrm{rk}(\nu)$, for all $\kappa\in\mathbb{R}$ with $\left\lvert \kappa\right\rvert\leq 1/100d$ we have

$$
(1-100 d\left\lvert \kappa\right\rvert)\leq \frac{\left\lvert \mathrm{Bohr}((1+\kappa)\nu)\right\rvert}{\left\lvert \mathrm{Bohr}(\nu)\right\rvert}\leq(1+ 100 d\left\lvert \kappa\right\rvert)
$$

## Depends on

- [Bohr sets](bohr-set.md)

## Lean

Formalized as [`BohrSet.IsRegular`](https://yaeldillies.github.io/apap/docs/find/#doc/BohrSet.IsRegular).

## Sources

- [Kelley-Meka bound blueprint: chapter/bohr.tex, line 44](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/bohr.tex#L44)
