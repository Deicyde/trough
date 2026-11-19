---
declaration: lemma
origin: cited
lean: spec_hoelder
statement: formalized
proof: formalized
---

# spec_hoelder

Let $G$ be a finite abelian group and $f:G\to\mathbb{C}$. Let $\Delta\subseteq \Delta_\eta(f)$. Then, for any $m\geq 1$.

$$
N^{-1}\eta^{2m}\frac{\lVert f\rVert_1^2}{\lVert f\rVert_2^2}\left\lvert \Delta\right\rvert^{2m}\le E_{2m}(\Delta).
$$

## Depends on

- [Energy](energy.md)

## Proof depends on

- [general_hoelder](general-hoelder.md)

## Proof

Apply Lemma [general_hoelder](general-hoelder.md) with $\nu\equiv 1$, and use the fact that $\sum_x \lambda(x)$ is $N$ if $\lambda\equiv 1$ and $0$ otherwise.

## Lean

Formalized as [`spec_hoelder`](https://yaeldillies.github.io/apap/docs/find/#doc/spec_hoelder).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 135](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L135)
