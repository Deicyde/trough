---
declaration: section
origin: cited
lean: MetaMathlibExt.higherOrderBernoulliNumber, MetaMathlibExt.higherOrderBernoulliNumber_nat, MetaMathlibExt.higherOrderBernoulliNumber_one, MetaMathlibExt.neto_higher_order_bernoulli_identity
statement: formalized
proof: formalized
---

# Higher-order Bernoulli numbers

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers/index.html).

## Higher-order Bernoulli numbers

For a complex number $\alpha$ and a natural number $n$, the
higher-order Bernoulli number $B_n^{(\alpha)}$ is $n!$ times the coefficient of $t^n$ in the
formal power series $\left(t / (e^t - 1)\right)^{\alpha}$. Here $t / (e^t - 1)$ is the Bernoulli
generating series $\sum_{k \ge 0} B_k t^k / k!$ (with $B_1 = -1/2$), and its $\alpha$-th power is
the binomial series $(1 + u)^{\alpha} = \sum_{j \ge 0} \binom{\alpha}{j} u^j$ with
$u = t / (e^t - 1) - 1$ substituted.

Equivalently, $B_n^{(\alpha)} = B_n^{(\alpha)}(0)$, where the generalized Bernoulli polynomials
$B_n^{(\alpha)}(x)$ are given by the exponential generating function
$\sum_{n \ge 0} B_n^{(\alpha)}(x) t^n / n! = \left(t / (e^t - 1)\right)^{\alpha} e^{tx}$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL23/Chellal/chellal7.tex, lines 99-112.

Formalized by `MetaMathlibExt.higherOrderBernoulliNumber`, a definition declared in [MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers/index.html#higher-order-bernoulli-number).

## Higher-order Bernoulli numbers of natural order

Let $B_k$ denote the Bernoulli numbers,
with $B_1 = -1/2$. For natural numbers $d$ and $n$, the higher-order Bernoulli number
$B_n^{(d)}$ equals $n!$ times the coefficient of $t^n$ in the $d$-th power of the Bernoulli
generating series $\sum_{k \ge 0} B_k t^k / k!$.

Formalized by `MetaMathlibExt.higherOrderBernoulliNumber_nat`, a theorem declared in [MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers/index.html#higher-order-bernoulli-number-nat).

## Higher-order Bernoulli numbers of order one

For every natural number $n$, the
higher-order Bernoulli number $B_n^{(1)}$ equals the Bernoulli number $B_n$, with the
convention $B_1 = -1/2$.

Formalized by `MetaMathlibExt.higherOrderBernoulliNumber_one`, a theorem declared in [MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers/index.html#higher-order-bernoulli-number-one).

## Neto's identity for higher-order Bernoulli numbers

For every complex number $x$ and all
natural numbers $n$ and $\ell$,

$$\sum_{k=0}^{n} \binom{n}{k} x^{n-k} B_{\ell+k}^{(x)} =
(-1)^{n+\ell} \sum_{k=0}^{\ell} \binom{\ell}{k} x^{\ell-k} B_{n+k}^{(x)},$$

where $B_m^{(x)}$ is the higher-order Bernoulli number of order $x$.

Proof: The substitution coefficient formula makes both sides polynomial in the order. For natural
orders, the cited Bernoulli EGF gives the reflection identity, formal differentiation proves Neto's
formula, and equality on all natural complex points finishes the polynomial argument.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL23/Chellal/chellal7.tex, lines 662-670.

Formalized by `MetaMathlibExt.neto_higher_order_bernoulli_identity`, a theorem declared in [MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NetoHigherOrderBernoulli.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers/index.html#neto-higher-order-bernoulli-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Higher-order Bernoulli numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/bernoulli-numbers/higher-order-bernoulli-numbers)
