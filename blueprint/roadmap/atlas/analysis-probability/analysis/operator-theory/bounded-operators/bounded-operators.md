---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.SymmetricOperatorToDualBoundedWanted.exists_bound_of_symmetric_linearMap_to_strongDual, MathlibExt.Analysis.FunctionalAnalysis.BartleGravesWanted.bartle_graves, MathlibExt.Analysis.FunctionalAnalysis.LomonosovInvariantSubspaceWanted.lomonosov_invariantSubspace, MathlibExt.Analysis.OperatorTheory.StrongOperatorConvergenceIffWeakAndAdjointWanted.tendsto_apply_iff_tendsto_inner_and_tendsto_inner_adjoint_comp
statement: formalized
---

# Bounded operators and operator topologies: its own results

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/index.html).

General bounded operators: Douglas lemma, direct sums, strong and weak operator convergence, uniform boundedness, Hellinger–Toeplitz, invariant subspaces (Lomonosov), hypercyclicity criteria, Wold decomposition.

## A symmetric linear map from a Banach space to its dual is bounded

Let $E$ be a real
Banach space with dual space $E^*$ of continuous linear functionals, and let $T : E \to E^*$ be
a linear map that is symmetric: $(Tx)(y) = (Ty)(x)$ for all $x, y \in E$. Then $T$ is bounded:
there is a constant $C \ge 0$ such that $\|Tx\| \le C \|x\|$ for all $x \in E$, where $\|Tx\|$
is the operator norm of the functional $Tx$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Operator theory; General theory of linear operators), problem `ma_proofbench_l1_22`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.SymmetricOperatorToDualBoundedWanted.exists_bound_of_symmetric_linearMap_to_strongDual` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/SymmetricOperatorToDualBoundedWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/SymmetricOperatorToDualBoundedWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/index.html#exists-bound-of-symmetric-linear-map-to).

## Bartle–Graves theorem

Let $E$ and $F$ be real Banach spaces and let $T : E \to F$ be a
surjective continuous linear map. Then there are a continuous map $g : F \to E$, in general not
linear, and a constant $C \ge 0$ such that $T(g(y)) = y$ for every $y \in F$, $g(0) = 0$,
$g(t y) = t \, g(y)$ for every real $t \ge 0$ and every $y \in F$, and $\|g(y)\| \le C \|y\|$
for every $y \in F$.

## Sources

- R. G. Bartle and L. M. Graves, Mappings between function spaces, Trans. Amer. Math. Soc. 72 (1952), 400–413, DOI 10.1090/S0002-9947-1952-0047910-X; Michael selection theorem precursor; Lean states real Banach case with continuous right inverse, positive homogeneity, and linear growth bound.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BartleGravesWanted.bartle_graves`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BartleGraves.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/BartleGraves.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/index.html#bartle-graves).

## Lomonosov's invariant subspace theorem

Let $E$ be an infinite-dimensional complex Banach
space, let $K$ be a nonzero compact operator on $E$, and let $T$ be a bounded linear operator on
$E$ with $TK = KT$. Then there is a closed linear subspace $M$ of $E$ with $M \ne \{0\}$ and
$M \ne E$ that is invariant under $T$: $T x \in M$ for every $x \in M$.

## Sources

- V. Lomonosov, Functional Anal. Appl. 7 (1973) and J. Hilden elementary proof, Bull. Amer. Math. Soc.; Aronszajn-Smith 1954 precursor; Radjavi-Rosenthal invariant subspace book, 1973; Lean states complex Banach infinite-dimensional case `K≠0` compact commuting with `T` yields nontrivial closed invariant subspace.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LomonosovInvariantSubspaceWanted.lomonosov_invariantSubspace`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LomonosovInvariantSubspace.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/LomonosovInvariantSubspace.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/index.html#lomonosov-invariant-subspace).

## Strong operator convergence characterized by weak operator convergence

Let $H$ be a real
or complex Hilbert space with inner product $\langle \cdot, \cdot \rangle$, let
$(T_n)_{n \in \mathbb{N}}$ be a sequence of bounded linear operators on $H$, let $T$ be a bounded
linear operator on $H$, and write $S^*$ for the adjoint of an operator $S$. Then $T_n \to T$ in
the strong operator topology, that is, $T_n x \to T x$ for every $x \in H$, if and only if both
$T_n \to T$ in the weak operator topology, that is, $\langle y, T_n x \rangle \to
\langle y, T x \rangle$ for all $x, y \in H$, and $T_n^* T_n \to T^* T$ in the weak operator
topology, that is, $\langle y, T_n^* T_n x \rangle \to \langle y, T^* T x \rangle$ for all
$x, y \in H$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_59`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.StrongOperatorConvergenceIffWeakAndAdjointWanted.tendsto_apply_iff_tendsto_inner_and_tendsto_inner_adjoint_comp` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/StrongOperatorConvergenceIffWeakAndAdjointWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OperatorTheory/StrongOperatorConvergenceIffWeakAndAdjointWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/index.html#tendsto-apply-iff-tendsto-inner-and-tend).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded operators and operator topologies](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/bounded-operators)
