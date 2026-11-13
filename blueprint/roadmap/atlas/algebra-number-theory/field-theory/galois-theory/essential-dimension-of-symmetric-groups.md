---
declaration: section
origin: cited
lean: MathlibExt.FieldTheory.EssentialDimensionSymmetric.rootsField, MathlibExt.FieldTheory.EssentialDimensionSymmetric.root, MathlibExt.FieldTheory.EssentialDimensionSymmetric.coeff, MathlibExt.FieldTheory.EssentialDimensionSymmetric.generalBaseField, MathlibExt.FieldTheory.EssentialDimensionSymmetric.coeffElem, MathlibExt.FieldTheory.EssentialDimensionSymmetric.root_injective, MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraicIndependent_esymm, MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraicIndependent_map
statement: formalized
---

# Essential dimension of symmetric groups

36 results, 29 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html).

## The function field $\mathbb{C}(x_1, \dots, x_n)$

For $n \in \mathbb{N}$, the function
field $\mathbb{C}(x_1, \dots, x_n)$ is the fraction field of the polynomial ring
$\mathbb{C}[x_1, \dots, x_n]$ in $n$ indeterminates.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.rootsField`, an abbreviation declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#roots-field).

## The roots $x_i$

For $n \in \mathbb{N}$ and $i \in \{1, \dots, n\}$, $x_i$ is the $i$-th
indeterminate of the polynomial ring $\mathbb{C}[x_1, \dots, x_n]$, viewed as an element of its
fraction field, the function field $\mathbb{C}(x_1, \dots, x_n)$.

These elements are the roots of the general polynomial.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.root`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#root).

## The coefficients of the general polynomial

For $0 \le i < n$, the coefficient
$a_{i+1}$ is the $(i+1)$-st elementary symmetric function of $x_1, \dots, x_n$, as an element of
the function field $\mathbb{C}(x_1, \dots, x_n)$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.coeff`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#coeff).

## Coefficient field of the general polynomial

For a natural number $n$, let
$\mathbb{C}(x_1, \dots, x_n)$ be the field of rational functions in $n$ indeterminates and,
for $1 \le k \le n$, let $a_k$ be the $k$-th elementary symmetric function of
$x_1, \dots, x_n$. The coefficient field $\mathbb{C}(a_1, \dots, a_n)$ is the intermediate
field of $\mathbb{C} \subseteq \mathbb{C}(x_1, \dots, x_n)$ generated over $\mathbb{C}$ by
$a_1, \dots, a_n$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.generalBaseField`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#general-base-field).

## Coefficients in the coefficient field

For $0 \le i < n$, the coefficient $a_{i+1}$,
the $(i+1)$-st elementary symmetric function of $x_1, \dots, x_n$, regarded as an element of the
coefficient field $\mathbb{C}(a_1, \dots, a_n)$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.coeffElem`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#coeff-elem).

## The roots $x_i$ are pairwise distinct

For every $n \in \mathbb{N}$, the elements
$x_1, \dots, x_n$ of the function field $\mathbb{C}(x_1, \dots, x_n)$ are pairwise distinct:
$x_i = x_j$ implies $i = j$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.root_injective`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#root-injective).

## Algebraic independence of the elementary symmetric polynomials

For every natural number
$n$, the elementary symmetric polynomials $e_1, \dots, e_n \in \mathbb{C}[X_1, \dots, X_n]$ are
algebraically independent over $\mathbb{C}$.

This follows from the fundamental theorem of symmetric polynomials.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraicIndependent_esymm`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#algebraic-independent-esymm).

## Injective algebra maps preserve algebraic independence

Let $A$ and $B$ be commutative
$\mathbb{C}$-algebras, let $f : A \to B$ be an injective $\mathbb{C}$-algebra homomorphism, and
let $(x_i)_{i \in \iota}$ be a family in $A$ that is algebraically independent over
$\mathbb{C}$. Then the family $(f(x_i))_{i \in \iota}$ is algebraically independent over
$\mathbb{C}$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraicIndependent_map`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#algebraic-independent-map).

## The coefficients are algebraically independent

For every natural number $n$, the
coefficients $a_1, \dots, a_n$ of the general polynomial, the elementary symmetric functions of
$x_1, \dots, x_n$, are algebraically independent over $\mathbb{C}$ in the function field
$\mathbb{C}(x_1, \dots, x_n)$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraicIndependent_coeff`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#algebraic-independent-coeff).

## The roots are algebraically independent

For every natural number $n$, the roots
$x_1, \dots, x_n$ are algebraically independent over $\mathbb{C}$ in the function field
$\mathbb{C}(x_1, \dots, x_n)$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraicIndependent_root`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#algebraic-independent-root).

