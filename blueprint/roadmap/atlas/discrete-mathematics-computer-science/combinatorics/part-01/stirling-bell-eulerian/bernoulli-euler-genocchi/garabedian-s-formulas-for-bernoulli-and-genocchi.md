---
declaration: section
origin: cited
lean: MetaMathlibExt.garabedian_genocchi_formula_general, MetaMathlibExt.garabedian_genocchi_formula, MetaMathlibExt.genocchiNumber_eq_stirlingSecond_sum_general, MetaMathlibExt.genocchiNumber_eq_stirlingSecond_sum
statement: formalized
proof: formalized
---

# Garabedian's formulas for Bernoulli and Genocchi numbers

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi/index.html).

## Garabedian's formula for the Bernoulli numbers, including $n = 0$

For every natural
number $n$,

$$2(1 - 2^n) B_n = n \sum_{k=1}^{n} \frac{(-1)^{n-k} (k-1)!\, S(n, k)}{2^{k-1}},$$

where $B_n$ is the $n$-th Bernoulli number, with $B_1 = -\frac{1}{2}$, and $S(n, k)$ is the
Stirling number of the second kind. At $n = 0$ both sides are $0$.

Formalized by `MetaMathlibExt.garabedian_genocchi_formula_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GarabedianBernoulliStirling.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GarabedianBernoulliStirling.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi/index.html#garabedian-genocchi-formula-general).

## Garabedian's formula for the Bernoulli numbers

For every natural number $n \ge 1$,

$$2(1 - 2^n) B_n = n \sum_{k=1}^{n} \frac{(-1)^{n-k} (k-1)!\, S(n, k)}{2^{k-1}},$$

where $B_n$ is the $n$-th Bernoulli number, with $B_1 = -\frac{1}{2}$, and $S(n, k)$ is the
Stirling number of the second kind.

The identity also holds for $n = 0$, where both sides are $0$.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers," Journal of Integer Sequences 28 (2025), Article 25.6.7, equation (g19), lines 188–191 of the official TeX, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Zerroukhat/zerrou3.tex>, which displays `2(1-2^n)B_n = G_n = n ∑ ...` and notes Garabedian's formula is equivalent to it; this article states the outer (Bernoulli-to-sum) equality. Original: H. L. Garabedian, "A new formula for the Bernoulli numbers," Bull. Amer. Math. Soc. 46 (1940), 531–533.

Formalized by `MetaMathlibExt.garabedian_genocchi_formula`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GarabedianBernoulliStirling.lean, line 845](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GarabedianBernoulliStirling.lean#L845). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi/index.html#garabedian-genocchi-formula).

## Garabedian's formula for the Genocchi numbers, including $n = 0$

For every natural
number $n$, the Genocchi number $G_n$, defined by $\sum_{m \ge 0} G_m x^m / m! = 2x/(e^x + 1)$,
satisfies

$$G_n = n \sum_{k=1}^{n} \frac{(-1)^{n-k} (k-1)!\, S(n, k)}{2^{k-1}},$$

where $S(n, k)$ is the Stirling number of the second kind. At $n = 0$ both sides are $0$.

Formalized by `MetaMathlibExt.genocchiNumber_eq_stirlingSecond_sum_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GarabedianGenocchiFormula.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GarabedianGenocchiFormula.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi/index.html#genocchi-number-eq-stirling-second-sum-g).

## Garabedian's formula for the Genocchi numbers

For every natural number $n \ge 1$, the
Genocchi number $G_n$, defined by $\sum_{m \ge 0} G_m x^m / m! = 2x/(e^x + 1)$, satisfies

$$G_n = n \sum_{k=1}^{n} \frac{(-1)^{n-k} (k-1)!\, S(n, k)}{2^{k-1}},$$

where $S(n, k)$ is the Stirling number of the second kind.

The identity also holds for $n = 0$, where both sides are $0$.

The formula is due to H. L. Garabedian, "A new formula for the Bernoulli numbers," Bulletin of
the American Mathematical Society 46 (1940), 531–533, DOI 10.1090/S0002-9904-1940-07255-6.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers," Journal of Integer Sequences 28 (2025), Article 25.6.7, lines 184–194 of the official TeX: <https://cs.uwaterloo.ca/journals/JIS/VOL28/Zerroukhat/zerrou3.tex>.

Formalized by `MetaMathlibExt.genocchiNumber_eq_stirlingSecond_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GarabedianGenocchiFormula.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GarabedianGenocchiFormula.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi/index.html#genocchi-number-eq-stirling-second-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Garabedian's formulas for Bernoulli and Genocchi numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/garabedian-s-formulas-for-bernoulli-and-genocchi)
