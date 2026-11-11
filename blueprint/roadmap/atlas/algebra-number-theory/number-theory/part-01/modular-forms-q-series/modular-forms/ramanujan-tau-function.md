---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.RamanujanTauWanted.NumberTheory.RamanujanTauProblem.τ, MathlibExt.NumberTheory.RamanujanTauWanted.NumberTheory.RamanujanTauProblem.τ_one, MathlibExt.NumberTheory.RamanujanTauWanted.NumberTheory.RamanujanTauProblem.ramanujan_petersson
statement: formalized
---

# Ramanujan tau function

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-tau-function/index.html).

## Ramanujan τ-function

For a natural number $n$, $\tau(n)$ is the complex number given by
the coefficient of $q^n$ in the $q$-expansion of the modular discriminant $\Delta = \eta^{24}$,
where $\eta$ is the Dedekind eta function and $q = e^{2\pi i z}$.

Formalized by `MathlibExt.NumberTheory.RamanujanTauWanted.NumberTheory.RamanujanTauProblem.τ`, a definition declared in [WantedExt/NumberTheory/RamanujanTauWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanTauWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-tau-function/index.html#untitled).

## Normalisation of the Ramanujan τ-function

The Ramanujan τ-function satisfies
$\tau(1) = 1$: the coefficient of $q$ in the $q$-expansion of the modular discriminant $\Delta$
is $1$.

Formalized by `MathlibExt.NumberTheory.RamanujanTauWanted.NumberTheory.RamanujanTauProblem.τ_one`, a theorem declared in [WantedExt/NumberTheory/RamanujanTauWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanTauWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-tau-function/index.html#one).

## Ramanujan–Petersson conjecture for τ (Deligne's theorem)

For every prime $p$, the
Ramanujan τ-function satisfies $|\tau(p)| \le 2p^{11/2}$, where $|\cdot|$ is the absolute value
of a complex number.

## Sources

- S. Ramanujan, 'On certain arithmetical functions', Trans. Cambridge Philos. Soc. 22 (1916) 159–184. H. Petersson, 'Theorie der automorphen Formen beliebiger reeller Dimension und ihre Darstellung durch eine neue Art Poincaréscher Reihen', Math. Ann. 103 (1930) 369–436. P. Deligne, 'Formes modulaires et représentations ℓ-adiques', Séminaire Bourbaki 1968/69: Exposés 347–363, Lecture Notes in Math. 179, Springer (1971). P. Deligne, 'La conjecture de Weil. I', Publ. Math. IHÉS 43 (1974) 273–307. Background: https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Petersson_conjecture. Problem `ramanujan_petersson` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanTauWanted.NumberTheory.RamanujanTauProblem.ramanujan_petersson` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanTauWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanTauWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-tau-function/index.html#ramanujan-petersson).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan tau function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-tau-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-tau-function)
