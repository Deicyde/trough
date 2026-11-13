---
declaration: section
origin: cited
lean: MetaMathlibExt.sumsetTrivialElements, MetaMathlibExt.sumsetTrivialElements_zero, MetaMathlibExt.sumsetTrivialElements_one, MetaMathlibExt.adjacent_sum_mem_sumsetTrivialElements, MetaMathlibExt.mem_sumsetTrivialElements_iff, MetaMathlibExt.nsmul_sumset_erase_max_nontrivial, MetaMathlibExt.nontrivial_sumset_card_of_last_gap_ne_nsmul, MetaMathlibExt.nontrivial_sumset_card_of_last_gap_eq_nsmul
statement: formalized
---

# Possible sizes of h-fold sumsets

13 results, 5 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html).

## Trivial elements of an $h$-fold sumset

Let $G$ be an additive commutative monoid, let
$h, k \in \mathbb{N}$ and let $a \colon \mathbb{N} \to G$ list the set
$A = \{a_0, a_1, \dots, a_{k-1}\}$; write $n x$ for the $n$-fold sum $x + \dots + x$. The
trivial elements of the $h$-fold sumset $hA$ form the finite set that is empty when $k = 0$ and
otherwise consists of $h a_0$ together with the sums $(h - i) a_j + i a_{j+1}$ for all natural
numbers $i \le h$ and $j$ with $j + 1 < k$. An element of $hA$ that is not trivial is called
nontrivial.

