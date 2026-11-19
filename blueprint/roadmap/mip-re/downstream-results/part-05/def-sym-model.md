---
declaration: definition
origin: cited
lean: MIPRE.LIDT.Co.VecState, MIPRE.LIDT.Co.VecState.ev, MIPRE.LIDT.Co.SymModel, MIPRE.LIDT.Co.SymModel.flip, MIPRE.LIDT.Co.SymModel.R
statement: formalized
---

# Symmetric models

A *vector state* on a Hilbert space $K$ is a unit vector $\Psi \in K$, with the expectation $\mathrm{ev}(X) = \mathrm{Re}\, \langle \Psi, X \Psi \rangle$ of a bounded operator $X$ on $K$. A *symmetric model* over a C$^*$-algebra $\mathcal{P}$ consists of a vector state $\Psi$ on $K$, a unital $*$-homomorphism $L : \mathcal{P} \to B(K)$, the first player's placement, and a linear isometry $J$ of $K$ onto itself with $J^2 = 1$ and $J \Psi = \Psi$, such that $L(x)$ commutes with $J L(y) J$ for all $x, y \in \mathcal{P}$. The *flip* is the $*$-automorphism $X \mapsto J X J$ of $B(K)$, and the second player's placement is $R = \mathrm{flip} \circ L$, so that $L(x)$ and $R(y)$ commute.

The vendored proof of Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md) works with a state on $\mathbb{C}^\iota \otimes \mathbb{C}^\iota$: its local operators are the $\iota \times \iota$ matrices, its joint operators those of the tensor product, and its placements $A \mapsto A \otimes {I}$ and $A \mapsto {I} \otimes A$. A symmetric model replaces them by $\mathcal{P}$, $B(K)$, $L$ and $R$, and the Kronecker product $A \otimes B$ by $L(A)\, R(B)$. Measurements are generic over the ring of operators, local ones in $\mathcal{P}$ and joint ones in $B(K)$. A quantity that uses only the state, not the placements, belongs to the vector state, so that it applies as well to a state on one space, tensored with an ancilla, or reduced.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.LIDT.Co.VecState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.VecState), [`MIPRE.LIDT.Co.VecState.ev`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.VecState.ev), [`MIPRE.LIDT.Co.SymModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel), [`MIPRE.LIDT.Co.SymModel.flip`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.flip), [`MIPRE.LIDT.Co.SymModel.R`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.R).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3241](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3241)
