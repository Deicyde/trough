---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CompactOperatorAdjoint.isCompactOperator_adjoint_of_finiteRank, MathlibExt.Analysis.InnerProductSpace.CompactOperatorAdjoint.isCompactOperator_adjoint, MathlibExt.Analysis.InnerProductSpace.CompactOperatorAdjoint.isCompactOperator_adjoint_iff
statement: formalized
proof: formalized
---

# Schauder's theorem on compact adjoints

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/schauder-s-theorem-on-compact-adjoints/index.html).

## The adjoint of a finite-rank operator is compact

Let $E$ and $F$ be Hilbert spaces over
$\mathbb{R}$ or $\mathbb{C}$. If a bounded linear operator $T : E \to F$ has finite-dimensional
range, then its adjoint $T^* : F \to E$ is a compact operator.

The proof factors $T$ through its range $R$ as $T = i \circ \pi$, where $\pi : E \to R$ is $T$
with its codomain restricted to $R$ and $i : R \to F$ is the inclusion. Then
$T^* = \pi^* \circ i^*$, and $\pi^*$ is compact because its domain $R$ is finite-dimensional,
hence locally compact.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactOperatorAdjoint.isCompactOperator_adjoint_of_finiteRank`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactOperatorAdjoint.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompactOperatorAdjoint.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/schauder-s-theorem-on-compact-adjoints/index.html#is-compact-operator-adjoint-of-finite-ra).

## Schauder's theorem

The adjoint of a compact operator between
Hilbert spaces is compact.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactOperatorAdjoint.isCompactOperator_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactOperatorAdjoint.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompactOperatorAdjoint.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/schauder-s-theorem-on-compact-adjoints/index.html#is-compact-operator-adjoint).

## Schauder's theorem, iff form

A bounded operator between Hilbert
spaces is compact if and only if its adjoint is compact.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactOperatorAdjoint.isCompactOperator_adjoint_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactOperatorAdjoint.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompactOperatorAdjoint.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/schauder-s-theorem-on-compact-adjoints/index.html#is-compact-operator-adjoint-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schauder's theorem on compact adjoints](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/schauder-s-theorem-on-compact-adjoints/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/schauder-s-theorem-on-compact-adjoints)
