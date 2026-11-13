---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.QTree.sqReg, Cslib.Algorithms.Lean.QTree.mem_sqReg, Cslib.Algorithms.Lean.QTree.get, Cslib.Algorithms.Lean.QTree.qt_of_fun, Cslib.Algorithms.Lean.QTree.height_qt_of_fun, Cslib.Algorithms.Lean.QTree.get_qt_of_fun, Cslib.Algorithms.Lean.QTree.fdsa_chap13_ex02
statement: formalized
proof: formalized
---

# Function reconstruction by quadtrees

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html).

## Square region represented by a quadtree

The represented square: both natural coordinates are below `2 ^ n`.

Formalized by `Cslib.Algorithms.Lean.QTree.sqReg`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#sq-reg).

## Membership in the represented square

Membership in the represented square is a pair of strict bounds.

Formalized by `Cslib.Algorithms.Lean.QTree.mem_sqReg`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#mem-sq-reg).

## Polymorphic quadtree lookup

Polymorphic lookup. A leaf is constant; at zero scale a branch follows
its first child at `(0, 0)`. Positive scales select quadrants by the split.

Formalized by `Cslib.Algorithms.Lean.QTree.get`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#get).

## Full quadtree sampled from a function

Samples `f` into a full tree. Every branch splits its coordinate square
into four equal quadrants, without compressing equal leaves.

Formalized by `Cslib.Algorithms.Lean.QTree.qt_of_fun`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#qt-of-fun).

## Height of the quadtree sampled from a function

Reconstruction builds exactly the requested number of branch levels.

Formalized by `Cslib.Algorithms.Lean.QTree.height_qt_of_fun`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#height-qt-of-fun).

## Sampled quadtree recovers the function on the represented square

Reading a sampled function recovers its value within the represented
square.

Formalized by `Cslib.Algorithms.Lean.QTree.get_qt_of_fun`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#get-qt-of-fun).

## Correctness of function reconstruction by quadtrees

The original graded reconstruction theorem, under its original name.

Formalized by `Cslib.Algorithms.Lean.QTree.fdsa_chap13_ex02`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/OfFunction.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html#fdsa-chap13-ex02).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Function reconstruction by quadtrees](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/function-reconstruction-by-quadtrees)
