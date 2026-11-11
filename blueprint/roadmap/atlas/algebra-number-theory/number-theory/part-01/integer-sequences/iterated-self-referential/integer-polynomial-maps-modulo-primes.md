---
declaration: section
origin: cited
lean: MetaMathlibExt.IntegerPolynomialMap, MetaMathlibExt.IntegerPolynomialMap.toFun, MetaMathlibExt.IntegerPolynomialMap.toFunReduce, MetaMathlibExt.IntegerPolynomialMap.iterate, MetaMathlibExt.IntegerPolynomialMap.iterateReduce
statement: formalized
proof: formalized
---

# Integer polynomial maps modulo primes

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html).

## Integer polynomial map

For natural numbers $n$ and $m$, an integer polynomial map from
$n$ variables to $m$ components is an $m$-tuple $F = (F_0, \dots, F_{m-1})$ of polynomials with
integer coefficients in the $n$ variables $x_0, \dots, x_{n-1}$.

Formalized by `MetaMathlibExt.IntegerPolynomialMap`, a definition declared in [MathlibExt/NumberTheory/IntegerPolynomialMap.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerPolynomialMap.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html#integer-polynomial-map).

## Evaluation of an integer polynomial map

Let $F = (F_0, \dots, F_{m-1})$ be an integer
polynomial map from $n$ variables to $m$ components. The value of $F$ at a point
$x \in \mathbb{Z}^n$ is the point $(F_0(x), \dots, F_{m-1}(x)) \in \mathbb{Z}^m$.

Formalized by `MetaMathlibExt.IntegerPolynomialMap.toFun`, a definition declared in [MathlibExt/NumberTheory/IntegerPolynomialMap.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerPolynomialMap.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html#to-fun).

## Reduction of an integer polynomial map modulo a natural number

Let
$F = (F_0, \dots, F_{m-1})$ be an integer polynomial map from $n$ variables to $m$ components and
let $p$ be a natural number. For $x \in (\mathbb{Z}/p\mathbb{Z})^n$, the value of the reduction of
$F$ modulo $p$ at $x$ is $(\bar F_0(x), \dots, \bar F_{m-1}(x)) \in (\mathbb{Z}/p\mathbb{Z})^m$,
where $\bar F_i$ is the polynomial obtained from $F_i$ by reducing its coefficients modulo $p$.

The definition allows an arbitrary natural modulus; the source applies it when $p$ is prime.

Formalized by `MetaMathlibExt.IntegerPolynomialMap.toFunReduce`, a definition declared in [MathlibExt/NumberTheory/IntegerPolynomialMap.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerPolynomialMap.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html#to-fun-reduce).

## Iterates of an integer polynomial map

Let $F$ be an integer polynomial map from $n$
variables to $n$ components, viewed as the map $\mathbb{Z}^n \to \mathbb{Z}^n$ given by
evaluation. For a natural number $k$ and $x \in \mathbb{Z}^n$, the $k$-th iterate of $F$ at $x$ is
$F^k(x)$, the result of applying $F$ to $x$ exactly $k$ times; in particular $F^0(x) = x$.

Formalized by `MetaMathlibExt.IntegerPolynomialMap.iterate`, a definition declared in [MathlibExt/NumberTheory/IntegerPolynomialMap.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerPolynomialMap.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html#iterate).

## Iterates of an integer polynomial map modulo a natural number

Let $F$ be an integer
polynomial map from $n$ variables to $n$ components, let $p$ be a natural number, and let
$\bar F \colon (\mathbb{Z}/p\mathbb{Z})^n \to (\mathbb{Z}/p\mathbb{Z})^n$ be the map obtained by
reducing the coefficients of $F$ modulo $p$ and evaluating. For a natural number $k$ and
$x \in (\mathbb{Z}/p\mathbb{Z})^n$, the $k$-th iterate of $F$ modulo $p$ at $x$ is $\bar F^k(x)$,
the result of applying $\bar F$ to $x$ exactly $k$ times; in particular $\bar F^0(x) = x$.

Formalized by `MetaMathlibExt.IntegerPolynomialMap.iterateReduce`, a definition declared in [MathlibExt/NumberTheory/IntegerPolynomialMap.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IntegerPolynomialMap.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html#iterate-reduce).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer polynomial maps modulo primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/integer-polynomial-maps-modulo-primes)