## Polynomials in the roots

For every natural number $n$ and every polynomial
$p \in \mathbb{C}[X_1, \dots, X_n]$, the image of $p$ in the function field
$\mathbb{C}(x_1, \dots, x_n)$ lies in the $\mathbb{C}$-subalgebra generated by the roots
$x_1, \dots, x_n$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraMap_mem_adjoin_roots`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#algebra-map-mem-adjoin-roots).

## Rational functions are algebraic over the polynomial subalgebra

For a natural number
$n$, every element of the field $\mathbb{C}(x_1, \dots, x_n)$ of rational functions in $n$
indeterminates is algebraic over the $\mathbb{C}$-subalgebra generated by $x_1, \dots, x_n$:
it is a ratio of two polynomials in $x_1, \dots, x_n$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.isAlgebraic_adjoin_roots`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#is-algebraic-adjoin-roots).

## Transcendence degree of $\mathbb{C}(x_1, \dots, x_n)$

For every $n \in \mathbb{N}$, the
function field $\mathbb{C}(x_1, \dots, x_n)$ has transcendence degree $n$ over $\mathbb{C}$, as a
cardinal.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.trdeg_rootsField`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#trdeg-roots-field).

## Numeric transcendence degree

For a field $F$ that is a $\mathbb{C}$-algebra, the numeric
transcendence degree of $F$ is its transcendence degree over $\mathbb{C}$ as a natural number when
that degree is finite, and $0$ when it is infinite.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.transDegNat`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#trans-deg-nat).

## Elementary symmetric polynomials evaluated at the roots

For all natural numbers $n$
and $k$, the image of the $k$-th elementary symmetric polynomial
$e_k \in \mathbb{C}[X_1, \dots, X_n]$ in the function field $\mathbb{C}(x_1, \dots, x_n)$ is the
$k$-th elementary symmetric function of the multiset of roots $\{x_1, \dots, x_n\}$, that is,
the sum of the products $x_{i_1} \cdots x_{i_k}$ over all $i_1 < \dots < i_k$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.algebraMap_esymm`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#algebra-map-esymm).

## Coefficients indexed by degree

Let $n$ be a natural number, for $1 \le k \le n$ let $a_k$
be the $k$-th elementary symmetric function of $x_1, \dots, x_n$ in the function field
$\mathbb{C}(x_1, \dots, x_n)$, and let $\mathbb{C}(a_1, \dots, a_n)$ be the coefficient field. For
each natural number $k$, the element $c_k$ of $\mathbb{C}(a_1, \dots, a_n)$ is defined by
$c_0 = 1$, $c_k = a_k$ for $1 \le k \le n$, and $c_k = 0$ for $k > n$.

In a variable $X$, the general polynomial is $\sum_{k=0}^{n} (-1)^k c_k X^{n-k}$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.coeffNat`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#coeff-nat).

## General polynomial

For a natural number $n$, let $x_1, \dots, x_n$ be the
indeterminates of the rational function field $\mathbb{C}(x_1, \dots, x_n)$, let $a_0 = 1$ and,
for $1 \le k \le n$, let $a_k$ be the $k$-th elementary symmetric function of
$x_1, \dots, x_n$. The general polynomial of degree $n$ is the polynomial
$\sum_{j=0}^{n} (-1)^j a_j X^{n-j} = X^n - a_1 X^{n-1} + \cdots + (-1)^n a_n$ with
coefficients in the coefficient field $\mathbb{C}(a_1, \dots, a_n)$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.generalPolynomial`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#general-polynomial).

## Distinct linear factors are coprime

For a natural number $n$ and distinct elements
$a \ne b$ of the field $\mathbb{C}(x_1, \dots, x_n)$ of rational functions in $n$
indeterminates, the polynomials $X - a$ and $X - b$ are coprime in
$\mathbb{C}(x_1, \dots, x_n)[X]$: there are polynomials $u$ and $v$ with
$u (X - a) + v (X - b) = 1$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.isCoprime_X_sub_C_of_ne`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#is-coprime-x-sub-c-of-ne).

## The product of the linear factors $X - x_i$ is separable

For every $n \in \mathbb{N}$,
the polynomial $\prod_{i=1}^{n} (X - x_i)$ over the function field
$\mathbb{C}(x_1, \dots, x_n)$ is separable.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.separable_prod_roots`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#separable-prod-roots).

## The roots generate the function field

For every natural number $n$, the intermediate
field of $\mathbb{C}(x_1, \dots, x_n)$ generated over $\mathbb{C}$ by the roots
$x_1, \dots, x_n$ is the whole function field $\mathbb{C}(x_1, \dots, x_n)$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.adjoin_roots_eq_top`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#adjoin-roots-eq-top).

