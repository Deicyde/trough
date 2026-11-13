---
declaration: section
origin: cited
lean: Set.IsAPOfLengthWith, Set.IsAPOfLength, Set.IsAPOfLength.card, Set.IsAPOfLength.eq, List.IsAPOfLengthWith, List.IsAPOfLength, HasMonotoneAP, Set.IsAPOfLengthFree
statement: formalized
proof: formalized
---

# Arithmetic progressions and progression-free sets

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html).

## Set arithmetic progressions with given first term and difference

Let $M$ be an
additive commutative monoid, $l \in \mathbb{N} \cup \{\infty\}$ and $a, d \in M$. A set
$s \subseteq M$ is an arithmetic progression of length $l$ with first term $a$ and difference
$d$ if $s = \{a + n d : n \in \mathbb{N},\ n < l\}$ and $s$ has exactly $l$ elements, counting
the size of an infinite set as $\infty$; here $n d$ is the sum of $n$ copies of $d$.

Formalized by `Set.IsAPOfLengthWith`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length-with).

## Sets that are arithmetic progressions

Let $\alpha$ be an additive commutative monoid
and $l \in \mathbb{N} \cup \{\infty\}$. A set $s \subseteq \alpha$ is an arithmetic progression
of length $l$ if there are $a, d \in \alpha$ such that
$s = \{a + nd : n \in \mathbb{N},\ n < l\}$ and $s$ has exactly $l$ elements (infinitely many
when $l = \infty$). Here $nd$ denotes the sum of $n$ copies of $d$.

Formalized by `Set.IsAPOfLength`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length).

## Cardinality of a set arithmetic progression

Let $M$ be an additive commutative monoid
and $l \in \mathbb{N} \cup \{\infty\}$. If a set $s \subseteq M$ is an arithmetic progression of
length $l$, then $s$ has exactly $l$ elements, counting the size of an infinite set as $\infty$.

Formalized by `Set.IsAPOfLength.card`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#card).

## First term and difference of a set arithmetic progression

Let $M$ be an additive
commutative monoid and $l \in \mathbb{N} \cup \{\infty\}$. If a set $s \subseteq M$ is an
arithmetic progression of length $l$, then there are $a, d \in M$ with
$s = \{a + n d : n \in \mathbb{N},\ n < l\}$, where $n d$ is the sum of $n$ copies of $d$.

Formalized by `Set.IsAPOfLength.eq`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#eq).

## List arithmetic progressions with given start and difference

Let $M$ be an additive
commutative monoid, $l \in \mathbb{N}$ and $a, d \in M$. A list $s$ of elements of $M$ is an
arithmetic progression of length $l$ starting from $a$ with difference $d$, in either direction,
if $s = (a, a + d, \dots, a + (l - 1)d)$ or $s = (a + (l - 1)d, \dots, a + d, a)$, where $n d$ is
the sum of $n$ copies of $d$; when $l = 0$ both lists are empty.

Formalized by `List.IsAPOfLengthWith`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length-with-2).

## Arithmetic progressions of lists

Let $M$ be an additive commutative monoid and
$l \in \mathbb{N}$. A list $s$ of elements of $M$ is an arithmetic progression of length $l$ if
there are $a, d \in M$ such that $s = (a, a + d, \dots, a + (l - 1)d)$ or
$s = (a + (l - 1)d, \dots, a + d, a)$, where $n d$ is the sum of $n$ copies of $d$.

Formalized by `List.IsAPOfLength`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length-2).

## Monotone arithmetic progressions in a function

Let $M$ be an additive commutative
monoid, $\beta$ a preordered type, $f : \beta \to M$ and $k \in \mathbb{N}$. Then $f$ contains a
monotone arithmetic progression of length $k$ if there are $x_1 < x_2 < \dots < x_k$ in $\beta$
such that the list $(f(x_1), \dots, f(x_k))$ is an arithmetic progression of length $k$: for
some $a, d \in M$ it equals $(a, a + d, \dots, a + (k - 1)d)$ or its reverse.

