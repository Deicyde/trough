---
declaration: section
origin: cited
lean: OAI.StrongThinTree.strongThinTree, OAI.AlgorithmicThinTrees.algorithmic_strong_thin_trees
statement: formalized
proof: formalized
---

# 174. Deterministic construction of strong thin spanning trees

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the strong thin-tree conjecture constructively. Every finite loopless *k*-edge-connected multigraph on at least two vertices has a spanning tree containing at most a universal $C/k$ fraction of the edges of every cut. Such a tree can be found deterministically in polynomial time, even with binary-encoded parallel-edge multiplicities.

## The strong thin tree conjecture

We prove that every finite loopless *k*-edge-connected multigraph on at least two vertices, with *k* ≥ 1, has a spanning tree meeting each cut in at most $C/k$ times the size of the cut, where *C* is a universal constant. This resolves the strong thin tree conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A polynomial-time construction of strong thin trees

We give a deterministic polynomial-time construction of strong thin trees. Given a finite *k*-edge-connected loopless multigraph on at least one vertex, the algorithm constructs a spanning tree meeting every cut in at most a $C/k$ fraction of its edges, for a universal constant *C*. The running time is polynomial in the binary input length, including when parallel-edge multiplicities are encoded in binary.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The strong thin-tree conjecture asks for spanning trees that cross every cut sparsely relative to the original graph. The formalized result gives one absolute constant $C>0$ such that every finite loopless $k$-edge-connected multigraph with at least two vertices has a spanning tree crossing each nontrivial cut at most $(C/k)$ times the original cut size. Parallel edges remain distinct. No numerical value of $C$ or construction algorithm is asserted.

The strong thin-tree problem asks for a spanning tree that crosses every cut sparsely relative to the original graph. The formalization gives one deterministic polynomial-time algorithm and an absolute constant $C>0$ such that a finite $k$-edge-connected loopless multigraph yields a spanning tree using at most a $C/k$ fraction of the edges of every cut. The input may encode parallel-edge multiplicities in binary, and the running time is polynomial in that binary input length.

## Lean: Strong thin-tree bound

Stated in [StrongThinTree.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StrongThinTree.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem strongThinTree : MainStatement
```

Proved in [lean/OAI/Combinatorics/ThinTrees/Main.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ThinTrees/Main.lean#L24).

## Lean: Polynomial-time construction of strong thin trees

Stated in [AlgorithmicThinTrees.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/AlgorithmicThinTrees.lean).

```lean
theorem algorithmic_strong_thin_trees : AlgorithmicStrongThinTrees
```

Proved in [lean/OAI/Combinatorics/ThinTrees/Encoding/AlgorithmicMain.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ThinTrees/Encoding/AlgorithmicMain.lean#L65).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/174.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/174.md)
