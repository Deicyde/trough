---
declaration: section
origin: cited
lean: MetaMathlibExt.polyBernoulli, MetaMathlibExt.arakawa_kaneko_duality, MetaMathlibExt.polyBernoulli_negative_symmetric_exponential_generating_function
statement: formalized
proof: formalized
---

# Poly-Bernoulli numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/poly-bernoulli-numbers/index.html).

## Poly-Bernoulli numbers

Let $S(n, r)$ denote the Stirling numbers of the second kind. For
a natural number $n$ and an integer $k$, the poly-Bernoulli number $B_n^{(k)}$ is the rational
number given by Kaneko's explicit formula

$$B_n^{(k)} = (-1)^n \sum_{r=0}^{n} \frac{(-1)^r\, r!\, S(n, r)}{(r+1)^k}.$$

Introduced by M. Kaneko, "Poly-Bernoulli numbers," Journal de Théorie des
Nombres de Bordeaux 9 (1997), 221–228; see also T. Arakawa and M. Kaneko,
"On poly-Bernoulli numbers," Commentarii Mathematici Universitatis
Sancti Pauli 48 (1999), 159–167, as cited by the source.

## Sources

- Y. Hamahata and H. Masubuchi, "Special Multi-Poly-Bernoulli Numbers," Journal of Integer Sequences 10 (2007), Article 07.4.1, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Hamahata/hamahata3.tex>. The poly-Bernoulli generating-series definition and Kaneko's formula are lines 106–152 of the official TeX.

Formalized by `MetaMathlibExt.polyBernoulli`, a definition declared in [MathlibExt/NumberTheory/Bernoulli/PolyBernoulliDuality.lean, line 669](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Bernoulli/PolyBernoulliDuality.lean#L669). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/poly-bernoulli-numbers/index.html#poly-bernoulli).

## Arakawa–Kaneko duality for poly-Bernoulli numbers

Let $S(n, r)$ denote the Stirling
numbers of the second kind. For a natural number $n$ and an integer $k$, let $B_n^{(k)}$ be the
poly-Bernoulli number given by Kaneko's explicit formula

$$B_n^{(k)} = (-1)^n \sum_{r=0}^{n} \frac{(-1)^r\, r!\, S(n, r)}{(r+1)^k}.$$

Then for all natural numbers $n$ and $k$,

$$B_n^{(-k)} = B_k^{(-n)}.$$

## Sources

- Y. Hamahata and H. Masubuchi, "Special Multi-Poly-Bernoulli Numbers," Journal of Integer Sequences 10 (2007), Article 07.4.1, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Hamahata/hamahata3.tex>. The symmetric closed formula and the duality are lines 156–174 of the official TeX, attributed there to T. Arakawa and M. Kaneko, "On poly-Bernoulli numbers," Commentarii Mathematici Universitatis Sancti Pauli 48 (1999), 159–167.

Formalized by `MetaMathlibExt.arakawa_kaneko_duality`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/PolyBernoulliDuality.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Bernoulli/PolyBernoulliDuality.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/poly-bernoulli-numbers/index.html#arakawa-kaneko-duality).

## Generating function of negative-index poly-Bernoulli numbers

For natural numbers $n, k$
let $B_{n,k} = \sum_{j=0}^{\min(n,k)} (j!)^2 \, S(n+1, j+1) \, S(k+1, j+1)$, where $S$ denotes
the Stirling numbers of the second kind. Then for all real numbers $x, y$ with
$(e^{|x|} - 1)(e^{|y|} - 1) < 1$,

$$\sum_{n=0}^{\infty} \left( \sum_{k=0}^{\infty} B_{n,k} \frac{x^n}{n!} \frac{y^k}{k!} \right) =
\frac{e^{x+y}}{e^x + e^y - e^{x+y}}.$$

By Kaneko's closed formula, $B_{n,k}$ is the poly-Bernoulli number $B_n^{(-k)}$ of negative
index. The condition $(e^{|x|} - 1)(e^{|y|} - 1) < 1$ is the domain of absolute convergence of
the double series (all $B_{n,k} \ge 0$). The weaker condition $|(e^x - 1)(e^y - 1)| < 1$ does
not suffice: at $x = -3$, $y = \log 1.9$ the outer series diverges.

Proof: The Stirling EGF is derived from the finite-difference formula, then absolute convergence
permits a Fubini rearrangement and a geometric-series sum, following Hamahata–Masubuchi,
Theorems 2 and 4, and Kaneko's original formula.

## Sources

- Y. Hamahata and H. Masubuchi, "Special Multi-Poly-Bernoulli Numbers," Journal of Integer Sequences 10 (2007), Article 07.4.1, Theorem 4 (symmetric formula), lines 180–186, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Hamahata/hamahata3.tex>; the closed formula identifying `B` is Theorem 2 there, lines 156–166. Both are attributed there to M. Kaneko, "Poly-Bernoulli numbers," Journal de Théorie des Nombres de Bordeaux 9 (1997), 221–228.

Formalized by `MetaMathlibExt.polyBernoulli_negative_symmetric_exponential_generating_function`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/PolyBernoulliSymmetricExponentialGeneratingFunction.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Bernoulli/PolyBernoulliSymmetricExponentialGeneratingFunction.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/poly-bernoulli-numbers/index.html#poly-bernoulli-negative-symmetric-expone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poly-Bernoulli numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/poly-bernoulli-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/poly-bernoulli-numbers)
