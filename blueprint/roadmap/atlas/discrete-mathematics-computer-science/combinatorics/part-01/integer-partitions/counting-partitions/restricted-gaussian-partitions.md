---
declaration: section
origin: cited
lean: MetaMathlibExt.GaussianPartition, MetaMathlibExt.Block, MetaMathlibExt.BranchStep, MetaMathlibExt.basicCount, MetaMathlibExt.branchBoundExp, MetaMathlibExt.removeFirstNPos, MetaMathlibExt.applySplit, MetaMathlibExt.blockFinalDims
statement: formalized
proof: formalized
---

# Restricted Gaussian partitions

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html).

## Gaussian partition

A Gaussian partition is represented by its list of subspace
dimensions, which is a nonincreasing list of natural numbers.

Formalized by `MetaMathlibExt.GaussianPartition`, a structure declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#gaussian-partition).

## Block

A block is a pair $(d, m)$ of natural numbers, read as a part size $d$ of an integer
partition together with its multiplicity $m$. No condition is imposed on a single block.

Formalized by `MetaMathlibExt.Block`, a structure declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#block).

## Branch step

A branch step is a triple $(a, b, c)$ of natural numbers. It describes one
simultaneous split level: for the ambient parameter $q$, $c$ copies of the parent dimension
$a + b$ become $c$ copies of $a$ and $c q^a$ copies of $b$.

Formalized by `MetaMathlibExt.BranchStep`, a structure declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#branch-step).

## Basic block multiplicity

Let $q$ be a natural number and
$(d_0, m_0), \dots, (d_{k-1}, m_{k-1})$ a list of blocks, and put $p_i = \sum_{j < i} m_j d_j$.
The basic multiplicity of block $i$ is $N_i = \sum_{j=0}^{m_i - 1} q^{p_i + j d_i}$ when $i < k$,
and $N_i = 0$ when $i \ge k$.

Formalized by `MetaMathlibExt.basicCount`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#basic-count).

## First-split exponent

Let $(d_0, m_0), \dots, (d_{k-1}, m_{k-1})$ be a list of blocks and
put $p_i = \sum_{j < i} m_j d_j$. The first-split exponent of block $i$ is
$u_i = p_i + (m_i - 1) d_i$ when $i < k$, where $m_i - 1$ is taken to be $0$ if $m_i = 0$, and
$u_i = 0$ when $i \ge k$.

Formalized by `MetaMathlibExt.branchBoundExp`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#branch-bound-exp).

## Removing the first occurrences of an entry

Let $x$ and $c$ be natural numbers and let
$l$ be a list of natural numbers. For $c = 0$ the result is the pair of the empty list and $l$.
For $c \ge 1$, if $l$ has at least $c$ entries equal to $x$, the result is the pair of the list
of entries different from $x$ that come before the $c$-th entry equal to $x$, in their order in
$l$, and the part of $l$ after that entry. If $l$ has fewer than $c$ entries equal to $x$, there
is no result.

Formalized by `MetaMathlibExt.removeFirstNPos`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#remove-first-npos).

## Split replacement in a dimension list

For natural numbers $q, a, b, c$ and a list $l$ of
natural numbers, the split replacement is defined exactly when $l$ has at least $c$ entries equal
to $a + b$. It removes the last $c$ entries of $l$ equal to $a + b$ and, at the position of the
first of these removed entries, inserts $c$ copies of $a$ followed by $c q^a$ copies of $b$; the
entries of $l$ before that position stay in front, and the entries after it that were not removed
follow in their original order. For $c = 0$ the list is unchanged.

No sorting is performed.

Formalized by `MetaMathlibExt.applySplit`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#apply-split).

## Final dimensions of a block

Let $q$ be a natural number,
$(d_0, m_0), \dots, (d_{k-1}, m_{k-1})$ a list of blocks and $C$ a list of chains of branch steps.
The final dimension list of block $i$ is defined when $C$ has an entry $s_1, \dots, s_r$ at index
$i$: start from $N_i$ copies of $d_i$, where $N_i$ is the basic multiplicity of block $i$ (the
empty list when $i \ge k$), and for $t = 1, \dots, r$ in order apply the split replacement of step
$s_t = (a_t, b_t, c_t)$, which replaces $c_t$ copies of $a_t + b_t$ by $c_t$ copies of $a_t$ and
$c_t q^{a_t}$ copies of $b_t$. It is undefined when $C$ has no entry at index $i$ or when one of
these split replacements is undefined.

Formalized by `MetaMathlibExt.blockFinalDims`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#block-final-dims).

## Stage segments of a restricted Gaussian partition

Let $q$ be a natural number, let
$(d_0, m_0), \dots, (d_{\ell-1}, m_{\ell-1})$ be blocks, let $C_0, C_1, \dots$ be chains of
branch steps, let $F_0, F_1, \dots$ be lists of natural numbers, and let $i$ and $k$ be natural
numbers; blocks, chains and lists are indexed from $0$. With $p_h = \sum_{g < h} m_g d_g$, the
basic segment of block $h$ is the list of $\sum_{j=0}^{m_h - 1} q^{p_h + j d_h}$ copies of $d_h$.
A step $(a, b, c)$ acts on a list by deleting its last $c$ entries equal to $a + b$ and putting
$c$ copies of $a$ followed by $c q^a$ copies of $b$ where the first deleted entry was, after the
entries before it and before the remaining entries after it (a step with $c = 0$ changes
nothing); it fails if the list has fewer than $c$ entries equal to $a + b$.

