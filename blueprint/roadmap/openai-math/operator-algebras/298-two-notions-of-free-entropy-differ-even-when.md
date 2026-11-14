---
declaration: section
origin: cited
lean: OAI.FiniteEntropySeparation.main
statement: formalized
proof: formalized
---

# 298. Two notions of free entropy differ even when both are finite

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a bounded self-adjoint tuple in a tracial von Neumann algebra whose microstates and nonmicrostates free entropies satisfy $-\infty\lt \chi\lt \chi^*\lt \infty$. This answers Voiculescu’s finite-entropy equality question negatively: the matrix-approximation and free-Fisher-information definitions differ even when both are finite.

## A finite-entropy separation of microstates and nonmicrostates free entropy

We answer the finite-entropy equality question for microstates and nonmicrostates free entropy negatively. We construct a bounded self-adjoint tuple *X* in a von Neumann algebra with faithful normal tracial state such that $-\infty\lt \chi(X)\leq\chi^*(X)-\tfrac12\lt \infty$. Here *χ* is the original microstates entropy with an operator-norm cutoff and a limsup over matrix sizes. The counterexample uses a large but fixed number of variables.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization disproves equality of microstates and nonmicrostates free entropy even when both quantities are finite. It constructs a bounded self-adjoint tuple $X$ in a von Neumann algebra with a faithful normal tracial state such that $-\infty<\chi(X)\le\chi^*(X)-1/2<\infty$. Here $\chi$ is the microstates entropy with an operator-norm cutoff and a limsup over matrix sizes, and $\chi^*$ is the nonmicrostates entropy defined using free semicircular noise. The example has a fixed finite number of variables.

## Lean: Finite separation of microstates and nonmicrostates free entropy

```lean
theorem main :
    ∃ (H : Type) (_ : NormedAddCommGroup H) (_ : InnerProductSpace ℂ H)
      (_ : CompleteSpace H) (M : VonNeumannAlgebra H) (τ : TracialVector M)
      (n : ℕ) (X S : Fin n → H →L[ℂ] H),
      2 ≤ n ∧
      (∀ i, X i ∈ M ∧ IsSelfAdjoint (X i)) ∧
      (∀ i, S i ∈ M ∧ IsSelfAdjoint (S i)) ∧
      FreeStandardNoise τ X S ∧
      (⊥ : EReal) < chi τ X ∧
      chi τ X ≤ chiStar τ X S - (1 / 2 : EReal) ∧
      chiStar τ X S - (1 / 2 : EReal) < (⊤ : EReal)
```

Stated in [FiniteEntropySeparation.lean, line 108](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FiniteEntropySeparation.lean#L108). Proved in [lean/OAI/Analysis/FreeEntropy/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/FreeEntropy/Main.lean#L9).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/298.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/298.md)
