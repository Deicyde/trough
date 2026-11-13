---
declaration: section
origin: cited
lean: Set.partialDensity, Set.upperDensity, Set.lowerDensity, Set.HasDensity, Set.HasPosDensity, Set.intPartialDensity, Set.HasIntDensity, Set.HasDensity.univ
statement: formalized
proof: formalized
---

# Natural and logarithmic density

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html).

## Densities

## Partial density

Let $\beta$ be a preorder in which every set $\{x \in \beta \mid x \le b\}$
is finite, let $S, A \subseteq \beta$ and $b \in \beta$, and write
$A_{\lt b} = \{x \in A \mid x < b\}$. The partial density of $S$ relative to $A$ at $b$ is the
proportion $\lvert S \cap A_{\lt b} \rvert / \lvert A_{\lt b} \rvert$ of elements of $A_{\lt b}$ that lie
in $S$, taken to be $0$ when $A_{\lt b}$ is empty. By default $A = \beta$.

## Sources

- inspired by https://github.com/b-mehta/unit-fractions

Formalized by `Set.partialDensity`, an abbreviation declared in [MathlibExt/Data/Set/Density.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#partial-density).

## Upper density

Let $\beta$ be a preorder in which every set $\{x \in \beta \mid x \le b\}$
is finite, and let $S, A \subseteq \beta$. The upper density of $S$ relative to $A$ is the limit
superior, as $b \to \infty$ in $\beta$, of the partial densities of $S$ relative to $A$ at $b$.
By default $A = \beta$.

Formalized by `Set.upperDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#upper-density).

## Lower density

Let $\beta$ be a preorder in which every set $\{x \in \beta \mid x \le b\}$
is finite, and let $S, A \subseteq \beta$. The lower density of $S$ relative to $A$ is the limit
inferior, as $b \to \infty$ in $\beta$, of the partial densities of $S$ relative to $A$ at $b$.
By default $A = \beta$.

Formalized by `Set.lowerDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#lower-density).

## Density of a set

Let $\beta$ be a preorder in which every set
$\{x \in \beta \mid x \le b\}$ is finite, let $S, A \subseteq \beta$ and $\alpha \in \mathbb{R}$,
and write $\beta_{\lt b} = \{x \in \beta \mid x < b\}$. The set $S$ has density $\alpha$ relative to
$A$ if the partial density
$\lvert S \cap A \cap \beta_{\lt b} \rvert / \lvert A \cap \beta_{\lt b} \rvert$, taken to be $0$ when
the denominator is $0$, tends to $\alpha$ as $b \to \infty$ in $\beta$.

By default $A = \beta$; for $\beta = \mathbb{N}$ this is the natural density of $S$.

Formalized by `Set.HasDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#has-density).

## Positive density

Let $\beta$ be a preorder in which every set
$\{x \in \beta \mid x \le b\}$ is finite, and let $S, A \subseteq \beta$. The set $S$ has positive
density relative to $A$ if there is a real number $\alpha > 0$ such that $S$ has density $\alpha$
relative to $A$. By default $A = \beta$.

Formalized by `Set.HasPosDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#has-pos-density).

## Two-sided partial density

For a set $S$ of integers and a natural number $N$, the
two-sided partial natural density of $S$ at $N$ is $\lvert S \cap [-N, N] \rvert / (2N + 1)$,
where $[-N, N]$ is the set of integers $m$ with $-N \le m \le N$.

Formalized by `Set.intPartialDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#int-partial-density).

## Two-sided natural density

A set $S$ of integers has two-sided natural density
$\alpha \in \mathbb{R}$ if $\lvert S \cap [-N, N] \rvert / (2N + 1)$ tends to $\alpha$ as the
natural number $N$ tends to infinity, where $[-N, N]$ is the set of integers $m$ with
$-N \le m \le N$.

Formalized by `Set.HasIntDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#has-int-density).

## The whole order has density one

Let $\beta$ be a partial order with a least element
and at least two elements, in which every closed interval $[a, b]$ is finite. Then the set of
all elements of $\beta$ has density $1$ (relative to all of $\beta$).

Formalized by `Set.HasDensity.univ`, a theorem declared in [MathlibExt/Data/Set/Density.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#univ).

## Natural density of the even numbers

The set of even natural numbers has natural
density $1/2$.

Formalized by `Nat.hasDensity_even`, a theorem declared in [MathlibExt/Data/Set/Density.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#has-density-even).

## Finite sets have natural density zero

Every finite set of natural numbers has natural
density $0$.

Formalized by `Nat.hasDensity_zero_of_finite`, a theorem declared in [MathlibExt/Data/Set/Density.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#has-density-zero-of-finite).

## Sets of nonzero natural density are infinite

If a set $S$ of natural numbers has
natural density $\alpha$ with $\alpha \neq 0$, then $S$ is infinite.

Formalized by `Nat.infinite_of_hasDensity_pos`, a theorem declared in [MathlibExt/Data/Set/Density.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#infinite-of-has-density-pos).

## Logarithmic density

A set $A$ of natural numbers has logarithmic density
$d \in \mathbb{R}$ if
$\frac{1}{\log n} \sum_{k \in A,\, k \le n} \frac{1}{k}$
tends to $d$ as $n \to \infty$, where $\log$ is the natural logarithm, the term $1/k$ for $k = 0$
is taken to be $0$, and the whole expression is taken to be $0$ when $\log n = 0$.

Logarithmic density is a weaker notion than natural density: if a set has natural density $d$,
then it also has logarithmic density $d$, but the converse is false.

Formalized by `Set.HasLogDensity`, a definition declared in [MathlibExt/Data/Set/Density.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Density.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html#has-log-density).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Natural and logarithmic density](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/natural-and-logarithmic-density)
