---
declaration: section
origin: cited
lean: Cslib.Databases.Access, Cslib.Databases.Op, Cslib.Databases.Op.Conflicts, Cslib.Databases.Op.OrderMatters, Cslib.Databases.ConflictEquiv, Cslib.Databases.TxnBefore, Cslib.Databases.IsSerial, Cslib.Databases.ConflictSerializable
statement: formalized
proof: formalized
---

# Conflict serializability

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html).

## Databases

## Read or write access

The kind of access an operation makes to its data item is one of
two values: a read or a write.

Formalized by `Cslib.Databases.Access`, an inductive type declared in [CSLibExt/Databases/Serializability.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#access).

## Operation of a schedule

For $n$ transactions, numbered $0, \dots, n - 1$, and data items
of type $X$, an operation consists of a transaction $t \in \{0, \dots, n - 1\}$, an occurrence
identifier $k \in \mathbb{N}$, an access, which is a read or a write, and a data item $x \in X$:
transaction $t$ reads or writes $x$, and $k$ makes repeated accesses of $t$ to an item distinct
operations.

Formalized by `Cslib.Databases.Op`, a structure declared in [CSLibExt/Databases/Serializability.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#op).

## Conflicting operations

Two operations of a schedule conflict when they belong to different
transactions, access the same data item, and at least one of the two accesses is a write.

Formalized by `Cslib.Databases.Op.Conflicts`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#conflicts).

## Operations whose relative order matters

Two operations $a$ and $b$ are order-relevant when
they belong to the same transaction or they conflict. These are the pairs whose relative order a
conflict-equivalent schedule must keep.

Formalized by `Cslib.Databases.Op.OrderMatters`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#order-matters).

## Conflict equivalence

A schedule $s'$ is conflict-equivalent to a schedule $s$ when $s'$
is a permutation of $s$ and, for any two operations $a$ and $b$ that belong to the same
transaction or conflict, an occurrence of $a$ comes before an occurrence of $b$ in $s$ if and
only if the same holds in $s'$.

Formalized by `Cslib.Databases.ConflictEquiv`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#conflict-equiv).

## One transaction before another in a schedule

For a schedule $s$ and transactions $i$ and
$j$, transaction $i$ precedes transaction $j$ in $s$ when every operation of $i$ in $s$ occurs in
$s$ before every operation of $j$ in $s$.

Formalized by `Cslib.Databases.TxnBefore`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#txn-before).

## Serial schedule

A schedule $s$ is serial when, for any two distinct transactions $i$ and
$j$, either every operation of $i$ in $s$ occurs before every operation of $j$ in $s$, or every
operation of $j$ in $s$ occurs before every operation of $i$ in $s$.

Formalized by `Cslib.Databases.IsSerial`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#is-serial).

## Conflict-serializable schedule

A schedule $s$ is conflict-serializable when some serial
schedule is conflict-equivalent to $s$.

Formalized by `Cslib.Databases.ConflictSerializable`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#conflict-serializable).

## Edge of the precedence graph

For a schedule $s$ and transactions $i$ and $j$, there is a
precedence edge from $i$ to $j$ in $s$ when some operation of $i$ occurs in $s$ before some
operation of $j$ in $s$ that conflicts with it.

Formalized by `Cslib.Databases.PrecedenceEdge`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#precedence-edge).

## Precedence graph

The precedence (serialization) graph of a schedule $s$ of $n$
transactions is the directed adjacency graph whose vertices are the transactions
$0, \dots, n - 1$, listed in increasing order, and whose adjacency list at a transaction $i$ lists,
in increasing order, the transactions $j$ such that there is a precedence edge from $i$ to $j$
in $s$.

Formalized by `Cslib.Databases.precedenceGraph`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#precedence-graph).

## Serialization of a schedule along a transaction order

For a list $\sigma$ of transactions
and a schedule $s$, the serialization of $s$ along $\sigma$ sorts the operations of $s$ by the
position of the first occurrence of their transaction in $\sigma$, where a transaction that does
not occur in $\sigma$ gets the length of $\sigma$ as its position. The sort is stable: operations
with the same position keep their relative order in $s$.

Formalized by `Cslib.Databases.serialize`, a definition declared in [CSLibExt/Databases/Serializability.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#serialize).

## A conflict-serializable schedule has an acyclic precedence graph

If a schedule $s$ in
which no operation occurs twice is conflict-serializable, then the precedence graph of $s$ is
acyclic.

In a conflict-equivalent serial schedule, the position of the first operation of each
transaction increases along every edge of the precedence graph.

Formalized by `Cslib.Databases.ConflictSerializable.isAcyclic`, a theorem declared in [CSLibExt/Databases/Serializability.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#is-acyclic).

## Serializing along a complete transaction order gives a serial schedule

Let $s$ be a
schedule and $L$ a list in which every transaction occurs. Then the schedule obtained from $s$
by stably sorting its operations by the first position of their transaction in $L$ is serial.

Formalized by `Cslib.Databases.isSerial_serialize`, a theorem declared in [CSLibExt/Databases/Serializability.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#is-serial-serialize).

## Serializing along a topological order preserves conflict equivalence

Let $s$ be a
schedule in which no operation occurs twice, and let $L$ be a topological order of the
precedence graph of $s$. Then the schedule obtained from $s$ by stably sorting its operations
by the first position of their transaction in $L$ is conflict-equivalent to $s$.

Formalized by `Cslib.Databases.conflictEquiv_serialize`, a theorem declared in [CSLibExt/Databases/Serializability.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#conflict-equiv-serialize).

## The serializability theorem

A schedule without duplicate operations is
conflict-serializable exactly when its precedence graph is acyclic.

Formalized by `Cslib.Databases.conflictSerializable_iff_isAcyclic`, a theorem declared in [CSLibExt/Databases/Serializability.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#conflict-serializable-iff-is-acyclic).

## A rank increasing along precedence edges gives conflict serializability

Let $s$ be a
schedule in which no operation occurs twice. If $r$ is a function from the transactions to the
natural numbers with $r(i) < r(j)$ whenever the precedence graph of $s$ has an edge from $i$ to
$j$, then $s$ is conflict-serializable.

Formalized by `Cslib.Databases.conflictSerializable_of_rank`, a theorem declared in [CSLibExt/Databases/Serializability.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Databases/Serializability.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html#conflict-serializable-of-rank).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conflict serializability](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/databases/conflict-serializability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/databases/conflict-serializability)
