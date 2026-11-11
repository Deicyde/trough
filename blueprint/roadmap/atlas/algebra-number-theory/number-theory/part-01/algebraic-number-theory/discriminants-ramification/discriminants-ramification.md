---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.MartinetTotallyRealTowersWanted.NumberTheory.exists_totallyReal_discr_le, MetaMathlibExt.odlyzko_root_discr_ge, Ideal.card_inertia_eq_ramificationIdxIn_mul_finInsepDegree, NumberField.Units.finiteIndex_closure_range_of_lt_one_off_diagonal
statement: formalized
---

# Discriminants, ramification and ideals: its own results

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/index.html).

Discriminants and their bounds, ramification and inertia, orders, units, ideal counting, local degrees under completion, field enumeration and towers.

## Martinet's totally real towers

There is a real constant $C > 0$ such that for every
$N \in \mathbb{N}$ there exist a natural number $d \ge N$ and a totally real number field $K$ of
degree $[K : \mathbb{Q}] = d$ whose discriminant $\Delta_K$ satisfies $|\Delta_K| \le C^d$.

## Sources

- Theorem 3.2 of T. F. Bloom, W. Sawin, C. Schildkraut, D. Zhelezov, *The sum-product conjecture is false for real numbers*, arXiv:2605.28781. Lean axiom: https://github.com/mathlib-initiative/sum_product (SumProduct.exists_totallyReal_discr_le). Underlying result: J. Martinet, *Tours de corps de classes et estimations de discriminants*, Invent. Math. 44 (1978), 65–73. Problem `martinet_totally_real_towers` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.MartinetTotallyRealTowersWanted.NumberTheory.exists_totallyReal_discr_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/MartinetTotallyRealTowersWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MartinetTotallyRealTowersWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/index.html#exists-totally-real-discr-le).

## Odlyzko's root discriminant bound in degree at least 18

Let $K$ be a totally complex
number field of degree $n = [K : \mathbb{Q}] \ge 18$ and discriminant $d_K$. Then
$|d_K| \ge 8.25^n$; equivalently, the root discriminant $|d_K|^{1/n}$ of $K$ is at least $8.25$.

Minkowski's elementary argument is not strong enough; the bound comes from analysing the zeros
of the Dedekind zeta function of $K$.

## Sources

- A. M. Odlyzko, *Bounds for discriminants and related estimates for class numbers, regulators and zeros of zeta functions: a survey of recent results*, Sém. Delange-Pisot-Poitou 18(1) (1976–1977), exp. 6, <https://www.numdam.org/item/SDPP_1976-1977__18_1_A6_0/>.

Stated but not proved: `MetaMathlibExt.odlyzko_root_discr_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/OdlyzkoRootDiscriminantWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OdlyzkoRootDiscriminantWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/index.html#odlyzko-root-discr-ge).

## Order of the inertia group

Let $A$ and $B$ be integral domains, with $B$ an $A$-algebra
that is finite and flat as an $A$-module, and let $G$ be a finite group acting faithfully on $B$
by $A$-algebra automorphisms such that every $G$-invariant element of $B$ comes from $A$. Let
$\mathfrak p$ be a maximal ideal of $A$ and $\mathfrak P$ a maximal ideal of $B$ lying over
$\mathfrak p$. Then the inertia group of $\mathfrak P$, consisting of the $\sigma \in G$ with
$\sigma(b) - b \in \mathfrak P$ for all $b \in B$, has order $e \cdot i$, where $e$ is the
ramification index of $\mathfrak p$ in $B$ (the common ramification index of the primes of $B$
over $\mathfrak p$) and $i$ is the inseparable degree of the residue field extension
$(B/\mathfrak P)/(A/\mathfrak p)$, that is, the degree of $B/\mathfrak P$ over the separable
closure of $A/\mathfrak p$ in it.

Formalized by `Ideal.card_inertia_eq_ramificationIdxIn_mul_finInsepDegree`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Inseparable.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RamificationInertia/Inseparable.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/index.html#card-inertia-eq-ramification-idx-in-mul).

## Units small away from the diagonal generate a subgroup of finite index

Let $F$ be a
number field and let $(u_v)$ be a family of units of the ring of integers of $F$, indexed by
the infinite places $v$ of $F$. Write $w(x)$ for the absolute value of $x$ at an infinite place
$w$. If $w(u_v) < 1$ for all infinite places $v$ and $w$ with $w \ne v$, then the subgroup of
the unit group of the ring of integers generated by the $u_v$ has finite index.

After dropping the coordinate of one infinite place, the logarithmic embeddings of the
remaining $u_v$ form a square matrix with negative off-diagonal entries and positive column
sums. It is therefore strictly diagonally dominant by columns, hence invertible, so these
units generate a subgroup of maximal rank.

Formalized by `NumberField.Units.finiteIndex_closure_range_of_lt_one_off_diagonal`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Units.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Units.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/index.html#finite-index-closure-range-of-lt-one-off).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discriminants, ramification and ideals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification)
