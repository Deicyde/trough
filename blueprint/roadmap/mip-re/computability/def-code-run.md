---
declaration: definition
origin: cited
lean: Turing.Code.Produces, Turing.Code.evalWithin
statement: formalized
---

# Runs of coded machines

Let $c$ be a machine code with $i$ input tapes, $x = (x_1, \ldots, x_i)$ bit strings and $y \in \{0,1\}^*$. The code $c$ *produces* $y$ on $x$ if its run on $x$ halts with output $y$ (in some time and space). The *budgeted evaluation* of $c$ on $x$ with budget $T$ returns the output if $c$ has halted within $T$ steps, and a timeout marker otherwise; it is total and executable, and the two notions agree: $c$ produces $y$ if and only if some budget suffices to observe it.

## Depends on

- [Machine codes](def-machine-code.md)

## Lean

Formalized as [`Turing.Code.Produces`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.Code.Produces), [`Turing.Code.evalWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.Code.evalWithin).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 51](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L51)