Formalized by `HasMonotoneAP`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#has-monotone-ap).

## Progression-free sets

Let $M$ be an additive commutative monoid and
$l \in \mathbb{N} \cup \{\infty\}$. A set $s \subseteq M$ is free of nontrivial arithmetic
progressions of length $l$ if every subset of $s$ that is an arithmetic progression of length $l$
forces $l \le 1$; equivalently, $l \le 1$ or no subset of $s$ is an arithmetic progression of
length $l$.

Formalized by `Set.IsAPOfLengthFree`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length-free).

## A progression of length greater than one is not progression-free

Let $s$ be a set in an
additive commutative monoid and $l \in \mathbb{N} \cup \{\infty\}$ with $l > 1$. If $s$ is an
arithmetic progression of length $l$, then $s$ is not free of nontrivial arithmetic progressions
of length $l$.

Formalized by `Set.IsAPOfLength.not_isAPOfLengthFree`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#not-is-apof-length-free).

## Progression-free finite sets

Let $M$ be an additive commutative monoid and
$l \in \mathbb{N} \cup \{\infty\}$. A finite set $s \subseteq M$ is free of nontrivial arithmetic
progressions of length $l$ if it is so as a set: $l \le 1$, or no subset of $s$ is an
arithmetic progression of length $l$.

Formalized by `Finset.IsAPOfLengthFree`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length-free-2).

## Sets of naturals without three-term progressions

Let $s$ be a set of natural numbers
such that $a = b$ whenever $a, b, c \in s$ satisfy $a + c = 2b$. Then $s$ is free of nontrivial
arithmetic progressions of length $3$: no subset of $s$ is an arithmetic progression of
length $3$.

Formalized by `ThreeAPFree.isAPOfLengthFree_three`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#is-apof-length-free-three).

## Largest size of a progression-free subset of $\{1, \dots, N\}$

For natural numbers
$k$ and $N$, $r_k(N)$ is the largest cardinality of a subset $S \subseteq \{1, \dots, N\}$ that
is free of nontrivial arithmetic progressions of length $k$, meaning that if $k \ge 2$ then no
subset of $S$ is an arithmetic progression of length $k$ (for $k \le 1$ every subset
qualifies).

Formalized by `Set.IsAPOfLengthFree.maxCard`, a definition declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#max-card).

## Trivial upper bound for the largest progression-free subset

For all natural numbers $k$
and $N$, the largest size $r_k(N)$ of a subset of $\{1, \dots, N\}$ free of nontrivial
arithmetic progressions of length $k$ satisfies $r_k(N) \le N$.

Formalized by `Set.IsAPOfLengthFree.maxCard_le`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#max-card-le).

## A largest progression-free subset is attained

For all natural numbers $k$ and $N$, let
$r_k(N)$ be the largest size of a subset of $\{1, \dots, N\}$ free of nontrivial arithmetic
progressions of length $k$. Then some subset $S \subseteq \{1, \dots, N\}$ free of nontrivial
arithmetic progressions of length $k$ has exactly $r_k(N)$ elements.

Formalized by `Set.IsAPOfLengthFree.maxCard_spec`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#max-card-spec).

## Progression-free subsets are bounded by the extremal size

Let $k$ and $N$ be natural
numbers, and let $S$ be a finite set of natural numbers with $S \subseteq \{1, \dots, N\}$ that
is free of nontrivial arithmetic progressions of length $k$. Then $|S| \le r_k(N)$, where
$r_k(N)$ is the largest size of a subset of $\{1, \dots, N\}$ containing no nontrivial $k$-term
arithmetic progression.

Formalized by `Set.IsAPOfLengthFree.card_le_maxCard`, a theorem declared in [MathlibExt/Combinatorics/AP/Basic.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AP/Basic.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html#card-le-max-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic progressions and progression-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/arithmetic-progressions-and-progression-free-set)
