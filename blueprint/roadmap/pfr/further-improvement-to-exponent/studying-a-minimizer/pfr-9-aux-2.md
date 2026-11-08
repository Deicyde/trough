---
declaration: corollary
origin: cited
lean: better_PFR_conjecture_aux
statement: formalized
proof: formalized
---

# pfr-9-aux'

If $|A+A| \leq K|A|$, then there exist a subgroup $H$ and a subset $c$ of $G$ with $A \subseteq c + H$, such that $|c| \leq K^{5} |A|^{1/2}/|H|^{1/2}$ and $|H|/|A|\in[K^{-8},K^8]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr-9-aux](pfr-9-aux.md)
- [Ruzsa covering lemma](../../proof-of-pfr/ruz-cov.md)

## Proof

Apply [Corollary pfr-9-aux](pfr-9-aux.md) and [Ruzsa covering lemma](../../proof-of-pfr/ruz-cov.md) to get the result, as in the proof of [Lemma pfr_aux](../../proof-of-pfr/pfr-aux.md).

## Lean

Formalized as [`better_PFR_conjecture_aux`](https://teorth.github.io/pfr/docs/find/#doc/better_PFR_conjecture_aux).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 363](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L363)
