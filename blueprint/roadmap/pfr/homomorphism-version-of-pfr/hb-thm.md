---
declaration: lemma
origin: cited
lean: hahn_banach
statement: formalized
proof: formalized
---

# Hahn-Banach type theorem

Let $H_0$ be a subgroup of $G$. Then every homomorphism $\phi: H_0 \to G'$ can be extended to a homomorphism $\tilde \phi: G \to G'$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By induction it suffices to treat the case where $H_0$ has index $2$ in $G$, but then the extension can be constructed by hand.

## Lean

Formalized as [`hahn_banach`](https://teorth.github.io/pfr/docs/find/#doc/hahn_banach).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/hom_pfr.tex, line 5](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/hom_pfr.tex#L5)
