---
declaration: section
origin: cited
lean: Ideal.absNorm_discriminantIdeal, NumberField.pow_div_factorial_sq_mul_pi_div_four_pow_gt, NumberField.middle_term_le_abs_discr, NumberField.abs_discr_gt_exp_term, latticeDiscriminantSet, latticeDiscriminant, latticeDiscriminant_le_span_singleton, latticeDiscriminant_isFractional
statement: formalized
proof: formalized
---

# Discriminants of number fields

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html).

## Absolute norm of the discriminant ideal of a number field

Let $K$ be a number
field with ring of integers $\mathcal{O}_K$ and discriminant $d_K$. The absolute norm of the
discriminant ideal of $\mathcal{O}_K$ over $\mathbb{Z}$ equals $|d_K|$.

Formalized by `Ideal.absNorm_discriminantIdeal`, a theorem declared in [MathlibExt/NumberTheory/NumberField/DiscriminantIdeal.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/DiscriminantIdeal.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#abs-norm-discriminant-ideal).

## Comparison of the Minkowski and exponential discriminant bounds

Let $n$ and $s$ be
natural numbers with $n \ne 0$ and $2s \le n$, and let $e$ be Euler's number. Then

$$\frac{1}{e^2 n} \left(\frac{\pi e^2}{4}\right)^n <
\left(\frac{n^n}{n!}\right)^2 \left(\frac{\pi}{4}\right)^{2s}.$$

## Sources

- ATLAS `NumberTheoryI` Corollary 14.26 (second inequality), with $n$ the degree of a number field and $s$ its number of complex places.

Formalized by `NumberField.pow_div_factorial_sq_mul_pi_div_four_pow_gt`, a theorem declared in [MathlibExt/NumberTheory/NumberField/DiscriminantLowerBound.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/DiscriminantLowerBound.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#pow-div-factorial-sq-mul-pi-div-four-pow).

## Minkowski's lower bound for the discriminant

Let $K$ be a number field of degree
$n = [K : \mathbb{Q}]$ with $s$ complex places and discriminant $d_K$. Then

$$|d_K| \ge \left(\frac{n^n}{n!}\right)^2 \left(\frac{\pi}{4}\right)^{2s}.$$

## Sources

- ATLAS `NumberTheoryI` Corollary 14.26 (first inequality); this is Mathlib's `NumberField.abs_discr_ge'`, restated in the form used by the book.

Formalized by `NumberField.middle_term_le_abs_discr`, a theorem declared in [MathlibExt/NumberTheory/NumberField/DiscriminantLowerBound.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/DiscriminantLowerBound.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#middle-term-le-abs-discr).

## Exponential lower bound for the discriminant

Let $K$ be a number field of degree
$n = [K : \mathbb{Q}]$ and discriminant $d_K$, and let $e$ be Euler's number. Then

$$|d_K| > \frac{1}{e^2 n} \left(\frac{\pi e^2}{4}\right)^n,$$

so the absolute discriminant grows at least exponentially in the degree.

## Sources

- ATLAS `NumberTheoryI` Corollary 14.26 (second inequality).

Formalized by `NumberField.abs_discr_gt_exp_term`, a theorem declared in [MathlibExt/NumberTheory/NumberField/DiscriminantLowerBound.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/DiscriminantLowerBound.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#abs-discr-gt-exp-term).

## Discriminants of tuples from a submodule

Let $A$ be a commutative ring and $L/K$ a finite
extension of fields, with $A$-algebra structures on $K$ and $L$ forming a scalar tower
$A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, this is the set of all
discriminants $\operatorname{disc}_{L/K}(b_1, \dots, b_n) = \det(\operatorname{Tr}_{L/K}(b_i b_j))$
in $K$ of $n$-tuples $(b_1, \dots, b_n)$ of elements of $M$.

Formalized by `latticeDiscriminantSet`, a definition declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-set).

## Discriminant of a lattice

Let $A$ be a commutative ring and $L/K$ a finite extension of
fields, with $A$-algebra structures on $K$ and $L$ forming a scalar tower $A \to K \to L$, and let
$n = [L : K]$. The discriminant $D(M)$ of an $A$-submodule $M$ of $L$ is the $A$-submodule of $K$
generated by the discriminants
$\operatorname{disc}_{L/K}(b_1, \dots, b_n) = \det(\operatorname{Tr}_{L/K}(b_i b_j))$ of all
$n$-tuples $(b_1, \dots, b_n)$ of elements of $M$.

Formalized by `latticeDiscriminant`, a definition declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant).

## The discriminant of a lattice inside a basis lattice

Let $A$ be a commutative ring and
$L/K$ a finite extension of fields, with $A$-algebra structures on $K$ and $L$ forming a scalar
tower $A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let $D(M)$ be its
discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all $n$-tuples of
elements of $M$. If $b_1, \dots, b_n$ is a $K$-basis of $L$ and $M$ is contained in the $A$-span of
$b_1, \dots, b_n$, then $D(M) \subseteq A \cdot \operatorname{disc}_{L/K}(b_1, \dots, b_n)$.

Formalized by `latticeDiscriminant_le_span_singleton`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-le-span-singleton).

## The discriminant of a lattice inside a basis lattice is fractional

Let $A$ be a commutative
ring and $L/K$ a finite extension of fields, with $A$-algebra structures on $K$ and $L$ forming a
scalar tower $A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let $D(M)$ be
its discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all $n$-tuples
of elements of $M$. Assume $K$ is the fraction field of $A$. If $M$ is contained in the $A$-span of
a $K$-basis $b_1, \dots, b_n$ of $L$, then $D(M)$ is a fractional ideal: there is a non-zero-divisor
$a \in A$ such that $a x$ lies in the image of $A$ in $K$ for every $x \in D(M)$.

Formalized by `latticeDiscriminant_isFractional`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-is-fractional).

## The discriminant of a lattice containing a basis is nonzero

Let $A$ be a commutative ring
and $L/K$ a finite extension of fields, with $A$-algebra structures on $K$ and $L$ forming a scalar
tower $A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let $D(M)$ be its
discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all $n$-tuples of
elements of $M$. Assume $L/K$ is separable. If $M$ contains a $K$-basis $b_1, \dots, b_n$ of $L$,
then $D(M) \neq 0$.

Formalized by `latticeDiscriminant_ne_bot_of_basis`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-ne-bot-of-basis).

## The discriminant of a sandwiched lattice is a nonzero fractional ideal

Let $A$ be a
commutative ring and $L/K$ a finite extension of fields, with $A$-algebra structures on $K$ and $L$
forming a scalar tower $A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let
$D(M)$ be its discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all
$n$-tuples of elements of $M$. Assume $K$ is the fraction field of $A$ and $L/K$ is separable. If
$M$ contains a $K$-basis $b_1, \dots, b_n$ of $L$ and is contained in the $A$-span of a $K$-basis
$c_1, \dots, c_n$ of $L$, then $D(M)$ is a fractional ideal (there is a non-zero-divisor $a \in A$
such that $a x$ lies in the image of $A$ in $K$ for every $x \in D(M)$) and $D(M) \neq 0$.

Formalized by `latticeDiscriminant_isFractional_and_ne_bot`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-is-fractional-and-n).

## The discriminant of a lattice spanned by a basis

Let $A$ be a commutative ring and $L/K$ a
finite extension of fields, with $A$-algebra structures on $K$ and $L$ forming a scalar tower
$A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let $D(M)$ be its
discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all $n$-tuples of
elements of $M$. If $b_1, \dots, b_n$ is a $K$-basis of $L$, every $b_i$ lies in $M$ and $M$ is
contained in the $A$-span of $b_1, \dots, b_n$, then
$D(M) = A \cdot \operatorname{disc}_{L/K}(b_1, \dots, b_n)$.

Formalized by `latticeDiscriminant_eq_span_singleton`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-eq-span-singleton).

## Equal discriminants force equal lattices

Let $A$ be a commutative ring and $L/K$ a finite
extension of fields, with $A$-algebra structures on $K$ and $L$ forming a scalar tower
$A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let $D(M)$ be its
discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all $n$-tuples of
elements of $M$. Assume $L/K$ is separable and the map $A \to K$ is injective. Let $M' \subseteq M$
be $A$-submodules of $L$. Suppose that $b_1, \dots, b_n$ is a $K$-basis of $L$ with every $b_i$ in
$M$ and $M$ contained in the $A$-span of $b_1, \dots, b_n$, and that $b'_1, \dots, b'_n$ is a
$K$-basis of $L$ with every $b'_i$ in $M'$ and $M'$ contained in the $A$-span of
$b'_1, \dots, b'_n$. If $D(M') = D(M)$, then $M' = M$.

## Sources

- Sutherland, MIT 18.785 Number Theory I (Fall 2021), Lecture 12, Lemma 12.10.

Formalized by `latticeDiscriminant_eq_imp_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-eq-imp-eq).

## Equal discriminants force equal lattices (fraction field version)

Let $A$ be a commutative
ring and $L/K$ a finite extension of fields, with $A$-algebra structures on $K$ and $L$ forming a
scalar tower $A \to K \to L$, and let $n = [L : K]$. For an $A$-submodule $M$ of $L$, let $D(M)$ be
its discriminant, the $A$-submodule of $K$ generated by the discriminants over $K$ of all $n$-tuples
of elements of $M$. Assume $K$ is the fraction field of $A$ and $L/K$ is separable. Let
$M' \subseteq M$ be $A$-submodules of $L$. Suppose that $b_1, \dots, b_n$ is a $K$-basis of $L$ with
every $b_i$ in $M$ and $M$ contained in the $A$-span of $b_1, \dots, b_n$, and that
$b'_1, \dots, b'_n$ is a $K$-basis of $L$ with every $b'_i$ in $M'$ and $M'$ contained in the
$A$-span of $b'_1, \dots, b'_n$. If $D(M') = D(M)$, then $M' = M$.

Formalized by `latticeDiscriminant_eq_imp_eq_of_isFractionRing`, a theorem declared in [MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/LatticeDiscriminant.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#lattice-discriminant-eq-imp-eq-of-is-fra).

## Image of $B$ in $L$

Let $A$ and $B$ be commutative rings and $L$ a field, with algebra
maps $A \to B$, $B \to L$ and $A \to L$ forming a scalar tower. The image of $B$ in $L$ is the
range of the algebra map $B \to L$, regarded as an $A$-submodule of $L$.

Formalized by `imageOfB`, a definition declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#image-of-b).

## Membership in the image of $B$

Let $A$ and $B$ be commutative rings and $L$ a field,
with algebra maps $A \to B$, $B \to L$ and $A \to L$ forming a scalar tower. An element
$x \in L$ lies in the image of $B$ in $L$ if and only if $x$ is the image of some $b \in B$
under the algebra map $B \to L$.

Formalized by `mem_imageOfB`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#mem-image-of-b).

## Elements of $B$ lie in the image of $B$

Let $A$ and $B$ be commutative rings and $L$ a
field, with algebra maps $A \to B$, $B \to L$ and $A \to L$ forming a scalar tower. For every
$b \in B$, the image of $b$ under the algebra map $B \to L$ lies in the image of $B$ in $L$,
regarded as an $A$-submodule of $L$.

Formalized by `algebraMap_mem_imageOfB`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#algebra-map-mem-image-of-b).

## Extension discriminant

Let $A$ and $B$ be commutative rings and $K$ and $L$ fields with $L$
finite-dimensional over $K$, with algebra maps forming scalar towers $A \to K \to L$ and
$A \to B \to L$, and let $n = [L : K]$. The extension discriminant is the $A$-submodule of $K$
spanned by the discriminants $\operatorname{disc}_{L/K}(b_1, \dots, b_n)$ of all $n$-tuples of
elements of $L$ lying in the image of $B$ in $L$.

At this level of generality it is only an $A$-submodule of $K$, not an ideal of $A$.

Formalized by `extensionDiscriminant`, a definition declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#extension-discriminant).

## The extension discriminant is a lattice discriminant

Let $A$ and $B$ be commutative
rings and $K$ and $L$ fields with $L$ finite-dimensional over $K$, with algebra maps forming
scalar towers $A \to K \to L$ and $A \to B \to L$. The extension discriminant of the tower
equals the lattice discriminant over $A$ and $K$ of the image of $B$ in $L$, regarded as an
$A$-submodule of $L$.

Formalized by `extensionDiscriminant_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#extension-discriminant-eq).

## Discriminants of tuples from $B$ lie in the extension discriminant

Let $A$ and $B$ be
commutative rings and $K$ and $L$ fields with $L$ finite-dimensional over $K$, with algebra maps
forming scalar towers $A \to K \to L$ and $A \to B \to L$, and let $n = [L : K]$. If
$b_1, \dots, b_n \in L$ all lie in the image of $B$ in $L$, then their discriminant
$\operatorname{disc}_{L/K}(b_1, \dots, b_n)$ lies in the extension discriminant of the tower,
an $A$-submodule of $K$.

Formalized by `discr_mem_extensionDiscriminant`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminant.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#discr-mem-extension-discriminant).

## Localization of the extension discriminant

Let $A$ and $B$ be commutative rings and $K$
and $L$ fields, with ring maps $A \to K \to L$ and $A \to B \to L$ whose composites $A \to L$
agree, and with $L$ finite-dimensional over $K$ of degree $n$. Write $D_{B/A}$ for the
$A$-submodule of $K$ generated by the discriminants $\operatorname{disc}_{L/K}(b_1, \dots, b_n)$
of all $n$-tuples of elements of the image of $B$ in $L$. Let $S$ be a submonoid of $A$, let
$S^{-1}A$ be a localization of $A$ at $S$, and let $S^{-1}B$ be a localization of $B$ at the
image of $S$ in $B$. Suppose given ring maps $S^{-1}A \to K$, $S^{-1}A \to S^{-1}B$ and
$S^{-1}B \to L$ such that the composite $A \to S^{-1}A \to K$ is the map $A \to K$, the
composite $B \to S^{-1}B \to L$ is the map $B \to L$, and the composites
$S^{-1}A \to K \to L$ and $S^{-1}A \to S^{-1}B \to L$ agree. Then the $S^{-1}A$-submodule of
$K$ spanned by $D_{B/A}$ equals $D_{S^{-1}B/S^{-1}A}$, the $S^{-1}A$-submodule of $K$ generated
by the discriminants of $n$-tuples of elements of the image of $S^{-1}B$ in $L$.

No Dedekind, fraction-ring, integrally-closed, or separability hypotheses are used.

Formalized by `extensionDiscriminant_localization`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ExtensionDiscriminantLocalization.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ExtensionDiscriminantLocalization.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html#extension-discriminant-localization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discriminants of number fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-number-fields)
