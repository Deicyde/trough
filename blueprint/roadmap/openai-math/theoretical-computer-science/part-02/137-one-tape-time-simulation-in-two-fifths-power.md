---
declaration: section
origin: cited
lean: OAI.Fifths.Single.capped, OAI.Fifths.Single.unknown
statement: formalized
proof: formalized
---

# 137. One-tape time simulation in two-fifths-power space

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines the halting and finite-control outcome of a fixed deterministic one-writable-tape machine up to time *T* using $O(T^{2/5}\log^C(T+2))$ space, improving the square-root exponent. Heads move at most one cell per step; finitely many read-only input heads are allowed. Initial contents are independent of *T*, and contents and input symbols have polylogarithmic-space access. Simulation time is unrestricted.

## Simulating One-Tape Time in Two-Fifths-Power Space

We show that a fixed deterministic Turing machine with one writable tape and head can be simulated in $O(T^{2/5}\mathop{\mathrm{polylog}}\nolimits (T+2))$ work-space bits when a binary time cap *T* ≥ 2 is supplied. The simulator computes the finite-control and halting outcome by time *T*; its running time is unrestricted. The result allows a fixed number of read-only input heads and requires a fixed accessor that supplies every initial writable and read-only symbol within distance *T* of the relevant head origin in polylogarithmic space. This improves the square-root space exponent for one-tape machines, answering Williams's question for this model.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives two-fifths-power space simulation of a fixed deterministic machine with one writable tape and finitely many read-only input heads. Heads move at most one cell per step, initial contents are independent of the time bound, and contents and input symbols must be accessible in polylogarithmic space. Given a binary time cap $T\ge2$, the simulator returns the source's finite-control outcome and halting flag using $O(T^{2/5}(\log(T+2))^C)$ space.

A second simulator needs no time cap: on an input that halts at time $t$, it returns the halted outcome using $O((t+2)^{2/5}(\log(t+2))^C)$ space. Simulation time is unrestricted. General multitape simulation, hierarchy consequences, and bounded-space-halting results are outside these selected statements.

## Lean: Time-capped and unknown-time one-tape simulation in two-fifths-power space

Stated in [OneTapeSpace.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OneTapeSpace.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem capped [Fintype X] (A : M.Sym) (p q : ℝ) (hp : 1 ≤ p) (_hq : 1 ≤ q) :
    ∃ (N : TM X Unit M.Outcome) (e : ℕ) (c : ℝ), 0 < c ∧
      ∀ (x : List X) (T : ℕ), 2 ≤ T → M.Access A p q x T →
        ∃ b : ℕ, N.Within (binaryIn x (fun _ => T)) (M.outcome x T) b ∧
          (b:ℝ) ≤ c*(T:ℝ)^exponent*(Log T)^e
```

Proved in [lean/OAI/Computability/SpaceSimulation/Main.lean, line 39](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/SpaceSimulation/Main.lean#L39).

```lean
theorem unknown [Fintype X] (A : M.Sym) (p q : ℝ) (hp : 1 ≤ p) (_hq : 1 ≤ q) :
    ∃ (N : TM X Empty M.Outcome) (e : ℕ) (c : ℝ), 0 < c ∧
      ∀ (x : List X), (∀ T, 2 ≤ T → M.Access A p q x T) →
        ∀ (t : ℕ), (M.outcome x t).2 = true →
          ∃ b, N.Within (files x) (M.outcome x t) b ∧
            (b:ℝ) ≤ c*((t:ℝ)+2)^exponent*(Log t)^e
```

Proved in [lean/OAI/Computability/SpaceSimulation/Main.lean, line 64](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/SpaceSimulation/Main.lean#L64).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/137.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/137.md)
