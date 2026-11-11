---
declaration: section
origin: cited
lean: MetaMathlibExt.TripSternTree, MetaMathlibExt.TripSternTree.nodeAtPath, MetaMathlibExt.TripSternTree.nodeAtEmptyPath, MetaMathlibExt.TripSternTree.nodeAtPathAppendLeft, MetaMathlibExt.TripSternTree.nodeAtPathAppendRight, MetaMathlibExt.TripSternTree.nodesAtDepth, MetaMathlibExt.TripSternTree.nodeMembershipAtDepth, MetaMathlibExt.TripSternTree.nodesAtDepthZero
statement: formalized
proof: formalized
---

# TRIP-Stern sequences

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html).

## TRIP-Stern tree

A TRIP-Stern tree with node values in a type $\alpha$ consists of a root
seed in $\alpha$ together with two maps from $\alpha$ to $\alpha$, the left transition and the
right transition. No condition is imposed on the seed or on the two transitions; in the source
the seed is $(1,1,1)$ and the left and right transitions are induced by the maps $F_0$ and $F_1$
defined there.

## Sources

- Ilya Amburg, Krishna Dasaratha, Laure Flapan, Thomas Garrity, Chansoo Lee, Cornelia Mihaila, Nicholas Neumann-Chun, Sarah Peluse, and Matthew Stoffregen, *Stern Sequences for a Family of Multidimensional Continued Fractions: TRIP-Stern Sequences*, Journal of Integer Sequences 20 (2017), Article 17.1.7, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Garrity/garrity6.tex>. The tree abstracts Definition TRIPSternDef, lines 471-481 (seed (1,1,1), even/odd recursion by F_0/F_1, levels as index intervals), with F_0/F_1 from line 387; binary paths follow the triangle(v) definition, lines 485-488.

Formalized by `MetaMathlibExt.TripSternTree`, a structure declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#trip-stern-tree).

## Node selected by a binary path

Let $T$ be a TRIP-Stern tree with seed $s$, left
transition $L$ and right transition $R$. A binary path is a finite sequence of steps, each left
or right. The node of $T$ selected by a path $(b_1, \dots, b_k)$ is obtained by starting at $s$
and applying, for $i = 1, \dots, k$ in order, $L$ if $b_i$ is a left step and $R$ if $b_i$ is a
right step.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodeAtPath`, a definition declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#node-at-path).

## The empty path selects the seed

For every TRIP-Stern tree $T$, the node of $T$ selected
by the empty binary path is the seed of $T$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodeAtEmptyPath`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#node-at-empty-path).

## Extending a path by a left step

Let $T$ be a TRIP-Stern tree with left transition $L$.
For every binary path $p$, the node of $T$ selected by $p$ followed by one left step equals $L$
applied to the node of $T$ selected by $p$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodeAtPathAppendLeft`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#node-at-path-append-left).

## Extending a path by a right step

Let $T$ be a TRIP-Stern tree with right transition $R$.
For every binary path $p$, the node of $T$ selected by $p$ followed by one right step equals $R$
applied to the node of $T$ selected by $p$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodeAtPathAppendRight`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#node-at-path-append-right).

## Nodes at a given depth of a TRIP-Stern tree

Let $T$ be a TRIP-Stern tree and $n$ a
natural number. The set of nodes of $T$ at depth $n$ is the set of all values $y$ such that some
binary path of length $n$ selects $y$ in $T$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodesAtDepth`, a definition declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#nodes-at-depth).

## Membership in a level of a TRIP-Stern tree

For every TRIP-Stern tree $T$, natural number
$n$ and node value $y$, $y$ lies in the set of nodes of $T$ at depth $n$ if and only if there is
a binary path of length $n$ whose selected node in $T$ is $y$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodeMembershipAtDepth`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#node-membership-at-depth).

## Depth zero is the seed

For every TRIP-Stern tree $T$ and every node value $y$, $y$ lies
in the set of nodes of $T$ at depth $0$ if and only if $y$ is the seed of $T$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.nodesAtDepthZero`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#nodes-at-depth-zero).

## Left-most node of a TRIP-Stern tree

Let $T$ be a TRIP-Stern tree with seed $s$ and left
transition $L$. The left-most node of $T$ at depth $n$ is $L^n(s)$, the result of applying $L$
$n$ times to $s$; that is, it is $s$ at depth $0$, and at depth $n + 1$ it is $L$ applied to the
left-most node at depth $n$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.leftmostNode`, a definition declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#leftmost-node).

## Rightmost node of a TRIP-Stern tree

For a TRIP-Stern tree $T$ and a natural number $n$,
the rightmost node of $T$ at depth $n$ is obtained from the seed of $T$ by applying the right
transition of $T$ exactly $n$ times: at depth $0$ it is the seed, and at depth $n + 1$ it is the
image of the rightmost node at depth $n$ under the right transition.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.rightmostNode`, a definition declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#rightmost-node).

## Left-most node at depth zero

For every TRIP-Stern tree $T$, the left-most node of $T$ at
depth $0$ is the seed of $T$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.leftmostNodeAtZero`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#leftmost-node-at-zero).

## Recursion for the left-most node

Let $T$ be a TRIP-Stern tree with left transition
$L$. For every natural number $n$, the left-most node of $T$ at depth $n + 1$ equals $L$ applied
to the left-most node of $T$ at depth $n$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.leftmostNodeAtSuccessor`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#leftmost-node-at-successor).

## Rightmost node at depth zero

For every TRIP-Stern tree $T$, the rightmost node of $T$ at
depth $0$ is the seed of $T$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.rightmostNodeAtZero`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#rightmost-node-at-zero).

## Successor step of the rightmost node

For every TRIP-Stern tree $T$ and every natural
number $n$, the rightmost node of $T$ at depth $n + 1$ is the image of the rightmost node of
$T$ at depth $n$ under the right transition of $T$.

## Sources

- Amburg et al., *TRIP-Stern Sequences*, JIS 20 (2017), Article 17.1.7, Definition TRIPSternDef, lines 471-481.

Formalized by `MetaMathlibExt.TripSternTree.rightmostNodeAtSuccessor`, a theorem declared in [MathlibExt/NumberTheory/TripSternTree.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TripSternTree.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html#rightmost-node-at-successor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: TRIP-Stern sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/trip-stern-sequences)
