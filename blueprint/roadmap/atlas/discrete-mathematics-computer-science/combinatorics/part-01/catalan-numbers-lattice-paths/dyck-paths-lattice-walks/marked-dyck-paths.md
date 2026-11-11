---
declaration: section
origin: cited
lean: MetaMathlibExt.MarkedDyckStep, MetaMathlibExt.markedDyckCountE, MetaMathlibExt.markedDyckCountN, MetaMathlibExt.markedDyckCountNstar, MetaMathlibExt.MarkedDyckPath, MetaMathlibExt.IsMarkedStep, MetaMathlibExt.MarkedDyckPath.pathSize, MetaMathlibExt.MarkedDyckPath.size_eq
statement: formalized
proof: formalized
---

# Marked Dyck paths

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html).

## Steps of a marked Dyck path

A step of a marked Dyck path is one of three kinds: a
horizontal step $E = (1, 0)$, an unmarked vertical step $N = (0, 1)$, or a marked vertical step
$N^* = (0, 1)$.

Formalized by `MetaMathlibExt.MarkedDyckStep`, an inductive type declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#marked-dyck-step).

## Number of horizontal steps in a marked Dyck step sequence

For a finite sequence $P$ of
marked Dyck steps, $E(P)$ is the number of horizontal steps $E$ in $P$.

Formalized by `MetaMathlibExt.markedDyckCountE`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#marked-dyck-count-e).

## Number of unmarked vertical steps

For a finite sequence $P$ of marked Dyck steps,
$N(P)$ is the number of unmarked vertical steps $N$ in $P$.

Formalized by `MetaMathlibExt.markedDyckCountN`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#marked-dyck-count-n).

## Number of marked vertical steps

For a finite sequence $P$ of marked Dyck steps,
$N^*(P)$ is the number of marked vertical steps $N^*$ in $P$.

Formalized by `MetaMathlibExt.markedDyckCountNstar`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#marked-dyck-count-nstar).

## Marked Dyck path

Let $E(Q)$, $N(Q)$ and $N^*(Q)$ denote the numbers of horizontal steps
$E$, unmarked vertical steps $N$ and marked vertical steps $N^*$ in a finite sequence $Q$ of
marked Dyck steps. A marked Dyck path is a finite sequence $P$ of marked Dyck steps such that
$E(P) = N(P) + N^*(P)$ and every prefix $Q$ of $P$ satisfies $N(Q) + N^*(Q) \le E(Q)$: a
lattice path from $(0, 0)$ that ends on the diagonal and never goes above it.

Formalized by `MetaMathlibExt.MarkedDyckPath`, a structure declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#marked-dyck-path).

## Marked step of a marked Dyck path

Let $P$ be a marked Dyck path with $\ell$ steps. For a
position $i$ with $0 \le i < \ell$, the step of $P$ at position $i$ is marked when it is the
marked vertical step $N^*$ (rather than an unmarked vertical step $N$ or a horizontal step $E$).

Formalized by `MetaMathlibExt.IsMarkedStep`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#is-marked-step).

## Size of a marked Dyck path

The size of a marked Dyck path $P$ is $N^*(P) + E(P)$,
where $N^*(P)$ is the number of marked vertical steps of $P$ and $E(P)$ the number of its
horizontal steps.

Formalized by `MetaMathlibExt.MarkedDyckPath.pathSize`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#path-size).

## Size of a marked Dyck path in vertical steps

For every marked Dyck path $P$, the size of
$P$ equals $N(P) + 2N^*(P)$, where $N(P)$ and $N^*(P)$ are the numbers of unmarked and marked
vertical steps of $P$.

