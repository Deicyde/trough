---
declaration: section
origin: cited
lean: OAI.SLEExactGauge.sourceLowerMain_proved
statement: formalized
proof: formalized
---

# 230. Exact Hausdorff gauges for SLE

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves Schramm’s Hausdorff-measure question for chordal SLE$_{κ}$, $0\lt \kappa\lt 8$. The explicit gauge $r^d(\log\log(1/r))^{(2-d)/2}$, $d=1+\kappa/8$, gives almost surely positive finite measure to every trace segment $\gamma([s,t])$ with $0\lt s\lt t\lt \infty$, and finite expected measure to the trace in every bounded disk.

## An exact Hausdorff gauge for SLE

For each $0\lt \kappa\lt 8$, we construct a deterministic Hausdorff gauge that almost surely assigns positive finite measure to every nontrivial compact positive-time segment of chordal Schramm–Loewner evolution. This answers Schramm's Hausdorff-measure existence problem in this parameter range. The entire trace has finite expected gauge measure in each bounded box.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/An-exact-Hausdorff-gauge-for-SLE-September-25-2026.pdf); the Lean below formalizes results from it.

## An explicit exact Hausdorff gauge for SLE

For each fixed $0\lt \kappa\lt 8$, let $d=1+\kappa/8$. The gauge $h(r)=r^d(\log\log(1/r))^{(2-d)/2}$ at sufficiently small radii almost surely gives positive finite Hausdorff measure to every nontrivial positive-time compact segment of chordal SLE$_{κ}$. This gives an explicit solution to Schramm's Hausdorff-measure problem in this parameter range. The entire trace has finite expected measure in every bounded disk. The exponent-one iterated-logarithm gauge suggested by Schramm is not sigma-finite on any such segment.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

For $0<\kappa<8$, put $d=1+\kappa/8$. The formalization proves that every continuous nondecreasing Hausdorff gauge agreeing with $h(r)=r^d(\log\log(1/r))^{(2-d)/2}$ at sufficiently small positive radii almost surely assigns positive measure to every nontrivial compact positive-time segment of ordinary chordal $\mathrm{SLE}_\kappa$.

## Lean: Positivity of the explicit gauge on every positive-time segment

```lean
theorem sourceLowerMain_proved : SourceLowerMainTarget
```

Stated in [SLELowerPositivity.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SLELowerPositivity.lean#L78). Proved in [lean/OAI/Probability/SLE/LowerPositivity.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SLE/LowerPositivity.lean#L60).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/230.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/230.md)
