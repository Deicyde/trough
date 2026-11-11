---
declaration: section
origin: cited
lean: MetaMathlibExt.ascPochhammer_eval_add, MetaMathlibExt.ClassicalOrthogonalPolynomialFamily, MetaMathlibExt.riordan_coeff_orth_equiv
statement: formalized
proof: formalized
---

# Orthogonal polynomials and polynomial sequences: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/index.html).

Classical and combinatorial families of polynomials, their recurrences and generating functions, and orthogonality via Favard's theorem, J-fractions and Riordan arrays.

## Binomial theorem for rising factorials

For every natural number $n$ and all real numbers
$a$ and $b$, writing $x^{\overline{m}} = x(x+1)\cdots(x+m-1)$ for the rising factorial,

$$(a+b)^{\overline{n}} = \sum_{k=0}^{n} \binom{n}{k}\, a^{\overline{k}}\, b^{\overline{n-k}}.$$

## Sources

- Paul Eloe and Catherine Kublik, "When Numerical Analysis Crosses Paths with Catalan and Generalized Motzkin Numbers," Journal of Integer Sequences 21 (2018), Article 18.8.4, Theorem, equation, lines 156–161, https://cs.uwaterloo.ca/journals/JIS/VOL21/Kublik/kublik2.tex

Formalized by `MetaMathlibExt.ascPochhammer_eval_add`, a theorem declared in [MathlibExt/Algebra/Polynomial/RisingFactorialBinomial.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RisingFactorialBinomial.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/index.html#asc-pochhammer-eval-add).

## Classical orthogonal polynomial family

A classical orthogonal polynomial family consists
of real polynomials $P_0, P_1, P_2, \dots$, each $P_n$ monic of degree exactly $n$, a measure
$\mu$ on $\mathbb{R}$, a measurable set $D \subseteq \mathbb{R}$ that is an interval with
nonempty interior, and a function $w : \mathbb{R} \to \mathbb{R}$ (the weight), such that
$w(x) \ge 0$ for every $x \in D$; $\mu$ is the measure with density $w$ with respect to
Lebesgue measure restricted to $D$; $\int P_m P_n \, d\mu = 0$ whenever $m \ne n$;
$\int P_n^2 \, d\mu \ne 0$ for every $n$; and there are real numbers $u_0, u_1, v_0, v_1, v_2$,
with $v_0, v_1, v_2$ not all zero, such that at every interior point $x$ of $D$ the weight is
differentiable and $(v_0 + v_1 x + v_2 x^2) \, w'(x) = (u_0 + u_1 x) \, w(x)$ (the Pearson
equation).

Formalized by `MetaMathlibExt.ClassicalOrthogonalPolynomialFamily`, a structure declared in [MathlibExt/Analysis/SpecialFunctions/ClassicalOrthogonalPolynomial.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ClassicalOrthogonalPolynomial.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/index.html#classical-orthogonal-polynomial-family).

## Meixner-type characterization of Riordan orthogonal polynomial arrays

Let $d$ and $h$ be
real formal power series with $[x^0]\,h = 0$, $[x^1]\,h \ne 0$ and $[x^0]\,d \ne 0$, where
$[x^n]$ denotes the coefficient of $x^n$, and let $L$ be the Riordan array of $(d, h)$, with
entries $L_{n,k} = [x^n]\,(d h^k)$ for $n, k \ge 0$. Call $L$ a monic orthogonal coefficient
array if there are real polynomials $P_0, P_1, \dots$ with $[x^k]\,P_n = L_{n,k}$ for all
$n, k$, each $P_n$ monic, and the family $(P_n)$ formally orthogonal. Each of the following
three conditions is equivalent to $L$ being a monic orthogonal coefficient array.

1. Meixner form: there are real numbers $\lambda, \mu, r, s$ with $s \ne 0$ and $s + \mu \ne 0$
   such that $d\,(1 + r x + s x^2) = 1 - \lambda x - \mu x^2$ and $h\,(1 + r x + s x^2) = x$.
2. Stieltjes form of the inverse: $L_{0,0} = 1$, and there are an array $(L'_{n,k})$ and real
   numbers $r_1, s_1, r, s$ with $s_1 \ne 0$ and $s \ne 0$ such that $L_{n,k} = L'_{n,k} = 0$
   whenever $k > n$; $\sum_{j=0}^{n} L_{n,j} L'_{j,k}$ and $\sum_{j=0}^{n} L'_{n,j} L_{j,k}$
   both equal $1$ if $n = k$ and $0$ otherwise; and
   $L'_{n+1,k} = \sum_{j=0}^{n+1} L'_{n,j} S_{j,k}$ for all $n, k$, where $S$ is the
   Stieltjes matrix with parameters $r_1, s_1, r, s$: its superdiagonal entries are $1$, its
   diagonal is $r_1, r, r, \dots$, its subdiagonal is $s_1, s, s, \dots$, and all other
   entries are $0$.
3. Coefficient recurrence: there are real numbers $\lambda, \mu, r, s$ with $s \ne 0$ and
   $s + \mu \ne 0$ such that for all $N, K \ge 0$,
   $L_{N,K} + r L_{N-1,K} - L_{N-1,K-1} + s L_{N-2,K} = c_{N,K}$, where any entry of $L$
   with a negative index is read as $0$, $c_{0,0} = 1$, $c_{1,0} = -\lambda$,
   $c_{2,0} = -\mu$, and $c_{N,K} = 0$ otherwise.

Proof: The coefficient recurrence is the common hub. The Meixner equivalence follows from
Barry-Hennessy, the orthogonality equivalence from Favard's theorem as in Chihara, and the
inverse-array equivalence from the Stieltjes production construction of the inverse array.

## Sources

- Paul Barry and Aoife Hennessy, "Meixner-Type Results for Riordan Arrays and Associated Integer Sequences," Journal of Integer Sequences 13 (2010), Article 10.9.4, Proposition (referee's summary of the main results), lines 733–752, https://cs.uwaterloo.ca/journals/JIS/VOL13/Barry5/barry96s.tex

Formalized by `MetaMathlibExt.riordan_coeff_orth_equiv`, a theorem declared in [MathlibExt/Algebra/Polynomial/RiordanOrthogonalPolynomials.lean, line 2710](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RiordanOrthogonalPolynomials.lean#L2710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/index.html#riordan-coeff-orth-equiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orthogonal polynomials and polynomial sequences](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/orthogonal-polynomials)
