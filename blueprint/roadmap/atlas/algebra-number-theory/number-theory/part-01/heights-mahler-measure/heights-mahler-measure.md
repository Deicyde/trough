---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.SchinzelZassenhausWanted.NumberTheory.dimitrov
statement: formalized
---

# Heights and Mahler measure: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/index.html).

Absolute heights of algebraic numbers, Mahler measure, Lehmer's problem, Dobrowolski bounds, Schinzel–Zassenhaus, house and trace problems.

## Dimitrov's lower bound for the house of an algebraic integer

Let $K$ be a number field
and let $\alpha \in K$ be a nonzero algebraic integer that is not a root of unity. Let $d'$ be
the number of distinct values of the argument $\arg \sigma(\alpha)$ as $\sigma$ ranges over the
ring homomorphisms $K \to \mathbb{C}$. Then the house of $\alpha$, the maximum of
$|\sigma(\alpha)|$ over these $\sigma$, is at least $2^{1/(4d')}$.

## Sources

- James McKee and Chris Smyth, Around the Unit Circle, Chapter 4, Theorem 4.1; Vesselin Dimitrov (2019). Problem `dimitrov` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.SchinzelZassenhausWanted.NumberTheory.dimitrov` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchinzelZassenhausWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SchinzelZassenhausWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/index.html#dimitrov).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heights and Mahler measure](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/heights-mahler-measure)
