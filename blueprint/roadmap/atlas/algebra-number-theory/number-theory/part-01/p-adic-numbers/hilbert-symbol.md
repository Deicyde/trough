---
declaration: section
origin: cited
lean: HilbertSymbol.IsSolvable, hilbertSymbol, hilbertSymbol.eq_one_or_neg_one, padicHilbertSymbol, padicHilbertSymbol.eq_one_iff, padicHilbertSymbol.eq_neg_one_iff, padicHilbertSymbol.eq_one_or_neg_one, HilbertSymbol.diagonal_unit_isotropic
statement: formalized
proof: formalized
---

# Hilbert symbol

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html).

## Solvability of $ax^2 + by^2 = 1$

For a field $F$ and nonzero elements $a, b \in F$, the
equation $ax^2 + by^2 = 1$ is solvable over $F$ if there exist $x, y \in F$ with
$ax^2 + by^2 = 1$.

Formalized by `HilbertSymbol.IsSolvable`, a definition declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#is-solvable).

## Hilbert symbol of a field

For a field $F$ and nonzero elements $a, b \in F$, the Hilbert
symbol $(a, b)_F$ is the integer $1$ if there exist $x, y \in F$ with $ax^2 + by^2 = 1$, and $-1$
otherwise.

Formalized by `hilbertSymbol`, a definition declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#hilbert-symbol).

## The Hilbert symbol of a field is $\pm 1$

For every field $F$ and all nonzero
$a, b \in F$, the Hilbert symbol $(a, b)_F$ of $a$ and $b$ over $F$ equals $1$ or $-1$.

Formalized by `hilbertSymbol.eq_one_or_neg_one`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-one-or-neg-one).

## The $p$-adic Hilbert symbol

For a prime $p$ and nonzero $a, b \in \mathbb{Q}_p$, the
$p$-adic Hilbert symbol $(a, b)_p$ is the integer $1$ if there exist $x, y \in \mathbb{Q}_p$ with
$ax^2 + by^2 = 1$, and $-1$ otherwise.

Formalized by `padicHilbertSymbol`, a definition declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#padic-hilbert-symbol).

## When the $p$-adic Hilbert symbol is $1$

For a prime $p$ and nonzero
$a, b \in \mathbb{Q}_p$, the $p$-adic Hilbert symbol $(a, b)_p$ equals $1$ if and only if there
exist $x, y \in \mathbb{Q}_p$ with $ax^2 + by^2 = 1$.

Formalized by `padicHilbertSymbol.eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-one-iff).

## When the $p$-adic Hilbert symbol is $-1$

For a prime $p$ and nonzero
$a, b \in \mathbb{Q}_p$, the $p$-adic Hilbert symbol $(a, b)_p$ equals $-1$ if and only if there
are no $x, y \in \mathbb{Q}_p$ with $ax^2 + by^2 = 1$.

Formalized by `padicHilbertSymbol.eq_neg_one_iff`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-neg-one-iff).

## The $p$-adic Hilbert symbol is $\pm 1$

For a prime $p$ and all nonzero
$a, b \in \mathbb{Q}_p$, the $p$-adic Hilbert symbol $(a, b)_p$ equals $1$ or $-1$.

Formalized by `padicHilbertSymbol.eq_one_or_neg_one`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-one-or-neg-one-2).

## Unit diagonal forms in at least three variables over $\mathbb{Q}_p$ are isotropic for odd $p$

**Unit diagonal forms in at least three variables over $\mathbb{Q}_p$ are isotropic for odd
$p$.** Let $p$ be an odd prime, let $n > 2$, and let $a_1, \dots, a_n$ be units of $\mathbb{Z}_p$.
Then there is a nonzero vector $(x_1, \dots, x_n) \in \mathbb{Q}_p^n$ with
$a_1 x_1^2 + \dots + a_n x_n^2 = 0$.

## Sources

- ArithmeticGeometry:75.

Formalized by `HilbertSymbol.diagonal_unit_isotropic`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Isotropic.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Isotropic.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#diagonal-unit-isotropic).

## Real Hilbert symbol

For nonzero real numbers $a$ and $b$, the real Hilbert symbol of $a$
and $b$ is the integer $1$ if there are real numbers $x, y$ with $a x^2 + b y^2 = 1$, and the
integer $-1$ otherwise.

Formalized by `realHilbertSymbol`, a definition declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#real-hilbert-symbol).

## Real Hilbert symbol equal to $1$

For nonzero real numbers $a$ and $b$, the real Hilbert
symbol of $a$ and $b$ equals $1$ if and only if there are real numbers $x, y$ with
$a x^2 + b y^2 = 1$.

Formalized by `realHilbertSymbol.eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-one-iff-2).

