---
declaration: lemma
origin: cited
lean: Turing.exists_boundedUniversalCode
statement: formalized
---

# Bounded universal machine

For each arity $i$ there are a machine code $U$ with $i + 2$ input tapes and a polynomial $P$ such that on input $(\alpha;\, T \text{ in binary};\, x)$, the machine $U$ always halts within $P(\left\vert {\alpha} \right\vert + T)$ steps, outputting the canonically encoded budgeted evaluation of $[\alpha]_i$ on $x$ with budget $T$.

## Depends on

- [Machine codes](def-machine-code.md)
- [Runs of coded machines](def-code-run.md)

## Proof

Not planned: issue \#18 was closed on 2026-09-24, and the Lean statement is left as a `sorry`. The main theorem does not use this lemma; its universal machine is the ambient one of Lemma [Efficient universal Turing machine](lem-universal-tm.md).

## Lean

Stated as [`Turing.exists_boundedUniversalCode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.exists_boundedUniversalCode); the blueprint marks no proof of it as formalized.

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 101](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L101)
