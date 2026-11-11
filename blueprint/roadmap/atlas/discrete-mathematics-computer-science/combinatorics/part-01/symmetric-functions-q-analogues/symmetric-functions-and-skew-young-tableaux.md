---
declaration: section
origin: cited
lean: MetaMathlibExt.MvPolynomial.omegaAlgHom, MvPowerSeries.exponentialSpecialization, MetaMathlibExt.symmetricScalarProduct, MetaMathlibExt.SkewShape, MetaMathlibExt.SkewSemistandardYoungTableau, MetaMathlibExt.SkewStandardYoungTableau
statement: formalized
proof: formalized
---

# Symmetric functions and skew Young tableaux

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html).

## The omega homomorphism on symmetric polynomials

Let $R$ be a commutative ring and let $V$
be a finite set with $n$ elements. A polynomial in $R[x_v : v \in V]$ is symmetric if it is
unchanged by every permutation of the variables. For $k \ge 0$, the elementary symmetric polynomial
$e_k$ is the sum of $\prod_{v \in T} x_v$ over all $k$-element subsets $T \subseteq V$, and the
complete homogeneous symmetric polynomial $h_k$ is the sum of $\prod_{v \in M} x_v$ over all
multisets $M$ of size $k$ with elements from $V$, each element counted with its multiplicity.
Every symmetric polynomial $f$ equals $P(e_1, \dots, e_n)$ for exactly one polynomial
$P \in R[y_1, \dots, y_n]$. The omega homomorphism $\omega$ is the $R$-algebra homomorphism from the
symmetric polynomials in $R[x_v : v \in V]$ to themselves given by
$\omega(P(e_1, \dots, e_n)) = P(h_1, \dots, h_n)$; equivalently, it is the unique $R$-algebra
homomorphism with $\omega(e_k) = h_k$ for $1 \le k \le n$.

