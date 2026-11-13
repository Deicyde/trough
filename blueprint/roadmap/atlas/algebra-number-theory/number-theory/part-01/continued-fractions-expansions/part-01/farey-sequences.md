---
declaration: section
origin: cited
lean: Farey.fareyFinset, Farey.fareySeq, Farey.mem_fareyFinset_iff, Farey.fareyFinset_mono, Farey.IsFareyNeighbor, Farey.mediant, Farey.neighbor_den_sum_gt, Farey.det_one_and_sum_gt_imp_neighbor
statement: formalized
proof: formalized
---

# Farey sequences

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html).

## Farey set

For a natural number $n$, the Farey set $F_n$ of order $n$ is the finite set of
rationals $a/d$ with $a$ and $d$ natural numbers, $1 \le d \le n$ and $0 \le a \le d$.

Equivalently, $F_n$ consists of the rationals $q$ with $0 \le q \le 1$ whose denominator in lowest
terms is at most $n$. In particular $F_0$ is empty.

Formalized by `Farey.fareyFinset`, a definition declared in [MathlibExt/NumberTheory/Farey.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#farey-finset).

## Farey sequence

For a natural number $n$, the Farey sequence of order $n$ is the list of the
elements of the Farey set $F_n$ in increasing order.

Formalized by `Farey.fareySeq`, a definition declared in [MathlibExt/NumberTheory/Farey.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#farey-seq).

## Membership in the Farey set

For a natural number $n$ and a rational number $q$, $q$
belongs to the Farey set $F_n$ of order $n$ if and only if $0 \le q \le 1$ and the denominator of
$q$ in lowest terms is at most $n$.

Formalized by `Farey.mem_fareyFinset_iff`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#mem-farey-finset-iff).

## Farey sets grow with the order

If $m \le n$ are natural numbers, then every element of the
Farey set $F_m$ belongs to $F_n$, that is, $F_m \subseteq F_n$.

Formalized by `Farey.fareyFinset_mono`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#farey-finset-mono).

## Farey neighbors

For a natural number $n$, rationals $x$ and $y$ are Farey neighbors of
order $n$ when both lie in the Farey set $F_n$, $x < y$, and no element $z$ of $F_n$ satisfies
$x < z < y$.

Formalized by `Farey.IsFareyNeighbor`, a definition declared in [MathlibExt/NumberTheory/Farey.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#is-farey-neighbor).

## Mediant

For rational numbers $x = a/b$ and $y = c/d$ written in lowest terms with
$b, d > 0$, the mediant of $x$ and $y$ is the rational number $(a + c)/(b + d)$.

Formalized by `Farey.mediant`, a definition declared in [MathlibExt/NumberTheory/Farey.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#mediant).

## Farey neighbors have denominator sum exceeding the order

Let $n$ be a natural number
and let $F_n$ be the Farey set of order $n$. If $x < y$ are neighbors in $F_n$, meaning that
$x, y \in F_n$ and no element of $F_n$ lies strictly between them, then the denominators $b$ of
$x$ and $d$ of $y$ in lowest terms satisfy $b + d > n$.

Formalized by `Farey.neighbor_den_sum_gt`, a lemma declared in [MathlibExt/NumberTheory/Farey.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#neighbor-den-sum-gt).

## Determinant one and large denominator sum give Farey neighbors

Let $n$ be a natural
number and let $x = a/b$ and $y = c/d$ be elements of the Farey set $F_n$, written in lowest
terms with $b, d > 0$. If $bc = ad + 1$ and $n < b + d$, then $x$ and $y$ are Farey neighbors of
order $n$.

Formalized by `Farey.det_one_and_sum_gt_imp_neighbor`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#det-one-and-sum-gt-imp-neighbor).

## Consecutive Farey fractions have determinant one

Let $n$ be a natural number. If $x$ and
$y$ are Farey neighbors of order $n$, written in lowest terms as $x = a/b$ and $y = c/d$ with
$b, d > 0$, then $bc = ad + 1$.

Formalized by `Farey.IsFareyNeighbor.det_eq_one`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#det-eq-one).

## Arithmetic characterization of Farey neighbors

Let $n$ be a natural number and let
$x = a/b$ and $y = c/d$ be elements of the Farey set $F_n$, written in lowest terms with
$b, d > 0$. Then $x$ and $y$ are Farey neighbors of order $n$ if and only if $bc = ad + 1$ and
$n < b + d$.

Formalized by `Farey.isFareyNeighbor_iff_det_and_sum`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#is-farey-neighbor-iff-det-and-sum).

## The mediant of Farey neighbors is not in the Farey set

Let $n$ be a natural number. If
$x$ and $y$ are Farey neighbors of order $n$, then the mediant of $x$ and $y$ does not belong to
the Farey set $F_n$.

Formalized by `Farey.IsFareyNeighbor.mediant_not_mem`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#mediant-not-mem).

## Mediants that enter the next Farey set

Let $n$ be a natural number and let $x$ and $y$
be Farey neighbors of order $n$ whose denominators in lowest terms sum to $n + 1$. Then the
mediant of $x$ and $y$ belongs to the Farey set $F_{n+1}$ and does not belong to $F_n$.

Formalized by `Farey.IsFareyNeighbor.mediant_mem_succ`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#mediant-mem-succ).

## Mediants generate the next Farey set

Let $n \ge 1$ be a natural number. A rational
number $q$ belongs to the Farey set $F_{n+1}$ if and only if $q$ belongs to $F_n$, or there are
Farey neighbors $x$ and $y$ of order $n$ whose denominators in lowest terms sum to $n + 1$ such
that $q$ is the mediant of $x$ and $y$.

Formalized by `Farey.farey_succ_generation`, a theorem declared in [MathlibExt/NumberTheory/Farey.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Farey.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html#farey-succ-generation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Farey sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-sequences)
