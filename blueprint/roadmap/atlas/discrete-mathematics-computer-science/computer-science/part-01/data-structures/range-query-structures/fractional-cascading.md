---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.FractionalCascading.sampleAux, Cslib.Algorithms.Lean.FractionalCascading.sample, Cslib.Algorithms.Lean.FractionalCascading.sampleAux_sublist, Cslib.Algorithms.Lean.FractionalCascading.sample_sublist, Cslib.Algorithms.Lean.FractionalCascading.mem_of_mem_sample, Cslib.Algorithms.Lean.FractionalCascading.two_mul_length_sample_le, Cslib.Algorithms.Lean.FractionalCascading.length_sample_le, Cslib.Algorithms.Lean.FractionalCascading.length_sample_le_length
statement: formalized
proof: formalized
---

# Fractional cascading

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html).

## Alternating selection with a flag

For a flag $b$ (true or false) and a list $\ell$, the
alternating selection of $\ell$ with initial flag $b$ is defined by recursion on $\ell$: the empty
list gives the empty list; for a list with head $a$ and tail $\ell'$, if $b$ is true it keeps $a$
and continues on $\ell'$ with flag false, and if $b$ is false it drops $a$ and continues on
$\ell'$ with flag true.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.sampleAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#sample-aux).

## Sample of a catalog

The sample of a list $[x_0, x_1, x_2, \dots]$ is the list
$[x_0, x_2, x_4, \dots]$ of every other element, starting with the first, in their original
order.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.sample`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#sample).

## Alternating selection gives a sublist

For every flag $b$ (true or false) and every list
$\ell$, the alternating selection of $\ell$ with initial flag $b$ is a sublist of $\ell$: it is
obtained from $\ell$ by deleting some elements and keeping the rest in order.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.sampleAux_sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#sample-aux-sublist).

## The sample is a sublist

For every list $\ell$, the sample of $\ell$ is a sublist of
$\ell$: it is obtained from $\ell$ by deleting some elements and keeping the rest in order.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.sample_sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#sample-sublist).

## Entries of a sample are entries of the catalog

For a catalog (finite list) $L$, every
entry of the sample of $L$ (every other entry of $L$, starting with the first) is an entry of
$L$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.mem_of_mem_sample`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#mem-of-mem-sample).

## Doubled sample length bound

For every catalog $L$, twice the length of the sample of $L$
is at most the length of $L$ plus one.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.two_mul_length_sample_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#two-mul-length-sample-le).

## The sample has at most half the length, rounded up

For every list $xs$ (over any
type), the sample of $xs$ has length at most $\lfloor (|xs| + 1)/2 \rfloor$, half the length of
$xs$ rounded up: for an even length $2m$ the bound is $m$, and for an odd length $2m + 1$ it is
$m + 1$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_sample_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-sample-le).

## The sample is no longer than the list

For every list $xs$ (over any type), the sample
of $xs$, every other element starting with the first, has length at most the length of $xs$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_sample_le_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-sample-le-length).

## The sample of a sorted list is sorted

