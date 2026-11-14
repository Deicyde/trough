---
declaration: lemma
origin: cited
lean: MIPRE.ValueApprox.posSemidef_realSmul_one_add_and_sub_iff
statement: formalized
proof: formalized
---

# Decidable candidate set: a norm constraint is two psd tests

Let $M$ be a Hermitian matrix and $c$ a real number. Then $c{I} + M \succeq 0$ and $c{I} - M \succeq 0$ both hold if and only if $-c\left\| {x} \right\|^2 \leq \langlex| M |x\rangle \leq c \left\| {x} \right\|^2$ for every vector $x$ — which for Hermitian $M$ says $\left\| {M} \right\| \leq c$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Both directions are the defining property of positive semidefiniteness applied to the quadratic form, read once forwards and once backwards; the scalar step is $\langlex|(c{I} \pm M)|x\rangle = c\left\| {x} \right\|^2 \pm \langlex| M |x\rangle$.

## Lean

Formalized as [`MIPRE.ValueApprox.posSemidef_realSmul_one_add_and_sub_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.posSemidef_realSmul_one_add_and_sub_iff).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7445](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7445)
