---
declaration: section
origin: cited
lean: BurnsidePaqb.simple_fdrep_of_irreducible, BurnsidePaqb.irreducible_of_simple_fdrep_aux, BurnsidePaqb.irreducible_of_simple_fdrep, BurnsidePaqb.Simple.isoSetoid, BurnsidePaqb.Irr, BurnsidePaqb.Irr.charFun, BurnsidePaqb.Irr.repBundle, BurnsidePaqb.Irr.charFun_inj
statement: formalized
proof: formalized
---

# Burnside's p^a q^b theorem

99 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html).

## Irreducible representations are simple

Let $G$ be a finite group and $\sigma$ an
irreducible representation of $G$ on a finite-dimensional complex vector space $V$. Then $V$ with
the action $\sigma$ is a simple object of the category of finite-dimensional complex
representations of $G$.

Formalized by `BurnsidePaqb.simple_fdrep_of_irreducible`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#simple-fdrep-of-irreducible).

## Simple finite-dimensional representations are irreducible (auxiliary form)

Let $G$ be a
finite group and $V$ a simple object of the category of finite-dimensional complex representations
of $G$. If $\sigma$ is a representation of $G$ on the underlying vector space of $V$ that equals the
action of $G$ on $V$, then $\sigma$ is irreducible.

Formalized by `BurnsidePaqb.irreducible_of_simple_fdrep_aux`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#irreducible-of-simple-fdrep-aux).

## Simple finite-dimensional complex representations of a finite group are irreducible

Let
$G$ be a finite group. If $V$ is a simple object of the category of finite-dimensional complex
representations of $G$, then the representation of $G$ on the underlying vector space of $V$ is
irreducible.

Formalized by `BurnsidePaqb.irreducible_of_simple_fdrep`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#irreducible-of-simple-fdrep).

## Isomorphism of simple representations

For a finite group $G$, two simple
finite-dimensional complex representations of $G$ are related when they are isomorphic; this is an
equivalence relation on the simple finite-dimensional complex representations of $G$.

Formalized by `BurnsidePaqb.Simple.isoSetoid`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#iso-setoid).

## Isomorphism classes of simple representations

For a finite group $G$, $\mathrm{Irr}(G)$ is
the set of isomorphism classes of simple finite-dimensional complex representations of $G$.

Formalized by `BurnsidePaqb.Irr`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#irr).

## Character of an isomorphism class

Let $G$ be a group. For an isomorphism class $c$ of
simple finite-dimensional complex representations of $G$, the character of $c$ is the function
$\chi_c \colon G \to \mathbb{C}$ given by $\chi_c(g) = \operatorname{tr} \rho(g)$ for any
representative $(V, \rho)$ of $c$. It does not depend on the representative, since isomorphic
representations have the same character.

Formalized by `BurnsidePaqb.Irr.charFun`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-fun).

## Chosen representative of an isomorphism class

For a finite group $G$ and an isomorphism
class $c$ of simple finite-dimensional complex representations of $G$, this is a simple
finite-dimensional complex representation of $G$ in the class $c$, fixed by the axiom of choice.

Formalized by `BurnsidePaqb.Irr.repBundle`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#rep-bundle).

## Characters determine irreducible representations

Let $G$ be a finite group. Two
isomorphism classes of simple finite-dimensional complex representations of $G$ that have the
same character are equal.

Formalized by `BurnsidePaqb.Irr.charFun_inj`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-fun-inj).

## The trivial irreducible class

Let $G$ be a finite group. The trivial representation of
$G$ on $\mathbb{C}$, where every element of $G$ acts as the identity, is simple, and this is its
class among the isomorphism classes of simple finite-dimensional complex representations of
$G$.

Formalized by `BurnsidePaqb.Irr.triv`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#triv).

## Character of the trivial representation

Let $G$ be a finite group. The character of the
isomorphism class of the trivial representation of $G$ on $\mathbb{C}$ takes the value $1$ at
every $g \in G$.

Formalized by `BurnsidePaqb.Irr.charFun_triv`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-fun-triv).

## Character value at the identity

Let $G$ be a group and let $c$ be an isomorphism class of
simple finite-dimensional complex representations of $G$. The character of $c$ at the identity
$1 \in G$ equals the dimension over $\mathbb{C}$ of the chosen representative of $c$.

Formalized by `BurnsidePaqb.Irr.charFun_one`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-fun-one).

## Character of a class via its chosen representative

Let $G$ be a group and let $c$ be an
isomorphism class of simple finite-dimensional complex representations of $G$, with chosen
representative $(V, \rho)$. For every $x \in G$, the character of $c$ at $x$ equals the character
of the representation $\rho$ at $x$, namely $\operatorname{tr} \rho(x)$.

Formalized by `BurnsidePaqb.Irr.charFun_eq_repBundle_char`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-fun-eq-rep-bundle-char).

## Orthogonality of irreducible characters

Let $G$ be a finite group and let $\chi_i$ and
$\chi_j$ be the characters of isomorphism classes $i$ and $j$ of simple finite-dimensional
complex representations of $G$. Then

$$\frac{1}{|G|} \sum_{g \in G} \chi_i(g)\, \chi_j(g^{-1}) =
\begin{cases} 1 & \text{if } i = j, \\ 0 & \text{otherwise.} \end{cases}$$

Formalized by `BurnsidePaqb.charInner_orth`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-inner-orth).

## Class function

A function $f \colon G \to \mathbb{C}$ on a finite group $G$ is a class
function when $f(hgh^{-1}) = f(g)$ for all $g, h \in G$, that is, when $f$ is constant on
conjugacy classes.

Formalized by `BurnsidePaqb.IsClassFun`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#is-class-fun).

