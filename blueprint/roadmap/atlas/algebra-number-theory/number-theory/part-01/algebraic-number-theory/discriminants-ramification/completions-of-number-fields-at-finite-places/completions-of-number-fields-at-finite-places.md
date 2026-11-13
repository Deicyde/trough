---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.finrank_adicCompletion_le, IsDedekindDomain.HeightOneSpectrum.comap_maximalIdeal_adicCompletionIntegersMap, IsDedekindDomain.HeightOneSpectrum.inertiaDeg_adicCompletionIntegersMap, IsDedekindDomain.HeightOneSpectrum.finrank_adicCompletion_eq_ramificationIdx_mul_inertiaDeg, IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersMap_algebraMap
statement: formalized
proof: formalized
---

# Completions of number fields at finite places: its own results

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html).

## Local degree is at most the global degree

Let $L/K$ be an extension of number fields,
let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ (a finite place of $K$) and let $w$ be a
nonzero prime ideal of $\mathcal{O}_L$ lying over $v$. Regard the $w$-adic completion $L_w$ as
an algebra over the $v$-adic completion $K_v$ via the canonical map $K_v \to L_w$. Then the
dimension of $L_w$ over $K_v$ is at most $[L : K]$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.finrank_adicCompletion_le`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverDegreeBound.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverDegreeBound.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html#finrank-adic-completion-le).

## Maximal ideals of completed integer rings lie over each other

Let $L/K$ be an extension
of number fields, let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime
ideal of $\mathcal{O}_L$ lying over $v$. Let $\mathcal{O}_{K_v}$ and $\mathcal{O}_{L_w}$ be the
rings of integers of the completions $K_v$ and $L_w$. Then the preimage of the maximal ideal of
$\mathcal{O}_{L_w}$ under the canonical map $\mathcal{O}_{K_v} \to \mathcal{O}_{L_w}$ is the
maximal ideal of $\mathcal{O}_{K_v}$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.comap_maximalIdeal_adicCompletionIntegersMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverMaximalIdeal.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverMaximalIdeal.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html#comap-maximal-ideal-adic-completion-inte).

## Completion preserves the inertia degree

Let $L/K$ be an extension of number fields, let
$v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero prime ideal of $\mathcal{O}_L$
lying over $v$. Let $\mathcal{O}_{K_v}$ and $\mathcal{O}_{L_w}$ be the rings of integers of the
completions $K_v$ and $L_w$, with $\mathcal{O}_{L_w}$ an algebra over $\mathcal{O}_{K_v}$ via the
canonical map. Then the inertia degree of the maximal ideal of $\mathcal{O}_{L_w}$ over
$\mathcal{O}_{K_v}$ equals the inertia degree of $w$ over $v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.inertiaDeg_adicCompletionIntegersMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverInertiaDegree.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverInertiaDegree.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html#inertia-deg-adic-completion-integers-map).

## The local degree is the product of ramification index and inertia degree

Let $L/K$ be an
extension of number fields, let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ (a finite place of
$K$) and $w$ a nonzero prime ideal of $\mathcal{O}_L$ lying over $v$. Regard the completion $L_w$
as an algebra over $K_v$ via the canonical map $K_v \to L_w$. Then the dimension of $L_w$ over
$K_v$ equals $e(w \mid v) \, f(w \mid v)$, the ramification index of $w$ over $v$ times the
inertia degree of $w$ over $v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.finrank_adicCompletion_eq_ramificationIdx_mul_inertiaDeg`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverLocalDegree.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverLocalDegree.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html#finrank-adic-completion-eq-ramification).

## The completed integer map is compatible with the rings of integers

Let $L/K$ be an
extension of number fields, let $v$ be a nonzero prime ideal of $\mathcal{O}_K$ and $w$ a nonzero
prime ideal of $\mathcal{O}_L$ lying over $v$. Let $\mathcal{O}_{K_v}$ and $\mathcal{O}_{L_w}$ be
the rings of integers of the completions $K_v$ and $L_w$. For every $a \in \mathcal{O}_K$, the
canonical map $\mathcal{O}_{K_v} \to \mathcal{O}_{L_w}$ sends the image of $a$ in
$\mathcal{O}_{K_v}$ to the image in $\mathcal{O}_{L_w}$ of the image of $a$ in $\mathcal{O}_L$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersMap_algebraMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueField.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FiniteLiesOverResidueField.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html#adic-completion-integers-map-algebra-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Completions of number fields at finite places](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places)
