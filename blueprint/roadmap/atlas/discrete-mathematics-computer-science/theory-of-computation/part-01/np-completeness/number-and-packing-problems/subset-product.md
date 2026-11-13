---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.SubsetProduct.SubsetProductInstance, MetaMathlibExt.Complexity.NPComplete.SubsetProduct.WellFormed, MetaMathlibExt.Complexity.NPComplete.SubsetProduct.SubsetProductFeasible, MetaMathlibExt.Complexity.NPComplete.SubsetProduct.subsetProductDec, MetaMathlibExt.Complexity.NPComplete.SubsetProduct.subsetProduct_npComplete
statement: formalized
---

# Subset product

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html).

## SUBSET PRODUCT instances

An instance of SUBSET PRODUCT is a pair $(a, T)$ of a finite
list $a$ of natural numbers and a target natural number $T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubsetProduct.SubsetProductInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SubsetProductWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SubsetProductWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html#subset-product-instance).

## Well-formed SUBSET PRODUCT instances

An instance $(a, T)$ of SUBSET PRODUCT, with $a$ a
finite list of natural numbers and $T$ a natural number, is well formed when every entry of $a$
is positive.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubsetProduct.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SubsetProductWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SubsetProductWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html#well-formed).

## Feasible SUBSET PRODUCT instances

An instance $(a, T)$ of SUBSET PRODUCT, with $a$ a
finite list of natural numbers and $T$ a natural number, is feasible when some sublist of $a$ (a
list obtained from $a$ by deleting entries and keeping the order of the rest) has product exactly
$T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubsetProduct.SubsetProductFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SubsetProductWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SubsetProductWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html#subset-product-feasible).

## SUBSET PRODUCT as a decision problem

The decision problem SUBSET PRODUCT accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of pairs of a finite
list of natural numbers and a natural number, to an instance $(a, T)$ that is well formed (every
entry of $a$ is positive) and feasible (some sublist of $a$ has product exactly $T$). It rejects
every bitstring that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubsetProduct.subsetProductDec`, a definition declared in [WantedExt/Complexity/NPComplete/SubsetProductWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SubsetProductWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html#subset-product-dec).

## SUBSET PRODUCT is NP-complete

The decision problem SUBSET PRODUCT lies in NP, and every
decision problem in NP has a polynomial-time many-one reduction to SUBSET PRODUCT.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SUBSET PRODUCT.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.SubsetProduct.subsetProduct_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SubsetProductWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SubsetProductWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html#subset-product-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subset product](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-product)