## Bound on the number of irreducible representations

Let $G$ be a finite group. Every
finite set of isomorphism classes of simple finite-dimensional complex representations of $G$
has at most $|G|$ elements.

Formalized by `BurnsidePaqb.cardBound`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#card-bound).

## Zimmerman's averaging operator

Let $G$ be a finite group, let $M$ be a module over the
group algebra $\mathbb{C}[G]$ with a compatible $\mathbb{C}$-module structure, and write
$\rho(g)$ for the action of $g \in G$ on $M$. For a function $f : G \to \mathbb{C}$, the averaging
operator of $f$ is the $\mathbb{C}$-linear endomorphism $T_f = \sum_{g \in G} f(g)\,\rho(g^{-1})$
of $M$.

Formalized by `BurnsidePaqb.zimmOp`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#zimm-op).

## The averaging operator of a class function is $G$-equivariant

Let $G$ be a finite group,
let $M$ be a module over the group algebra $\mathbb{C}[G]$ with a compatible $\mathbb{C}$-module
structure, and write $\rho(h)$ for the action of $h \in G$ on $M$. If $f : G \to \mathbb{C}$ is a
class function, then its averaging operator $T_f = \sum_{g \in G} f(g)\,\rho(g^{-1})$ satisfies
$\rho(h)(T_f x) = T_f(\rho(h) x)$ for all $h \in G$ and $x \in M$.

Formalized by `BurnsidePaqb.zimmOp_comm`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#zimm-op-comm).

## Class functions orthogonal to all irreducible characters vanish

Let $G$ be a finite
group and let $f \colon G \to \mathbb{C}$ be a class function, that is, $f(hgh^{-1}) = f(g)$ for
all $g, h \in G$. Suppose that for every isomorphism class $c$ of simple finite-dimensional
complex representations of $G$, with character $\chi_c$,

$$\frac{1}{|G|} \sum_{g \in G} f(g)\, \chi_c(g^{-1}) = 0.$$

Then $f = 0$.

## Sources

- Zimmerman, Theorem 5 (core step).

Formalized by `BurnsidePaqb.classfun_eq_zero_of_orth`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#classfun-eq-zero-of-orth).

## Expansion of class functions in irreducible characters

Let $G$ be a finite group, let
$f \colon G \to \mathbb{C}$ be a class function, and for each of the finitely many isomorphism
classes $c$ of simple finite-dimensional complex representations of $G$ let $\chi_c$ be its
character. Then

$$f = \sum_{c} \Big(\frac{1}{|G|} \sum_{g \in G} f(g)\, \chi_c(g^{-1})\Big)\, \chi_c,$$

where $c$ runs over all these isomorphism classes.

## Sources

- Zimmerman, Proposition 4 (setup).

Formalized by `BurnsidePaqb.classfun_expand`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#classfun-expand).

## Delta function at the identity

For a finite group $G$, $\delta_1 \colon G \to \mathbb{C}$
is the function with $\delta_1(1) = 1$ and $\delta_1(g) = 0$ for every $g \ne 1$.

Formalized by `BurnsidePaqb.deltaOne`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 842](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L842). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#delta-one).

## Pairing of the identity indicator with a character

Let $G$ be a finite group, let
$\delta \colon G \to \mathbb{C}$ be the indicator function of the identity, so $\delta(1) = 1$ and
$\delta(g) = 0$ for $g \neq 1$, and let $\chi_c$ be the character of an isomorphism class $c$ of
simple finite-dimensional complex representations of $G$. Then

$$\frac{1}{|G|} \sum_{g \in G} \delta(g)\, \chi_c(g^{-1}) = \frac{\chi_c(1)}{|G|}.$$

Formalized by `BurnsidePaqb.deltaOne_inner`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 863](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L863). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#delta-one-inner).

## Column orthogonality at the identity

Let $G$ be a finite group and, for each isomorphism
class $c$ of simple finite-dimensional complex representations of $G$, let $\chi_c$ be its
character. For every $g \in G$ with $g \ne 1$, $\sum_c \chi_c(1)\,\chi_c(g) = 0$, where the sum runs
over all such classes $c$.

Equivalently, the character of the regular representation vanishes away from the identity.

Formalized by `BurnsidePaqb.regular_character_vanishes`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#regular-character-vanishes).

## Sum of squared degrees

Let $G$ be a finite group and, for each isomorphism class $c$ of
simple finite-dimensional complex representations of $G$, let $\chi_c$ be its character. Then
$\sum_c \chi_c(1)^2 = |G|$, where the sum runs over all such classes $c$.

