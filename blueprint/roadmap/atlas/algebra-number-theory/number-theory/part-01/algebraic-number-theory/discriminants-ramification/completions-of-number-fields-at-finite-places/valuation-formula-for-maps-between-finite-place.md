---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.valuation_adicCompletionMap, IsDedekindDomain.HeightOneSpectrum.adicCompletionMap_mem_integers, IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersMap
statement: formalized
proof: formalized
---

# Valuation formula for maps between finite-place completions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/valuation-formula-for-maps-between-finite-place/index.html).

## Valuation of the image under the completion map

Let $L/K$ be an extension of number
fields, let $v$ be a finite place of $K$, given as a height-one prime of the ring of integers
$\mathcal{O}_K$, let $w$ be a finite place of $L$ lying over $v$, and let $e$ be the ramification
index of $w$ over $v$. Let $\iota : K_v \to L_w$ be the continuous ring homomorphism between the
completions that extends $K \to L$. Then for every $x \in K_v$, the valuation of $\iota(x)$ on
$L_w$ equals the $e$-th power of the valuation of $x$ on $K_v$, where both valuations are the
multiplicative adic valuations extended to the completions.

Formalized by `IsDedekindDomain.HeightOneSpectrum.valuation_adicCompletionMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverValuation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverValuation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/valuation-formula-for-maps-between-finite-place/index.html#valuation-adic-completion-map).

## The completion map preserves integrality

Let $L/K$ be an extension of number fields, let
$v$ be a finite place of $K$, given as a height-one prime of the ring of integers $\mathcal{O}_K$,
and let $w$ be a finite place of $L$ lying over $v$. The continuous ring homomorphism
$K_v \to L_w$ between the completions that extends $K \to L$ maps every element of the ring of
integers of $K_v$ into the ring of integers of $L_w$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.adicCompletionMap_mem_integers`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverValuation.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverValuation.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/valuation-formula-for-maps-between-finite-place/index.html#adic-completion-map-mem-integers).

## Restriction of the completion map to the rings of integers

Let $L/K$ be an extension of
number fields, let $v$ be a finite place of $K$, given as a height-one prime of the ring of
integers $\mathcal{O}_K$, and let $w$ be a finite place of $L$ lying over $v$. Let $K_v$ and $L_w$
be the completions, with rings of integers $\mathcal{O}_v$ and $\mathcal{O}_w$. The continuous
ring homomorphism $K_v \to L_w$ extending $K \to L$ restricts to a ring homomorphism
$\mathcal{O}_v \to \mathcal{O}_w$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverValuation.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverValuation.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/valuation-formula-for-maps-between-finite-place/index.html#adic-completion-integers-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Valuation formula for maps between finite-place completions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/valuation-formula-for-maps-between-finite-place/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/valuation-formula-for-maps-between-finite-place)
