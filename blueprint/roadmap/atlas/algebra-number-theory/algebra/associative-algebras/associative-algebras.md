---
declaration: section
origin: cited
lean: MathlibExt.Algebra.Algebra.AmitsurLevitzkiWanted.amitsur_levitzki, MathlibExt.Algebra.Algebra.BurnsideMatrixWanted.burnside_matrix, MathlibExt.Algebra.Algebra.FrobeniusDivisionWanted.frobenius_real_division_algebra, MathlibExt.Algebra.Central.SkolemNoether.skolem_noether
statement: formalized
proof: formalized
---

# Associative rings and algebras: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/index.html).

Noncommutative rings and finite-dimensional associative algebras, including division and central simple algebras, quaternion algebras, polynomial identities, nil ideals and Hopf algebras. Group rings are under Group Theory.

## Amitsur–Levitzki theorem

Let $R$ be a commutative ring and $n$ a natural number. For all
$n \times n$ matrices $M_1, \dots, M_{2n}$ over $R$, the sum over all permutations $\sigma$ of
$\{1, \dots, 2n\}$ of $\mathrm{sgn}(\sigma) M_{\sigma(1)} M_{\sigma(2)} \cdots M_{\sigma(2n)}$ is
the zero matrix, where $\mathrm{sgn}(\sigma) \in \{1, -1\}$ is the sign of $\sigma$. In other
words, the standard polynomial of degree $2n$ vanishes on $n \times n$ matrices over $R$.

## Sources

- A. S. Amitsur and J. Levitzki, Minimal identities for algebras, Proc. Amer. Math. Soc. 1 (1950), 449-463, DOI 10.1090/S0002-9939-1950-0036751-9; textbook in Rowen, Polynomial Identities in Ring Theory.

Formalized by `MathlibExt.Algebra.Algebra.AmitsurLevitzkiWanted.amitsur_levitzki`, a theorem declared in [MathlibExt/Algebra/Algebra/AmitsurLevitzki.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Algebra/AmitsurLevitzki.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/index.html#amitsur-levitzki).

## Burnside's theorem on matrix algebras

Let $k$ be an algebraically closed field, $n$ a natural
number, and $A$ a $k$-subalgebra of the algebra $M_n(k)$ of $n \times n$ matrices over $k$.
Suppose that the only subspaces $W$ of $k^n$ with $Mv \in W$ for all $M \in A$ and all $v \in W$
are $0$ and $k^n$. Then $A = M_n(k)$.

## Sources

- W. Burnside, On the condition of reducibility of any group of linear substitutions, Proc. London Math. Soc. 3 (1905), 430–434, DOI 10.1112/plms/s2-3.1.430; textbook in Lam, First Course in Noncommutative Rings, Thm 1.2. Burnside's theorem on matrix algebras / Burnside density.

Formalized by `MathlibExt.Algebra.Algebra.BurnsideMatrixWanted.burnside_matrix`, a theorem declared in [MathlibExt/Algebra/Algebra/BurnsideMatrix.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Algebra/BurnsideMatrix.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/index.html#burnside-matrix).

## Frobenius theorem on real division algebras

Let $A$ be a finite-dimensional associative
unital division algebra over $\mathbb{R}$. Then $A$ is isomorphic as an $\mathbb{R}$-algebra to
$\mathbb{R}$, to $\mathbb{C}$, or to the algebra $\mathbb{H}$ of real quaternions.

## Sources

- G. Frobenius, Ueber lineare Substitutionen und bilineare Formen, J. reine angew. Math. 84 (1878), 1–63, DOI 10.1515/crelle-1878-18788403; textbook in Jacobson, Basic Algebra II; Lean states associative unital case via `DivisionRing` excluding octonions intentionally.

Formalized by `MathlibExt.Algebra.Algebra.FrobeniusDivisionWanted.frobenius_real_division_algebra`, a theorem declared in [MathlibExt/Algebra/Algebra/FrobeniusDivision.lean, line 862](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Algebra/FrobeniusDivision.lean#L862). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/index.html#frobenius-real-division-algebra).

## Skolem–Noether theorem

Let $k$ be a field and let $A$ be a finite-dimensional central
simple algebra over $k$. Then every $k$-algebra automorphism $\sigma$ of $A$ is inner: there is
a unit $u \in A^\times$ such that $\sigma(x) = u x u^{-1}$ for all $x \in A$.

## Sources

- T. Skolem, Zur Theorie der assoziativen Zahlensysteme, Skrifter Vidensk. Kristiania I (1927), no. 12; E. Noether, Nichtkommutative Algebra, Math. Z. 37 (1933), 514-541, DOI 10.1007/BF01474591.

Formalized by `MathlibExt.Algebra.Central.SkolemNoether.skolem_noether`, a theorem declared in [MathlibExt/Algebra/Central/SkolemNoether.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Central/SkolemNoether.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/index.html#skolem-noether).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Associative rings and algebras](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/associative-algebras)
