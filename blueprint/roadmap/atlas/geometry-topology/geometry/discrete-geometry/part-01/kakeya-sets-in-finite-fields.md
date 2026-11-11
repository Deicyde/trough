---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.Space, MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.dot, MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.affineLine, MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.IsKakeya, MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.IsProbabilityMeasureOn, MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.fourier, MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.fraser_kakeya_fourier_decay_and_sharp, MathlibExt.Combinatorics.FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.finiteFieldKakeyaCubeLowerBound
statement: formalized
---

# Kakeya sets in finite fields

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html).

## Coordinate space

For a type $F$ and a natural number $d$, $F^d$ denotes the set of
$d$-tuples $(x_1, \dots, x_d)$ of elements of $F$, that is, functions from a $d$-element index set
to $F$.

Here $F$ is a finite field, so $F^d$ is the $d$-dimensional vector space over $F$.

Formalized by `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.Space`, an abbreviation declared in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#space).

## Dot product

Let $F$ be a finite field and $d$ a natural number. For $x, y \in F^d$, the
dot product is $x \cdot y = \sum_{i} x_i y_i \in F$, the sum running over the $d$ coordinates.

Formalized by `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.dot`, a definition declared in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#dot).

## Affine line

Let $F$ be a finite field and $d$ a natural number. For $y, x \in F^d$, the
affine line with base point $y$ and direction $x$ is the set $\{y + a x : a \in F\} \subseteq F^d$.
When $x = 0$ this set is the single point $\{y\}$.

Formalized by `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.affineLine`, a definition declared in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#affine-line).

## Kakeya set

Let $F$ be a finite field and $d$ a natural number. A set $K \subseteq F^d$ is a
Kakeya set if for every $x \in F^d$ there is $y \in F^d$ such that the affine line
$\{y + a x : a \in F\}$ is contained in $K$; that is, $K$ contains a line in every direction.

Formalized by `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.IsKakeya`, a definition declared in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#is-kakeya).

## Probability measure supported on a set

Let $F$ be a finite field, $d$ a natural number
and $K \subseteq F^d$. A function $\mu : F^d \to \mathbb{R}$ is a probability measure on $K$ if
$\mu(x) \ge 0$ for every $x \in F^d$, $\sum_{x \in F^d} \mu(x) = 1$, and $\mu(x) \ne 0$ implies
$x \in K$.

Formalized by `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.IsProbabilityMeasureOn`, a definition declared in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#is-probability-measure-on).

## Finite-field Fourier transform

Let $F$ be a finite field, $d$ a natural number and $\chi$
an additive character of $F$ with values in $\mathbb{C}$. For $\mu : F^d \to \mathbb{R}$ and
$\xi \in F^d$, the Fourier transform of $\mu$ at $\xi$ is
$\hat{\mu}(\xi) = \sum_{x \in F^d} \chi(-\xi \cdot x)\, \mu(x) \in \mathbb{C}$, where
$\xi \cdot x$ is the dot product.

The definition allows any character; it is used with a nontrivial one.

Formalized by `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.fourier`, a definition declared in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#fourier).

## Fraser's Fourier decay theorem for finite-field Kakeya sets

Let $F$ be a finite field
with $q$ elements, let $d \ge 2$ be a natural number, let $K \subseteq F^d$ be a Kakeya set and let
$\chi$ be a nontrivial additive character of $F$ with values in $\mathbb{C}$. Then, first, there is
a probability measure $\mu$ on $K$ whose Fourier transform $\hat{\mu}$ with respect to $\chi$
satisfies $|\hat{\mu}(\xi)| \le q^{-1}$ for every nonzero $\xi \in F^d$. Second, this bound is
sharp: for every real $\kappa$ with $0 < \kappa < 1$ there is a natural number $Q$ such that for
every finite field $F'$ with $q' \ge Q$ elements there is a Kakeya set $K' \subseteq (F')^d$ such
that every probability measure $\mu$ on $K'$ has a nonzero $\xi \in (F')^d$ at which its Fourier
transform $\hat{\mu}$ with respect to a fixed primitive additive character of $F'$ satisfies
$|\hat{\mu}(\xi)| \ge \kappa \, q'^{-1}$.

## Sources

- J.M. Fraser, 'Fourier analytic properties of Kakeya sets in finite fields', Bull. London Math. Soc. 58(5) (2026); DOI 10.1112/blms.70367; arXiv:2505.09464. Problem `fraser_kakeya_fourier_decay` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.FraserKakeyaWanted.Combinatorics.FraserKakeyaProblem.fraser_kakeya_fourier_decay_and_sharp` is written with `theorem_wanted` in [WantedExt/Combinatorics/FraserKakeyaWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FraserKakeyaWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#fraser-kakeya-fourier-decay-and-sharp).

## Statement of the finite field Kakeya bound in dimension three

This is the statement that
there is a real number $c > 0$ such that for every finite field $F$ and every Kakeya set
$E \subseteq F^3$, that is, a set such that for every $x \in F^3$ there is $y \in F^3$ with
$\{y + a x : a \in F\} \subseteq E$, we have $|E| \ge c\,|F|^3$.

This is Dvir's form of Tao's question (AIM, Recent trends in additive combinatorics, Problem 3.8),
which asks for $|E| \gtrsim |F|^{5/2 + \varepsilon}$ for some $\varepsilon > 0$; the exponent $3$
gives $\varepsilon = 1/2$.

Formalized by `MathlibExt.Combinatorics.FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.finiteFieldKakeyaCubeLowerBound`, a definition declared in [WantedExt/Combinatorics/FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#finite-field-kakeya-cube-lower-bound).

## Finite field Kakeya sets in dimension three have cubic size

There is a real number $c > 0$
such that for every finite field $F$ and every Kakeya set $E \subseteq F^3$, that is, a set such
that for every $x \in F^3$ there is $y \in F^3$ with $\{y + a x : a \in F\} \subseteq E$, we have
$|E| \ge c\,|F|^3$.

Dvir proved by the polynomial method that every Kakeya set $K \subseteq F^n$ over a finite field
$F$ with $q$ elements has $|K| \ge C_n q^n$, with $C_n$ depending only on $n$ (Theorem 3, the
Alon–Tao form of his Theorem 1). For $n = 3$ this answers Tao's question, which asks for
$|E| \gtrsim |F|^{5/2 + \varepsilon}$ for some $\varepsilon > 0$, beyond Wolff's bound
$|F|^{5/2}$, with $\varepsilon = 1/2$.

## Sources

- AIM workshop Recent trends in additive combinatorics (2004), problem list collected by E. Croot and V. F. Lev, https://aimath.org/WWN/additivecomb/additivecomb.pdf, Problem 3.8 (T. Tao); resolution: Z. Dvir, On the size of Kakeya sets in finite fields, J. Amer. Math. Soc. 22 (2009), 1093-1097, arXiv:0803.2336, Theorem 3 (Section 1.1, the Alon-Tao improvement of Theorem 1): every Kakeya set K ⊂ Fⁿ satisfies |K| ≥ C_n qⁿ with C_n depending only on n; for n = 3 this is |K| ≫ q³, https://doi.org/10.1090/S0894-0347-08-00607-3.

Stated but not proved: `MathlibExt.Combinatorics.FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.finiteFieldKakeyaCubeLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FiniteFieldKakeyaThreeAIMCombinatoricsProblem245Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html#finite-field-kakeya-cube-lower-bound-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kakeya sets in finite fields](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/kakeya-sets-in-finite-fields)
