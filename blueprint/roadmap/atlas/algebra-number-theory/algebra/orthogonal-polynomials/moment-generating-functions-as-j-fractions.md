---
declaration: section
origin: cited
lean: MetaMathlibExt.moment_generating_function_as_J_fraction_general, MetaMathlibExt.moment_generating_function_as_J_fraction
statement: formalized
proof: formalized
---

# Moment generating functions as J-fractions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/moment-generating-functions-as-j-fractions/index.html).

## Moment generating function as a J-fraction, general form

Let $p_0, p_1, \dots$ be real
polynomials, let $L$ be an $\mathbb{R}$-linear functional on $\mathbb{R}[x]$, and let
$(\alpha_n)$, $(\beta_n)$ and $(\mu_k)$ be real sequences such that $p_0 = 1$,
$p_1 = x - \alpha_0$, $p_{n+1} = (x - \alpha_n) p_n - \beta_n p_{n-1}$ for $n \ge 1$,
$\mu_k = L(x^k)$ for every $k$, and $L(p_n) = 0$ for $n \ge 1$. Then there are formal power
series $S_0, S_1, \dots$ over $\mathbb{R}$, each with constant term $1$, giving $\mu$ a Jacobi
fraction with coefficients $\alpha$ and $\beta$, numerator $\mu_0$ and tails $S_n$: that is,
$\sum_{k \ge 0} \mu_k x^k = \mu_0 S_0$ and $(1 - \alpha_n x - \beta_{n+1} x^2 S_{n+1}) S_n = 1$
for every $n \ge 0$.

No monicity, degree or $\beta_n \ne 0$ hypothesis is needed, and orthogonality enters only
through $L(p_n) = 0$ for $n \ge 1$.

Formalized by `MetaMathlibExt.moment_generating_function_as_J_fraction_general`, a theorem declared in [MathlibExt/Algebra/Polynomial/MomentGeneratingJFraction.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/MomentGeneratingJFraction.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/moment-generating-functions-as-j-fractions/index.html#moment-generating-function-as-j-fraction).

## Moment generating function as a J-fraction

Let $p_0, p_1, \dots$ be real polynomials, each
$p_n$ monic of degree $n$, let $L$ be an $\mathbb{R}$-linear functional on $\mathbb{R}[x]$, and
let $(\alpha_n)$, $(\beta_n)$ and $(\mu_k)$ be real sequences. Suppose that $p_0 = 1$,
$p_1 = x - \alpha_0$ and $p_{n+1} = (x - \alpha_n) p_n - \beta_n p_{n-1}$ for $n \ge 1$, that
$\beta_n \ne 0$ for $n \ge 1$, that the $p_n$ are orthogonal for $L$, meaning $L(p_m p_n) = 0$
for $m \ne n$ and $L(p_n^2) \ne 0$ for every $n$, that $\mu_k = L(x^k)$ for every $k$, and that
$\mu_0 \ne 0$. Let $g = \sum_{k \ge 0} \mu_k x^k$ be the moment generating function. Then there
are formal power series $S_0, S_1, \dots$ over $\mathbb{R}$, each with constant term $1$, such
that $g = \mu_0 S_0$ and $S_n (1 - \alpha_n x - \beta_{n+1} x^2 S_{n+1}) = 1$ for every
$n \ge 0$.

These equations present $g$ as the J-fraction
$\mu_0 / (1 - \alpha_0 x - \beta_1 x^2 / (1 - \alpha_1 x - \beta_2 x^2 / \cdots))$ with tails
$S_n$. The hypotheses that each $p_n$ is monic of degree $n$, that $\beta_n \ne 0$, that
$L(p_n^2) \ne 0$ and that $\mu_0 \ne 0$ are not needed, and orthogonality is used only through
$L(p_n) = 0$ for $n \ge 1$.

The source's recurrence line reads $\beta_n(x)$; it is read as $\beta_n p_{n-1}$, as in the
surrounding lines 315–317 and 364–366 of the source.

## Sources

- Paul Barry and Aoife Hennessy, "Meixner-Type Results for Riordan Arrays and Associated Integer Sequences," Journal of Integer Sequences 13 (2010), Article 10.9.4, J-fraction theorem citing C. Krattenthaler (cf. Viennot Proposition 1, (7), p. V-5; Wall Theorem 51.1), lines 353–362, https://cs.uwaterloo.ca/journals/JIS/VOL13/Barry5/barry96s.tex

Formalized by `MetaMathlibExt.moment_generating_function_as_J_fraction`, a theorem declared in [MathlibExt/Algebra/Polynomial/MomentGeneratingJFraction.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/MomentGeneratingJFraction.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/moment-generating-functions-as-j-fractions/index.html#moment-generating-function-as-j-fraction-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moment generating functions as J-fractions](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/moment-generating-functions-as-j-fractions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/orthogonal-polynomials/moment-generating-functions-as-j-fractions)
