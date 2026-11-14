---
declaration: theorem
origin: cited
lean: STIR.proximity_gap
statement: formalized
proof: formalized
---

# proximity_gap

Let $\mathcal{C} := \mathrm{RS}[\mathbb{F},\mathcal{L},d]$ be a Reed Solomon code with $d\ge1$ and rate $\rho:=\frac{d}{|\mathcal{L}|}$ and let $B^*(\rho):=\sqrt{\rho}$. For every $\delta \in (0,1 - B^*(\rho))$ and functions $f_0,\ldots,f_{m-1} : \mathcal{L} \to \mathbb{F}$, if

$$
\Pr_{r\leftarrow\mathbb{F}}\!\Bigl[
\Delta\Bigl(\sum_{j=0}^{m-1} r^j\cdot {f_j},\mathrm{RS}[\mathbb{F},\mathcal{L},d]\Bigr)
\le \delta
\Bigr]>\mathsf{err}^*(d,\rho,\delta,m),
$$

then there exists a subset $S \subseteq \mathcal{L}$ with $|S| \ge (1 - \delta)\cdot|\mathcal{L}|$, and for every $i \in \{0,\ldots,m-1\}$, there exists $u \in \mathrm{RS}[\mathbb{F},\mathcal{L},d]$ such that $f_i(S) = u(S)$.

Above, $\mathsf{err}^*(d,\rho,\delta,m)$ is defined as follows:

- if $\delta \in \left(0,\frac{1-\rho}{2}\right]$ then

    $$
    \mathsf{err}^*(d,\rho,\delta,m)=\frac{(m-1)\cdot d}{\rho\cdot|\mathbb{F}|}
    $$

- if $\delta \in \Bigl(\frac{1-\rho}{2}, 1-\sqrt{\rho}\Bigr)$ then

    $$
    \mathsf{err}^*(d,\rho,\delta,m)=\frac{(m-1)\cdot {d}^2}{|\mathbb{F}|\cdot{\Bigl(2\cdot\min\{1-\sqrt{\rho}-\delta,\frac{\sqrt{\rho}}{20}\}\Bigr)}^7}
    $$

## Depends on

- [Distance from a Code](../../supporting-theories/coding-theory/def-distance-from-code.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)
- [List of Close Codewords](../../supporting-theories/coding-theory/def-list-close-codewords.md)

## Proof

For an empty family, take the whole evaluation domain. Otherwise write $m=k+1$ and apply correlated agreement for affine curves from ([Ben-Sasson et al. 2020](https://eprint.iacr.org/2020/654)). In the admissible distance range, the error above equals $k$ times the correlated-agreement error bound, in both the unique-decoding and Johnson regimes. The resulting joint agreement gives the common set $S$.

## Lean

Formalized as [`STIR.proximity_gap`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/STIR.proximity_gap).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 10](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L10)
