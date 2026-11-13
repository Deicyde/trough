---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersMap_injective, IsDedekindDomain.HeightOneSpectrum.ramificationIdx_adicCompletionIntegersMap
statement: formalized
proof: formalized
---

# Ramification index under finite-place completion

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/ramification-index-under-finite-place-completion/index.html).

## The map of completed integer rings is injective

Let $L/K$ be an extension of number
fields, let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime ideal of
$\mathcal{O}_L$ lying over $v$. Then the canonical map $\mathcal{O}_{K_v} \to \mathcal{O}_{L_w}$
from the ring of integers of the completion $K_v$ to the ring of integers of the completion $L_w$
is injective.

Formalized by `IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersMap_injective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverRamificationIndex.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverRamificationIndex.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/ramification-index-under-finite-place-completion/index.html#adic-completion-integers-map-injective).

## Completion preserves the ramification index

Let $L/K$ be an extension of number fields,
let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime ideal of
$\mathcal{O}_L$ lying over $v$. Let $\mathcal{O}_{K_v}$ and $\mathcal{O}_{L_w}$ be the rings of
integers of the completions $K_v$ and $L_w$, with $\mathcal{O}_{L_w}$ an algebra over
$\mathcal{O}_{K_v}$ via the canonical map. Then the ramification index of the maximal ideal of
$\mathcal{O}_{L_w}$ over $\mathcal{O}_{K_v}$ equals the ramification index of $w$ over $v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.ramificationIdx_adicCompletionIntegersMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverRamificationIndex.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverRamificationIndex.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/ramification-index-under-finite-place-completion/index.html#ramification-idx-adic-completion-integer).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramification index under finite-place completion](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/ramification-index-under-finite-place-completion/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/ramification-index-under-finite-place-completion)
