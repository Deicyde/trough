---
declaration: section
origin: cited
lean: List.Pairwise.idxOf_lt_iff, List.Pairwise.product_lex, List.getD_splitLengths, List.getD_splitLengths_map, List.getD_splitLengths_replicate, List.eq_of_extract_mul_eq, List.length_flatMap_range, List.extract_flatMap_range
statement: formalized
proof: formalized
---

# List operations

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html).

## List positions agree with values of an increasing map

In a list along which `f` increases, position order agrees with value order.

Formalized by `List.Pairwise.idxOf_lt_iff`, a theorem declared in [MathlibExt/Data/List/PairwiseIdxOf.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/PairwiseIdxOf.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#idx-of-lt-iff).

## Pairwise relations on list products in lexicographic order

The Cartesian product of two pairwise-related lists is pairwise-related in lexicographic
order.

Formalized by `List.Pairwise.product_lex`, a theorem declared in [MathlibExt/Data/List/PairwiseProduct.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/PairwiseProduct.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#product-lex).

## Start position of a chunk in a split list

A valid indexed chunk begins after the total length of the preceding chunks.

Formalized by `List.getD_splitLengths`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#get-d-split-lengths).

## Named chunk lookup uses the first occurrence

Looking up a named chunk uses the first occurrence of its name.

Formalized by `List.getD_splitLengths_map`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#get-d-split-lengths-map).

## Splitting a list at a repeated width

Splitting at a repeated width recovers the corresponding uniform chunk.

Formalized by `List.getD_splitLengths_replicate`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#get-d-split-lengths-replicate).

## Equality of uniformly split lists from equal block extracts

Lists of the same uniform-block length are equal when every block extract agrees.

Formalized by `List.eq_of_extract_mul_eq`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#eq-of-extract-mul-eq).

## Length of a concatenation of equal-length lists

Concatenating `count` lists of length `width` has length `count * width`.

Formalized by `List.length_flatMap_range`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#length-flat-map-range).

## Extracting a member from a uniform-width concatenation

A uniform-width extract of a concatenated family recovers that family member.

Formalized by `List.extract_flatMap_range`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#extract-flat-map-range).

## Every equal-length list family is realized by its concatenation

Every finite family of equal-length lists is realized by their concatenation.

Formalized by `List.exists_length_eq_and_extract_eq`, a theorem declared in [MathlibExt/Data/List/SplitLengths.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/SplitLengths.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#exists-length-eq-and-extract-eq).

## Inclusive first-hit prefix of a list

The prefix through the first element satisfying `p`, including that element. If no element
satisfies `p`, this is the whole list.

Formalized by `List.takeThrough`, a definition declared in [MathlibExt/Data/List/TakeThrough.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through).

## Inclusive first-hit prefix of the empty list

The inclusive first-hit prefix of an empty list is empty.

Formalized by `List.takeThrough_nil`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-nil).

## Inclusive first-hit prefix when the head is a hit

If the head satisfies the predicate, it is the whole inclusive first-hit prefix.

Formalized by `List.takeThrough_cons_of_pos`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-cons-of-pos).

## Inclusive first-hit prefix when the head is not a hit

If the head does not satisfy the predicate, the search continues through the tail.

Formalized by `List.takeThrough_cons_of_neg`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-cons-of-neg).

## Inclusive first-hit prefix of a singleton

A singleton is its own inclusive first-hit prefix.

Formalized by `List.takeThrough_singleton`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-singleton).

## Members of an inclusive first-hit prefix lie in the list

Every member of an inclusive first-hit prefix belongs to the source list.

Formalized by `List.mem_of_mem_takeThrough`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#mem-of-mem-take-through).

## Inclusive first-hit prefix of a list with no hit

If no element satisfies the predicate, the inclusive first-hit prefix is the whole list.

Formalized by `List.takeThrough_eq_self_of_any_eq_false`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-eq-self-of-any-eq-false).

## Inclusive first-hit prefix of an append with a hit on the left

Once the left list has a hit, appending another list does not change the prefix.

Formalized by `List.takeThrough_append_of_any_eq_true`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-append-of-any-eq-true).

## Inclusive first-hit prefix of an append with no hit on the left

If the left list has no hit, the prefix contains all of it and continues into the right list.

Formalized by `List.takeThrough_append_of_any_eq_false`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-append-of-any-eq-false).

## Inclusive first-hit prefix has a hit iff the list does

The inclusive first-hit prefix has a hit exactly when the source list has one.

Formalized by `List.any_takeThrough`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#any-take-through).

## Inclusive first-hit prefix of a range of naturals

On `range n`, the prefix ends one past the first hit, or at `n` if there is no hit.

Formalized by `List.takeThrough_range`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-range).

## Inclusive first-hit prefix commutes with filter-map

