---
declaration: section
origin: cited
lean: OAI.BufferedIsing.finite_graph_comparison
statement: formalized
proof: formalized
---

# 218. Conformal universality for weakly interacting and random-bond Ising models

6 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Weak finite-range square-symmetric even multispin perturbations of the square-lattice Ising model preserve critical bulk spin and energy limits; weak square-symmetric contour interactions also yield chordal SLE$_{3}$ interface limits. With sufficiently weak iid bond disorder of any fixed bounded nondegenerate mean-zero law, critical spin interfaces converge to the same law in probability over environments.

## Quenched SLE₃ limits for general weak random-bond Ising models

For the planar Ising model with bonds $J_e=1+\varepsilon\xi_e$, where the $ξ_{e}$ have any fixed bounded, nondegenerate, mean-zero iid law, we prove quenched chordal SLE$_{3}$ convergence for sufficiently small *ε* > 0. The temperature is the spontaneous-magnetization threshold. Convergence holds in probability over environments for the full oriented curve law in deterministic Jordan-domain approximations.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/general-weak-random-bond-ising.pdf).

## Quenched SLE₃ Universality for the Weak Random-Bond Ising Model

We prove quenched chordal SLE$_{3}$ convergence for the planar Ising model with sufficiently weak independent symmetric two-valued ferromagnetic bonds. The temperature is the critical point defined by spontaneous magnetization. Convergence holds in probability over environments for the full oriented curve law in deterministic Jordan-domain approximations.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/quenched-sle3-weak-random-bond-ising.pdf).

## Logarithmic Relative Fluctuations in the Weakly Disordered Planar Ising Model

Assuming the stated deterministic critical-reference estimates, we prove that the relative second moment of the quenched critical spin correlation in the square-lattice Ising model with independent fair bonds $1\pm\varepsilon$ grows as $(\log r)^{1/4+o(1)}$ for each sufficiently small fixed *ε* > 0. The correlation is evaluated at the physical critical temperature, with the thermodynamic limit taken before the disorder moments and the large-distance limit.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/critical-relative-second-moment-weak-random-bond-ising.pdf).

## Conformal universality of bulk Ising correlations under weak interactions

We prove conformal universality of mixed bulk spin and energy correlations for the square-lattice Ising model with sufficiently small, square-symmetric, finite-range even multispin perturbations of either sign. One critical-temperature branch and two field normalizations apply in every bounded simply connected $C^{2}$ Jordan domain with free, plus, or minus boundary conditions, and in the periodic thermodynamic plane state. Energies are centered in their actual states.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/paper.pdf).

## SLE3 universality for weak finite-range Ising interactions

We prove that every sufficiently small, square-symmetric finite-range perturbation of the planar Ising contour energy has a domain-independent inverse temperature at which its spin interface converges to chordal SLE$_{3}$. The result allows interactions of either sign, arbitrary admissible exterior contours, and uniformly approximated Jordan domains. Convergence holds for the full oriented curve law in uniform distance modulo increasing reparametrization.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/paper.pdf).

## Buffered comparison and stopping-band resolution in critical Ising

We prove pointwise comparison and finite stopping-band approximation theorems for the critical nearest-neighbor Ising model on the square lattice. Arbitrary common pinned spins are allowed in the comparison: the likelihood ratio is controlled by a zero-field FK connection probability on the graph with those vertices deleted. For an interface exploration across a band of fixed positive width, finitely many regular signed barriers approximate every good conditional target law in total variation, uniformly over bounded observables and sufficiently fine meshes.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result compares conditional Ising probabilities on finite graphs when two boundary mixtures differ but a common set of spins is pinned. If $q_0$ is the associated zero-field Fortuin–Kasteleyn connection probability after deleting the pinned vertices, the likelihood ratio lies between $\exp(-4\mathrm{artanh}\,q_0)$ and $\exp(4\mathrm{artanh}\,q_0)$. The statement allows arbitrary external fields and arbitrary probability mixtures satisfying the stated disjointness conditions. The paper's finite stopping-band approximation theorem is outside this selected statement.

## Lean: Finite-graph buffered Ising likelihood comparison

```lean
theorem finite_graph_comparison {n m : ℕ} (G : FiniteGraph n m)
    (h : Fin n → ℝ) (I J F : Finset (Fin n))
    (hIJ : Disjoint I J) (hIF : Disjoint I F) (hJF : Disjoint J F)
    (i j : KeptVertex F) (hi : i.val ∈ I) (hj : j.val ∈ J)
    (a τ : Spins n) (mix mix' : Spins n → ℝ)
    (hmix : ∀ b, 0 ≤ mix b) (hmix' : ∀ b, 0 ≤ mix' b)
    (hmixsum : ∑ b, mix b = 1) (hmix'sum : ∑ b, mix' b = 1) :
    Real.exp (-4 * Real.artanh (qZero G I J F i j)) ≤
        mixtureProb G h I J F a τ mix / mixtureProb G h I J F a τ mix' ∧
      mixtureProb G h I J F a τ mix / mixtureProb G h I J F a τ mix' ≤
        Real.exp (4 * Real.artanh (qZero G I J F i j))
```

Stated in [BufferedIsing.lean, line 98](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BufferedIsing.lean#L98). Proved in [lean/OAI/Probability/Ising/Main.lean, line 72](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/Ising/Main.lean#L72).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/218.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/218.md)
