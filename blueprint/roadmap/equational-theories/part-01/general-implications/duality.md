---
declaration: lemma
origin: cited
lean: Law.MagmaLaw.implies_iff_dual
statement: formalized
---

# Duality of laws

The law $w \simeq w'$ implies $w''\simeq w'''$, if and only if $w^{\mathrm{op}} \simeq (w')^{\mathrm{op}}$ implies $w''^{\mathrm{op}} \simeq (w''')^{\mathrm{op}}$.

## Depends on

Its statement uses no other node that has an article here.

## Proof

This follows from the fact that a magma $G$ satisfies a law $w \simeq w'$ if and only if $G^{\mathrm{op}}$ satisfies $w^{\mathrm{op}} \simeq (w')^{\mathrm{op}}$.

## Lean

Stated as [`Law.MagmaLaw.implies_iff_dual`](https://teorth.github.io/equational_theories/docs/find/#doc/Law.MagmaLaw.implies_iff_dual); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/general_implications.tex, line 57](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/general_implications.tex#L57)