Formalized by `MetaMathlibExt.MarkedDyckPath.size_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMarkedDyckPath.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#size-eq).

## Steps of a multi-marked Dyck path

A step of a multi-marked Dyck path is one of the
horizontal step $E = (1, 0)$, the plain vertical step $N = (0, 1)$, or, for an integer
$t \ge 2$, the marked vertical step $N^*_t = (0, 1)$ of index $t$. There are no marked steps
of index less than $2$.

Formalized by `MetaMathlibExt.MultiMarkedStep`, an inductive type declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-step).

## Number of horizontal steps in a multi-marked step sequence

For a finite sequence $P$ of
multi-marked steps (horizontal steps $E$, plain vertical steps $N$ and marked vertical steps
$N^*_t$ with index $t \ge 2$), $E(P)$ is the number of horizontal steps $E$ in $P$.

Formalized by `MetaMathlibExt.multiMarkedCountE`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-count-e).

## Number of plain vertical steps

For a finite sequence $P$ of multi-marked steps
(horizontal steps $E$, plain vertical steps $N$ and marked vertical steps $N^*_t$ with index
$t \ge 2$), $N(P)$ is the number of plain (unmarked) vertical steps $N$ in $P$.

Formalized by `MetaMathlibExt.multiMarkedCountPlainN`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-count-plain-n).

## Number of vertical steps

For a finite sequence $P$ of multi-marked steps (horizontal
steps $E$, plain vertical steps $N$ and marked vertical steps $N^*_t$ with index $t \ge 2$),
this is the number of vertical steps in $P$, plain steps $N$ and marked steps $N^*_t$ counted
together.

Formalized by `MetaMathlibExt.multiMarkedCountVert`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-count-vert).

## Number of steps

For a finite sequence $P$ of multi-marked steps (horizontal steps $E$,
plain vertical steps $N$ and marked vertical steps $N^*_t$ with index $t \ge 2$), this is the
total number of steps in $P$, that is, the length of $P$.

Formalized by `MetaMathlibExt.multiMarkedCountTotal`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-count-total).

## Index sum of a multi-marked step sequence

For a finite sequence $s$ of steps of a
multi-marked Dyck path, the index sum of $s$ is the sum of the indices $t$ over all occurrences
of marked steps $N^*_t$ in $s$, each occurrence counted separately; the steps $E$ and $N$
contribute nothing.

Grouping the occurrences by index, the index sum equals $\sum_t t \cdot N^*_t(s)$, where
$N^*_t(s)$ is the number of marked steps of index $t$ in $s$.

Formalized by `MetaMathlibExt.multiMarkedIndexSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-index-sum).

## Shifted index sum of a multi-marked step sequence

For a finite sequence $s$ of steps of
a multi-marked Dyck path, the shifted index sum of $s$ is the sum of $t - 1$ over all
occurrences of marked steps $N^*_t$ in $s$, each occurrence counted separately; the steps $E$
and $N$ contribute nothing.

Grouping the occurrences by index, the shifted index sum equals
$\sum_t (t - 1) \cdot N^*_t(s)$, where $N^*_t(s)$ is the number of marked steps of index $t$ in $s$.

Formalized by `MetaMathlibExt.multiMarkedShiftedIndexSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-shifted-index-sum).

## Number of marked steps of a given index

For a finite sequence $P$ of multi-marked steps
(horizontal steps $E$, plain vertical steps $N$ and marked vertical steps $N^*_s$ with index
$s \ge 2$) and a natural number $t$, $N^*_t(P)$ is the number of marked steps in $P$ whose index
is exactly $t$.

Formalized by `MetaMathlibExt.multiMarkedCountMarkedT`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-count-marked-t).

## Size of a multi-marked step sequence

The size of a finite sequence $s$ of steps of a
multi-marked Dyck path is $E(s) + \sum (t - 1)$, where $E(s)$ is the number of horizontal steps
$E$ in $s$ and the sum runs over all occurrences of marked steps $N^*_t$ in $s$.

Formalized by `MetaMathlibExt.multiMarkedSize`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-size).

## Multi-marked Dyck path

A multi-marked Dyck path is a finite sequence $P$ of steps, each
a horizontal step $E = (1,0)$, a plain vertical step $N = (0,1)$ or a marked vertical step
$N^*_t = (0,1)$ carrying an index $t \ge 2$, such that every prefix of $P$, including the empty
prefix and $P$ itself, has at most as many vertical steps (plain and marked) as horizontal
steps, and $P$ has exactly as many vertical steps as horizontal steps.

Read as a lattice path from $(0,0)$, $P$ never rises above the diagonal and ends on it.

Formalized by `MetaMathlibExt.MultiMarkedDyckPath`, a structure declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-dyck-path).

## Equal horizontal and vertical step counts

For every multi-marked Dyck path $P$, the
number $E(P)$ of horizontal steps of $P$ equals the number of vertical steps of $P$, plain steps
$N$ and marked steps $N^*_t$ counted together.

Formalized by `MetaMathlibExt.multiMarkedCountEq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-count-eq).

