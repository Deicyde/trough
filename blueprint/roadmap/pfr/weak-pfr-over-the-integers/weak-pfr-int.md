---
declaration: theorem
origin: cited
lean: weak_PFR_int
statement: formalized
proof: formalized
---

# weak-pfr-int

Let $A\subseteq \mathbb{Z}^d$ and $\lvert A-A\rvert\leq K\lvert A\rvert$. There exists $A'\subseteq A$ such that $\lvert A'\rvert \geq K^{-17}\lvert A\rvert$ and $\dim A' \leq \frac{40}{\log 2}\log K$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [weak-pfr-symm](weak-pfr-symm.md)
- [dimension-def](dimension-def.md)

## Proof

As in the beginning of [PFR](../proof-of-pfr/pfr.md) the doubling condition forces $d[U_A;U_A]\leq \log K$, and then we apply [Theorem weak-pfr-symm](weak-pfr-symm.md).

## Lean

Formalized as [`weak_PFR_int`](https://teorth.github.io/pfr/docs/find/#doc/weak_PFR_int).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 224](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/weak_pfr.tex#L224)
