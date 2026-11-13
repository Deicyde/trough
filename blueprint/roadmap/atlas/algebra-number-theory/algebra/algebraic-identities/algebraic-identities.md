---
declaration: section
origin: cited
lean: MetaMathlibExt.candido_identity, Set.indicatorOne, MetaMathlibExt.IsLAdditive, Fintype.prod_comp_eq_prod_pow
statement: formalized
proof: formalized
---

# Algebraic identities and operations: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/index.html).

Polynomial and product identities, sum-of-squares identities, functional equations on rings, and elementary operations on functions and sets.

## Candido's identity

For all elements $x$ and $y$ of a commutative semiring,
$2\left(x^4 + y^4 + (x + y)^4\right) = \left(x^2 + y^2 + (x + y)^2\right)^2$.

## Sources

- Kunle Adegoke, "Fibonacci Identities via Fibonacci Functions." <https://cs.uwaterloo.ca/journals/JIS/VOL27/Adegoke/adegoke12.tex>, lines 826-833.

Formalized by `MetaMathlibExt.candido_identity`, a theorem declared in [MathlibExt/Algebra/Ring/CandidoIdentity.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Ring/CandidoIdentity.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/index.html#candido-identity).

## Indicator function of a set

For a set $A \subseteq \alpha$ and a type $R$ with a zero
and a one, the indicator function $\mathbb{1}_A : \alpha \to R$ takes the value $1$ at every
point of $A$ and the value $0$ at every point outside $A$.

Formalized by `Set.indicatorOne`, a definition declared in [MathlibExt/Algebra/Group/Indicator.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Group/Indicator.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/index.html#indicator-one).

## L-additive functions on a ring

A function $f \colon K \to K$ on a ring $K$ is
L-additive when $f(mn) = f(m)\,n + f(n)\,m$ for all $m, n \in K$.

Formalized by `MetaMathlibExt.IsLAdditive`, a definition declared in [MathlibExt/Algebra/LAdditiveFunction.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/LAdditiveFunction.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/index.html#is-ladditive).

## Products regrouped by the values of a function

Let $\beta$ and $\gamma$ be finite types,
let $M$ be a commutative monoid, and let $g : \beta \to \gamma$ and $f : \gamma \to M$. Then

$$\prod_{b \in \beta} f(g(b)) = \prod_{c \in \gamma} f(c)^{\#\{b \in \beta \mid g(b) = c\}},$$

where the product on the right runs over all of $\gamma$ and $\#\{b \in \beta \mid g(b) = c\}$ is
the number of elements $b$ of $\beta$ with $g(b) = c$.

Formalized by `Fintype.prod_comp_eq_prod_pow`, a theorem declared in [MathlibExt/Algebra/BigOperators/ProdCompPow.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/BigOperators/ProdCompPow.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/index.html#prod-comp-eq-prod-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Algebraic identities and operations](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/algebraic-identities)
