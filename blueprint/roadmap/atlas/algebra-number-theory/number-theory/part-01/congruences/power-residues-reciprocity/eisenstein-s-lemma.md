---
declaration: section
origin: cited
lean: MetaMathlibExt.eisenstein_lemma_jacobi_symbol_general, MetaMathlibExt.eisenstein_lemma_jacobi_symbol
statement: formalized
proof: formalized
---

# Eisenstein's lemma

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/eisenstein-s-lemma/index.html).

## Eisenstein's lemma for Jacobi symbols (odd coprime form)

Let $a$ and $b$ be odd natural
numbers that are coprime. Then the Jacobi symbol $\left(\frac{a}{b}\right)$ equals $(-1)^{S}$,
where $S = \sum_{i=1}^{(b-1)/2} \lfloor ia/b \rfloor$.

Formalized by `MetaMathlibExt.eisenstein_lemma_jacobi_symbol_general`, a theorem declared in [MathlibExt/NumberTheory/LegendreSymbol/EisensteinJacobiSymbol.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LegendreSymbol/EisensteinJacobiSymbol.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/eisenstein-s-lemma/index.html#eisenstein-lemma-jacobi-symbol-general).

## Eisenstein's lemma for Jacobi symbols

Let $a$ and $b$ be positive odd natural numbers that
are coprime. Then the Jacobi symbol $\left(\frac{a}{b}\right)$ equals $(-1)^{S}$, where
$S = \sum_{i=1}^{(b-1)/2} \lfloor ia/b \rfloor$.

## Sources

- Damanvir Singh Binner, "Generalization of a Result of Sylvester Related to the Frobenius Coin Problem", Journal of Integer Sequences 24 (2021), Article 21.8.4, Theorem `Eisenstein`, lines 272-278, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Binner/binner13.tex>. It follows from `eisenstein_lemma_jacobi_symbol_general`; the hypotheses `ha_pos` and `hb_pos` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.eisenstein_lemma_jacobi_symbol`, a theorem declared in [MathlibExt/NumberTheory/LegendreSymbol/EisensteinJacobiSymbol.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LegendreSymbol/EisensteinJacobiSymbol.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/eisenstein-s-lemma/index.html#eisenstein-lemma-jacobi-symbol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eisenstein's lemma](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/eisenstein-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/power-residues-reciprocity/eisenstein-s-lemma)