Formalized by `BurnsidePaqb.sum_deg_sq`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean, line 898](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CharacterOrthogonality.lean#L898). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#sum-deg-sq).

## Cyclotomic subfield of $\mathbb{C}$

For a natural number $m$, the $m$-th cyclotomic
field is the intermediate field of $\mathbb{C}/\mathbb{Q}$ generated over $\mathbb{Q}$ by the
$m$-th roots of unity, that is, by the complex roots of $X^m - 1$.

For $m = 0$ the polynomial $X^0 - 1$ is zero and is taken to have no roots, so the field is
$\mathbb{Q}$.

Formalized by `BurnsidePaqb.cycSubfield`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#cyc-subfield).

## $X^m - 1$ over $\mathbb{Q}$ and over $\mathbb{C}$

For every natural number $m$, mapping
the coefficients of the rational polynomial $X^m - 1$ along the inclusion
$\mathbb{Q} \to \mathbb{C}$ gives the complex polynomial $X^m - 1$.

Formalized by `BurnsidePaqb.map_X_pow_sub_C_rat`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#map-x-pow-sub-c-rat).

## Complex roots of $X^m - 1$

For every natural number $m \neq 0$, the set of complex roots
of the rational polynomial $X^m - 1$ is exactly the set of $m$-th roots of unity in $\mathbb{C}$.

Formalized by `BurnsidePaqb.cyc_rootSet`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#cyc-root-set).

## The $m$-th cyclotomic field is a splitting field of $X^m - 1$

For every natural number
$m \neq 0$, the subfield of $\mathbb{C}$ generated over $\mathbb{Q}$ by the $m$-th roots of unity
is a splitting field over $\mathbb{Q}$ of the polynomial $X^m - 1 \in \mathbb{Q}[X]$.

Formalized by `BurnsidePaqb.cyc_isSplitting`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#cyc-is-splitting).

## The zeroth cyclotomic field is $\mathbb{Q}$

For $m = 0$ the cyclotomic subfield of
$\mathbb{C}$ is the bottom intermediate field, that is $\mathbb{Q}$ itself: the polynomial
$X^0 - 1$ is zero and is taken to have no roots, so nothing is adjoined.

Formalized by `BurnsidePaqb.cycSubfield_zero`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CyclotomicField.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#cyc-subfield-zero).

## Conjugacy class

For an element $g$ of a finite group $G$, the conjugacy class of $g$ is
the finite set $\{h g h^{-1} : h \in G\}$, the orbit of $g$ under the action of $G$ on itself
by conjugation.

Formalized by `BurnsidePaqb.conjClass`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqbReduction.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqbReduction.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-class).

## Orbit–stabilizer for a conjugacy class

For every element $g$ of a finite group $G$, the
size of the conjugacy class of $g$ times the order of the stabilizer of $g$ under the action of
$G$ on itself by conjugation, $x \cdot y = x y x^{-1}$, equals the order of $G$.

Formalized by `BurnsidePaqb.conjClass_card_mul_stabilizer_card`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqbReduction.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqbReduction.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-class-card-mul-stabilizer-card).

## Centralizer as a conjugation stabilizer

For an element $g$ of a finite group $G$, this
is the bijection from the centralizer $C_G(g) = \{x \in G : xg = gx\}$ onto the stabilizer of
$g$ for the action of $G$ on itself by conjugation, $x \cdot y = x y x^{-1}$, that sends each
element $x$ to itself.

Formalized by `BurnsidePaqb.centralizerEquivStabilizer`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqbReduction.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqbReduction.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#centralizer-equiv-stabilizer).

## Class size times centralizer order

Let $g$ be an element of a finite group $G$, let
$g^G$ be its conjugacy class and let $C_G(g) = \{x \in G : xg = gx\}$ be its centralizer.
Then $|g^G| \cdot |C_G(g)| = |G|$.

Formalized by `BurnsidePaqb.conjClass_card_mul_centralizer_card`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqbReduction.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqbReduction.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-class-card-mul-centralizer-card).

## Conjugacy classes are closed under conjugation

Let $g$, $h$ and $x$ be elements of a
finite group $G$. If $x$ lies in the conjugacy class of $g$, then so does $h x h^{-1}$.

Formalized by `BurnsidePaqb.conj_mem_conjClass`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqbReduction.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqbReduction.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-mem-conj-class).

## A nontrivial element whose class size is a power of $p$

Let $p$ and $q$ be primes, let
$a$ and $b$ be natural numbers with $b \ge 1$, and let $G$ be a finite group of order
$p^a q^b$. Then there are an element $g \ne 1$ of $G$ and a natural number $k \le a$ such that
the conjugacy class of $g$ has exactly $p^k$ elements.

In the proof, $g$ is a nontrivial element of the center of a subgroup of $G$ of order $q^b$
(a Sylow $q$-subgroup when $p \ne q$).

Formalized by `BurnsidePaqb.exists_ne_one_class_prime_pow`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqbReduction.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqbReduction.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#exists-ne-one-class-prime-pow).

## Class sum of a finite subset

Let $G$ be a group. The class sum of a finite subset
$C \subseteq G$ is the element $\widehat{C} = \sum_{x \in C} x$ of the complex group algebra
$\mathbb{C}[G]$.

Formalized by `BurnsidePaqb.classSum`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-sum).

## Class sums commute with group elements

Let $G$ be a finite group, let $g \in G$, and let
$\widehat{C_g} = \sum_{x \in C_g} x$ be the sum, in the complex group algebra $\mathbb{C}[G]$, of
the elements of the conjugacy class $C_g$ of $g$. Then $\widehat{C_g} h = h \widehat{C_g}$ for
every $h \in G$, where $h$ is viewed as a basis element of $\mathbb{C}[G]$.

Formalized by `BurnsidePaqb.classSum_central`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-sum-central).

## The class sum of the conjugacy class of an element is central

Let $G$ be a finite group,
let $g \in G$, and let $\widehat{C_g} = \sum_{x \in C_g} x$ be the sum, in the complex group
algebra $\mathbb{C}[G]$, of the elements of the conjugacy class $C_g$ of $g$. Then
$w \widehat{C_g} = \widehat{C_g} w$ for every $w \in \mathbb{C}[G]$.

Formalized by `BurnsidePaqb.classSum_central'`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-sum-central-2).

## Chosen representative of a conjugacy class

For each conjugacy class $K$ of a group $G$,
the representative of $K$ is an element $g_K \in G$, fixed once and for all by choice, whose
conjugacy class is $K$.

Formalized by `BurnsidePaqb.classRep`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-rep).

## Conjugacy class of the chosen representative

Let $G$ be a finite group. For every
conjugacy class $K$ of $G$, the set of elements of $K$ equals the conjugacy class of the chosen
representative of $K$.