If a list over a linear order is sorted in
nondecreasing order, then so is its sample.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.pairwise_sample`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#pairwise-sample).

## Sorted merge of two catalogs

For lists $\ell_1$ and $\ell_2$ over a linearly ordered
type, their sorted merge is the result of merge sort, with respect to $\le$, applied to the
concatenation of $\ell_1$ followed by $\ell_2$.

This models the merge of two sorted catalogs; the linear-time merge itself is not part of this statement.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.sortedMerge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#sorted-merge).

## A sorted merge rearranges the concatenation

For any lists $\ell_1$ and $\ell_2$ over a
linear order, the sorted merge of $\ell_1$ and $\ell_2$ is a permutation of the concatenation of
$\ell_1$ followed by $\ell_2$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.perm_sortedMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#perm-sorted-merge).

## Length of a sorted merge

For catalogs (finite lists) $L$ and $M$ over a linearly ordered
type, the sorted merge of $L$ and $M$ has length equal to the length of $L$ plus the length of
$M$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_sortedMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-sorted-merge).

## A sorted merge is sorted

For any lists $\ell_1$ and $\ell_2$ over a linear order, sorted
or not, their sorted merge is sorted in nondecreasing order.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.pairwise_sortedMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#pairwise-sorted-merge).

## Elements of a sorted merge

For lists $\ell_1$ and $\ell_2$ over a linear order and any
element $v$, $v$ belongs to the sorted merge of $\ell_1$ and $\ell_2$ if and only if $v$ belongs
to $\ell_1$ or to $\ell_2$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.mem_sortedMerge_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#mem-sorted-merge-iff).

## Lower bound of a value in a catalog

For a value $x$ of a linearly ordered type and a catalog
(finite list) $L$, the lower bound of $x$ in $L$ is the number of entries of $L$ that are less
than $x$, counted with multiplicity. For a sorted catalog this is the first index whose entry is
not less than $x$, or the length of $L$ if there is none.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.lowerBound`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#lower-bound).

## Lower bound is at most the catalog length

For a value $x$ and a catalog $L$ over a
linearly ordered type, the lower bound of $x$ in $L$ (the number of entries of $L$ less than $x$)
is at most the length of $L$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.lowerBound_le_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#lower-bound-le-length).

## Lower bound in a sorted merge splits

For a value $x$ and catalogs $L$ and $M$ over a
linearly ordered type, the lower bound of $x$ in the sorted merge of $L$ and $M$ equals the lower
bound of $x$ in $L$ plus the lower bound of $x$ in $M$, where the lower bound of $x$ in a catalog
is the number of its entries less than $x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.lowerBound_sortedMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#lower-bound-sorted-merge).

## Lower bound in a sample is at most the lower bound in the catalog

For a value $x$ and a
catalog $L$ over a linearly ordered type, the number of entries less than $x$ in the sample of
$L$ (every other entry of $L$, starting with the first) is at most the number of entries of $L$
less than $x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.lowerBound_sample_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#lower-bound-sample-le).

## Scan count of smaller elements

For a value $x$ and a catalog $L$, the scan count of $x$ in
$L$ is the number of elements of $L$ that are $< x$, computed by a direct scan: it is $0$ for
the empty catalog, and for a catalog with head $a$ and tail $L'$ it is the scan count of $x$ in
$L'$, plus $1$ if $a < x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.countLT`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#count-lt).

## The scan count equals the lower bound

For every value $x$ and every catalog $L$, the scan
count of elements of $L$ that are $< x$ equals the lower bound of $x$ in $L$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.countLT_eq_lowerBound`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#count-lt-eq-lower-bound).

## Augmenting a catalog by the next one

For catalogs $c$ and $a$, the augmentation of $c$
by $a$ is the sorted merge of $c$ with the sample of $a$ (every other element of $a$, starting
with the first). In fractional cascading, $a$ is the next augmented catalog.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.augmentOne`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#augment-one).

## One augmentation step yields a sorted list

For any lists $c$ and $a$ over a linear order,
sorted or not, the augmented catalog obtained by merging $c$ with the sample of $a$ is sorted in
nondecreasing order.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.pairwise_augmentOne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#pairwise-augment-one).

## Length of one augmented catalog

For lists $c$ and $a$ over a linearly ordered type, the
augmented catalog obtained by merging $c$ with the sample $s(a)$ of $a$ has length
$|c| + |s(a)|$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_augmentOne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-augment-one).

## Length bound for one augmented catalog

For lists $c$ and $a$ over a linearly ordered
type, the augmented catalog obtained by merging $c$ with the sample of $a$ has length at most
$|c| + \lfloor (|a| + 1)/2 \rfloor$, the length of $c$ plus half the length of $a$ rounded up.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_augmentOne_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-augment-one-le).

