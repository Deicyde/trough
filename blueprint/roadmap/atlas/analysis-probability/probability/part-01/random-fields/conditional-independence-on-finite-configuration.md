---
declaration: section
origin: cited
lean: MetaMathlibExt.FiniteWeight.marginal, MetaMathlibExt.FiniteWeight.marginal_anti, MetaMathlibExt.FiniteWeight.CondIndep, MetaMathlibExt.FiniteWeight.CondIndep.cond_eq_mul, MetaMathlibExt.FiniteWeight.marginal_mul, MetaMathlibExt.FiniteWeight.condIndep_of_dependsOn, MetaMathlibExt.FiniteWeight.condIndep_of_sdiff, MetaMathlibExt.FiniteWeight.card_filter_agree
statement: formalized
proof: formalized
---

# Conditional independence on finite configuration spaces

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html).

## Marginal of a weight

Let $V$ and $\alpha$ be finite types, a configuration being a map
$x : V \to \alpha$, and let $p$ be a real-valued weight on configurations. The (unnormalized)
marginal of $p$ on a set of variables $U \subseteq V$ at a configuration $x$ is

$$\sum_{y \,:\, y(v) = x(v) \text{ for all } v \in U} p(y),$$

the total weight of the configurations that agree with $x$ on $U$.

Formalized by `MetaMathlibExt.FiniteWeight.marginal`, a definition declared in [MathlibExt/Probability/FiniteWeight.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#marginal).

## Monotonicity of marginals in the fixed variables

Let $V$ and $\alpha$ be finite types, let
$p$ be a real-valued weight on the configurations $x : V \to \alpha$ with $p(x) \ge 0$ for every
$x$, and let $U \subseteq U' \subseteq V$. Then for every configuration $x$, the marginal of $p$
on $U'$ at $x$ is at most the marginal of $p$ on $U$ at $x$.

Formalized by `MetaMathlibExt.FiniteWeight.marginal_anti`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#marginal-anti).

## Conditional independence for a finite weight

Let $V$ and $\alpha$ be finite types, let $p$
be a real-valued weight on the configurations $x : V \to \alpha$, and for $U \subseteq V$ write
$p(x_U)$ for the marginal of $p$ on $U$ at $x$, the total weight of the configurations that agree
with $x$ on $U$. For $A, B, S \subseteq V$, the variables in $A$ and in $B$ are conditionally
independent given those in $S$ under $p$ when

$$p(x_{A \cup B \cup S})\, p(x_S) = p(x_{A \cup S})\, p(x_{B \cup S})$$

for every configuration $x$.

Formalized by `MetaMathlibExt.FiniteWeight.CondIndep`, a definition declared in [MathlibExt/Probability/FiniteWeight.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#cond-indep).

## Conditional independence in ratio form

Let $V$ and $\alpha$ be finite types, let $p$ be a
real-valued weight on the configurations $x : V \to \alpha$, and for $U \subseteq V$ write
$p(x_U)$ for the marginal of $p$ on $U$ at $x$. If, for $A, B, S \subseteq V$, the variables in
$A$ and in $B$ are conditionally independent given those in $S$ under $p$, then every
configuration $x$ with $p(x_S) \ne 0$ satisfies

$$\frac{p(x_{A\cup B\cup S})}{p(x_S)} = \frac{p(x_{A\cup S})}{p(x_S)}\frac{p(x_{B\cup S})}{p(x_S)}$$

For a nonnegative weight of positive total mass these ratios are the conditional probabilities of
the normalized distribution, so this is $P(x_A, x_B \mid x_S) = P(x_A \mid x_S)\, P(x_B \mid x_S)$.

Formalized by `MetaMathlibExt.FiniteWeight.CondIndep.cond_eq_mul`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#cond-eq-mul).

## Marginals of a product

Let $V$ and $\alpha$ be finite types, let $f$ and $g$ be real-valued
weights on the configurations $x : V \to \alpha$, and let $P, Q, U \subseteq V$ with
$P \cup Q = V$ and $P \cap Q \subseteq U$, such that $f(x)$ depends only on the values of $x$ on
$P$ and $g(x)$ only on its values on $Q$. Write $fg$ for the pointwise product, $P^c$ and $Q^c$
for the complements in $V$, and, for a weight $h$, a set $T \subseteq V$ and a configuration $x$,
$m_h(T, x)$ for the marginal of $h$ on $T$ at $x$, the total weight of the configurations that
agree with $x$ on $T$. Then for every configuration $x$,

$$m_{fg}(U, x) = m_f(U \cup P^c, x)\, m_g(U \cup Q^c, x).$$

Here the free variables of $f$ are those of $P$ outside $U$, and those of $g$ are those of $Q$
outside $U$.

Formalized by `MetaMathlibExt.FiniteWeight.marginal_mul`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#marginal-mul).

## The factorization criterion for conditional independence

Let $V$ and $\alpha$ be finite
types, let $f$ and $g$ be real-valued weights on the configurations $x : V \to \alpha$, and let
$P, Q \subseteq V$ with $P \cup Q = V$ such that $f(x)$ depends only on the values of $x$ on $P$
and $g(x)$ only on its values on $Q$. If $A \subseteq V$ is disjoint from $Q$ and $B \subseteq V$
is disjoint from $P$, then the variables in $A$ and in $B$ are conditionally independent given
those in $P \cap Q$ under the pointwise product $fg$.

Formalized by `MetaMathlibExt.FiniteWeight.condIndep_of_dependsOn`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#cond-indep-of-depends-on).

## Conditional independence from the variables outside the conditioning set

Let $V$ and
$\alpha$ be finite types, let $p$ be a real-valued weight on the configurations
$x : V \to \alpha$, and let $A, B, S \subseteq V$. If the variables in $A \setminus S$ and in
$B \setminus S$ are conditionally independent given those in $S$ under $p$, then the variables in
$A$ and in $B$ are conditionally independent given those in $S$ under $p$.

Formalized by `MetaMathlibExt.FiniteWeight.condIndep_of_sdiff`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#cond-indep-of-sdiff).

## Agreement classes of configurations have equal size

Let $V$ and $\alpha$ be finite types
and $W \subseteq V$. For any two configurations $x, z : V \to \alpha$, the number of
configurations $y : V \to \alpha$ with $y(v) = z(v)$ for all $v \in W$ equals the number of
configurations $y$ with $y(v) = x(v)$ for all $v \in W$.

Formalized by `MetaMathlibExt.FiniteWeight.card_filter_agree`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#card-filter-agree).

## Marginalizing in two steps

Let $V$ and $\alpha$ be finite types, let $p$ be a real-valued
weight on the configurations $x : V \to \alpha$, let $U \subseteq W \subseteq V$, and let $p_W$
be the $W$-marginal of $p$, the weight sending $x$ to the total weight of the configurations that
agree with $x$ on $W$. Then for every configuration $x$, the $U$-marginal of $p_W$ at $x$ equals
$N$ times the $U$-marginal of $p$ at $x$, where $N$ is the number of configurations that agree
with $x$ on $W$ (the number of assignments of values to the variables outside $W$).

Formalized by `MetaMathlibExt.FiniteWeight.marginal_marginal`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#marginal-marginal).

## Conditional independence can be read off a marginal

Let $V$ and $\alpha$ be finite types,
let $p$ be a real-valued weight on the configurations $x : V \to \alpha$, let $W \subseteq V$, and
let $p_W$ be the $W$-marginal of $p$, the weight sending $x$ to the total weight of the
configurations that agree with $x$ on $W$. For all $A, B, S \subseteq W$, the variables in $A$
and in $B$ are conditionally independent given those in $S$ under $p_W$ if and only if they are
conditionally independent given those in $S$ under $p$.

Formalized by `MetaMathlibExt.FiniteWeight.condIndep_marginal_iff`, a theorem declared in [MathlibExt/Probability/FiniteWeight.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/FiniteWeight.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html#cond-indep-marginal-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conditional independence on finite configuration spaces](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/random-fields/conditional-independence-on-finite-configuration)
