---
declaration: section
origin: cited
lean: MathlibExt.InformationTheory.Fano.fano_inequality_general, MathlibExt.InformationTheory.Fano.fano_inequality
statement: formalized
proof: formalized
---

# Fano's inequality

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/fano-s-inequality/index.html).

## Fano's inequality, general form

Let $\alpha$ and $\beta$ be finite nonempty sets with
$|\alpha| \ge 2$, let $p : \alpha \times \beta \to \mathbb{R}$ satisfy $p(a, b) > 0$ for all
$a, b$ and $\sum_{a, b} p(a, b) = 1$, and let $g : \beta \to \alpha$. Put
$p_Y(b) = \sum_a p(a, b)$, let $P_e = \sum_b \sum_{a \ne g(b)} p(a, b)$ be the probability that
$g$ guesses wrong, and let $H(X \mid Y) = -\sum_{a, b} p(a, b) \log (p(a, b) / p_Y(b))$, where
$\log$ is the natural logarithm. Then

$$H(X \mid Y) \le -P_e \log P_e - (1 - P_e) \log (1 - P_e) + P_e \log (|\alpha| - 1).$$

This version does not assume decidable equality on $\beta$.

Formalized by `MathlibExt.InformationTheory.Fano.fano_inequality_general`, a theorem declared in [MathlibExt/InformationTheory/Fano.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/Fano.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/fano-s-inequality/index.html#fano-inequality-general).

## Fano's inequality

Let $\alpha$ and $\beta$ be finite nonempty sets with $|\alpha| \ge 2$, let
$p : \alpha \times \beta \to \mathbb{R}$ satisfy $p(a, b) > 0$ for all $a, b$ and
$\sum_{a, b} p(a, b) = 1$, and let $g : \beta \to \alpha$ be an estimator. Put
$p_Y(b) = \sum_a p(a, b)$, let $P_e = \sum_b \sum_{a \ne g(b)} p(a, b)$ be the probability that
$g$ guesses wrong, and let $H(X \mid Y) = -\sum_{a, b} p(a, b) \log (p(a, b) / p_Y(b))$, where
$\log$ is the natural logarithm. Then

$$H(X \mid Y) \le -P_e \log P_e - (1 - P_e) \log (1 - P_e) + P_e \log (|\alpha| - 1).$$

## Sources

- R. M. Fano, Transmission of Information, MIT Press (1961). It follows from `fano_inequality_general`; the unused `[DecidableEq β]` keeps the source's shape.

Formalized by `MathlibExt.InformationTheory.Fano.fano_inequality`, a theorem declared in [MathlibExt/InformationTheory/Fano.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/Fano.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/fano-s-inequality/index.html#fano-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fano's inequality](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/fano-s-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/InformationTheory/information-inequalities/fano-s-inequality)
