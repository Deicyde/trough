---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.Breeder.Model, MathlibExt.Biology.StatisticalGenetics.Breeder.Model.selectionDifferential, MathlibExt.Biology.StatisticalGenetics.Breeder.Model.response, MathlibExt.Biology.StatisticalGenetics.Breeder.Model.response_eq, MathlibExt.Biology.StatisticalGenetics.Breeder.Model.selectionDifferential_univ, MathlibExt.Biology.StatisticalGenetics.Breeder.Model.response_univ
statement: formalized
proof: formalized
---

# Breeder's equation

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html).

## Breeder

## Linear parent–offspring regression model

The linear parent–offspring model on a population described by a probability measure `μ`:
the parental (mid-parent) value `parent` and the offspring value `offspring` are integrable,
`mean` is the population mean of the parental value, and the offspring value regresses linearly
on the parental value, `𝔼[O | P] = mean + h2 * (P - mean)` (equivalently
`O = mean + h2 (P - mean) + e` with `𝔼[e | P] = 0`). Here `h2` is the heritability.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Breeder.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/Breeder.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Breeder.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html#model).

## Selection differential

The selection differential `S = 𝔼[P | selected] - μ` of the selected group `s`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Breeder.Model.selectionDifferential`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Breeder.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Breeder.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html#selection-differential).

## Response to selection

The response to selection `R = 𝔼[O | selected] - μ`: the mean offspring value of the
selected parents, relative to the population mean.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Breeder.Model.response`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Breeder.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Breeder.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html#response).

## Breeder's equation

The breeder's equation (Lush 1937): if the selected group `s` is determined by the parental
value (an event of `σ(P)`) and has positive mass, the response to selection is the heritability
times the selection differential, `R = h² S`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Breeder.Model.response_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Breeder.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Breeder.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html#response-eq).

## Selecting the whole population gives zero selection differential

Selecting the whole population gives no selection differential, `S = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Breeder.Model.selectionDifferential_univ`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Breeder.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Breeder.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html#selection-differential-univ).

## Selecting the whole population gives zero response

Selecting the whole population gives no response, `R = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Breeder.Model.response_univ`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Breeder.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Breeder.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html#response-univ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Breeder's equation](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/breeder-s-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/quantitative-genetics/breeder-s-equation)
