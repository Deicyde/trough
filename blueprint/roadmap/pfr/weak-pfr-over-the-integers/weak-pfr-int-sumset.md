---
declaration: corollary
origin: cited
lean: weak_PFR_int_sumset
statement: formalized
proof: formalized
---

# weak-pfr-int-sumset

Let $A\subseteq \mathbb{Z}^d$ and $\lvert A+A\rvert\leq K\lvert A\rvert$. There exists $A'\subseteq A$ such that $\lvert A'\rvert \geq K^{-34}\lvert A\rvert$ and $\dim A' \leq \frac{80}{\log 2}\log K$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [weak-pfr-int](weak-pfr-int.md)

## Proof

By the Ruzsa triangle inequality one has $\lvert A-A\rvert \leq K^2 \lvert A\rvert$, and then we apply [Theorem weak-pfr-int](weak-pfr-int.md).

## Lean

Formalized as [`weak_PFR_int_sumset`](https://teorth.github.io/pfr/docs/find/#doc/weak_PFR_int_sumset).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 234](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/weak_pfr.tex#L234)
