---
declaration: section
origin: cited
lean: MetaMathlibExt.spectralNorm_le_one_iff_isIntegral, MetaMathlibExt.spectralNorm_le_one_iff_exists_integralClosure
statement: formalized
proof: formalized
---

# Spectral norm on algebraic extensions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/spectral-norm-on-algebraic-extensions/index.html).

## Spectral-norm unit ball is the integral closure

Let $A$ be an integral domain, $K$ a
complete nontrivially normed field whose norm is ultrametric, and $L$ a field extension of $K$ of
finite degree, where $K$ and $L$ are $A$-algebras and the algebra maps $A \to K \to L$ compose to
$A \to L$. Suppose that for every $y \in K$, $\|y\| \le 1$ if and only if $y$ is integral over
$A$. Then for every $x \in L$, the spectral norm of $x$ over $K$ is at most $1$ if and only if
$x$ is integral over $A$.

Formalized by `MetaMathlibExt.spectralNorm_le_one_iff_isIntegral`, a theorem declared in [MathlibExt/NumberTheory/SpectralNormUnitBall.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SpectralNormUnitBall.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/spectral-norm-on-algebraic-extensions/index.html#spectral-norm-le-one-iff-is-integral).

## Spectral-norm unit ball as the image of an integral closure

Let $A$ be an integral domain,
$K$ a complete nontrivially normed field whose norm is ultrametric, and $L$ a field extension of
$K$ of finite degree, where $K$ and $L$ are $A$-algebras and the algebra maps $A \to K \to L$
compose to $A \to L$. Let $B$ be an integral domain that is an $A$-algebra with an algebra map
$B \to L$ such that $A \to B \to L$ composes to $A \to L$, and suppose $B$ is an integral closure
of $A$ in $L$: the map $B \to L$ is injective and its image is the set of elements of $L$ integral
over $A$. Suppose that for every $y \in K$, $\|y\| \le 1$ if and only if $y$ is integral over $A$.
Then for every $x \in L$, the spectral norm of $x$ over $K$ is at most $1$ if and only if $x$ is
the image of some element of $B$.

Formalized by `MetaMathlibExt.spectralNorm_le_one_iff_exists_integralClosure`, a theorem declared in [MathlibExt/NumberTheory/SpectralNormUnitBall.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SpectralNormUnitBall.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/spectral-norm-on-algebraic-extensions/index.html#spectral-norm-le-one-iff-exists-integral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectral norm on algebraic extensions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/spectral-norm-on-algebraic-extensions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/p-adic-numbers/spectral-norm-on-algebraic-extensions)
