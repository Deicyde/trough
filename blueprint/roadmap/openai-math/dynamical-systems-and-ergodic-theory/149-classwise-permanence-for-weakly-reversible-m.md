---
declaration: section
origin: cited
lean: OAI.Problem326.global_bounded_persistent_solution
statement: formalized
proof: formalized
---

# 149. Classwise permanence for weakly reversible mass-action systems

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the permanence conjecture for every finite weakly reversible mass-action system with fixed positive rate constants. Every positive stoichiometric compatibility class, even an unbounded one, has a common compact convex forward-invariant absorbing set. All positive trajectories in that class therefore eventually share positive lower and finite upper concentration bounds.

## Uniform Permanence in Weakly Reversible Mass-Action Systems

We prove the permanence conjecture for finite weakly reversible mass-action systems with fixed positive reaction rates. Every positive stoichiometric compatibility class admits one compact convex forward-invariant set that every positive trajectory in that class enters in finite time, even when the class is unbounded. The set depends only on the network, the rates, and the class; the entry time may depend on the initial state. Thus, after its entry time, every concentration satisfies the same positive lower and finite upper bounds throughout that class.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf).

## Boundedness and persistence of weakly reversible mass-action systems

We prove the boundedness and persistence conjectures for finite weakly reversible mass-action systems with positive constant reaction rates. For every positive initial condition, the solution exists for all forward time, and every concentration remains bounded above and bounded away from zero. The bounds may depend on the initial condition, and no boundedness assumption is imposed on its stoichiometric compatibility class.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The boundedness and persistence conjectures for mass-action systems ask whether positive concentrations remain finite and separated from zero. The formalization proves this for every finite weakly reversible reaction network with positive constant reaction rates and every strictly positive initial state. A global forward solution exists, and one $\varepsilon\in(0,1)$ bounds every concentration of every global forward solution between $\varepsilon$ and $\varepsilon^{-1}$ for all nonnegative times. The bound may depend on the network, rates, and initial state.

## Lean: Global boundedness and persistence for weakly reversible mass-action systems

Stated in [MassAction.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MassAction.lean).

```lean
theorem global_bounded_persistent_solution :
    ∀ (d : ℕ) (N : ReactionNetwork d) (κ : Reaction N → ℝ),
      0 < d → WeaklyReversible N → (∀ e, 0 < κ e) →
      ∀ x0 : Fin d → ℝ, PositiveState x0 →
      ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
        (∃ x : ℝ → (Fin d → ℝ), IsGlobalForwardSolution N κ x0 x) ∧
        ∀ x : ℝ → (Fin d → ℝ), IsGlobalForwardSolution N κ x0 x →
        ∀ t : ℝ, 0 ≤ t → ∀ i : Fin d, ε ≤ x t i ∧ x t i ≤ ε⁻¹
```

Proved in [lean/OAI/Analysis/MassAction/Main.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/MassAction/Main.lean#L73).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/149.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/149.md)