## Membership in an augmented catalog

For catalogs $c$ and $a$ over a linearly ordered type,
a value $v$ is an entry of the augmented catalog of $c$ with $a$ (the sorted merge of $c$ with the
sample of $a$) if and only if $v$ is an entry of $c$ or an entry of the sample of $a$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.mem_augmentOne_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#mem-augment-one-iff).

## Entries of an augmented catalog come from the two catalogs

For catalogs $c$ and $a$ over
a linearly ordered type, every entry $v$ of the augmented catalog of $c$ with $a$ (the sorted
merge of $c$ with the sample of $a$) is an entry of $c$ or an entry of $a$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.mem_augmentOne_imp`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#mem-augment-one-imp).

## Lower bound in an augmented catalog splits

For a value $x$ and catalogs $c$ and $a$ over a
linearly ordered type, the lower bound of $x$ in the augmented catalog of $c$ with $a$ (the sorted
merge of $c$ with the sample of $a$) equals the lower bound of $x$ in $c$ plus the lower bound of
$x$ in the sample of $a$, where the lower bound of $x$ in a catalog is the number of its entries
less than $x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.lowerBound_augmentOne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#lower-bound-augment-one).

## Lower bound in an augmented catalog is at most the sum

For a value $x$ and catalogs $c$
and $a$ over a linearly ordered type, the lower bound of $x$ in the augmented catalog of $c$ with
$a$ (the sorted merge of $c$ with the sample of $a$) is at most the lower bound of $x$ in $c$
plus the lower bound of $x$ in $a$, where the lower bound of $x$ in a catalog is the number of
its entries less than $x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.lowerBound_augmentOne_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#lower-bound-augment-one-le).

## Augmenting a catalog by the head of a list

Given a catalog $c$ and a list $L$ of
catalogs, the result is $c$ itself if $L$ is empty, and otherwise the sorted merge of $c$
with the sample (every other element, starting with the first) of the first catalog of $L$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.augmentHead`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#augment-head).

## Augmented catalogs

For a list of catalogs $c_1, \dots, c_k$, the augmented catalogs
$A_1, \dots, A_k$ are built from the last one backwards: $A_k = c_k$, and for $i < k$, $A_i$ is
the sorted merge of $c_i$ with the sample (every other element, starting with the first) of
$A_{i+1}$. The empty list of catalogs has no augmented catalogs.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.augmented`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#augmented).

## Number of augmented catalogs

For every list $cs$ of catalogs over a linearly ordered
type, the list of augmented catalogs built from $cs$ has the same length as $cs$: there is one
augmented catalog per catalog.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_augmented`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-augmented).

## Augmenting a single catalog

For every catalog $c$, the list of augmented catalogs of the
one-element list $[c]$ is $[c]$: the only augmented catalog is $c$ itself.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.augmented_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#augmented-singleton).

## The augmented catalogs of sorted catalogs are sorted

If every catalog in a list of
catalogs over a linear order is sorted in nondecreasing order, then every augmented catalog built
from that list is sorted in nondecreasing order.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.pairwise_augmented`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#pairwise-augmented).

## Augmented catalogs are bounded by the total input size

For every list
$cs = [c_1, \dots, c_k]$ of catalogs over a linearly ordered type, every augmented catalog built
from $cs$ has length at most $|c_1| + \dots + |c_k|$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_mem_augmented_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-mem-augmented-le).

## Bridge pointer

For a catalog $L$ and a value $v$, the bridge pointer of $v$ into $L$ is
the number of elements of $L$ that are $\le v$.

When $L$ is sorted, this is the index just past the elements of $L$ that are $\le v$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.bridgePtr`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#bridge-ptr).

## Bridge pointers are at most the catalog length

For every catalog $L$ and value $v$, the
bridge pointer of $v$ into $L$ is at most the length of $L$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.bridgePtr_le_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#bridge-ptr-le-length).

