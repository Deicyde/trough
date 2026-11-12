---
declaration: section
origin: cited
lean: OAI.PinchedHartogs.main_theorem, OAI.PinchedHartogs.controlled_potential, OAI.PinchedHartogs.metric_transfer
statement: formalized
proof: formalized
---

# 359. Negative Kähler curvature without bounded holomorphic coordinates

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a contractible domain in ℂ$^{3}$ with a complete negatively pinched Kähler metric but no bounded holomorphic coordinates, disproving bounded-domain uniformization in this setting. A higher-dimensional example has sectional curvature at most −1 and only constant bounded holomorphic functions; its curvature is not bounded below.

## A negatively pinched Kähler threefold without bounded holomorphic coordinates

We construct a contractible domain in complex dimension three with a complete Kähler metric whose real sectional curvatures lie between two finite negative constants. It admits no bounded holomorphic map to ℂ$^{3}$ with nowhere-vanishing Jacobian and is therefore not biholomorphic to a bounded domain. This gives a negative answer to the negatively pinched Kähler uniformization question.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## One-sided negative sectional curvature and the holomorphic Liouville property

We construct, in some sufficiently large fixed finite complex dimension *m*, a domain in ℂ$^{m}$ diffeomorphic to $\mathbb R^{2m}$ that admits a complete Kähler metric with real sectional curvature at most −1 and has only constant bounded holomorphic functions. Its sectional curvatures are unbounded below. The construction gives a negative answer to the one-sided bounded-holomorphic-function question.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf).

## The Lean formalization

The formalized result constructs a nonempty contractible complex threefold with a complete Kähler metric whose real sectional curvatures lie between two fixed negative constants. Nevertheless, it has no system of bounded holomorphic coordinates and is not biholomorphic to a bounded domain. The metric is obtained from an explicitly controlled potential. This is the negatively pinched construction; the different companion with only one-sided curvature control is separate.

## Lean: Negatively pinched Kähler threefold without bounded coordinates

Stated in [PinchedKahler.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PinchedKahler.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_theorem : MainTheorem
```

Proved in [lean/OAI/Geometry/Kahler/Main.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Kahler/Main.lean#L38).

```lean
theorem controlled_potential : ControlledPotential
```

Proved in [lean/OAI/Geometry/Kahler/Main.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Kahler/Main.lean#L23).

```lean
theorem metric_transfer : MetricTransfer
```

Proved in [lean/OAI/Geometry/Kahler/HartogsTransfer.lean, line 22](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Kahler/HartogsTransfer.lean#L22).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/359.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/359.md)
