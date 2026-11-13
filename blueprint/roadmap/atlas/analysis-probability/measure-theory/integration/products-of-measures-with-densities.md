---
declaration: section
origin: cited
lean: MeasureTheory.lmarginal_prod, MeasureTheory.lintegral_fintype_prod_eq_prod, MeasureTheory.Measure.pi_withDensity
statement: formalized
proof: formalized
---

# Products of measures with densities

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/products-of-measures-with-densities/index.html).

## Iterated integrals of a product of one-variable functions

Let $\mu_i$ be σ-finite
measures on measurable spaces $X_i$, indexed by a finite type $\iota$, and let
$g_i : X_i \to [0, \infty]$ be measurable functions. For a finite set $s \subseteq \iota$ and a
point $x \in \prod_i X_i$, integrating $y \mapsto \prod_{i \in \iota} g_i(y_i)$ over the
coordinates $y_i$ with $i \in s$, each against $\mu_i$, while the other coordinates are fixed to
those of $x$, gives $\left(\prod_{i \in s} \int g_i \, d\mu_i\right) \cdot
\prod_{i \notin s} g_i(x_i)$.

Formalized by `MeasureTheory.lmarginal_prod`, a theorem declared in [MathlibExt/MeasureTheory/Measure/PiWithDensity.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/PiWithDensity.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/products-of-measures-with-densities/index.html#lmarginal-prod).

## Tonelli for products

Let $\mu_i$ be σ-finite measures on measurable spaces $X_i$,
indexed by a finite type $\iota$, and let $g_i : X_i \to [0, \infty]$ be measurable functions.
Then the integral of $y \mapsto \prod_{i \in \iota} g_i(y_i)$ with respect to the product measure
$\prod_i \mu_i$ equals $\prod_{i \in \iota} \int g_i \, d\mu_i$.

Formalized by `MeasureTheory.lintegral_fintype_prod_eq_prod`, a theorem declared in [MathlibExt/MeasureTheory/Measure/PiWithDensity.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/PiWithDensity.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/products-of-measures-with-densities/index.html#lintegral-fintype-prod-eq-prod).

## A product of measures with densities

Let $\mu_i$ be σ-finite measures on measurable
spaces $X_i$, indexed by a finite type $\iota$, and let $f_i : X_i \to [0, \infty]$ be measurable
functions such that, for each $i$, the measure $f_i \mu_i$ with density $f_i$ with respect to
$\mu_i$ is σ-finite. Then the product measure $\prod_i f_i \mu_i$ equals the measure with density
$y \mapsto \prod_{i \in \iota} f_i(y_i)$ with respect to the product measure $\prod_i \mu_i$.

The σ-finiteness of the weighted measures guarantees that their product measure is characterized
on boxes.

Formalized by `MeasureTheory.Measure.pi_withDensity`, a theorem declared in [MathlibExt/MeasureTheory/Measure/PiWithDensity.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/PiWithDensity.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/products-of-measures-with-densities/index.html#pi-with-density).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of measures with densities](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/products-of-measures-with-densities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/integration/products-of-measures-with-densities)
