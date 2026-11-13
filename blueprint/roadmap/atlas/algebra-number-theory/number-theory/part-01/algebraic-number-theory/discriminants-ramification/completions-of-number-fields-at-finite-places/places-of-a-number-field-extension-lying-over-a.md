---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.placesOver, IsDedekindDomain.HeightOneSpectrum.placesOverEquivPrimesOver
statement: formalized
proof: formalized
---

# Places of a number field extension lying over a fixed finite place

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/places-of-a-number-field-extension-lying-over-a/index.html).

## Finite places lying over a finite place

Let $L/K$ be an extension of number fields and
let $v$ be a finite place of $K$, given as a height-one prime of the ring of integers
$\mathcal{O}_K$. The finite places of $L$ lying over $v$ form the type of height-one primes $w$ of
$\mathcal{O}_L$ that lie over $v$, that is, whose preimage in $\mathcal{O}_K$ is $v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.placesOver`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOver.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOver.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/places-of-a-number-field-extension-lying-over-a/index.html#places-over).

## Places over a finite place correspond to primes over it

Let $L/K$ be an extension of
number fields and let $v$ be a finite place of $K$, given as a height-one prime of the ring of
integers $\mathcal{O}_K$. Sending a finite place $w$ of $L$ lying over $v$ to its prime ideal of
$\mathcal{O}_L$ is a bijection from the finite places of $L$ lying over $v$ onto the set of prime
ideals of $\mathcal{O}_L$ lying over $v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.placesOverEquivPrimesOver`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOver.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOver.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/places-of-a-number-field-extension-lying-over-a/index.html#places-over-equiv-primes-over).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Places of a number field extension lying over a fixed finite place](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/places-of-a-number-field-extension-lying-over-a/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/places-of-a-number-field-extension-lying-over-a)
