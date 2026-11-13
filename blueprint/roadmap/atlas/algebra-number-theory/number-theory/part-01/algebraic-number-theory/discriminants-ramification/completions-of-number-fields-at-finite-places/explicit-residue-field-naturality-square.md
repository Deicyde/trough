---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.ringOfIntegersResidueQuotientMap, IsDedekindDomain.HeightOneSpectrum.adicCompletionResidueQuotientMap, IsDedekindDomain.HeightOneSpectrum.completionResidueFieldEquiv_naturality
statement: formalized
proof: formalized
---

# Explicit residue-field naturality square

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/explicit-residue-field-naturality-square/index.html).

## Residue map of rings of integers

Let $L/K$ be an extension of number fields, let $v$ be
a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime ideal of $\mathcal{O}_L$ lying
over $v$. This is the ring homomorphism $\mathcal{O}_K/v \to \mathcal{O}_L/w$ induced by the
canonical map $\mathcal{O}_K \to \mathcal{O}_L$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.ringOfIntegersResidueQuotientMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueNaturality.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueNaturality.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/explicit-residue-field-naturality-square/index.html#ring-of-integers-residue-quotient-map).

## Residue map of completed integer rings

Let $L/K$ be an extension of number fields, let
$v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime ideal of $\mathcal{O}_L$
lying over $v$. Let $\mathcal{O}_{K_v}$ and $\mathcal{O}_{L_w}$ be the rings of integers of the
completions $K_v$ and $L_w$, with maximal ideals $\mathfrak{m}_v$ and $\mathfrak{m}_w$. This is
the ring homomorphism $\mathcal{O}_{K_v}/\mathfrak{m}_v \to \mathcal{O}_{L_w}/\mathfrak{m}_w$
induced by the canonical map $\mathcal{O}_{K_v} \to \mathcal{O}_{L_w}$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.adicCompletionResidueQuotientMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueNaturality.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueNaturality.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/explicit-residue-field-naturality-square/index.html#adic-completion-residue-quotient-map).

## Naturality of the residue field identifications

Let $L/K$ be an extension of number
fields, let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime ideal of
$\mathcal{O}_L$ lying over $v$. Let $\mathcal{O}_{K_v}$ and $\mathcal{O}_{L_w}$ be the rings of
integers of the completions $K_v$ and $L_w$, with maximal ideals $\mathfrak{m}_v$ and
$\mathfrak{m}_w$. Then the two maps $\mathcal{O}_{K_v}/\mathfrak{m}_v \to \mathcal{O}_L/w$ agree:
the residue field isomorphism $\mathcal{O}_{K_v}/\mathfrak{m}_v \cong \mathcal{O}_K/v$ followed by
the map $\mathcal{O}_K/v \to \mathcal{O}_L/w$ induced by $\mathcal{O}_K \to \mathcal{O}_L$, and
the map $\mathcal{O}_{K_v}/\mathfrak{m}_v \to \mathcal{O}_{L_w}/\mathfrak{m}_w$ induced by the
canonical map $\mathcal{O}_{K_v} \to \mathcal{O}_{L_w}$ followed by the residue field isomorphism
$\mathcal{O}_{L_w}/\mathfrak{m}_w \cong \mathcal{O}_L/w$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionResidueFieldEquiv_naturality`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueNaturality.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueNaturality.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/explicit-residue-field-naturality-square/index.html#completion-residue-field-equiv-naturalit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Explicit residue-field naturality square](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/explicit-residue-field-naturality-square/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/explicit-residue-field-naturality-square)
