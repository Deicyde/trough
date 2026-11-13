---
declaration: section
origin: cited
lean: MetaMathlibExt.zykovZeroIndicator, MetaMathlibExt.independentSetCharacteristic, MetaMathlibExt.relationPairing, MetaMathlibExt.zykovTransferMatrix
statement: formalized
proof: formalized
---

# Fibonacci numbers of graphs

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs/index.html).

## Zero indicator of a natural number

For a natural number $z$, the zero indicator of $z$ is
the Boolean value that is true if $z = 0$ and false otherwise.

Formalized by `MetaMathlibExt.zykovZeroIndicator`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs/index.html#zykov-zero-indicator).

## Characteristic vector of an independent set

Let $G$ be a simple graph on a vertex type
$V$ and let $A$ be a finite independent set of $G$. The characteristic vector of $A$ is the
Boolean function on $V$ that sends a vertex $v$ to true if $v \in A$ and to false otherwise.

Formalized by `MetaMathlibExt.independentSetCharacteristic`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs/index.html#independent-set-characteristic).

## Pairing of Boolean vectors along a relation

Let $V$ and $W$ be finite types, let $R$ be a
relation between $V$ and $W$, and let $a$ and $b$ be Boolean functions on $V$ and on $W$. The
pairing of $a$ and $b$ along $R$ is the natural number of pairs $(v, w) \in V \times W$ such that
$R(v, w)$ holds and both $a(v)$ and $b(w)$ are true.

Formalized by `MetaMathlibExt.relationPairing`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs/index.html#relation-pairing).

## Transfer matrix of a generalized Zykov sum

Let $G$ and $H$ be simple graphs on finite
vertex types $V$ and $W$, and let $R$ be a relation between $V$ and $W$. The transfer matrix of
$G$ and $H$ along $R$ is indexed by pairs $(A, B)$ where $A$ is a finite independent set of $G$
and $B$ is a finite independent set of $H$. Its entry at $(A, B)$ is the Boolean value that is
true exactly when the pairing along $R$ of the characteristic vectors of $A$ and $B$ is zero,
that is, when there are no $v \in A$ and $w \in B$ with $R(v, w)$.

Only the loopless case is covered: $G$ and $H$ are simple graphs, whereas the source construction
of Bautista-Ramos and Guillén-Galván also allows loops.

Formalized by `MetaMathlibExt.zykovTransferMatrix`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/TransferMatrixOfGRH.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs/index.html#zykov-transfer-matrix).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci numbers of graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/independence-and-domination/fibonacci-numbers-of-graphs)
