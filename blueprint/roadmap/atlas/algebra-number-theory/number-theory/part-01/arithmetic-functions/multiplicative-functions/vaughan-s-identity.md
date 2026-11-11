---
declaration: section
origin: cited
lean: MetaMathlibExt.vaughan_identity_general, MetaMathlibExt.vaughan_identity
statement: formalized
proof: formalized
---

# Vaughan's identity

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/vaughan-s-identity/index.html).

## Vaughan's identity in a commutative ring

Let $R$ be a commutative ring, let $\mu$ and
$\Lambda$ be arithmetic functions with values in $R$ (so $\mu(0) = \Lambda(0) = 0$), and let
$L : \mathbb{N} \to R$ be any function. Suppose that for every natural number $m$,
$\sum_{d \mid m} \mu(d)$ is $1$ if $m = 1$ and $0$ otherwise, and
$\Lambda(m) = \sum_{d \mid m} \mu(d) \, L(m/d)$, where both sums run over the $d$ with
$0 \le d \le m$ and $d \mid m$. Then for all natural numbers $U$, $V$ and $n$ with $V < n$,

$$\Lambda(n) = \sum_{b \mid n,\ b \le U} \mu(b) \, L(n/b) -
\sum_{b \mid n,\ b \le U} \ \sum_{c \le V,\ bc \mid n} \mu(b) \, \Lambda(c) +
\sum_{b \mid n,\ b > U} \ \sum_{c > V,\ bc \mid n} \mu(b) \, \Lambda(c),$$

where $b$ and $c$ range over $0, 1, \dots, n$.

When $R = \mathbb{R}$, $\mu$ is the Möbius function, $L = \log$ and $\Lambda$ is the von Mangoldt
function, the hypotheses hold and this is the classical Vaughan identity.

Formalized by `MetaMathlibExt.vaughan_identity_general`, a theorem declared in [MathlibExt/NumberTheory/VaughanIdentity.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/VaughanIdentity.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/vaughan-s-identity/index.html#vaughan-identity-general).

## Vaughan's identity

Let $R$ be a commutative ring, let $\mu$ and $\Lambda$ be arithmetic
functions with values in $R$ (so $\mu(0) = \Lambda(0) = 0$), and let $L : \mathbb{N} \to R$ be
any function. Suppose that for every natural number $m$, $\sum_{d \mid m} \mu(d)$ is $1$ if
$m = 1$ and $0$ otherwise, and $\Lambda(m) = \sum_{d \mid m} \mu(d) \, L(m/d)$, where both sums
run over the $d$ with $0 \le d \le m$ and $d \mid m$. Then for all natural numbers $U \ge 1$,
$V \ge 1$ and $n > V$,

$$\Lambda(n) = \sum_{b \mid n,\ b \le U} \mu(b) \, L(n/b) -
\sum_{b \mid n,\ b \le U} \ \sum_{c \le V,\ bc \mid n} \mu(b) \, \Lambda(c) +
\sum_{b \mid n,\ b > U} \ \sum_{c > V,\ bc \mid n} \mu(b) \, \Lambda(c),$$

where $b$ and $c$ range over $0, 1, \dots, n$.

When $R = \mathbb{R}$, $\mu$ is the Möbius function, $L = \log$ and $\Lambda$ is the von Mangoldt
function, the hypotheses hold and this is the classical Vaughan identity.

## Sources

- https://en.wikipedia.org/wiki/Vaughan%27s_identity It follows from `vaughan_identity_general`; the hypotheses `hU` and `hV` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.vaughan_identity`, a theorem declared in [MathlibExt/NumberTheory/VaughanIdentity.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/VaughanIdentity.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/vaughan-s-identity/index.html#vaughan-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vaughan's identity](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/vaughan-s-identity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/vaughan-s-identity)