Formalized by `BurnsidePaqb.carrier_toFinset`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#carrier-to-finset).

## Structure constants of a pair of subsets

Let $G$ be a finite group. For finite subsets
$C_i, C_j \subseteq G$ and an element $z \in G$, the structure constant is the number of pairs
$(x, y) \in C_i \times C_j$ with $xy = z$.

Formalized by `BurnsidePaqb.structConst`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#struct-const).

## Class structure constants are class functions

Let $G$ be a finite group, let
$g_i, g_j \in G$ with conjugacy classes $C_{g_i}$ and $C_{g_j}$, and for $z \in G$ let $a(z)$ be
the number of pairs $(x, y) \in C_{g_i} \times C_{g_j}$ with $x y = z$. If $u, z \in G$ are
conjugate, then $a(u) = a(z)$.

Formalized by `BurnsidePaqb.structConst_conj`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#struct-const-conj).

## Coefficients of a product of class sums

Let $G$ be a group, let $C_i$ and $C_j$ be
finite subsets of $G$, and write $\widehat{C} = \sum_{x \in C} x$ in the complex group algebra
$\mathbb{C}[G]$. For every $u \in G$, the coefficient of $u$ in $\widehat{C_i} \widehat{C_j}$ is
the number of pairs $(x, y) \in C_i \times C_j$ with $x y = u$.

Formalized by `BurnsidePaqb.coeff_classSum_mul`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#coeff-class-sum-mul).

## Products of class sums expand in class sums

Let $G$ be a finite group. For a finite
subset $C$ of $G$ write $\widehat{C} = \sum_{x \in C} x$ in the complex group algebra
$\mathbb{C}[G]$, and for $g \in G$ let $C_g$ be its conjugacy class. Let $g_i, g_j \in G$, and for
each conjugacy class $K$ of $G$ with chosen representative $z_K$ let $a_K$ be the number of pairs
$(x, y) \in C_{g_i} \times C_{g_j}$ with $x y = z_K$. Then
$\widehat{C_{g_i}} \widehat{C_{g_j}} = \sum_K a_K \widehat{K}$, the sum running over all
conjugacy classes $K$ of $G$.

Formalized by `BurnsidePaqb.classSum_mul`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-sum-mul).

## Conjugate elements have the same conjugacy class

Let $G$ be a finite group. If
$g_1, g_2 \in G$ are conjugate, then the conjugacy class of $g_1$ equals the conjugacy class of
$g_2$.

Formalized by `BurnsidePaqb.conjClass_eq_of_isConj`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-class-eq-of-is-conj).

## Class sums of conjugacy classes are central

Let $G$ be a finite group. For every
conjugacy class $K$ of $G$ and every element $w$ of the complex group algebra $\mathbb{C}[G]$,
the class sum $\widehat{K} = \sum_{x \in K} x$ satisfies $w \widehat{K} = \widehat{K} w$.

Formalized by `BurnsidePaqb.classSum_carrier_central`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ClassSum.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-sum-carrier-central).

## Schur's lemma for central elements of the group algebra

Let $\rho$ be an irreducible
representation of a group $G$ on a finite-dimensional complex vector space $V$, extended linearly
to the group algebra $\mathbb{C}[G]$. If $z \in \mathbb{C}[G]$ commutes with every element of
$\mathbb{C}[G]$, then $z$ acts on $V$ as a scalar: there is $c \in \mathbb{C}$ with
$\rho(z) v = c\, v$ for all $v \in V$.

Formalized by `BurnsidePaqb.exists_scalar_of_central`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#exists-scalar-of-central).

## Central scalar of a conjugacy class

Let $\rho$ be an irreducible representation of a
finite group $G$ on a finite-dimensional complex vector space $V$. For a conjugacy class $C$ of
$G$, the class sum $\sum_{x \in C} x$ is central in the group algebra $\mathbb{C}[G]$, so it acts
on $V$ as multiplication by a complex number. The central scalar $\omega_\rho(C)$ is that number:
$\rho\bigl(\sum_{x \in C} x\bigr) v = \omega_\rho(C)\, v$ for all $v \in V$.

Formalized by `BurnsidePaqb.centralScalar`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#central-scalar).

## Central scalars multiply via the class structure constants

Let $\rho$ be an irreducible
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, and let
$\omega_\rho(C)$ be the scalar by which the class sum of a conjugacy class $C$ acts on $V$. Fix
a representative $g_C$ of each conjugacy class $C$. For conjugacy classes $C_1$ and $C_2$,

$$\omega_\rho(C_1)\,\omega_\rho(C_2) = \sum_{C} a_{C_1 C_2}^{C}\, \omega_\rho(C),$$

where $C$ runs over all conjugacy classes of $G$ and $a_{C_1 C_2}^{C}$ is the number of pairs
$(x, y) \in C_1 \times C_2$ with $x y = g_C$.

Formalized by `BurnsidePaqb.centralScalar_mul`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#central-scalar-mul).

## Trace formula for central scalars

Let $\rho$ be an irreducible representation of a
finite group $G$ on a finite-dimensional complex vector space $V$ with character $\chi$, and let
$\omega_\rho(C)$ be the scalar by which the class sum of a conjugacy class $C$ acts on $V$. Then
$\omega_\rho(C) \cdot \dim V = \sum_{x \in C} \chi(x)$.

Formalized by `BurnsidePaqb.centralScalar_trace`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#central-scalar-trace).

## Generators of the central-scalar ring

Let $\rho$ be an irreducible representation of a
finite group $G$ on a finite-dimensional complex vector space $V$, and let $\omega_\rho(C)$ be
the scalar by which the class sum of a conjugacy class $C$ acts on $V$. The set $S_\rho$ is the
finite set of complex numbers consisting of $1$ and the values $\omega_\rho(C)$ for all
conjugacy classes $C$ of $G$.

