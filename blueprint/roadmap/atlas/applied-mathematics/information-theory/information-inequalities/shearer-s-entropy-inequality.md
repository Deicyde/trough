---
declaration: section
origin: cited
lean: MathlibExt.InformationTheory.Shearer.shearerMarginal, MathlibExt.InformationTheory.Shearer.shearerFullEntropy, MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy, MathlibExt.InformationTheory.Shearer.shearerMarginal_nonneg, MathlibExt.InformationTheory.Shearer.shearerMarginal_sum, MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_mono, MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_submodular, MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_empty
statement: formalized
proof: formalized
---

# Shearer's entropy inequality

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html).

## Marginal on a set of coordinates

Let $\alpha$ be a finite type, $n$ a natural number and
$\mu$ a real-valued function on the strings $x = (x_0, \dots, x_{n-1}) \in \alpha^n$. For a set
$S \subseteq \{0, \dots, n-1\}$ of coordinates, write $x|_S : S \to \alpha$ for the restriction
of a string $x$ to $S$. For a map $y : S \to \alpha$, the $S$-marginal of $\mu$ at $y$ is the sum
$\sum_{x \in \alpha^n,\ x|_S = y} \mu(x)$ of $\mu(x)$ over all strings $x$ with $x|_S = y$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginal`, a definition declared in [MathlibExt/InformationTheory/Shearer.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal).

## Joint entropy

For a finite set $\alpha$, a natural number $n$ and a real-valued function
$\mu$ on $\alpha^n$, the full (joint) entropy of $\mu$ is
$H(\mu) = -\sum_{x \in \alpha^n} \mu(x) \log \mu(x)$, where $\log t$ is the natural logarithm
of $|t|$ for $t \neq 0$ and $\log 0 = 0$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerFullEntropy`, a definition declared in [MathlibExt/InformationTheory/Shearer.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-full-entropy).

## Marginal entropy

For a finite set $\alpha$, a natural number $n$, a real-valued function
$\mu$ on $\alpha^n$ and a set $S \subseteq \{0, \dots, n-1\}$ of coordinates, let $P_S$ be the
marginal of $\mu$ on $S$: for $y \in \alpha^S$, $P_S(y)$ is the sum of $\mu(x)$ over the
$x \in \alpha^n$ whose restriction to $S$ is $y$. The marginal entropy of $\mu$ on $S$ is
$H_S(\mu) = -\sum_{y \in \alpha^S} P_S(y) \log P_S(y)$, where $\log t$ is the natural logarithm
of $|t|$ for $t \neq 0$ and $\log 0 = 0$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy`, a definition declared in [MathlibExt/InformationTheory/Shearer.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-entropy).

## Marginals of a nonnegative function are nonnegative

Let $\alpha$ be a finite set, $n$ a
natural number, $\mu$ a real-valued function on $\alpha^n$ with $\mu(x) \ge 0$ for all $x$, and
$S$ a set of coordinates in $\{0, \dots, n-1\}$. Then the marginal $P_S$ of $\mu$ on $S$
satisfies $P_S(y) \ge 0$ for every $y \in \alpha^S$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginal_nonneg`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-nonneg).

## Marginals preserve total mass

Let $\alpha$ be a finite set, $n$ a natural number, $\mu$ a
real-valued function on $\alpha^n$ with $\sum_{x \in \alpha^n} \mu(x) = 1$, and $S$ a set of
coordinates in $\{0, \dots, n-1\}$. Then the marginal $P_S$ of $\mu$ on $S$ satisfies
$\sum_{y \in \alpha^S} P_S(y) = 1$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginal_sum`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-sum).

## Monotonicity of marginal entropy

Let $\alpha$ be a finite set, $n$ a natural number, and
$\mu$ a real-valued function on $\alpha^n$ with $\mu(x) \ge 0$ for all $x$. If $T \subseteq S$
are sets of coordinates in $\{0, \dots, n-1\}$, then the marginal entropy of $\mu$ on $T$ is at
most the marginal entropy of $\mu$ on $S$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_mono`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-entropy-mono).

## Submodularity of marginal entropy

Let $\alpha$ be a finite set, $n$ a natural number,
and $\mu$ a probability mass function on $\alpha^n$, that is, $\mu(x) \ge 0$ for all $x$ and
$\sum_{x \in \alpha^n} \mu(x) = 1$. Writing $H_S$ for the marginal entropy of $\mu$ on a set
$S \subseteq \{0, \dots, n-1\}$ of coordinates, any two such sets $A$ and $B$ satisfy
$H_{A \cup B} + H_{A \cap B} \le H_A + H_B$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_submodular`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-entropy-submodular).

## Marginal entropy on the empty set vanishes

Let $\alpha$ be a finite set, $n$ a natural
number, and $\mu$ a real-valued function on $\alpha^n$ with $\sum_{x \in \alpha^n} \mu(x) = 1$.
Then the marginal entropy of $\mu$ on the empty set of coordinates is $0$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_empty`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-entropy-empty).

## Marginal entropy on all coordinates is the full entropy

For a finite set $\alpha$, a
natural number $n$ and a real-valued function $\mu$ on $\alpha^n$, the marginal entropy of $\mu$
on the set $\{0, \dots, n-1\}$ of all coordinates equals the full entropy of $\mu$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearerMarginalEntropy_univ`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-marginal-entropy-univ).

## Shearer's entropy inequality for every cover multiplicity

Let $\alpha$ be a nonempty
finite set, $n$ a natural number, and $\mu$ a probability mass function on $\alpha^n$, that is,
$\mu(x) \ge 0$ for all $x \in \alpha^n$ and $\sum_{x \in \alpha^n} \mu(x) = 1$. Write $H(\mu)$
for the full entropy of $\mu$ and, for a set $S$ of coordinates in $\{0, \dots, n-1\}$, write
$H_S(\mu)$ for the marginal entropy of $\mu$ on $S$. Let $C$ be a set of subsets of
$\{0, \dots, n-1\}$ and $k$ a natural number, possibly $0$, such that every coordinate lies in
at least $k$ members of $C$. Then $k \, H(\mu) \le \sum_{S \in C} H_S(\mu)$.

Formalized by `MathlibExt.InformationTheory.Shearer.shearer_entropy_inequality_general`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 919](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-entropy-inequality-general).

## Shearer's entropy inequality

Let $\alpha$ be a nonempty finite set, $n$ a natural number,
and $\mu$ a probability mass function on $\alpha^n$, that is, $\mu(x) \ge 0$ for all
$x \in \alpha^n$ and $\sum_{x \in \alpha^n} \mu(x) = 1$. Write $H(\mu)$ for the full entropy of
$\mu$ and, for a set $S$ of coordinates in $\{0, \dots, n-1\}$, write $H_S(\mu)$ for the
marginal entropy of $\mu$ on $S$. Let $C$ be a set of subsets of $\{0, \dots, n-1\}$ and
$k \ge 1$ an integer such that every coordinate lies in at least $k$ members of $C$. Then
$k \, H(\mu) \le \sum_{S \in C} H_S(\mu)$.

## Sources

- F. R. K. Chung et al., J. Combin. Theory A 43 (1986), DOI 10.1016/0097-3165(86)90019-1. It follows from `shearer_entropy_inequality_general`; the hypothesis `hk` is unused and keeps the source's shape.

Formalized by `MathlibExt.InformationTheory.Shearer.shearer_entropy_inequality`, a theorem declared in [MathlibExt/InformationTheory/Shearer.lean, line 997](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Shearer.lean#L997). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html#shearer-entropy-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shearer's entropy inequality](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/information-inequalities/shearer-s-entropy-inequality)