## Vertical count plus shifted index sum

For every finite sequence $s$ of steps of a
multi-marked Dyck path, the number of vertical steps of $s$ plus the shifted index sum of $s$
equals the number of plain vertical steps $N$ of $s$ plus the index sum of $s$.

Each marked step $N^*_t$ contributes $1 + (t - 1)$ to the left side and $t$ to the right side.

Formalized by `MetaMathlibExt.multiMarkedVertShifted_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-vert-shifted-eq).

## Two expressions for the size of a multi-marked Dyck path

For every multi-marked Dyck
path $P$, the size $E(P) + \sum (t - 1)$ of $P$ equals $N(P) + \sum t$, where $E(P)$ is the
number of horizontal steps $E$ of $P$, $N(P)$ is the number of plain vertical steps $N$ of $P$,
and both sums run over all occurrences of marked steps $N^*_t$ in $P$.

Grouped by index, this reads
$E(P) + \sum_t (t - 1) N^*_t(P) = N(P) + \sum_t t N^*_t(P)$, where $N^*_t(P)$ is the number of
marked steps of index $t$ in $P$.

Formalized by `MetaMathlibExt.multiMarkedSizeEq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-size-eq).

## Vertical steps of a multi-marked Dyck path

A step of a multi-marked Dyck path is
vertical when it is the plain step $N$ or a marked step $N^*_t$; the horizontal step $E$ is not
vertical. This test delimits the final run of vertical steps of a step sequence.

Formalized by `MetaMathlibExt.multiMarkedIsVert`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-is-vert).

## Final run of vertical steps

The final run of vertical steps of a finite sequence $s$
of steps of a multi-marked Dyck path is the longest suffix of $s$ consisting of vertical steps
($N$ or $N^*_t$): the part of $s$ after its last horizontal step $E$, or all of $s$ if $s$ has
no step $E$.

Formalized by `MetaMathlibExt.multiMarkedTrailingVert`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-trailing-vert).

## Marked tail

A multi-marked Dyck path $P$ has a marked tail when its final run of
vertical steps (the steps after its last horizontal step $E$, or all of $P$ if $P$ has no step
$E$) contains a marked vertical step $N^*_t$ for some index $t \ge 2$.

Formalized by `MetaMathlibExt.MultiMarkedDyckPath.HasMarkedTail`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#has-marked-tail).

## Unmarked tail

A multi-marked Dyck path $P$ has an unmarked tail when it does not
have a marked tail, that is, when its final run of vertical steps (the steps after its last
horizontal step $E$, or all of $P$ if $P$ has no step $E$) contains no marked vertical step.

Formalized by `MetaMathlibExt.MultiMarkedDyckPath.HasUnmarkedTail`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#has-unmarked-tail).

## Multi-marked Dyck paths of a given size

For a natural number $n$, $\tilde P_n$ is the
set of multi-marked Dyck paths $P$ of size $n$. Here the size of $P$ is $E(P) + \sum (t - 1)$,
where $E(P)$ is the number of horizontal steps of $P$ and the sum runs over the marked steps
$N^*_t$ of $P$, each occurrence counted separately.

Formalized by `MetaMathlibExt.MultiMarkedDyckPathOfSize`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-dyck-path-of-size).

## Multi-marked Dyck paths with an unmarked tail

For a natural number $n$, $\tilde R_n$ is
the set of multi-marked Dyck paths of size $n$ with an unmarked tail, that is, whose final
run of vertical steps contains no marked step.

Formalized by `MetaMathlibExt.MultiMarkedUnmarkedTail`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MarkedStepInAMultiMarkedDyckPath.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html#multi-marked-unmarked-tail).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Marked Dyck paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/marked-dyck-paths)