These are the sums obtained by moving one summand at a time from each element to the next.
When $k \ge 1$ and $a_0 < a_1 < \dots < a_{k-1}$ in a linearly ordered additive group (the
paper's setting) they form an increasing list of $hk - h + 1$ distinct sums; for an arbitrary
$a$ they may coincide (for example $a = 0$ and $h = k = 2$ give a single element). The sum
$h a_0$ is listed separately so that for $k = 1$ the single sum $h a_0$ is trivial, as in the
paper's list.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, definition of trivial and nontrivial elements (arXiv:2505.07679v2, Definition 1.8).

Formalized by `MetaMathlibExt.sumsetTrivialElements`, a definition declared in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#sumset-trivial-elements).

## No trivial elements for $k = 0$

Let $G$ be an additive commutative monoid, $h$ a natural
number and $a \colon \mathbb{N} \to G$. For $k = 0$, when $\{a_0, \dots, a_{k-1}\}$ is the empty
set, the set of trivial elements of its $h$-fold sumset is empty.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, definition of trivial elements (arXiv:2505.07679v2, Definition 1.8).

Formalized by `MetaMathlibExt.sumsetTrivialElements_zero`, a theorem declared in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#sumset-trivial-elements-zero).

## Trivial elements of a one-element set

Let $G$ be an additive commutative monoid, $h$ a
natural number and $a \colon \mathbb{N} \to G$. For $k = 1$, when $\{a_0, \dots, a_{k-1}\}$ is
the one-element set $\{a_0\}$, the set of trivial elements of its $h$-fold sumset is exactly
$\{h a_0\}$, where $h a_0 = a_0 + \dots + a_0$ is the $h$-fold sum of $a_0$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, definition of trivial elements (arXiv:2505.07679v2, Definition 1.8).

Formalized by `MetaMathlibExt.sumsetTrivialElements_one`, a theorem declared in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#sumset-trivial-elements-one).

## Adjacent sums are trivial elements

Let $G$ be an additive commutative monoid,
$a_0, a_1, \ldots$ a sequence in $G$, and $h, k, i, j$ natural numbers with $j + 1 < k$ and
$i \le h$. Then $(h - i)a_j + i a_{j+1}$ is a trivial element of the $h$-fold sumset of
$a_0, \ldots, a_{k-1}$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, definition of trivial elements (arXiv:2505.07679v2, Definition 1.8).

Formalized by `MetaMathlibExt.adjacent_sum_mem_sumsetTrivialElements`, a theorem declared in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#adjacent-sum-mem-sumset-trivial-elements).

## Characterization of the trivial elements

Let $G$ be an additive commutative monoid,
$a_0, a_1, \ldots$ a sequence in $G$, and $h, k$ natural numbers. An element $x \in G$ is a
trivial element of the $h$-fold sumset of $a_0, \ldots, a_{k-1}$ if and only if either $k > 0$
and $x = h a_0$, or $x = (h - i)a_j + i a_{j+1}$ for some natural numbers $j$ and $i$ with
$j + 1 < k$ and $i \le h$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, definition of trivial elements (arXiv:2505.07679v2, Definition 1.8).

Formalized by `MetaMathlibExt.mem_sumsetTrivialElements_iff`, a theorem declared in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#mem-sumset-trivial-elements-iff).

## Dropping the largest element keeps nontrivial sums nontrivial

Let $G$ be a linearly
ordered additive commutative group, let $h$ and $k > 1$ be natural numbers, and let
$a_0, a_1, \ldots$ be a sequence in $G$ with $a_0 < a_1 < \cdots < a_{k-1}$. Put
$A = \{a_0, \ldots, a_{k-1}\}$ and $B = \{a_0, \ldots, a_{k-2}\}$, and write $hX$ for the
$h$-fold sumset of a set $X$, the set of sums of $h$ elements of $X$. Then $hB \subseteq hA$,
and every element of $hB$ that is not a trivial element of the $h$-fold sumset of
$a_0, \ldots, a_{k-2}$ is not a trivial element of the $h$-fold sumset of $a_0, \ldots, a_{k-1}$.

The paper takes $h > 1$; the statement holds for every $h$ (for $h = 0$ there are no
nontrivial elements).

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Lemma 1 (arXiv:2505.07679v2, Lemma 3.2).

Stated but not proved: `MetaMathlibExt.nsmul_sumset_erase_max_nontrivial` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#nsmul-sumset-erase-max-nontrivial).

## Many nontrivial sums when the last gap is not a multiple of the previous one

Let $G$ be
a linearly ordered additive commutative group, let $h$ and $k \ge 4$ be natural numbers, and let
$a_0, a_1, \ldots$ be a sequence in $G$ with $0 = a_0 < a_1 < \cdots < a_{k-3}$. Suppose that
$a_{k-2} = a_{k-3} + b$ and $a_{k-1} = a_{k-3} + b + c$, where $b, c \in G$ satisfy $b > 0$,
$c > 0$ and $c \ne db$ for every integer $d \ge 1$. Then at least $h - 1$ elements of the
$h$-fold sumset $h\{a_0, \ldots, a_{k-1}\}$ (the set of sums of $h$ elements of
$\{a_0, \ldots, a_{k-1}\}$) are not trivial elements of the $h$-fold sumset of
$a_0, \ldots, a_{k-1}$.

The paper takes $h > 1$; the bound is vacuous for $h \le 1$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Theorem 1 (arXiv:2505.07679v2, Theorem 3.3).

Stated but not proved: `MetaMathlibExt.nontrivial_sumset_card_of_last_gap_ne_nsmul` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#nontrivial-sumset-card-of-last-gap-ne-ns).

## Many nontrivial sums when the last gap is a proper multiple of the previous one

Let $G$
be a linearly ordered additive commutative group, let $h$ and $k \ge 4$ be natural numbers, and
let $a_0, a_1, \ldots$ be a sequence in $G$ with $0 = a_0 < a_1 < \cdots < a_{k-3}$. Suppose
that $a_{k-2} = a_{k-3} + b$ and $a_{k-1} = a_{k-3} + b + db$, where $b \in G$ satisfies
$b > 0$ and $d > 1$ is an integer. Then at least $h - 1$ elements of the $h$-fold sumset
$h\{a_0, \ldots, a_{k-1}\}$ (the set of sums of $h$ elements of $\{a_0, \ldots, a_{k-1}\}$)
are not trivial elements of the $h$-fold sumset of $a_0, \ldots, a_{k-1}$.

The paper's last gap $c$ is written as $db$ (its positivity follows). The paper takes $h > 1$;
the bound is vacuous for $h \le 1$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Theorem 2 (arXiv:2505.07679v2, Theorem 3.4).

Stated but not proved: `MetaMathlibExt.nontrivial_sumset_card_of_last_gap_eq_nsmul` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#nontrivial-sumset-card-of-last-gap-eq-ns).

## Equal last two gaps: an arithmetic progression or many nontrivial sums

Let $G$ be a
linearly ordered additive commutative group, let $h$ and $k \ge 4$ be natural numbers, and let
$a_0, a_1, \ldots$ be a sequence in $G$ with $0 = a_0 < a_1 < \cdots < a_{k-1}$ and
$a_{k-1} - a_{k-2} = a_{k-2} - a_{k-3}$. Then either $a_i = i a_1$ for every $i < k$, or at
least $h - 1$ elements of the $h$-fold sumset $hB$ of $B = \{a_0, \ldots, a_{k-2}\}$ (the set
of sums of $h$ elements of $B$) are not trivial elements of the $h$-fold sumset of
$a_0, \ldots, a_{k-2}$.

The gap hypothesis is the paper's $b_{k-2} = b_{k-3}$, where $b_j = a_{j+1} - a_j$ for
$j \ge 1$. The paper takes $h > 1$; the second alternative is vacuous for $h \le 1$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Theorem 3 (arXiv:2505.07679v2, Theorem 3.5).

Stated but not proved: `MetaMathlibExt.arithProg_or_nontrivial_sumset_card_of_last_gaps_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#arith-prog-or-nontrivial-sumset-card-of).

## A gap in the possible sumset sizes

Let $G$ be a torsion-free additive commutative
group and let $h$ and $k \ge 4$ be natural numbers. For every $k$-element set $A \subseteq G$,
the $h$-fold sumset $hA$ (the set of sums of $h$ elements of $A$) does not satisfy
$hk - h + 2 \le |hA| \le hk - 1$.

Equivalently, writing $R_G(h, k)$ for the set of sizes $|hA|$ of $k$-element sets
$A \subseteq G$, $R_G(h, k) \cap [hk - h + 2, hk - 1] = \emptyset$. The interval is empty for
$h \le 1$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Theorem 4 (arXiv:2505.07679v2, Theorem 3.6).

Stated but not proved: `MetaMathlibExt.card_nsmul_notMem_Icc_of_isAddTorsionFree` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#card-nsmul-not-mem-icc-of-is-add-torsion).

## Sumset sizes between $hk - h + 1$ and $hk$

Let $G$ be a nontrivial torsion-free
additive commutative group and let $h \ge 1$ and $k \ge 4$ be natural numbers. For a finite
set $A \subseteq G$ write $hA$ for its $h$-fold sumset, the set of sums of $h$ elements of $A$,
and write $R_G(h, k)$ for the set of sizes $|hA|$ of $k$-element sets $A \subseteq G$. Then
$R_G(h, k) \cap [hk - h + 1, hk] = \{hk - h + 1, hk\}$.

The hypotheses that $G$ is nontrivial (otherwise there is no $k$-element set and
$R_G(h, k)$ is empty) and that $h \ge 1$ (for $h = 0$ the interval $[1, 0]$ is empty while
the right side is $\{1, 0\}$) are added. The arXiv version states only $hk \in R_G(h, k)$
(Corollary 3.8); the rest combines Theorem 4 with the arithmetic-progression size
$hk - h + 1$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Corollary 1.

Stated but not proved: `MetaMathlibExt.sumsetSizes_inter_Icc_of_isAddTorsionFree` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#sumset-sizes-inter-icc-of-is-add-torsion).

## Sumset of an arithmetic progression with its second-to-last term removed

Let $G$ be a
linearly ordered additive commutative group, let $a \in G$ with $a > 0$, and let $k \ge 3$ and
$h \ge 1$ be natural numbers. The set $A = \{0, a, 2a, \ldots, (k - 2)a, ka\}$, obtained from
$\{0, a, 2a, \ldots, ka\}$ by removing $(k - 1)a$, has $|hA| = hk$, where $hA$ is the $h$-fold
sumset of $A$, the set of sums of $h$ elements of $A$.

The paper leaves $h$ unquantified; $h \ge 1$ is needed, since $|0A| = 1$.

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Theorem 5.

Stated but not proved: `MetaMathlibExt.card_nsmul_arithProg_skip_penultimate` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#card-nsmul-arith-prog-skip-penultimate).

## Rajagopal's family of missing sumset sizes

Let $G$ be a torsion-free additive
commutative group and let $h$, $k$ and $\ell$ be natural numbers with $\ell + 3 \le \min(h, k)$.
For every $k$-element set $A \subseteq G$, the $h$-fold sumset $hA$ (the set of sums of $h$
elements of $A$) does not satisfy
$hk - h + 2 + \ell h \le |hA| \le hk - h + 1 + \ell h + (h - 2 - \ell)$.

Equivalently, writing $R_G(h, k)$ for the set of sizes $|hA|$ of $k$-element sets
$A \subseteq G$, $R_G(h, k)$ misses the interval
$[hk - h + 2 + \ell h, hk - h + 1 + \ell h + (h - 2 - \ell)]$ for each
$0 \le \ell \le \min(h, k) - 3$, stated here one $\ell$ at a time. The journal statement does
not name the group; torsion-freeness is the setting of Theorem 4 and Corollary 1, which this
generalizes ($\ell = 0$ is Theorem 4, here also for $k = 3$).

## Sources

- Vincent Schinina, *On the Sumset of Sets of Size k*, INTEGERS 26 (2026), Article A31, Theorem 6 (journal version; credited to Rajagopal, Theorem 1.3).

Stated but not proved: `MetaMathlibExt.card_nsmul_notMem_Icc_add_mul_of_isAddTorsionFree` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetSetsOfSizeKWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html#card-nsmul-not-mem-icc-add-mul-of-is-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Possible sizes of h-fold sumsets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/possible-sizes-of-h-fold-sumsets)