## Each $x_i$ is a root of the general polynomial

For $n \in \mathbb{N}$, let
$E_n = \mathbb{C}(x_1, \dots, x_n)$, let $a_k$ be the $k$-th elementary symmetric function of
$x_1, \dots, x_n$, and let $f_n = X^n - a_1 X^{n-1} + \cdots + (-1)^n a_n$ be the general
polynomial, with coefficients in $F_n = \mathbb{C}(a_1, \dots, a_n) \subseteq E_n$. Then
$f_n(x_i) = 0$ in $E_n$ for every $i \in \{1, \dots, n\}$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.root_mem_generalPolynomial_roots`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#root-mem-general-polynomial-roots).

## Transcendence degree of the coefficient field

For $n \in \mathbb{N}$, let $a_k$ be the
$k$-th elementary symmetric function of $x_1, \dots, x_n$ in $\mathbb{C}(x_1, \dots, x_n)$. The
coefficient field $F_n = \mathbb{C}(a_1, \dots, a_n)$ of the general polynomial has numeric
transcendence degree $n$ over $\mathbb{C}$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.transDegNat_generalBaseField`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#trans-deg-nat-general-base-field).

## Descent of the general polynomial extension

For a natural number $n$, let
$E = \mathbb{C}(x_1, \dots, x_n)$ be the field of rational functions in $n$ indeterminates and
let $F = \mathbb{C}(a_1, \dots, a_n) \subseteq E$ be the coefficient field of the general
polynomial, where $a_k$ is the $k$-th elementary symmetric function of $x_1, \dots, x_n$. A
pair $(F_0, E_0)$ of intermediate fields of $\mathbb{C} \subseteq E$ is a descent when
$F_0 \subseteq F$, $F_0 \subseteq E_0$, $E_0 \cap F = F_0$, the compositum of $E_0$ and $F$ is
all of $E$, and there is a nonzero polynomial $p$ with coefficients in $F_0$ whose image in
$E[X]$ splits and is separable, such that $E_0$ is the field generated over $F_0$ by the
roots of $p$ in $E$.

Splitting and separability are imposed in $E$, where they say that the roots of $p$ are all
present and distinct.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.IsDescent`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#is-descent).

## The roots of the general polynomial generate the function field

For $n \in \mathbb{N}$,
let $E_n = \mathbb{C}(x_1, \dots, x_n)$, let $a_k$ be the $k$-th elementary symmetric function
of $x_1, \dots, x_n$, let $F_n = \mathbb{C}(a_1, \dots, a_n) \subseteq E_n$ be the coefficient
field, and let $f_n = X^n - a_1 X^{n-1} + \cdots + (-1)^n a_n \in F_n[X]$ be the general
polynomial. The subfield of $E_n$ generated over $F_n$ by all roots of $f_n$ in $E_n$ is $E_n$
itself.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.restrictScalars_adjoin_generalPolynomial`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#restrict-scalars-adjoin-general-polynomi).

## The trivial descent

For every natural number $n$, the pair $(F, E)$ is a descent of
the general polynomial extension, where $E = \mathbb{C}(x_1, \dots, x_n)$ is the field of
rational functions in $n$ indeterminates and $F = \mathbb{C}(a_1, \dots, a_n)$ is the
coefficient field, generated over $\mathbb{C}$ by the elementary symmetric functions
$a_1, \dots, a_n$ of $x_1, \dots, x_n$.

The general polynomial serves as the defining polynomial of this descent.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.isDescent_generalBaseField`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#is-descent-general-base-field).

## Essential dimension of the symmetric group

For a natural number $n$, let
$\mathbb{C}(x_1, \dots, x_n)$ be the field of rational functions in $n$ indeterminates. The
essential dimension of $S_n$ over $\mathbb{C}$, in the general-polynomial parameter sense, is
the least natural number $d$ such that some intermediate field $F_0$ of
$\mathbb{C} \subseteq \mathbb{C}(x_1, \dots, x_n)$ of transcendence degree at most $d$ over
$\mathbb{C}$ admits an intermediate field $E_0$ for which $(F_0, E_0)$ is a descent of the
general polynomial extension.

The transcendence degree is read as a natural number (an infinite degree would count as $0$;
this does not occur, since $F_0$ lies in the coefficient field).

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.edSn`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ed-sn).

## Trivial upper bound for the essential dimension of $S_n$

For every natural
number $n$, the essential dimension of the symmetric group $S_n$ over $\mathbb{C}$, in the
general-polynomial parameter sense, is at most $n$.

