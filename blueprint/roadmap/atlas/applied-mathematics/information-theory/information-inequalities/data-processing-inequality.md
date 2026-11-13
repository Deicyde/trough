---
declaration: section
origin: cited
lean: InformationTheory.measureMutualInformation_map_swap, InformationTheory.measureMutualInformation_comp_le, InformationTheory.measureMutualInformation_map_le
statement: formalized
proof: formalized
---

# Data-processing inequality

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/data-processing-inequality/index.html).

## Symmetry of mutual information

`I(Y; X) = I(X; Y)`.

Formalized by `InformationTheory.measureMutualInformation_map_swap`, a theorem declared in [MathlibExt/InformationTheory/MutualInformationDPI.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/MutualInformationDPI.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/data-processing-inequality/index.html#measure-mutual-information-map-swap).

## Data-processing inequality

If `Z` is produced from `Y` by a channel `κ` that does not see
`X` (a Markov chain `X → Y → Z`), then `I(X; Z) ≤ I(X; Y)`. The joint law of `(X, Z)` is
`(Kernel.id ∥ₖ κ) ∘ₘ μ`.

Formalized by `InformationTheory.measureMutualInformation_comp_le`, a theorem declared in [MathlibExt/InformationTheory/MutualInformationDPI.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/MutualInformationDPI.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/data-processing-inequality/index.html#measure-mutual-information-comp-le).

## Processing cannot increase information

`I(X; g(Y)) ≤ I(X; Y)` for a measurable `g`.

Formalized by `InformationTheory.measureMutualInformation_map_le`, a theorem declared in [MathlibExt/InformationTheory/MutualInformationDPI.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/MutualInformationDPI.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/data-processing-inequality/index.html#measure-mutual-information-map-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Data-processing inequality](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/data-processing-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/information-inequalities/data-processing-inequality)