The stage segments at $(i, k)$ form the list of $\ell$ segments whose entry for block $h$ is
$F_h$ if $h < i$; the result of applying the first $k + 1$ steps of $C_i$ in order to the basic
segment of block $i$ if $h = i$ (all steps of $C_i$ if it has at most $k + 1$, and none if there
is no chain $C_i$); and the basic segment of block $h$ if $h > i$. They are undefined if $F_h$ is
missing for some block $h < i$ or one of these steps fails.

Formalized by `MetaMathlibExt.stageSegments`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#stage-segments).

## Adjacently valid chain

A chain of branch steps
$(a_1, b_1, c_1), \dots, (a_r, b_r, c_r)$ is adjacently valid when for every $j$ with
$1 \le j < r$ we have $a_{j+1} + b_{j+1} = a_j$, $1 \le b_{j+1} \le a_{j+1}$ and
$1 \le c_{j+1} \le c_j$. Only consecutive steps are related, and nothing is required of the first
step alone; in particular every chain with at most one step is adjacently valid.

Formalized by `MetaMathlibExt.ChainAdjValid`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#chain-adj-valid).

## Valid branch

Let $q$ be a natural number, $(d_0, m_0), \dots, (d_{k-1}, m_{k-1})$ a list
of blocks and $i$ an index, and let $u_i$ and $N_i$ be the first-split exponent and the basic
multiplicity of block $i$, with $d_i$ read as $0$ when $i \ge k$. A chain of branch steps
$(a_1, b_1, c_1), \dots, (a_r, b_r, c_r)$ is a valid branch for block $i$ when either $r = 0$, or
$r \ge 1$, the first step satisfies $1 \le b_1 \le a_1$, $a_1 + b_1 = d_i$ and
$1 \le c_1 \le q^{u_i} - 1$ (subtraction truncated at $0$), $N_i \ne 1$, and the chain is
adjacently valid.

Formalized by `MetaMathlibExt.BranchValid`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#branch-valid).

## Restricted Gaussian partition

Let $q$ and $n$ be natural numbers and let $G$ be a
Gaussian partition. Then $G$ is a restricted Gaussian partition for $q$ and $n$ when $q$ is a
prime power, $n > 0$, and there exist blocks $(d_1, m_1), \dots, (d_\ell, m_\ell)$ and, for each
block $i$, a chain $C_i$ of branch steps $(a, b, c)$, with the following properties.

The blocks satisfy $d_i \ge 1$ and $m_i \ge 1$ for every $i$, $d_1 > d_2 > \dots > d_\ell$ and
$m_1 d_1 + \dots + m_\ell d_\ell = n$. With $p_i = \sum_{h < i} m_h d_h$, the basic segment of
block $i$ is the list of $\beta_i = \sum_{j=0}^{m_i - 1} q^{p_i + j d_i}$ copies of $d_i$.

Each chain $C_i$ is empty or satisfies the following: its first step $(a, b, c)$ has
$1 \le b \le a$, $a + b = d_i$, $1 \le c \le q^{p_i + (m_i - 1) d_i} - 1$ and $\beta_i \ne 1$,
and each pair of consecutive steps $(a, b, c), (a', b', c')$ has $a' + b' = a$,
$1 \le b' \le a'$ and $1 \le c' \le c$.

A step $(a, b, c)$ acts on a list of dimensions by deleting its last $c$ entries equal to
$a + b$ and putting $c$ copies of $a$ followed by $c q^a$ copies of $b$ where the first deleted
entry was, after the entries before it and before the remaining entries after it; it fails if
the list has fewer than $c$ entries equal to $a + b$. Applying the steps of $C_i$ in order to the
basic segment of block $i$ succeeds for every $i$, with final segment $F_i$.

The concatenation of the basic segments is nonincreasing, the concatenation $F_1 \cdots F_\ell$
is nonincreasing, and for every block $i$ and every $k$ smaller than the length of $C_i$, the
concatenation of $F_1, \dots, F_{i-1}$, the result of applying the first $k + 1$ steps of $C_i$
to the basic segment of block $i$, and the basic segments of blocks $i + 1, \dots, \ell$ is
nonincreasing. Finally, the dimension list of $G$ is $F_1 \cdots F_\ell$.

Formalized by `MetaMathlibExt.IsRestrictedGaussianPartition`, a definition declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#is-restricted-gaussian-partition).

## Basic ancestors are restricted

Let $q$ be a prime power and $n > 0$. Let
$(d_0, m_0), \dots, (d_{k-1}, m_{k-1})$ be blocks with $d_i \ge 1$ and $m_i \ge 1$ for all $i$,
$d_0 > d_1 > \dots > d_{k-1}$ and $m_0 d_0 + \dots + m_{k-1} d_{k-1} = n$. Put
$p_i = \sum_{j < i} m_j d_j$, and let the basic dimension list be the concatenation, for
$i = 0, \dots, k - 1$ in order, of $\sum_{j=0}^{m_i - 1} q^{p_i + j d_i}$ copies of $d_i$. If this
list is nonincreasing, then every Gaussian partition whose dimension list equals it is a
restricted Gaussian partition for $q$ and $n$.

The witness realizes every block with an empty branch.

Formalized by `MetaMathlibExt.basic_ancestor_is_restricted`, a theorem declared in [MathlibExt/Combinatorics/RestrictedGaussianPartition.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/RestrictedGaussianPartition.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html#basic-ancestor-is-restricted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricted Gaussian partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/restricted-gaussian-partitions)
