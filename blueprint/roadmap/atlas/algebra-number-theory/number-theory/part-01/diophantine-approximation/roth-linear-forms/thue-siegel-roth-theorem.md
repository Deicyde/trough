---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.RothAuxiliary.finite_of_divisible_approximations, MetaMathlibExt.ridout_padic_roth, MathlibExt.NumberTheory.ThueSiegelRothWanted.thue_siegel_roth
statement: formalized
proof: formalized
---

# Thue–Siegel–Roth theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/thue-siegel-roth-theorem/index.html).

## Roth's theorem with divisibility conditions

Let $\alpha$ be a real algebraic number, let
$0 < \varepsilon \le 1$, and let $S$ be a finite index set carrying, for each $l \in S$, a natural
number $p_l$ and reals $\mu_l, \nu_l \ge 0$ with $\sigma = \sum_{l \in S} (\mu_l + \nu_l)$ less
than $2 + \varepsilon$. Then there are only finitely many rationals $q$, written in lowest terms
with numerator $n$ and denominator $d \ge 1$, such that
$|\alpha - q| < 1/d^{2 + \varepsilon - \sigma}$ and there are exponents $a_l, b_l \in \mathbb{N}$
for $l \in S$ with $\prod_{l \in S} p_l^{a_l}$ dividing $n$, $\prod_{l \in S} p_l^{b_l}$ dividing
$d$, and $d^{\mu_l} \le p_l^{a_l}$ and $d^{\nu_l} \le p_l^{b_l}$ for every $l \in S$.

Taking $S$ empty gives the usual archimedean approximation statement.

Formalized by `MathlibExt.NumberTheory.RothAuxiliary.finite_of_divisible_approximations`, a theorem declared in [MathlibExt/NumberTheory/RothAuxiliary.lean, line 6000](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RothAuxiliary.lean#L6000). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/thue-siegel-roth-theorem/index.html#finite-of-divisible-approximations).

## Ridout's $p$-adic extension of Roth's theorem

Let $\xi$ be an irrational real algebraic
number, let $\varepsilon > 0$, and let $S$ be a finite set of primes. For a rational number $r$,
write $r = p/q$ in lowest terms with $p \in \mathbb{Z}$ and $q \ge 1$, and let
$H(r) = \max(|p|, q)$ be its height. For a prime $\ell$, let $|\cdot|_\ell$ be the $\ell$-adic
absolute value on $\mathbb{Q}$, normalized by $|\ell|_\ell = \ell^{-1}$. Then only finitely many
rationals $r = p/q$ satisfy

$$\Bigl(\prod_{\ell \in S} |p|_\ell |q|_\ell\Bigr) |\xi - r| < \frac{1}{H(r)^{2 + \varepsilon}}.$$

The source prints the right side as $1/q^{2 + \varepsilon}$. Over all rationals that bound fails:
with $2 \in S$ and $\xi = \sqrt{2}$, every $r = 2^k$ with $k \ge 1$ gives left side
$1 - \sqrt{2}/2^k < 1$, so the height $H(r)$ is used instead.

Proof: The proof follows Roth's auxiliary-polynomial and index route, with the
S-adic integrality step supplied by valuation divisibility and a finite pigeonhole.

## Sources

- Boris Adamczewski, "The Many Faces of the Kempner Number", Journal of Integer Sequences 16 (2013), Article 13.2.15, `thmRi` environment, lines 736–746, attributed there to Ridout, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Adamczewski/adam6.tex>.

Formalized by `MetaMathlibExt.ridout_padic_roth`, a theorem declared in [MathlibExt/NumberTheory/RidoutPadicRoth.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RidoutPadicRoth.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/thue-siegel-roth-theorem/index.html#ridout-padic-roth).

## Thue–Siegel–Roth theorem

Let $\alpha$ be an irrational real number that is algebraic over
$\mathbb{Q}$, and let $\varepsilon > 0$ be real. Then only finitely many rational numbers $q$
satisfy $|\alpha - q| < 1 / b^{2 + \varepsilon}$, where $b$ is the denominator of $q$ in lowest
terms.

Proof: The proof constructs Siegel's auxiliary polynomial, bounds its index at rational
approximation points by a Taylor estimate, and contradicts the inductive Roth lemma.

## Sources

- K. F. Roth, Rational approximations to algebraic numbers, Mathematika 2 (1955) 1–20; predecessors Thue 1909 and Siegel 1921; textbook in Schmidt, Diophantine Approximation

Formalized by `MathlibExt.NumberTheory.ThueSiegelRothWanted.thue_siegel_roth`, a theorem declared in [MathlibExt/NumberTheory/ThueSiegelRoth.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ThueSiegelRoth.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/thue-siegel-roth-theorem/index.html#thue-siegel-roth).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thue–Siegel–Roth theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/thue-siegel-roth-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/thue-siegel-roth-theorem)