Formalized by `MetaMathlibExt.MvPolynomial.omegaAlgHom`, a definition declared in [MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html#omega-alg-hom).

## Exponential specialization

Let $\mathbb{Q}[[x_1, x_2, \dots]]$ be the ring of formal
power series in the variables $x_1, x_2, \dots$ with rational coefficients: its elements are the
formal sums $f = \sum_\alpha c_\alpha x^\alpha$, where $\alpha = (\alpha_1, \alpha_2, \dots)$
runs over the sequences of nonnegative integers with only finitely many nonzero terms,
$c_\alpha \in \mathbb{Q}$ and $x^\alpha = x_1^{\alpha_1} x_2^{\alpha_2} \cdots$. For $m \ge 0$,
write $[x_1 \cdots x_m] f$ for the coefficient in $f$ of the monomial $x_1 x_2 \cdots x_m$; for
$m = 0$ this is the constant term of $f$. The exponential specialization of $f$ is the formal
power series in one variable $t$

$$\operatorname{ex}(f) = \sum_{m \ge 0} \frac{[x_1 \cdots x_m] f}{m!} \, t^m \in \mathbb{Q}[[t]].$$

Formalized by `MvPowerSeries.exponentialSpecialization`, a definition declared in [MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html#exponential-specialization).

## Scalar product of symmetric polynomials

Let $n \ge 0$, let $R$ be a commutative ring, and
call a polynomial in $R[x_1, \dots, x_n]$ symmetric if it is unchanged by every permutation of the
variables. Let $a_\delta = \prod_{1 \le i < j \le n} (x_i - x_j)$, so that $a_\delta = 1$ when
$n \le 1$. For a sequence $\lambda = (\lambda_1, \dots, \lambda_n)$ of
integers with $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n \ge 0$, write $c_\lambda(P)$ for the
coefficient in a polynomial $P$ of the monomial
$x^{\lambda+\delta} = \prod_{i=1}^{n} x_i^{\lambda_i + n - i}$; when $n = 0$ the only such sequence
is the empty one and $x^{\lambda+\delta} = 1$. The scalar product of symmetric polynomials $f$ and
$g$ in $R[x_1, \dots, x_n]$ is

$$\langle f, g \rangle_n = \sum_{\lambda} c_\lambda(a_\delta f) \, c_\lambda(a_\delta g),$$

the sum taken over all sequences $\lambda$ as above; only finitely many terms are nonzero.

Formalized by `MetaMathlibExt.symmetricScalarProduct`, a definition declared in [MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html#symmetric-scalar-product).

## Skew shape

A partition is a finite weakly decreasing sequence
$\lambda = (\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_m)$ of positive integers, possibly empty
($m = 0$); set $\lambda_k = 0$ for $k > m$. Its diagram is the set
$D(\lambda) = \{(i, j) \in \mathbb{Z}_{\ge 1} \times \mathbb{Z}_{\ge 1} : j \le \lambda_i\}$ of
cells, where the cell $(i, j)$ lies in row $i$ and column $j$, and a partition is identified with
its diagram. For partitions $\lambda$ and $\mu$ write $\mu \subseteq \lambda$ when
$D(\mu) \subseteq D(\lambda)$. A skew shape $\lambda/\mu$ is an ordered pair of partitions, an
outer partition $\lambda$ and an inner partition $\mu$, with $\mu \subseteq \lambda$.

Formalized by `MetaMathlibExt.SkewShape`, a structure declared in [MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html#skew-shape).

## Semistandard Young tableau of skew shape

Let $\lambda/\mu$ be a skew shape, and write
$\lambda_k$ and $\mu_k$ for the $k$-th parts of $\lambda$ and $\mu$, with $\lambda_k = 0$
($\mu_k = 0$) when $\lambda$ ($\mu$) has fewer than $k$ parts. The cells of $\lambda/\mu$ are the
pairs $(i, j) \in \mathbb{Z}_{\ge 1} \times \mathbb{Z}_{\ge 1}$ with $\mu_i < j \le \lambda_i$,
that is, the cells of $D(\lambda)$ that are not cells of $D(\mu)$. A semistandard Young tableau
of shape $\lambda/\mu$ is a function $T$ assigning a nonnegative integer $T_{i,j}$ to every pair
$(i, j) \in \mathbb{Z}_{\ge 1} \times \mathbb{Z}_{\ge 1}$ such that $T_{i,j} \ge 1$ for every cell
$(i, j)$ of $\lambda/\mu$; $T_{i,j} \le T_{i,j'}$ whenever $(i, j)$ and $(i, j')$ are cells of
$\lambda/\mu$ with $j < j'$ (rows weakly increase); $T_{i,j} < T_{i',j}$ whenever $(i, j)$ and
$(i', j)$ are cells of $\lambda/\mu$ with $i < i'$ (columns strictly increase); and $T_{i,j} = 0$
for every pair $(i, j)$ that is not a cell of $\lambda/\mu$.

Formalized by `MetaMathlibExt.SkewSemistandardYoungTableau`, a structure declared in [MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html#skew-semistandard-young-tableau).

## Standard Young tableau of skew shape

Let $\lambda/\mu$ be a skew shape, let $n$ be the
number of cells of $\lambda/\mu$ (the cells of $D(\lambda)$ that are not cells of $D(\mu)$), and
write $[n] = \{1, \dots, n\}$, so that $[0] = \emptyset$. A standard Young tableau of shape
$\lambda/\mu$ is a semistandard Young tableau $T$ of shape $\lambda/\mu$ such that the map
$(i, j) \mapsto T_{i,j}$ sends the cells of $\lambda/\mu$ bijectively onto $[n]$. If
$\mu = \emptyset$, a standard Young tableau of shape $\lambda/\emptyset$ is also called a standard
Young tableau of shape $\lambda$.

Formalized by `MetaMathlibExt.SkewStandardYoungTableau`, a structure declared in [MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SymmetricFunctionsYoungTableaux.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html#skew-standard-young-tableau).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Symmetric functions and skew Young tableaux](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/symmetric-functions-and-skew-young-tableaux)
