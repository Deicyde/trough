---
declaration: theorem
origin: cited
lean: weak_PFR
statement: formalized
proof: formalized
---

# weak-pfr-symm

If $A\subseteq \mathbb{Z}^d$ is a finite non-empty set with $d[U_A;U_A]\leq \log K$ then there exists a non-empty $A'\subseteq A$ such that

$$
\lvert A'\rvert\geq K^{-17}\lvert A\rvert
$$

and $\dim A'\leq \frac{40}{\log 2} \log K$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [weak-pfr-asymm](weak-pfr-asymm.md)
- [dimension-def](dimension-def.md)

## Proof

Immediate from [Theorem weak-pfr-asymm](weak-pfr-asymm.md) and rearranging.

## Lean

Formalized as [`weak_PFR`](https://teorth.github.io/pfr/docs/find/#doc/weak_PFR).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 209](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/weak_pfr.tex#L209)