Formalized by `BurnsidePaqb.scalarGens`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#scalar-gens).

## Products of central-scalar generators stay in their span

Let $\rho$ be an irreducible
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, and let
$S_\rho$ be the finite set of complex numbers consisting of $1$ and the scalars by which the
class sums of the conjugacy classes of $G$ act on $V$. If $a, b \in S_\rho$, then $ab$ lies in
the $\mathbb{Z}$-linear span of $S_\rho$.

Formalized by `BurnsidePaqb.scalarGens_mul`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#scalar-gens-mul).

## Ring generated by the central scalars

Let $\rho$ be an irreducible representation of a
finite group $G$ on a finite-dimensional complex vector space $V$, and let $S_\rho$ be the finite
set of complex numbers consisting of $1$ and the scalars by which the class sums of the
conjugacy classes of $G$ act on $V$. The $\mathbb{Z}$-linear span of $S_\rho$ is closed under
multiplication, and this is that span as a $\mathbb{Z}$-subalgebra of $\mathbb{C}$.

Formalized by `BurnsidePaqb.scalarSubalg`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#scalar-subalg).

## Central scalars are algebraic integers

Let $\rho$ be an irreducible representation of a
finite group $G$ on a finite-dimensional complex vector space $V$. For every conjugacy class $C$
of $G$, the complex number $\omega_\rho(C)$ by which the class sum $\sum_{x \in C} x$ acts on $V$
is an algebraic integer, that is, integral over $\mathbb{Z}$.

Formalized by `BurnsidePaqb.centralScalar_isIntegral`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#central-scalar-is-integral).

## Class size times character ratio is an algebraic integer

Let $\rho$ be an irreducible
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, with
character $\chi$. For every $g \in G$, if $C$ is the conjugacy class of $g$, then
$|C|\,\chi(g)/\chi(1)$ is an algebraic integer.

## Sources

- Bielefeld Prop 1.

Formalized by `BurnsidePaqb.classSum_centralScalar_isIntegral`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/CentralCharacter.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-sum-central-scalar-is-integral).

## Character value as the sum of characteristic roots

Let $\rho$ be a representation of a
group $G$ on a finite-dimensional complex vector space, with character $\chi$, and let $g \in G$.
Then $\chi(g)$ is the sum of the roots of the characteristic polynomial of $\rho(g)$, counted
with multiplicity.

Formalized by `BurnsidePaqb.character_eq_sum_roots`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#character-eq-sum-roots).

## Characteristic roots are killed by the order of the element

Let $G$ be a group, $V$ a
finite-dimensional complex vector space, $\rho$ a representation of $G$ on $V$, and $g \in G$
an element of order $n$, where $n = 0$ if $g$ has infinite order. Then every root $\mu$ of the
characteristic polynomial of $\rho(g)$ satisfies $\mu^n = 1$; in particular, when $g$ has finite
order, $\mu$ is a root of unity.

Formalized by `BurnsidePaqb.charpoly_root_pow_orderOf`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#charpoly-root-pow-order-of).

## Eigenvalues of a finite group representation have modulus one

Let $G$ be a finite
group, $V$ a finite-dimensional complex vector space and $\rho$ a representation of $G$ on $V$.
For every $g \in G$, every root $\mu$ of the characteristic polynomial of $\rho(g)$ satisfies
$|\mu| = 1$.

Formalized by `BurnsidePaqb.charpoly_root_norm_eq_one`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#charpoly-root-norm-eq-one).

## Real part of a product with a conjugate

For complex numbers $a$ and $b$,
$\operatorname{Re} a \operatorname{Re} b + \operatorname{Im} a \operatorname{Im} b =
\operatorname{Re}(a \bar{b})$.

Formalized by `BurnsidePaqb.re_mul_conj`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#re-mul-conj).

## Product of a unit complex number with a conjugate unit

For complex numbers $a$ and $b$
with $|a| = |b| = 1$, we have $|a \bar{b}| = 1$.

Formalized by `BurnsidePaqb.norm_mul_conj_eq_one`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#norm-mul-conj-eq-one).

## Cancelling a unit-modulus conjugate

Let $a, b \in \mathbb{C}$ with $|b| = 1$. If
$a \bar{b} = 1$, then $a = b$.

Formalized by `BurnsidePaqb.eq_of_mul_conj_eq_one`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#eq-of-mul-conj-eq-one).

## Real part of a unit complex number other than $1$

If $w \in \mathbb{C}$ satisfies
$|w| = 1$ and $w \neq 1$, then $\operatorname{Re} w < 1$.

Formalized by `BurnsidePaqb.re_lt_one_of_ne_one`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#re-lt-one-of-ne-one).

## Strict triangle inequality for unit complex numbers

Let $\mu_1, \dots, \mu_n$ be complex
numbers with $|\mu_i| = 1$ for every $i$, not all equal. Then
$\left|\sum_{i=1}^{n} \mu_i\right| < n$.

Formalized by `BurnsidePaqb.abs_sum_roots_of_unity_lt`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#abs-sum-roots-of-unity-lt).

## Character values are algebraic integers

Let $\rho$ be a representation of a finite group
$G$ on a finite-dimensional complex vector space, with character $\chi$. Then $\chi(g)$ is an
algebraic integer for every $g \in G$.

Each value $\chi(g)$ is a sum of roots of unity.

Formalized by `BurnsidePaqb.character_isIntegral`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#character-is-integral).

## Integrality of the normalized character value at a coprime class

