---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.ScottishBook170Wanted.szpilrajn170_homeomorphic_images_measurable_imp_absolute, MeasureTheory.vitali_nonmeasurable
statement: formalized
---

# Measures and measurable sets: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/index.html).

Construction and uniqueness of measures, atomless and vector measures, measures on Boolean algebras, and the limits of measurability shown by non-measurable sets and paradoxical decompositions.

## Szpilrajn's Problem 170: plane sets with measurable homeomorphic copies

Let $S$ be a subset
of the plane $\mathbb{R}^2$ such that every subset $T$ of $\mathbb{R}^2$ homeomorphic to $S$ (as
a subspace) is Lebesgue measurable, that is, Carathéodory measurable with respect to Lebesgue
outer measure on $\mathbb{R}^2$. Then $S$ is absolutely measurable: for every measure $\mu$ on
the Borel $\sigma$-algebra of $\mathbb{R}^2$, the set $S$ is Carathéodory measurable with respect
to the outer measure induced by $\mu$.

The hypothesis concerns every subset of the plane homeomorphic to $S$, not only the images of $S$
under homeomorphisms of the whole plane.

## Sources

- E. Szpilrajn, Problem 170 of the Scottish Book; the affirmative answer follows from an unpublished result of J. von Neumann, as recorded in Ad 170 of the typescript. See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015). Lebesgue measurability is stated as Carathéodory measurability with respect to `volume`; the case of linear sets, and the analogue for generalized homeomorphisms in the sense of Kuratowski, were already known.

Stated but not proved: `MathlibExt.MeasureTheory.ScottishBook170Wanted.szpilrajn170_homeomorphic_images_measurable_imp_absolute` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ScottishBook170Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScottishBook170Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/index.html#szpilrajn170-homeomorphic-images-measura).

## Vitali's theorem

There exists a subset of $\mathbb{R}$ that is not Lebesgue measurable.

## Sources

- G. Vitali, Sul problema della misura dei gruppi di punti di una retta, Tipografia Gamberini e Parmeggiani, Bologna (1905). Here `NullMeasurableSet` w.r.t. `volume` is the Lebesgue-measurability notion, i.e. measurability for the completion of Lebesgue measure.

Formalized by `MeasureTheory.vitali_nonmeasurable`, a theorem declared in [MathlibExt/MeasureTheory/Measure/VitaliNonmeasurable.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/VitaliNonmeasurable.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/index.html#vitali-nonmeasurable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Measures and measurable sets](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/measures)
