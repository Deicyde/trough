---
declaration: section
origin: cited
lean: AbsoluteValue.isNonarchimedean_of_charP, AbsoluteValue.eq_one_of_ne_zero_of_finite, AbsoluteValue.inducedTopology, AbsoluteValue.inducedTopology_eq_iff_isEquiv, AbsoluteValue.isNonarchimedean_iff_natCast_le_one, AbsoluteValue.isNonarchimedean_of_natCast_le_one, AbsoluteValue.isNonarchimedean_iff_natCast_le_one_of_pos, AbsoluteValue.rpow
statement: formalized
proof: formalized
---

# Absolute values on fields

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html).

## Absolute values in positive characteristic are nonarchimedean

Let $K$ be a field of
characteristic $p > 0$. Then every real-valued absolute value $v$ on $K$ is nonarchimedean:
$v(x + y) \le \max(v(x), v(y))$ for all $x, y \in K$.

Formalized by `AbsoluteValue.isNonarchimedean_of_charP`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/FiniteField.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/FiniteField.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#is-nonarchimedean-of-char-p).

## Absolute values on finite fields are trivial

Let $K$ be a finite field and $v$ a
real-valued absolute value on $K$. Then $v(x) = 1$ for every nonzero $x \in K$.

Formalized by `AbsoluteValue.eq_one_of_ne_zero_of_finite`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/FiniteField.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/FiniteField.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#eq-one-of-ne-zero-of-finite).

## Topology induced by an absolute value

Let $K$ be a field and $v$ a real-valued absolute
value on $K$. The topology induced by $v$ on $K$ is the topology pulled back along the identity
map from $K$ to $K$ equipped with the norm $v$; equivalently, it is the metric topology of the
distance $d(x, y) = v(x - y)$ on $K$.

Formalized by `AbsoluteValue.inducedTopology`, a definition declared in [MathlibExt/Analysis/AbsoluteValue/InducedTopology.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/InducedTopology.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#induced-topology).

## Absolute values inducing the same topology are equivalent

Let $K$ be a field and
$v$, $w$ real-valued absolute values on $K$. The topologies induced on $K$ by $v$ and by $w$
are equal if and only if $v$ and $w$ are equivalent.

This is about equality of the induced topologies on $K$, not about equality
of the absolute values themselves: inequivalent absolute values may still agree
on many elements while inducing different topologies.

Formalized by `AbsoluteValue.inducedTopology_eq_iff_isEquiv`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/InducedTopology.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/InducedTopology.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#induced-topology-eq-iff-is-equiv).

## Nonarchimedean criterion for absolute values

Let $K$ be a field and $v$ a real-valued
absolute value on $K$. Then $v$ is nonarchimedean, that is, $v(x + y) \le \max(v(x), v(y))$ for
all $x, y \in K$, if and only if $v(n) \le 1$ for every natural number $n$, viewed as the element
$n \cdot 1$ of $K$.

## Sources

- ATLAS NumberTheoryI, Section 1.2, Lemma 1.4.

Formalized by `AbsoluteValue.isNonarchimedean_iff_natCast_le_one`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/Nonarchimedean.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/Nonarchimedean.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#is-nonarchimedean-iff-nat-cast-le-one).

## Absolute values bounded by one on the natural numbers are nonarchimedean

Let $K$ be a field and $v$ a real-valued absolute value on $K$. If $v(n) \le 1$ for every natural
number $n$, viewed as the element $n \cdot 1$ of $K$, then $v$ is nonarchimedean:
$v(x + y) \le \max(v(x), v(y))$ for all $x, y \in K$.

## Sources

- ATLAS NumberTheoryI, Section 1.2, backward direction of Lemma 1.4.

Formalized by `AbsoluteValue.isNonarchimedean_of_natCast_le_one`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/Nonarchimedean.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/Nonarchimedean.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#is-nonarchimedean-of-nat-cast-le-one).

## Nonarchimedean criterion using positive integers

Let $K$ be a field and $v$ a real-valued
absolute value on $K$. Then $v$ is nonarchimedean, that is, $v(x + y) \le \max(v(x), v(y))$ for
all $x, y \in K$, if and only if $v(n) \le 1$ for every positive integer $n$, viewed as the
element $n \cdot 1$ of $K$.

The case $n = 0$ may be omitted because $v(0) = 0 \le 1$.

## Sources

- ATLAS NumberTheoryI, Section 1.2, Lemma 1.4 (in the book's form).

Formalized by `AbsoluteValue.isNonarchimedean_iff_natCast_le_one_of_pos`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/Nonarchimedean.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/Nonarchimedean.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#is-nonarchimedean-iff-nat-cast-le-one-of).

## Powers of an absolute value

Let $R$ be a semiring, $v$ a real-valued absolute value
on $R$ and $c$ a real number with $0 < c \le 1$. The $c$-th power of $v$ is the real-valued
absolute value $x \mapsto v(x)^c$ on $R$.

Formalized by `AbsoluteValue.rpow`, a definition declared in [MathlibExt/Analysis/AbsoluteValue/Rpow.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/Rpow.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#rpow).

## Values of a power of an absolute value

Let $R$ be a semiring, $v$ a real-valued
absolute value on $R$ and $c$ a real number with $0 < c \le 1$. The $c$-th power of $v$ takes
the value $v(x)^c$ at every $x \in R$.

Formalized by `AbsoluteValue.rpow_apply`, a theorem declared in [MathlibExt/Analysis/AbsoluteValue/Rpow.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/AbsoluteValue/Rpow.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html#rpow-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Absolute values on fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/p-adic-numbers/absolute-values-on-fields)
