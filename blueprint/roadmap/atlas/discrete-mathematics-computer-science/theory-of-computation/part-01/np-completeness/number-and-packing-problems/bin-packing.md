---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.BinPacking.BinPackingInstance, MetaMathlibExt.Complexity.NPComplete.BinPacking.BinPackingFeasible, MetaMathlibExt.Complexity.NPComplete.BinPacking.binPackingDec, MetaMathlibExt.Complexity.NPComplete.BinPacking.binPacking_npComplete
statement: formalized
---

# Bin packing

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing/index.html).

## Bin packing instances

An instance of BIN PACKING is a triple $(s, B, K)$ of a finite
list $s$ of natural numbers (the item sizes), a natural number $B$ (the bin capacity) and a
natural number $K$ (the number of bins).

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinPacking.BinPackingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BinPackingWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BinPackingWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing/index.html#bin-packing-instance).

## Feasible bin packing instances

An instance $(s, B, K)$ of BIN PACKING is feasible when
there is a list of exactly $K$ bins, each a finite list of natural numbers with sum at most $B$,
such that the concatenation of the bins is a permutation of $s$.

Since bins may be empty, this says that the items fit into at most $K$ bins of capacity $B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinPacking.BinPackingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BinPackingWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BinPackingWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing/index.html#bin-packing-feasible).

## The bin packing decision problem

BIN PACKING is the decision problem that accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of bin packing
instances, to a feasible instance; it rejects every bitstring that fails to decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinPacking.binPackingDec`, a definition declared in [WantedExt/Complexity/NPComplete/BinPackingWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BinPackingWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing/index.html#bin-packing-dec).

## BIN PACKING is NP-complete

The bin packing decision problem belongs to NP, and every
decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), BIN PACKING; D. S. Johnson, "Fast algorithms for bin packing" (1974).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.BinPacking.binPacking_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BinPackingWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BinPackingWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing/index.html#bin-packing-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bin packing](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/bin-packing)
