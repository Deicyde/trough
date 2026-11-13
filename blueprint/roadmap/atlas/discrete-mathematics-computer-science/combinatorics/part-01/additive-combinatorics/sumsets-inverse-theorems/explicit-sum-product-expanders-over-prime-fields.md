---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.bourgainExpanderSquarePlusProduct, MathlibExt.Combinatorics.BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.bourgainExpanderSquarePlusProduct_holds
statement: formalized
---

# Explicit sum-product expanders over prime fields

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/explicit-sum-product-expanders-over-prime-fields/index.html).

## Bourgain's expander property for x² + xy

The statement that there is a real
$\varepsilon > 0$ such that for every real $C \ge 1$ there are a real $c > 0$ and a natural number
$p_0$ such that for every prime $p \ge p_0$ and all sets $A, B \subseteq \mathbb{F}_p$ with
$\sqrt{p}/C \le |A| \le C\sqrt{p}$ and $\sqrt{p}/C \le |B| \le C\sqrt{p}$, the set
$\{a^2 + ab : a \in A,\ b \in B\}$ has at least $c\, p^{1/2 + \varepsilon}$ elements.

This says that $f(x, y) = x^2 + xy$ answers Bourgain's question (AIM, Recent trends in additive
combinatorics, Problem 3.1).

Formalized by `MathlibExt.Combinatorics.BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.bourgainExpanderSquarePlusProduct`, a definition declared in [WantedExt/Combinatorics/BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/explicit-sum-product-expanders-over-prime-fields/index.html#bourgain-expander-square-plus-product).

## x² + xy is an explicit expander over prime fields

Bourgain's expander property for
$f(x, y) = x^2 + xy$ holds: there is a real $\varepsilon > 0$ such that for every real $C \ge 1$
there are a real $c > 0$ and a natural number $p_0$ such that for every prime $p \ge p_0$ and all
sets $A, B \subseteq \mathbb{F}_p$ with $\sqrt{p}/C \le |A| \le C\sqrt{p}$ and
$\sqrt{p}/C \le |B| \le C\sqrt{p}$, the set
$f(A, B) = \{a^2 + ab : a \in A,\ b \in B\}$ has at least $c\, p^{1/2 + \varepsilon}$ elements.

Bourgain proved that $|f(A, B)| \gtrsim p^{\eta}$ for some $\eta > \delta$ whenever
$|A| \sim |B| \sim p^{\delta}$ with $0 < \delta < 1$ (as Shen recalls; $\delta = 1/2$ is the AIM
question). Stevens and de Zeeuw (Corollary 12) later gave an explicit exponent:
$|f(A, B)| \gg \min\{|A|^{1/2} |B|^{3/4}, |B|^2\}$ for $A \ne \{0\}$ and $|A|^2 |B| \ll p^2$,
which for $|A|, |B|$ between $p^{1/2}/C$ and $C p^{1/2}$ is $\gg_C p^{5/8}$, so
$\varepsilon = 1/8$ works for every $C$.

## Sources

- AIM workshop Recent trends in additive combinatorics (2004), problem list collected by E. Croot and V. F. Lev, https://aimath.org/WWN/additivecomb/additivecomb.pdf, Problem 3.1 (J. Bourgain); resolution: J. Bourgain, More on the sum-product phenomenon in prime fields and its applications, Int. J. Number Theory 1 (2005), 1-32; explicit exponent: S. Stevens and F. de Zeeuw, An improved point-line incidence bound over arbitrary fields, Bull. Lond. Math. Soc. 49 (2017), 842-858, arXiv:1609.06284; C.-Y. Shen, On the sum product estimates and two variables expanders, Publ. Mat. 54 (2010), 149-157, Shen, Section 1, recalling Bourgain: F(x, y) = x² + xy satisfies |F(A, B)| ≳ p^ε for some ε > δ whenever |A| ∼ |B| ∼ p^δ, 0 < δ < 1 (δ = 1/2 is the AIM question); Stevens-de Zeeuw, Section 4 and Corollary 12: for f(x, y) = x² + xy and finite A, B ⊂ F with A ≠ {0} (if char F = p > 0, assuming |A|²|B| ≪ p²), |f(A, B)| ≫ min{|A|^{1/2}|B|^{3/4}, |B|²}; they recall Bourgain's theorem that |f(A, B)| ≫ N^{1+δ} when |A| = |B| = N ≈ p^ε, https://doi.org/10.1112/blms.12077.

Stated but not proved: `MathlibExt.Combinatorics.BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.bourgainExpanderSquarePlusProduct_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BourgainExplicitExpanderAIMCombinatoricsProblem238Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/explicit-sum-product-expanders-over-prime-fields/index.html#bourgain-expander-square-plus-product-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Explicit sum-product expanders over prime fields](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/explicit-sum-product-expanders-over-prime-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/explicit-sum-product-expanders-over-prime-fields)
