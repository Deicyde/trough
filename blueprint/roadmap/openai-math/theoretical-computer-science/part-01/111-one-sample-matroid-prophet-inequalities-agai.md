---
declaration: section
origin: cited
lean: OAI.MatroidProphet.one_sample, OAI.MatroidProphet.Assigned.one_sample, OAI.MatroidProphet.Assigned.hidden_vector, OAI.MatroidProphet.Assigned.secretary
statement: formalized
proof: formalized
---

# 111. One-sample matroid prophet inequalities against an almighty adversary

1 manuscript and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every finite matroid known in advance, gives a distribution-independent online rule using one independent sample per element and earning a universal constant fraction of the expected offline optimum. Values are independent and nonnegative, with finite expected optimum. The guarantee holds even when the arrival-order adversary sees all samples, values, and the rule's entire random seed; no polynomial-time implementation is asserted.

## One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary

We prove that one independent sample per element suffices for a constant-competitive prophet inequality on every finite matroid. The guarantee holds even when the arrival-order adversary observes all samples, all online values, and the algorithm's entire random seed. The rule needs no description of the value distributions and achieves the absolute competitive ratio $2^{-310}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves a one-sample matroid prophet inequality with expected reward at least $2^{-310}$ times the expected offline optimum. Each element has one independent sample paired with an identically distributed nonnegative online value, and all coordinates are independent. The rule and finite seed law depend only on the labeled matroid; choices are irrevocable and feasible after every prefix. The arrival order may depend measurably on all samples, values, and the seed, and only the offline optimum must be integrable.

A supporting hidden-vector selection result for fixed nonnegative matroid weights gives expected worst-order reward at least $2^{-293}$ times the optimum, again with a finite seed law and prefix feasibility.

## Lean: One-sample matroid prophet inequality against an almighty adversary

Stated in [MatroidProphet.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatroidProphet.lean).

```lean
theorem one_sample.{u} : OneSampleChallenge.{u}
```

Proved in [lean/OAI/Probability/MatroidProphet/Main.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/MatroidProphet/Main.lean#L60).

## Lean: Hidden-vector matroid selection with worst-order guarantee

Stated in [MatroidSecretary.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatroidSecretary.lean).

```lean
theorem one_sample.{u} : MatroidProphet.OneSampleChallenge.{u}
```

Proved in [lean/OAI/Probability/MatroidSecretary/Contracts.lean, line 49](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/MatroidSecretary/Contracts.lean#L49).

```lean
theorem hidden_vector : MatroidProphet.HiddenVectorChallenge
```

Proved in [lean/OAI/Probability/MatroidSecretary/Contracts.lean, line 52](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/MatroidSecretary/Contracts.lean#L52).

```lean
theorem secretary.{u} : MatroidProphet.SecretaryChallenge.{u}
```

Proved in [lean/OAI/Probability/MatroidSecretary/Contracts.lean, line 118](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/MatroidSecretary/Contracts.lean#L118).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/111.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/111.md)
