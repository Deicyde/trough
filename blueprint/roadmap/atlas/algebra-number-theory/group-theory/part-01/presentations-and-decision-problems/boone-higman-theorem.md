---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BooneHigmanEmbeddingWanted.GroupTheory.BooneHigmanEmbedding.boone_higman_embedding, MathlibExt.GroupTheory.BooneHigmanSimpleWanted.GroupTheory.BooneHigmanSimpleProblem.boone_higman_simple
statement: formalized
---

# Boone–Higman theorem

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/boone-higman-theorem/index.html).

## Boone–Higman theorem (easy direction)

Let $\varphi \colon F_n \to G$ be a surjective
homomorphism from the free group $F_n$ on $n$ generators onto a group $G$. If there are injective
homomorphisms $G \to H$ and $H \to K$, where $H$ is a simple group and $K$ is a finitely presented
group, then the word problem of $G$ with respect to $\varphi$ is solvable.

## Sources

- W. W. Boone & G. Higman, *An algebraic characterization of groups with soluble word problem*, J. Austral. Math. Soc. 18 (1974). Knill, *Some fundamental theorems in mathematics*, §122. Problem `boone_higman_embedding` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.BooneHigmanEmbeddingWanted.GroupTheory.BooneHigmanEmbedding.boone_higman_embedding` is written with `theorem_wanted` in [WantedExt/GroupTheory/BooneHigmanEmbeddingWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BooneHigmanEmbeddingWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/boone-higman-theorem/index.html#boone-higman-embedding).

## Kuznetsov's theorem on finitely presented simple groups

Let $G$ be a simple group, let
$F_n$ be the free group on $n$ generators, and let $\varphi \colon F_n \to G$ be a surjective
homomorphism whose kernel is the normal closure of finitely many elements. Then the word problem
of $G$ with respect to $\varphi$ is solvable: there is an algorithm that decides, for every word
$w$ in the $n$ generators and their inverses, whether $\varphi(w) = 1$.

## Sources

- A.V. Kuznetsov, 'Algorithms as operations in algebraic systems', Uspekhi Mat. Nauk 13 (1958) 240–241 (Russian); W.W. Boone and G. Higman, 'An algebraic characterization of groups with soluble word problem', J. Austral. Math. Soc. 18 (1974) 41–53. §122 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `boone_higman_simple` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.BooneHigmanSimpleWanted.GroupTheory.BooneHigmanSimpleProblem.boone_higman_simple` is written with `theorem_wanted` in [WantedExt/GroupTheory/BooneHigmanSimpleWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BooneHigmanSimpleWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/boone-higman-theorem/index.html#boone-higman-simple).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boone–Higman theorem](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/boone-higman-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/boone-higman-theorem)