The bound comes from the trivial descent, whose parameter field is the coefficient field of
the general polynomial, of transcendence degree $n$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.edSn_le`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ed-sn-le).

## Asymptotic essential-dimension ratio of the symmetric groups

The catalogue constant
$C_{79}$ is the limit superior, as $n \to \infty$, of $\operatorname{ed}_{\mathbb{C}}(S_n) / n$,
where $\operatorname{ed}_{\mathbb{C}}(S_n)$ is the essential dimension of the symmetric group
$S_n$ over $\mathbb{C}$ in the general-polynomial parameter sense.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.essDimRatio`, a definition declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ess-dim-ratio).

## The essential-dimension ratio of the symmetric groups is at most one

The constant
$C_{79}$, the limit superior as $n \to \infty$ of $\operatorname{ed}_{\mathbb{C}}(S_n) / n$ with
the essential dimension of $S_n$ over $\mathbb{C}$ taken in the general-polynomial parameter
sense, satisfies $C_{79} \le 1$.

Formalized by `MathlibExt.FieldTheory.EssentialDimensionSymmetric.essDimRatio_le_one`, a theorem declared in [MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/EssentialDimensionSymmetric.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ess-dim-ratio-le-one).

## Upper bound for the essential dimension of symmetric groups

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\operatorname{ed}(S_n) \le n - 3$ for every natural number $n \ge 5$.

## Sources

- Buhler--Reichstein (1997), the classical Tschirnhaus bound `ed_ℂ(Sₙ) ≤ n - 3` for `n ≥ 5`.

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.buhlerReichstein1997UpperBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#buhler-reichstein1997-upper-bound-wanted).

## Lower bound for the essential dimension of symmetric groups

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\lfloor n/2 \rfloor \le \operatorname{ed}(S_n)$ for every natural number $n$.

## Sources

- Buhler--Reichstein (1997) and Duncan, the lower bound `⌊n/2⌋ ≤ ed_ℂ(Sₙ)`.

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.buhlerReichsteinDuncanLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#buhler-reichstein-duncan-lower-bound-wan).

## Lower bound for the asymptotic essential-dimension ratio

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\limsup_{n \to \infty} \operatorname{ed}(S_n)/n \ge 1/2$.

## Sources

- catalogue lower row for `C₇₉`, from the `⌊n/2⌋` lower bound: `1/2 ≤ C₇₉`.

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.essDimRatioLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ess-dim-ratio-lower-bound-wanted).

## Essential dimension of the symmetric group on five letters

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\operatorname{ed}(S_5) = 2$.

## Sources

- Buhler--Reichstein (1997), exact value `ed_ℂ(S₅) = 2`: their general bounds `⌊5/2⌋ ≤ ed_ℂ(S₅) ≤ 5 - 3` coincide at `2`. The classical Bring--Jerrard form `X^5 + pX + q` is not the descent behind that upper bound here: producing it already requires solving auxiliary equations over an extension of the coefficient field, and normalizing further to `X^5 + X + a` is again only a scaling over an extension, so neither form witnesses a descent over the original field in the sense of this file (in particular nothing here implies `edSn 5 ≤ 1`).

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.edSn_five_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ed-sn-five-wanted).

## Essential dimension of the symmetric group on four letters

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\operatorname{ed}(S_4) = 2$.

## Sources

- Buhler--Reichstein (1997), exact value `ed_ℂ(S₄) = 2`.

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.edSn_four_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ed-sn-four-wanted).

## Essential dimension of the symmetric group on six letters

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\operatorname{ed}(S_6) = 3$.

## Sources

- Buhler--Reichstein (1997), exact value `ed_ℂ(S₆) = 3`.

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.edSn_six_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ed-sn-six-wanted).

## Essential dimension of the symmetric group on seven letters

Write
$\operatorname{ed}(S_n)$ for the essential dimension of the symmetric group $S_n$ over
$\mathbb{C}$ in the general-polynomial sense: the least transcendence degree over $\mathbb{C}$
of a subfield $F_0$ of the coefficient field $\mathbb{C}(a_1, \dots, a_n)$ of the general
polynomial of degree $n$ over which that polynomial descends up to Tschirnhaus transformation.
Then $\operatorname{ed}(S_7) = 4$.

## Sources

- Duncan (2010), *Essential dimensions of `A₇` and `S₇`*, exact value `ed_ℂ(S₇) = 4`. Buhler--Reichstein's general bounds give only `3 ≤ ed_ℂ(S₇) ≤ 4` here.

Stated but not proved: `MathlibExt.FieldTheory.EssentialDimensionSymmetricWanted.edSn_seven_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EssentialDimensionSymmetricWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html#ed-sn-seven-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Essential dimension of symmetric groups](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/galois-theory/essential-dimension-of-symmetric-groups)
