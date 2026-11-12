---
declaration: section
origin: cited
lean: OAI.CHObstruction.main
statement: formalized
proof: formalized
---

# 240. Shelah's eventual categoricity and the prescribed-threshold obstruction

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Shelah's eventual categoricity conjecture in ZFC: for each bound on the Löwenheim–Skolem number, a uniform threshold makes categoricity of an abstract elementary class in one cardinal above that threshold imply categoricity throughout the same tail. Categoricity means uniqueness up to isomorphism at a given cardinality. Under the continuum hypothesis, a proposed specific Hanf threshold need not suffice.

## A CH obstruction to a prescribed categoricity threshold

Assuming the continuum hypothesis, we construct an abstract elementary class with Löwenheim–Skolem number ℵ$_{0}$ that is categorical in every sufficiently large cardinal but has at least two nonisomorphic models of cardinality $\beth_{\omega_2}$. Thus categoricity does not transfer down to the proposed bound $\beth_{(2^{\aleph_0})^+}$, which equals $\beth_{\omega_2}$ under CH. Consequently, if ZFC is consistent, the prescribed-threshold form of Shelah's categoricity conjecture is not provable in ZFC.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Eventual categoricity for abstract elementary classes

We prove Shelah's eventual categoricity conjecture for abstract elementary classes in ZFC. For each infinite bound on the Löwenheim–Skolem number there is a uniform threshold such that categoricity in any one cardinal at or above that threshold implies categoricity in every cardinal at or above the same threshold.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/paper.pdf).

## The Lean formalization

Under the continuum hypothesis, the formalized result refutes the proposed transfer of categoricity down to the Hanf threshold. It gives an abstract elementary class in a countable relational language, with Löwenheim–Skolem number $\aleph_0$, that has two nonisomorphic models at $\beth_{\omega_2}=h(\aleph_0)$ but is categorical in every cardinal at least $\beth_{(2^{\aleph_1})^+}$.

No amalgamation, joint embedding, tameness, or absence-of-maximal-models assumption is imposed. The later canonical-point obstruction and the separate eventual-categoricity theorem are not included.

## Lean: CH categoricity-threshold obstruction

Stated in [CHObstruction.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CHObstruction.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main (hCH : CH.{u}) :
    ∃ (L : ℕ → Type), Countable (Σ n, L n) ∧
      ∃ K : ClassData.{u} L, K.IsAEC ∧ K.HasLSNumber ℵ₀ ∧
        endpoint = hanf (ℵ₀ : Cardinal.{u}) ∧ K.TwoModels endpoint ∧
        ∀ μ, tailThreshold ≤ μ → K.Categorical μ
```

Proved in [lean/OAI/ModelTheory/Categoricity/Main.lean, line 233](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/ModelTheory/Categoricity/Main.lean#L233).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/240.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/240.md)
