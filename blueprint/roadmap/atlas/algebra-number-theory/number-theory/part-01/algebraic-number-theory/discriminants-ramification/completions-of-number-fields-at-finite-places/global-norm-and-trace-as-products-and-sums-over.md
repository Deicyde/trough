---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.algebraMap_norm_eq_prod_adicCompletion, IsDedekindDomain.HeightOneSpectrum.algebraMap_trace_eq_sum_adicCompletion
statement: formalized
proof: formalized
---

# Global norm and trace as products and sums over finite-place completions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/global-norm-and-trace-as-products-and-sums-over/index.html).

## Global norm as a product of local norms

Let $L/K$ be an extension of number fields, let
$v$ be a finite place of $K$, given as a height-one prime of the ring of integers $\mathcal{O}_K$,
and let $K_v$ be the completion of $K$ at $v$. For each of the finitely many finite places $w$ of
$L$ lying over $v$, regard the completion $L_w$ as a $K_v$-algebra through the continuous ring
homomorphism $K_v \to L_w$ extending $K \to L$. Then for every $\alpha \in L$, the image of the
norm $N_{L/K}(\alpha)$ in $K_v$ equals $\prod_{w \mid v} N_{L_w/K_v}(\alpha)$, where $\alpha$ is
viewed in $L_w$ and the product runs over the finite places $w$ of $L$ lying over $v$.

## Sources

- Corollary 11.24, norm part.

Formalized by `IsDedekindDomain.HeightOneSpectrum.algebraMap_norm_eq_prod_adicCompletion`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverNormTrace.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverNormTrace.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/global-norm-and-trace-as-products-and-sums-over/index.html#algebra-map-norm-eq-prod-adic-completion).

## Global trace as a sum of local traces

Let $L/K$ be an extension of number fields, let
$v$ be a finite place of $K$, given as a height-one prime of the ring of integers $\mathcal{O}_K$,
and let $K_v$ be the completion of $K$ at $v$. For each of the finitely many finite places $w$ of
$L$ lying over $v$, regard the completion $L_w$ as a $K_v$-algebra through the continuous ring
homomorphism $K_v \to L_w$ extending $K \to L$. Then for every $\alpha \in L$, the image of the
trace $\operatorname{Tr}_{L/K}(\alpha)$ in $K_v$ equals
$\sum_{w \mid v} \operatorname{Tr}_{L_w/K_v}(\alpha)$, where $\alpha$ is viewed in $L_w$ and the
sum runs over the finite places $w$ of $L$ lying over $v$.

## Sources

- Corollary 11.24, trace part.

Formalized by `IsDedekindDomain.HeightOneSpectrum.algebraMap_trace_eq_sum_adicCompletion`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverNormTrace.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverNormTrace.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/global-norm-and-trace-as-products-and-sums-over/index.html#algebra-map-trace-eq-sum-adic-completion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Global norm and trace as products and sums over finite-place completions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/global-norm-and-trace-as-products-and-sums-over/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/global-norm-and-trace-as-products-and-sums-over)
