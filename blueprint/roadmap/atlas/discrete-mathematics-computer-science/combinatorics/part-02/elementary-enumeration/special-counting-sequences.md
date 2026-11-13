---
declaration: section
origin: cited
lean: MetaMathlibExt.LatticePath, MetaMathlibExt.Necklace, MetaMathlibExt.Nat.lucas, MetaMathlibExt.Nat.motzkin, MetaMathlibExt.Nat.delannoy, MetaMathlibExt.SoutheastPath, MetaMathlibExt.SoutheastPath.weight, MetaMathlibExt.IsNonintersectingPathFamily
statement: formalized
proof: formalized
---

# Special counting sequences

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html).

## Lattice paths with prescribed steps

Let $d \in \mathbb{N}$, let $D \subseteq \mathbb{Z}^d$
and let $p, q \in \mathbb{Z}^d$. A lattice path from $p$ to $q$ with step set $D$ is a finite
sequence $(v_0, v_1, \dots, v_m)$ of points of $\mathbb{Z}^d$, for some $m \in \mathbb{N}$, such
that $v_0 = p$, $v_m = q$, and $v_i - v_{i-1} \in D$ for $1 \le i \le m$.

The case $m = 0$ is the path of length zero, which is a lattice path from $p$ to $q$ exactly when
$p = q$.

Formalized by `MetaMathlibExt.LatticePath`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#lattice-path).

## Fixed-length necklaces

Let $A$ be a set and let $n \in \mathbb{N}$. For $n \ge 1$, a word
of length $n$ over $A$ is a tuple $(a_0, a_1, \dots, a_{n-1})$ of elements of $A$, and two words
$(a_0, \dots, a_{n-1})$ and $(b_0, \dots, b_{n-1})$ are rotationally equivalent if there is an
integer $r$ with $0 \le r < n$ such that $b_i = a_{(i+r) \bmod n}$ for $0 \le i < n$. A necklace of
length $n$ over $A$ is an equivalence class of words of length $n$ under rotational equivalence.
For $n = 0$ there is exactly one necklace over $A$, represented by the empty word.

Reflections are not identified.

Formalized by `MetaMathlibExt.Necklace`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#necklace).

## Lucas number sequence

The Lucas numbers $(L_n)_{n \ge 0}$ are the natural numbers
defined by $L_0 = 2$, $L_1 = 1$, and $L_{n+2} = L_{n+1} + L_n$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.Nat.lucas`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#lucas).

## Motzkin number sequence

The Motzkin numbers $(M_n)_{n \ge 0}$ are the natural numbers
defined by $M_0 = 1$ and, for every $n \in \mathbb{N}$,
$M_{n+1} = M_n + \sum_{k=0}^{n-1} M_k M_{n-1-k}$, where the sum is empty when $n = 0$. Thus
$M_0, M_1, M_2, M_3 = 1, 1, 2, 4$.

Formalized by `MetaMathlibExt.Nat.motzkin`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#motzkin).

## Delannoy numbers

The Delannoy numbers $D(m,n)$, for $m, n \in \mathbb{N}$, are defined by
$D(0,n) = 1$ and $D(m,0) = 1$ for all $m, n \in \mathbb{N}$, and
$D(m+1,n+1) = D(m,n+1) + D(m+1,n) + D(m,n)$ for all $m, n \in \mathbb{N}$.

Equivalently, $D(m,n)$ is the number of lattice paths from $(0,0)$ to $(m,n)$ with steps
$(1,0)$, $(0,1)$ and $(1,1)$.

Formalized by `MetaMathlibExt.Nat.delannoy`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#delannoy).

## Southeast paths

A point of the quarter plane is a pair $(a, b) \in \mathbb{N}^2$, with $a$
the horizontal coordinate and $b$ the height. Let $p$ and $q$ be points of the quarter plane. A
southeast path from $p$ to $q$ is a list $v = [v_0, v_1, \dots, v_m]$ of points of the quarter
plane, for some $m \in \mathbb{N}$, with $v_0 = p$, $v_m = q$, and, for each $1 \le t \le m$,
either $v_t = v_{t-1} + (1, 0)$ (an east step) or $v_{t-1} = v_t + (0, 1)$ (a south step).

For $m = 0$ the path is the single point $[p]$, which is a southeast path from $p$ to $q$ exactly
when $p = q$. The empty list is not a southeast path. Writing $p = (a, b)$ and $q = (c, d)$, a
southeast path from $p$ to $q$ exists exactly when $a \le c$ and $d \le b$, and then
$m = (c - a) + (b - d)$.

Formalized by `MetaMathlibExt.SoutheastPath`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#southeast-path).

## Weight of a southeast path

Let $R$ be a commutative monoid, written multiplicatively, let
$x = (x_j)_{j \in \mathbb{N}}$ be a family of elements of $R$, let $p, q \in \mathbb{N}^2$, and let
$v = [v_0, \dots, v_m]$ be a southeast path from $p$ to $q$. For $1 \le t \le m$, the step from
$v_{t-1}$ to $v_t$ has weight $w_t = x_j$ if it is an east step at height $j$, that is,
$v_{t-1} = (a, j)$ and $v_t = (a+1, j)$, and weight $w_t = 1$ if it is a south step. The weight of
$v$ is $\operatorname{wt}(v) = \prod_{t=1}^{m} w_t$.

For $m = 0$ the product is empty, so the one-point path $[p]$ has weight $1$; so does every path
all of whose steps are south steps. The weight depends only on the list $v$.

Formalized by `MetaMathlibExt.SoutheastPath.weight`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#weight).

## Nonintersecting families of southeast paths

Let $n \in \mathbb{N}$ and let
$p_1, \dots, p_n$ and $q_1, \dots, q_n$ be points of $\mathbb{N}^2$. A family
$L = (L_1, \dots, L_n)$, in which $L_i$ is a southeast path from $p_i$ to $q_i$ for each $i$, is
nonintersecting when for all $i \ne j$ no point occurs both in $L_i$ and in $L_j$.

Endpoints count as points of a path, so two paths that meet only at a common endpoint do not
form a nonintersecting family. Distinctness is of indices, not of paths: if $i \ne j$ and
$L_i = L_j$, the family is not nonintersecting. For $n \le 1$ every family is nonintersecting.

Formalized by `MetaMathlibExt.IsNonintersectingPathFamily`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#is-nonintersecting-path-family).

## Weighted sum over nonintersecting path families

Let $R$ be a commutative semiring, let
$x = (x_j)_{j \in \mathbb{N}}$ be a family of elements of $R$, let $n \in \mathbb{N}$, and let
$p = (p_1, \dots, p_n)$ and $q = (q_1, \dots, q_n)$ be tuples of points of $\mathbb{N}^2$. The
nonintersecting path weight sum of type $(p, q)$ is
$W(p, q) = \sum_L \prod_{i=1}^{n} \operatorname{wt}(L_i)$, the sum taken over all nonintersecting
families $L = (L_1, \dots, L_n)$ in which $L_i$ is a southeast path from $p_i$ to $q_i$ for each
$i$, where $\operatorname{wt}(L_i)$ is the weight of $L_i$ with respect to $x$.

There are only finitely many such families. If for some $i$ there is no southeast path from
$p_i$ to $q_i$, then $W(p, q) = 0$. For $n = 0$ the empty family is the only one, and
$W(p, q) = 1$.

Formalized by `MetaMathlibExt.nonintersectingPathWeightSum`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Fundamentals/SpecialSequences.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html#nonintersecting-path-weight-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Special counting sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/elementary-enumeration/special-counting-sequences)