## Bridge pointer list

For catalogs $C$ and $L$, the bridge pointers of $C$ into $L$ form the
list obtained by replacing each entry $v$ of $C$, in order, by the bridge pointer of $v$ into
$L$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.bridges`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#bridges).

## Number of bridge pointers

For lists $c$ and $d$ over a linearly ordered type, the list
of bridge pointers of $c$ into $d$ has the same length as $c$: there is one bridge pointer per
entry of $c$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_bridges`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-bridges).

## Bridge pointers are at most the next catalog's length

For lists $c$ and $d$ over a
linearly ordered type, every entry $p$ of the list of bridge pointers of $c$ into $d$ satisfies
$p \le |d|$, where $|d|$ is the length of $d$; so every recorded bridge pointer is a boundary
index of $d$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.le_length_of_mem_bridges`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#le-length-of-mem-bridges).

## Searching every catalog

For a value $x$ and a list of catalogs, the search returns, for
each catalog in order, the number of its elements that are $< x$, computed by a direct scan of
that catalog. This is the lower-bound position of $x$ in each catalog.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAll`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-all).

## Searching no catalogs

Searching the empty list of catalogs for any value $x$ gives the
empty list of positions.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAll_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-all-nil).

## Searching a nonempty list of catalogs

For a value $x$, a catalog $c$ and a list of
catalogs $cs$, searching $c$ followed by $cs$ for $x$ gives first the direct-scan count of the
elements of $c$ that are $< x$, followed by the positions obtained by searching $cs$ for $x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAll_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-all-cons).

## One search position per catalog

For every value $x$ and every list $cs$ of catalogs
over a linearly ordered type, searching each catalog of $cs$ for $x$ gives a list of positions
of the same length as $cs$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_searchAll`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-search-all).

## Correctness of searching every catalog

For a value $x$ and a list of catalogs
$c_1, \dots, c_k$, searching every catalog for $x$ returns the list whose $i$-th entry is the
lower bound of $x$ in $c_i$, that is, the number of elements of $c_i$ that are $< x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAll_eq_map_lowerBound`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-all-eq-map-lower-bound).

## Search positions are lower bounds, index by index

For every value $x$, list of catalogs
$C_0, \dots, C_{k-1}$ and index $i$: if $i < k$, the $i$-th position returned by searching all
catalogs for $x$ is the lower bound of $x$ in $C_i$; if $i \ge k$, the search result has no
$i$-th entry.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.getElem?_searchAll`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#get-elem-search-all).

## Search positions are boundary indices

Let $x$ be a value and let $cs$ be a list of
catalogs whose entry at index $i$ is the catalog $c$. Then searching every catalog of $cs$ for
$x$ gives, at index $i$, the lower bound of $x$ in $c$ (the number of elements of $c$ that are
$< x$), and this lower bound is at most the length of $c$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAll_le_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-all-le-of-mem).

## Searching every augmented catalog

For a value $x$ and a list of catalogs, the augmented
search builds the augmented catalogs and returns, for each augmented catalog in order, the number
of its elements that are $< x$, computed by a direct scan of that catalog.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAugmented`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-augmented).

## One augmented search position per catalog

For every value $x$ and every list $cs$ of
catalogs over a linearly ordered type, searching each augmented catalog built from $cs$ for $x$
gives a list of positions of the same length as $cs$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.length_searchAugmented`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#length-search-augmented).

## Correctness of augmented search

For a value $x$ and a list of catalogs $cs$, searching
every augmented catalog of $cs$ for $x$ returns, for each augmented catalog in order, the lower
bound of $x$ in it, that is, the number of its elements that are $< x$.

Formalized by `Cslib.Algorithms.Lean.FractionalCascading.searchAugmented_eq_map_lowerBound`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FractionalCascading.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html#search-augmented-eq-map-lower-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fractional cascading](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/fractional-cascading)