Let $G$ be a finite
group, let $\rho$ be an irreducible representation of $G$ on a nonzero finite-dimensional complex
vector space $V$, with character $\chi$, and let $g \in G$. If the size of the conjugacy class of
$g$ is coprime to $\dim V$, then $\chi(g)/\chi(1)$ is an algebraic integer.

## Sources

- Bielefeld Theorem 5, integrality step.

Formalized by `BurnsidePaqb.charDivDeg_isIntegral_of_coprime`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-div-deg-is-integral-of-coprime).

## Sum of two distinct unit complex numbers

If $a$ and $b$ are distinct complex numbers
with $|a| = |b| = 1$, then $|a + b| < 2$.

Formalized by `BurnsidePaqb.abs_add_two_ne_unit_lt_two`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#abs-add-two-ne-unit-lt-two).

## Strict triangle inequality for unit complex numbers, multiset form

Let $s$ be a finite
multiset of complex numbers, each of absolute value $1$, containing two distinct elements. Then
the absolute value of the sum of $s$ is strictly less than the number of elements of $s$,
counted with multiplicity.

Formalized by `BurnsidePaqb.abs_multiset_sum_lt`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#abs-multiset-sum-lt).

## Number of characteristic roots of a representation matrix

Let $G$ be a group, $V$ a
finite-dimensional complex vector space, $\rho$ a representation of $G$ on $V$ and $g \in G$.
The characteristic polynomial of $\rho(g)$ has exactly $\dim_{\mathbb{C}} V$ roots in
$\mathbb{C}$, counted with multiplicity.

Formalized by `BurnsidePaqb.charpoly_roots_card`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#charpoly-roots-card).

## Characteristic roots are not all equal below the degree

Let $G$ be a finite group, let
$\rho$ be a representation of $G$ on a nonzero finite-dimensional complex vector space $V$, with
character $\chi$, and let $g \in G$. If $|\chi(g)| < \dim V$, then the characteristic polynomial
of $\rho(g)$ has two distinct roots.

Formalized by `BurnsidePaqb.char_roots_not_all_equal`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-roots-not-all-equal).

## Character values lie in a cyclotomic field

Let $\rho$ be a representation of a group $G$
on a finite-dimensional complex vector space, with character $\chi$, and let $g \in G$ have
finite order $m$. Then $\chi(g)$ lies in the subfield of $\mathbb{C}$ generated over $\mathbb{Q}$
by the $m$-th roots of unity.

Formalized by `BurnsidePaqb.char_mem_cycSubfield`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-mem-cyc-subfield).

## Characteristic roots as elements of the cyclotomic field

Let $m$ be a positive integer,
let $\rho$ be a representation of a finite group $G$ on a finite-dimensional complex vector
space $V$, and let $g \in G$ be such that every root $\mu$ of the characteristic polynomial of
$\rho(g)$ satisfies $\mu^m = 1$. Each such root $\mu$ is regarded as an element of the subfield
$K \subseteq \mathbb{C}$ obtained by adjoining the $m$-th roots of unity to $\mathbb{Q}$.

Formalized by `BurnsidePaqb.conjRootElem`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-root-elem).

## Field embeddings applied to character values

Let $G$ be a group, $\rho$ a
representation of $G$ on a finite-dimensional complex vector space $V$ with character $\chi$,
let $m$ be a positive integer, and let $g \in G$ be such that every root $\mu$ of the
characteristic polynomial of $\rho(g)$ satisfies $\mu^m = 1$. Let $K \subseteq \mathbb{C}$ be the
field obtained by adjoining the $m$-th roots of unity to $\mathbb{Q}$, and suppose
$\chi(g) \in K$. Then for every $\mathbb{Q}$-algebra homomorphism $\sigma : K \to \mathbb{C}$ we
have $\sigma(\chi(g)) = \sum_\mu \sigma(\mu)$, where the sum runs over the roots $\mu$ of the
characteristic polynomial of $\rho(g)$, counted with multiplicity, each regarded as an element
of $K$.

Formalized by `BurnsidePaqb.embedding_char_eq_conj_sum`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#embedding-char-eq-conj-sum).

## Character vanishing from coprimality and a strict norm bound

Let $G$ be a finite group,
let $\rho$ be an irreducible representation of $G$ on a nonzero finite-dimensional complex vector
space $V$, with character $\chi$, and let $g \in G$. If the size of the conjugacy class of $g$ is
coprime to $\dim V$ and $|\chi(g)| < \dim V$, then $\chi(g) = 0$.

## Sources

- Bielefeld Theorem 5, norm step.

Formalized by `BurnsidePaqb.char_eq_zero_of_coprime_of_norm_lt`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-eq-zero-of-coprime-of-norm-lt).

## Burnside's vanishing theorem for coprime class sizes

Let $G$ be a finite group, let
$\rho$ be an irreducible representation of $G$ on a nonzero finite-dimensional complex vector
space $V$, with character $\chi$, and let $g \in G$. If the size of the conjugacy class of $g$
is coprime to $\dim V$, then $|\chi(g)| = \dim V$ or $\chi(g) = 0$.

Since $\chi(1) = \dim V$, the first alternative says that $g$ lies in the center $Z(\chi)$ of
$\chi$, the set of $h \in G$ with $|\chi(h)| = \chi(1)$.

## Sources

- Bielefeld Theorem 5.

Formalized by `BurnsidePaqb.burnside_coprime_vanish`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/KillingLemma.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#burnside-coprime-vanish).

## Self-orthogonality of an irreducible character

Let $\rho$ be an irreducible representation
of a finite group $G$ on a finite-dimensional complex vector space, with character $\chi$. Then
$\sum_{g \in G} \chi(g)\chi(g^{-1}) = |G|$.

