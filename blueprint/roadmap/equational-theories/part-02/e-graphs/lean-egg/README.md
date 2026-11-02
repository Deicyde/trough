# lean-egg

## Methodology

The basic methodology of equality saturation is based on E-Graphs, a data structure that can store equivalence classes of terms efficiently. We used the `lean-egg` tactic (<https://github.com/marcusrossel/lean-egg>), based on equality saturation as a tactic, which (re)constructs a proof from the E-graph ([Koehler et al. 2024](https://doi.org/10.1145/3632900)) in Lean. This means that we do not have to trust either the egg tool nor the tactic: if something goes wrong, Lean will not accept the constructed proof. In fact, we found issues with the proof reconstruction from the examples in this project.

The `lean-egg` tactic works for equational reasoning, i.e. proving equalities as consequences of other equalities (potentially universally quantified), which is exactly what we need to prove implications of laws in Magmas. In many cases, we have laws of the form $x = y$, where neither set of variables in the left- and right-hand-side of the law is a subset of each other. In this case the laws cannot be used as rewrite rules: it's not clear what it would be rewritten to, since there are unknowns on both sides of the equation. For these cases we used a simple heuristic, where we instantiate the variables with terms found in the (proof) context, as those are likely to be important for proving the equality.

## Results

Out of the possible implications between the $34$ equations considered in [Selected laws](../../../part-01/selected-laws/README.md), this method found an additional 86 implications that were not found before. Some of these seem to be missing in the computation of the transitive closure of implications of the equalities (an investigation is in progress), but some of these are genuinely new theorems, and the `lean-egg` tactic finds good proofs of these (these can be rewritten using `calc` style with a different tactic, `calcify`: <https://github.com/nomeata/lean-calcify>). An example of this is the following proof, found by `lean-egg`:

- [14 implies 23](14-implies-23.md)

It was also able to (re)prove [1689 is equivalent to 2](../../../part-01/implications-between-selected-laws/1689-equiv-2.md), albeit with a manually-provided hint (guide, in the sense of ([Koehler et al. 2024](https://doi.org/10.1145/3632900))).