Filtering selected elements from an inclusive prefix commutes with taking the corresponding
inclusive prefix of the selected elements.

Formalized by `List.filterMap_takeThrough`, a theorem declared in [MathlibExt/Data/List/TakeThrough.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThrough.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#filter-map-take-through).

## Accumulator-stopped inclusive prefix of a list

The prefix through the first element after whose update the accumulator satisfies `stop`,
including that element. The initial accumulator is not tested. If no updated accumulator satisfies
`stop`, this is the whole list.

Formalized by `List.takeThroughAcc`, a definition declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc).

## Accumulator-stopped prefix of the empty list

An empty list has an empty accumulator-stopped prefix.

Formalized by `List.takeThroughAcc_nil`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-nil).

## Accumulator-stopped prefix when the head update stops

If the accumulator stops after the head update, the prefix contains only the head.

Formalized by `List.takeThroughAcc_cons_of_stop`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-cons-of-stop).

## Accumulator-stopped prefix when the head update continues

If the accumulator continues after the head update, the same updated accumulator processes the
tail.

Formalized by `List.takeThroughAcc_cons_of_continue`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-cons-of-continue).

## Accumulator-stopped list is a prefix of its source

The accumulator-stopped list is a prefix of its source list.

Formalized by `List.takeThroughAcc_prefix`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-prefix).

## Members of an accumulator-stopped prefix lie in the list

Every member of an accumulator-stopped prefix belongs to the source list.

Formalized by `List.mem_of_mem_takeThroughAcc`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#mem-of-mem-take-through-acc).

## Disjunction accumulator gives the inclusive first-hit prefix

Accumulating disjunction from `false` gives the ordinary inclusive first-hit prefix.

Formalized by `List.takeThroughAcc_or`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-or).

## First-witness accumulator gives the inclusive first-hit prefix

Accumulating a projection of the first witness in an `Option` gives the ordinary inclusive
first-hit prefix.

Formalized by `List.takeThroughAcc_first`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-first).

## First-witness fold over the inclusive first-hit prefix

Folding the first-witness update over the inclusive tested prefix returns the first witness in
the whole source list.

Formalized by `List.foldl_first_takeThrough`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#foldl-first-take-through).

## Accumulator-stopped prefix as a first-hit prefix of a scan

The recursive ETH operation is the ordinary inclusive first-hit prefix of the elements paired
with their updated accumulators.

Formalized by `List.takeThroughAcc_eq_map_takeThrough_scanl`, a theorem declared in [MathlibExt/Data/List/TakeThroughAcc.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/TakeThroughAcc.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#take-through-acc-eq-map-take-through-sca).

## Chunks of a list have length at most the chunk size

Let $n > 0$ and let $L$ be a list.
Split $L$ from left to right into consecutive chunks of size $n$: elements go into the current
chunk until it holds $n$ elements, then a new chunk is started. Every chunk produced has at most
$n$ elements.

Formalized by `List.length_le_of_mem_toChunks`, a theorem declared in [MathlibExt/Data/List/ToChunks.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/List/ToChunks.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#length-le-of-mem-to-chunks).

## Ordered insertion into a list

For an element $x$ of a linearly ordered type, the ordered
insertion of $x$ into the empty list is $[x]$. For a list with head $a$ and tail $\ell$, it is
$x$ followed by the whole list if $x < a$; it is $a$ followed by the ordered insertion of $x$
into $\ell$ if $a < x$; and it is the list unchanged if $a = x$.

On a strictly increasing list a key that is already present is therefore ignored. On an unsorted
list a later duplicate is not detected: inserting $2$ into $[3, 2]$ gives $[2, 3, 2]$.

Formalized by `Cslib.Algorithms.Lean.orderedInsert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderedInsert.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/OrderedInsert.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#ordered-insert).

## Members after ordered insertion

Over a linearly ordered type, for all elements $x$, $y$
and every list $\ell$, the element $y$ belongs to the ordered insertion of $x$ into $\ell$ if and
only if $y = x$ or $y$ belongs to $\ell$.

Formalized by `Cslib.Algorithms.Lean.mem_orderedInsert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderedInsert.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/OrderedInsert.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#mem-ordered-insert).

## Inserting a present element into a strictly increasing list

Over a linearly ordered
type, if every element of a list $\ell$ is smaller than every later element of $\ell$ and $x$
belongs to $\ell$, then the ordered insertion of $x$ into $\ell$ is $\ell$ itself.

Without strict increase this fails: inserting $2$ into $[3, 2]$ gives $[2, 3, 2]$.

Formalized by `Cslib.Algorithms.Lean.orderedInsert_eq_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderedInsert.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/OrderedInsert.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html#ordered-insert-eq-of-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: List operations](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/list-operations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/linear-structures/list-operations)
