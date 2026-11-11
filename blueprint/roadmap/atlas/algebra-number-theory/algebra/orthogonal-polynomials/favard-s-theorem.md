---
declaration: section
origin: cited
lean: MetaMathlibExt.Polynomial.IsFormallyOrthogonal, MetaMathlibExt.favard_forward, MetaMathlibExt.favard_iff
statement: formalized
proof: formalized
---

# Favard's theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/favard-s-theorem/index.html).

## Formally orthogonal polynomial family

Let $R$ be a field. A family $(p_n)_{n \ge 0}$ of
polynomials over $R$ is formally orthogonal if there is an $R$-linear functional
$L \colon R[x] \to R$ such that each $p_n$ has degree $n$, $L(p_n p_m) = 0$ whenever $n \ne m$,
and $L(p_n^2) \ne 0$ for every $n$.

## Sources

- Barry, JIS VOL14 (`Barry1/barry97r2.tex`), lines 326-331. URL: https://cs.uwaterloo.ca/journals/JIS/VOL14/Barry1/barry97r2.tex

Formalized by `MetaMathlibExt.Polynomial.IsFormallyOrthogonal`, a definition declared in [MathlibExt/Algebra/Polynomial/FormalOrthogonality.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/FormalOrthogonality.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/favard-s-theorem/index.html#is-formally-orthogonal).

## Favard's theorem, forward direction

Let $R$ be a field and let $(p_n)_{n \ge 0}$ be a
formally orthogonal family of monic polynomials over $R$. Then there are sequences
$(\alpha_n)_{n \ge 0}$ and $(\beta_n)_{n \ge 0}$ in $R$ with $\beta_n \ne 0$ for all $n \ge 1$
such that $p_0 = 1$, $p_1 = x - \alpha_0$, and
$p_{n+1} = (x - \alpha_n) \, p_n - \beta_n \, p_{n-1}$ for all $n \ge 1$.

## Sources

- Barry, JIS VOL14 (`Barry1/barry97r2.tex`), lines 346-352. URL: https://cs.uwaterloo.ca/journals/JIS/VOL14/Barry1/barry97r2.tex

Formalized by `MetaMathlibExt.favard_forward`, a theorem declared in [MathlibExt/Algebra/Polynomial/FavardForward.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/FavardForward.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/favard-s-theorem/index.html#favard-forward).

## Favard's theorem

Let $R$ be a field and let $(p_n)_{n \ge 0}$ be a family of monic
polynomials in $R[x]$. Then $(p_n)$ is formally orthogonal if and only if there are sequences
$(\alpha_n)_{n \ge 0}$ and $(\beta_n)_{n \ge 0}$ in $R$ with $\beta_n \ne 0$ for all $n \ge 1$
such that $p_0 = 1$, $p_1 = x - \alpha_0$, and
$p_{n+1} = (x - \alpha_n) \, p_n - \beta_n \, p_{n-1}$ for all $n \ge 1$.

## Sources

- Paul Barry, "Riordan Arrays, Orthogonal Polynomials as Moments, and Hankel Transforms," Journal of Integer Sequences 14 (2011), Article 11.2.2, https://cs.uwaterloo.ca/journals/JIS/VOL14/Barry1/barry97r2.tex, Favard theorem at lines 346–352.

Formalized by `MetaMathlibExt.favard_iff`, a theorem declared in [MathlibExt/Algebra/Polynomial/FavardIff.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/FavardIff.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/favard-s-theorem/index.html#favard-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Favard's theorem](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/favard-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/orthogonal-polynomials/favard-s-theorem)