Formalized by `BurnsidePaqb.self_pair_sum`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#self-pair-sum).

## Splitting a sum over conjugacy classes

For a finite group $G$ and every function
$f : G \to \mathbb{C}$, $\sum_{g \in G} f(g) = \sum_{l} \sum_{x \in l} f(x)$, where $l$ runs over
the conjugacy classes of $G$.

Formalized by `BurnsidePaqb.sum_over_classes`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#sum-over-classes).

## Members of a conjugacy class are conjugate to its representative

Let $l$ be a conjugacy
class of a finite group $G$ and $g_l$ its chosen representative. For every $x \in l$ there is
$c \in G$ with $c x c^{-1} = g_l$.

Formalized by `BurnsidePaqb.conj_to_rep`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#conj-to-rep).

## Characters are constant on conjugacy classes

Let $\rho$ be a representation of a finite
group $G$ on a finite-dimensional complex vector space, with character $\chi$, and let $g_l$ be the
chosen representative of a conjugacy class $l$ of $G$. Then $\chi(x) = \chi(g_l)$ for every
$x \in l$.

Formalized by `BurnsidePaqb.char_eq_of_mem_carrier`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-eq-of-mem-carrier).

## Characters at inverses are constant on conjugacy classes

Let $\rho$ be a representation
of a finite group $G$ on a finite-dimensional complex vector space, with character $\chi$, and let
$g_l$ be the chosen representative of a conjugacy class $l$ of $G$. Then
$\chi(x^{-1}) = \chi(g_l^{-1})$ for every $x \in l$.

Formalized by `BurnsidePaqb.char_inv_eq_of_mem_carrier`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-inv-eq-of-mem-carrier).

## Contribution of a conjugacy class to the self-pairing sum

Let $\rho$ be an irreducible
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, with
character $\chi$. For a conjugacy class $l$ of $G$, let $g_l$ be its chosen representative and
$\omega(l)$ the central scalar of $l$, the scalar by which the class sum of $l$ acts on $V$. Then
$\sum_{x \in l} \chi(x)\chi(x^{-1}) = (\dim_{\mathbb{C}} V)\,\omega(l)\,\chi(g_l^{-1})$.

Formalized by `BurnsidePaqb.class_inner_sum`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#class-inner-sum).

## Degrees of irreducible representations divide the group order

Let $\rho$ be an
irreducible representation of a finite group $G$ on a nonzero finite-dimensional complex vector
space $V$. Then $\dim_{\mathbb{C}} V$ divides $|G|$.

## Sources

- Bielefeld Corollary 2.

Formalized by `BurnsidePaqb.degree_dvd_card`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/DegreeDivides.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#degree-dvd-card).

## Characters of full absolute value have equal eigenvalues

Let $G$ be a finite group,
$V$ a nonzero finite-dimensional complex vector space and $\rho$ an irreducible representation of
$G$ on $V$ with character $\chi$. If $g \in G$ satisfies $|\chi(g)| = \dim V$, then any two roots
of the characteristic polynomial of $\rho(g)$ are equal.

Formalized by `BurnsidePaqb.all_roots_eq_of_norm_eq`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#all-roots-eq-of-norm-eq).

## Elements with a single eigenvalue act as scalars

Let $G$ be a finite group, $V$ a nonzero
finite-dimensional complex vector space, $\rho$ a representation of $G$ on $V$, $g \in G$ and
$\mu_0 \in \mathbb{C}$. If every root of the characteristic polynomial of $\rho(g)$ equals
$\mu_0$, then $\rho(g) = \mu_0 \cdot \mathrm{id}_V$.

Formalized by `BurnsidePaqb.eq_smul_one_of_all_roots_eq`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#eq-smul-one-of-all-roots-eq).

## Scalar center of a representation

Let $\rho$ be a representation of a group $G$ on a
nonzero complex vector space $V$. The scalar center of $\rho$ is the subgroup of $G$ consisting of
the elements $g$ such that $\rho(g) = c \cdot \mathrm{id}_V$ for some $c \in \mathbb{C}$.

Formalized by `BurnsidePaqb.charCenter`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-center).

## Membership in the scalar center

Let $\rho$ be a representation of a group $G$ on a nonzero
complex vector space $V$. An element $g \in G$ lies in the scalar center of $\rho$ if and only if
$\rho(g) = c \cdot \mathrm{id}_V$ for some $c \in \mathbb{C}$.

Formalized by `BurnsidePaqb.mem_charCenter_iff`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#mem-char-center-iff).

## Elements acting by a scalar lie in the scalar center

Let $\rho$ be a representation of a
group $G$ on a nonzero complex vector space $V$. If $g \in G$ and $c \in \mathbb{C}$ satisfy
$\rho(g) = c \cdot \mathrm{id}_V$, then $g$ lies in the scalar center of $\rho$.

Formalized by `BurnsidePaqb.mem_charCenter_of_eq_smul`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#mem-char-center-of-eq-smul).

## Elements of the scalar center act by scalars

Let $\rho$ be a representation of a group $G$
on a nonzero complex vector space $V$. If $g$ lies in the scalar center of $\rho$, then there is
$c \in \mathbb{C}$ with $\rho(g) = c \cdot \mathrm{id}_V$.

Formalized by `BurnsidePaqb.exists_eq_smul_of_mem_charCenter`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#exists-eq-smul-of-mem-char-center).

## The scalar center of a nonlinear irreducible representation is proper

Let $\rho$ be an
irreducible representation of a group $G$ on a finite-dimensional complex vector space $V$ with
$\dim V > 1$. Then the scalar center of $\rho$ is a proper subgroup of $G$.

