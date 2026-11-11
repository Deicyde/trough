---
declaration: section
origin: cited
lean: MetaMathlibExt.IsTree, MetaMathlibExt.level, MetaMathlibExt.IsNormalTreeAt
statement: formalized
proof: formalized
---

# Trees in set theory

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/trees-in-set-theory/index.html).

## Tree (set theory)

A *tree* is a partially ordered set (T, <) iwith the property that for each x ∈ T, the set {  y
∈ T : y < x  } of all predecessors of x is well-ordered by <).

Formalized by `MetaMathlibExt.IsTree`, a definition declared in [MathlibExt/SetTheory/Tree/Basic.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Basic.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/trees-in-set-theory/index.html#tree-set-theory).

## Level of a well-founded partial order

For an ordinal α, the *α-th level* of a well-founded partial order (T, <) is Lev_α(T) = {  x ∈ T
: ht(x) = α  }, the set of elements whose height equals α.

Formalized by `MetaMathlibExt.level`, a definition declared in [MathlibExt/SetTheory/Tree/Basic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Basic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/trees-in-set-theory/index.html#level-of-a-well-founded-partial-order).

## Normal tree at a cardinal

Let κ be a cardinal and (α,≤) a well-founded partial order; for x∈α let rank(x) denote the rank
of x in the well-founded relation <. α is a *normal tree at κ* if:

\begin{enumerate}
  \item $\alpha$ is a tree at $\kappa$, i.e.
  \begin{itemize}
    \item $\forall x\in\alpha$, $\{y \mid y\lt x\}$ is a chain,
    \item $\forall x\in\alpha,\ \exists a\lt \kappa.\mathrm{ord},\ x\in\mathrm{level}_\alpha(a)$,
    \item $\forall a\lt \kappa.\mathrm{ord},\ \mathrm{level}_\alpha(a)\neq\emptyset$
          and $|\mathrm{level}_\alpha(a)|\lt \kappa$;
  \end{itemize}
  \item $\alpha$ has a root: $\exists r\in\alpha\ \forall x\in\alpha,\ r\le x$;
  \item every node can be extended to any higher level below $\kappa$:
  \[
    \forall x\in\alpha\ \forall b\lt \kappa.\mathrm{ord}\;
    \bigl(\operatorname{rank}(x)\lt b \to
    \exists y\in\alpha\ (x\lt y \land \operatorname{rank}(y)=b)\bigr);
  \]
  \item every node splits:
  \[
    \forall x\in\alpha\ \exists y,z\in\alpha\;
    \bigl(x\lt y \land x\lt z \land y\not\le z \land z\not\le y\bigr).
  \]
\end{enumerate}

Formalized by `MetaMathlibExt.IsNormalTreeAt`, a definition declared in [MathlibExt/SetTheory/Tree/Basic.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Basic.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/trees-in-set-theory/index.html#normal-tree-at-a-cardinal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trees in set theory](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/trees-in-set-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/trees-in-set-theory)
