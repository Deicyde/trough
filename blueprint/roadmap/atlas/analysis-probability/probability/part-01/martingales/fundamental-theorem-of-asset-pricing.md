---
declaration: section
origin: cited
lean: MathlibExt.Probability.Finance.FundamentalTheoremAssetPricing.one_period_fundamental_theorem_asset_pricing_general, MathlibExt.Probability.Finance.FundamentalTheoremAssetPricing.one_period_fundamental_theorem_asset_pricing
statement: formalized
proof: formalized
---

# Fundamental theorem of asset pricing

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/fundamental-theorem-of-asset-pricing/index.html).

## Fundamental theorem of asset pricing for a finite one-period market

Let $\Omega$ be a
nonempty finite set of states and $A$ a finite set of assets, and let $g(a, \omega) \in \mathbb{R}$
be the gain of asset $a$ in state $\omega$. Call a portfolio $h \colon A \to \mathbb{R}$ an
arbitrage if its gain $\sum_{a \in A} h(a)\, g(a, \omega)$ is nonnegative in every state
$\omega$ and positive in some state. There is no arbitrage if and only if there is a function
$q \colon \Omega \to \mathbb{R}$ with $q(\omega) > 0$ for every $\omega \in \Omega$ and
$\sum_{\omega \in \Omega} q(\omega) = 1$ such that
$\sum_{\omega \in \Omega} q(\omega)\, g(a, \omega) = 0$ for every asset $a \in A$.

Formalized by `MathlibExt.Probability.Finance.FundamentalTheoremAssetPricing.one_period_fundamental_theorem_asset_pricing_general`, a theorem declared in [MathlibExt/Probability/Finance/FundamentalTheoremAssetPricing.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Finance/FundamentalTheoremAssetPricing.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/fundamental-theorem-of-asset-pricing/index.html#one-period-fundamental-theorem-asset-pri).

## One-period fundamental theorem of asset pricing

Let $\Omega$ be a nonempty finite set of
states and $A$ a finite set of assets, and let $g(a, \omega) \in \mathbb{R}$ be the gain of
asset $a$ in state $\omega$. Call a portfolio $h \colon A \to \mathbb{R}$ an arbitrage if its
gain $\sum_{a \in A} h(a)\, g(a, \omega)$ is nonnegative in every state $\omega$ and positive
in some state. There is no arbitrage if and only if there is a function
$q \colon \Omega \to \mathbb{R}$ with $q(\omega) > 0$ for every $\omega \in \Omega$ and
$\sum_{\omega \in \Omega} q(\omega) = 1$ such that
$\sum_{\omega \in \Omega} q(\omega)\, g(a, \omega) = 0$ for every asset $a \in A$, that is, a
strictly positive probability on the states under which every asset has zero expected gain.

## Sources

- J. M. Harrison and D. M. Kreps, J. Econom. Theory 20 (1979), DOI 10.1016/0022-0531(79)90043-7. It follows from `one_period_fundamental_theorem_asset_pricing_general`; the unused `[DecidableEq Ω]` and `[DecidableEq A]` keep the source's shape.

Formalized by `MathlibExt.Probability.Finance.FundamentalTheoremAssetPricing.one_period_fundamental_theorem_asset_pricing`, a theorem declared in [MathlibExt/Probability/Finance/FundamentalTheoremAssetPricing.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Finance/FundamentalTheoremAssetPricing.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/fundamental-theorem-of-asset-pricing/index.html#one-period-fundamental-theorem-asset-pri-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fundamental theorem of asset pricing](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/fundamental-theorem-of-asset-pricing/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/martingales/fundamental-theorem-of-asset-pricing)