Formalized by `BurnsidePaqb.charCenter_proper_of_nonlinear`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-center-proper-of-nonlinear).

## Elements of the scalar center have character of full absolute value

Let $G$ be a finite
group, $V$ a nonzero finite-dimensional complex vector space and $\rho$ a representation of $G$
on $V$ with character $\chi$. If $g$ lies in the scalar center of $\rho$, then
$|\chi(g)| = \dim V$.

Formalized by `BurnsidePaqb.norm_eq_of_mem_charCenter`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/ScalarCenter.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#norm-eq-of-mem-char-center).

## An algebraic integer cannot solve $1 + p\beta = 0$ for a prime $p$

Let $p$ be a prime
number. There is no algebraic integer $\beta \in \mathbb{C}$ with $1 + p\beta = 0$, since such a
$\beta$ would make $-1/p$ an algebraic integer.

Formalized by `BurnsidePaqb.false_of_one_add_prime_mul_isIntegral`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#false-of-one-add-prime-mul-is-integral).

## One-dimensional representations act by their character

Let $\rho$ be a representation
of a group $G$ on a complex vector space $V$ of dimension $1$, and let $\chi$ be the character of
$\rho$. Then for every $g \in G$ the operator $\rho(g)$ is multiplication by the scalar $\chi(g)$,
that is, $\rho(g) = \chi(g) \cdot \mathrm{id}_V$.

Formalized by `BurnsidePaqb.eq_smul_one_of_finrank_one`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#eq-smul-one-of-finrank-one).

## A linear character as a homomorphism to $\mathbb{C}^\times$

Let $G$ be a finite group and
let $\rho$ be a representation of $G$ on a complex vector space $V$ of dimension $1$, with
character $\chi$. This is the group homomorphism from $G$ to the multiplicative group
$\mathbb{C}^\times$ of nonzero complex numbers that sends $g$ to $\chi(g)$.

Formalized by `BurnsidePaqb.linearCharHom`, a definition declared in [MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#linear-char-hom).

## A simple group with a nontrivial linear character has prime order

Let $G$ be a finite
simple group and let $\rho$ be a representation of $G$ on a complex vector space $V$ of
dimension $1$. If the character of $\rho$ is not the constant function $1$, then the order of
$G$ is a prime number.

Formalized by `BurnsidePaqb.card_eq_prime_of_nontrivial_linear`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#card-eq-prime-of-nontrivial-linear).

## Nonlinear irreducible characters of a simple group vanish on nonidentity classes of coprime size

**Nonlinear irreducible characters of a simple group vanish on nonidentity classes of
coprime size.** Let $G$ be a finite simple group, let $\rho$ be an irreducible representation of
$G$ on a finite-dimensional complex vector space $V$ of dimension $d > 1$, and let $\chi$ be the
character of $\rho$. If $g \ne 1$ is an element of $G$ whose conjugacy class has size coprime to
$d$, then $\chi(g) = 0$.

Formalized by `BurnsidePaqb.char_zero_of_nonlinear_of_coprime`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#char-zero-of-nonlinear-of-coprime).

## A simple group with a prime-power conjugacy class has prime order

Let $G$ be a finite
simple group and let $g \ne 1$ be an element of $G$ whose conjugacy class has size $r^k$ for some
prime $r$ and some $k \ge 1$. Then the order of $G$ is a prime number.

## Sources

- Bielefeld Corollary 6.

Formalized by `BurnsidePaqb.cor6_of_prime_pow_class`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SimplePrime.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#cor6-of-prime-pow-class).

## Divisors of $p^a q^b$

Let $p$ and $q$ be primes and let $a$ and $b$ be natural numbers.
Every natural number $d$ dividing $p^a q^b$ has the form $d = p^{a'} q^{b'}$ for some natural
numbers $a'$ and $b'$.

Formalized by `BurnsidePaqb.eq_prime_pow_mul_of_dvd`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SolvableInduction.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SolvableInduction.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#eq-prime-pow-mul-of-dvd).

## Groups of prime order are solvable

Every finite group whose order is a prime number is
solvable.

Formalized by `BurnsidePaqb.isSolvable_of_prime_card`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SolvableInduction.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SolvableInduction.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#is-solvable-of-prime-card).

## Burnside's $p^a q^b$ theorem from the prime-power class corollary

Suppose that every
finite simple group $H$ having an element $h \ne 1$ whose conjugacy class has size $r^k$ for some
prime $r$ and some $k \ge 1$ has prime order. Then for all primes $p$ and $q$ and all natural
numbers $a$ and $b$, every finite group $G$ of order $p^a q^b$ is solvable.

## Sources

- Bielefeld Theorem 7.

Formalized by `BurnsidePaqb.burnside_paqb_of_simple_prime`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb/SolvableInduction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb/SolvableInduction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#burnside-paqb-of-simple-prime).

## Burnside's $p^a q^b$ theorem in the lowest universe

Let $G$ be a finite group whose
underlying type lies in the lowest type universe, let $p$ and $q$ be primes and let $a$ and
$b$ be natural numbers. If $G$ has order $p^a q^b$, then $G$ is solvable.

Formalized by `BurnsidePaqb.burnside_paqb_zero`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#burnside-paqb-zero).

## Burnside's $p^a q^b$ theorem

Let $G$ be a finite group, let $p$ and $q$ be primes and
let $a$ and $b$ be natural numbers. If $G$ has order $p^a q^b$, then $G$ is solvable.

Formalized by `BurnsidePaqb.burnside_paqb`, a theorem declared in [MathlibExt/GroupTheory/BurnsidePaqb.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/BurnsidePaqb.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html#burnside-paqb).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Burnside's p^a q^b theorem](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/burnside-s-p-a-q-b-theorem)
