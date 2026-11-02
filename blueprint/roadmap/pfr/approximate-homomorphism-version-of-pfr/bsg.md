---
declaration: lemma
origin: cited
lean: BSG_self
statement: formalized
proof: formalized
---

# Balog–Szemerédi–Gowers lemma

Let $G$ be a finite abelian group, and let $A$ be a non-empty subset of $G$ with $E(A) \geq \frac{1}{K} \left( \frac{|A|}{|G|} \right)^3$ for some $K \geq 1$. Then there is a subset $A'$ of $A$ with $|A'| \geq |A| / (C_1 K^{C_2})$ and $|A'-A'| \leq C_3 K^{C_4} |A|$, where

$$
C_1 = 2^4, C_2 = 1, C_3 = 2^{10}, C_4 = 5.
$$

The Lean statement gives the two conclusions as inequalities between densities; these are equivalent to the ones above, the common factor $|G|$ cancelling.

## Depends on

- [Additive energy](energy-def.md)

## Proof

See <https://terrytao.files.wordpress.com/2024/01/simplebsg.pdf>.

## Lean

Formalized as [`BSG_self`](https://teorth.github.io/pfr/docs/find/#doc/BSG_self).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 42](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/approx_hom_pfr.tex#L42)