## Real Hilbert symbol equal to $-1$

For nonzero real numbers $a$ and $b$, the real Hilbert
symbol of $a$ and $b$ equals $-1$ if and only if there are no real numbers $x, y$ with
$a x^2 + b y^2 = 1$.

Formalized by `realHilbertSymbol.eq_neg_one_iff`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-neg-one-iff-2).

## Sign rule for the real Hilbert symbol

For nonzero real numbers $a$ and $b$, the real
Hilbert symbol of $a$ and $b$ equals $-1$ if and only if $a < 0$ and $b < 0$.

Formalized by `realHilbertSymbol.eq_neg_one_iff_both_neg`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-neg-one-iff-both-neg).

## The real Hilbert symbol is $\pm 1$

For nonzero real numbers $a$ and $b$, the real Hilbert
symbol of $a$ and $b$ equals $1$ or $-1$.

Formalized by `realHilbertSymbol.eq_one_or_neg_one`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Real.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#eq-one-or-neg-one-3).

## Inclusion of $p$-adic integer units

For a prime $p$, this is the map from the units of
$\mathbb{Z}_p$ to the units of $\mathbb{Q}_p$ induced by the inclusion
$\mathbb{Z}_p \subseteq \mathbb{Q}_p$.

Formalized by `HilbertSymbol.unitZpToQp`, a definition declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#unit-zp-to-qp).

## Value of the inclusion of $p$-adic integer units

For a prime $p$ and a unit $u$ of
$\mathbb{Z}_p$, the image of $u$ under the inclusion of the units of $\mathbb{Z}_p$ into the units
of $\mathbb{Q}_p$, viewed as an element of $\mathbb{Q}_p$, equals $u$ viewed as an element of
$\mathbb{Q}_p$.

Formalized by `HilbertSymbol.unitZpToQp_coe`, a lemma declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#unit-zp-to-qp-coe).

## For odd $p$, a binary unit form over $\mathbb{Z}_p$ represents a unit square

Let $p$ be an
odd prime and let $u, v$ be units of $\mathbb{Z}_p$. Then there are $x_0, y_0 \in \mathbb{Z}_p$ and
a unit $z_0$ of $\mathbb{Z}_p$ with $z_0^2 = u x_0^2 + v y_0^2$.

## Sources

- Lemma 10.5, key step.

Formalized by `HilbertSymbol.chevalley_warning_hensel_lift`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#chevalley-warning-hensel-lift).

## The Hilbert symbol of two $p$-adic units is trivial for odd $p$

Let $p$ be an odd prime
and let $u, v$ be units of $\mathbb{Z}_p$. Then the $p$-adic Hilbert symbol of $u$ and $v$, viewed
as units of $\mathbb{Q}_p$, equals $1$.

## Sources

- Lemma 10.5.

Formalized by `HilbertSymbol.hilbert_symbol_units_eq_one_of_odd`, a theorem declared in [MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/HilbertSymbol/Units.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html#hilbert-symbol-units-eq-one-of-odd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert symbol](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/p-adic-numbers/hilbert-symbol)
