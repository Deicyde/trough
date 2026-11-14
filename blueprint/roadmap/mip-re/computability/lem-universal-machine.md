---
declaration: lemma
origin: cited
lean: Turing.exists_universalCode
statement: formalized
---

# Universal machine

For each arity $i$ there are a machine code $U$ with $i + 1$ input tapes and a polynomial $P$ such that for all $\alpha \in \{0,1\}^*$, all inputs $x$ and all $y$: $U$ on $(\alpha; x)$ produces $y$ if and only if $[\alpha]_i$ on $x$ produces $y$; and whenever $[\alpha]_i$ halts on $x$ within $t$ steps, $U$ halts on $(\alpha; x)$ within $P(\left\vert {\alpha} \right\vert + t)$ time and space.

## Depends on

- [Machine codes](def-machine-code.md)
- [Runs of coded machines](def-code-run.md)

## Proof

Not planned: issue \#17 was closed on 2026-09-24, and the Lean statement is left as a `sorry`. The main theorem does not use this lemma; its universal machine is the ambient one of Lemma [Efficient universal Turing machine](lem-universal-tm.md).

## Lean

Stated as [`Turing.exists_universalCode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.exists_universalCode); the blueprint marks no proof of it as formalized.

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 83](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L83)
