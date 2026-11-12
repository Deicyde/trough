---
declaration: section
origin: cited
lean: OAI.Kaplansky.kaplansky_quasitrace_counterexample, OAI.KaplanskyConsequences.stable_finiteness_bundle
statement: formalized
proof: formalized
---

# 294. Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves Kaplansky's quasitrace conjecture by constructing a separable unital complex $C^{∗}$-algebra admitting normalized 2-quasitraces, all of which are nonadditive. As a consequence, two unital simple stably finite $C^{∗}$-algebras can have a properly infinite minimal tensor product, with one factor $C_r^*(\mathbb F_2)$.

## A counterexample to Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness

We refute Kaplansky's quasitrace conjecture by constructing a separable unital complex $C^{∗}$-algebra that admits normalized 2-quasitraces but has no tracial state. As a consequence, we show that the minimal tensor product of two unital simple stably finite complex $C^{∗}$-algebras can be properly infinite, even when one factor is the reduced free-group algebra $C_r^*(\mathbb F_2)$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Kaplansky's quasitrace conjecture predicts that every $2$-quasitrace on a $C^*$-algebra is a trace. The formalization constructs a separable $C^*$-algebra with normalized $2$-quasitraces and fixed positive contractions $a,b$ for which every such quasitrace satisfies $\mathrm{Re}(\tau(a+b)-\tau(a)-\tau(b))\ge1/144$. Thus none is additive on this pair.

The formalization also gives simple stably finite $C^*$-algebras whose spatial tensor product is properly infinite, a separable stably finite algebra with no tracial state, and a tensor-product example in which normalized $2$-quasitraces are lost. These are the stable-finiteness consequences named in the paper's title.

## Lean: Nonadditive normalized $2$-quasitraces

Stated in [KaplanskyQuasitrace.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KaplanskyQuasitrace.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem kaplansky_quasitrace_counterexample : MainTarget
```

Proved in [lean/OAI/Analysis/Kaplansky/Main.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Kaplansky/Main.lean#L17).

## Lean: Tensor-product failure of stable finiteness and quasitrace consequences

Stated in [KaplanskyStableFiniteness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KaplanskyStableFiniteness.lean).

```lean
theorem stable_finiteness_bundle : StableFinitenessBundle
```

Proved in [lean/OAI/Analysis/Kaplansky/StableFiniteness.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Kaplansky/StableFiniteness.lean#L18).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/294.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/294.md)
