---
declaration: section
origin: cited
lean: OAI.CPTSeparation.main, OAI.WitnessedChoice.main
statement: formalized
proof: formalized
---

# 243. Separating choiceless counting from polynomial time and witnessed choice

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Confirms the Blass–Gurevich–Shelah noncapture conjecture: consistency of a linear system over 𝔽$_{3}$ defines a polynomial-time query on unordered finite structures that choiceless polynomial time with counting cannot express. A separate result shows that adding witnessed symmetric choice strictly increases expressive power. Both separations hold for the full counting formalism, allowing hereditarily finite sets of arbitrary finite rank.

## Choiceless polynomial time with counting does not capture polynomial time

We prove that choiceless polynomial time with counting does not capture polynomial time on unordered finite structures, confirming the noncapture conjecture of Blass, Gurevich and Shelah. A linear-consistency query over 𝔽$_{3}$ in a fixed binary vocabulary is decidable in polynomial time but not in the full counting formalism.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Witnessed symmetric choice is strictly stronger than choiceless polynomial time with counting

We prove that witnessed symmetric choice strictly increases the expressive power of choiceless polynomial time with counting. A fixed sentence with one witnessed-choice occurrence defines a Boolean query on every finite input that is not definable in the original counting formalism.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result separates polynomial time from choiceless polynomial time with counting. It gives an explicit query on finite structures with eight relations that is invariant under isomorphism and decidable in polynomial time, but is not definable in the stated hereditarily finite-set language with cardinality and polynomial bounds on stages and intermediate objects. The query applies to all finite inputs without a promise. The separate witnessed-symmetric-choice result is not included.

The formalization proves that witnessed symmetric choice strictly increases the expressive power of choiceless polynomial time with counting. It constructs one fixed sentence with exactly one witnessed-choice occurrence that gives a Boolean answer on every finite input, while no sentence of the original counting formalism defines the same class of inputs.

## Lean: Polynomial-time query outside choiceless polynomial time

Stated in [ChoicelessPolynomialTime.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ChoicelessPolynomialTime.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main :
    (∀ (A B : Type) [Fintype A] [Fintype B] (S : Input A) (T : Input B),
      S.Iso T → (S.query ↔ T.query)) ∧
    OrdinaryPolynomialTime ∧
    ¬ FullCPT.EvaluationDefinable (fun {_} [_] I => I.query)
```

Proved in [lean/OAI/ModelTheory/Choiceless/Separation.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/ModelTheory/Choiceless/Separation.lean#L7).

## Lean: Strict expressive gain from one witnessed symmetric choice

Stated in [WitnessedChoice.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/WitnessedChoice.lean).

```lean
theorem WitnessedChoice.main : WitnessedChoice.BGS.MainStatement
```

Proved in [lean/OAI/Computability/WitnessedChoice/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/WitnessedChoice/Main.lean#L12).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/243.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/243.md)
